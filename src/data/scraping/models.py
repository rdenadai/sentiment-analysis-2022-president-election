import os
import urllib.parse
from hashlib import sha256
from time import sleep

from arrow import Arrow
from arrow import get as arrow_get
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from src.data.processing.utils import is_number
from src.logger import log


def chrome_options() -> Options:
    options = Options()
    options.add_argument("--disable-extensions")
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")  # linux only
    options.add_argument("--headless")
    options.add_argument("--lang=pt-br")
    options.add_argument("--proxy-server='direct://'")
    options.add_argument("--proxy-bypass-list=*")
    return options


class TwitterTagsClient:
    def __init__(self, n_posts_2_extract: int = 5) -> None:
        self.n_posts_2_extract = n_posts_2_extract

    def treat_comment(self, comment: str) -> str:
        comment = comment.replace("\n", " ").strip()
        strip_pos = 0
        for pos in range(1, len(comment)):
            if is_number(comment[-pos]) or comment[-pos] == " ":
                strip_pos = pos
            else:
                break
        if strip_pos > 0:
            comment = comment[:-strip_pos]
        return comment

    def treat_data(self, date: webdriver.remote.webelement.WebElement) -> Arrow:
        time = date.get_attribute("datetime")
        return arrow_get(time).to("America/Sao_Paulo")

    def load_tags(self, hashtag: str) -> dict:
        driver = webdriver.Chrome(
            options=chrome_options(),
            executable_path=f"{os.getcwd()}/src/data/scraping/driver/chromedriver",
        )
        tz_params = {"timezoneId": "America/Sao_Paulo"}
        driver.execute_cdp_cmd("Emulation.setTimezoneOverride", tz_params)

        driver.get(
            f"https://twitter.com/search?q={urllib.parse.quote(hashtag)}%20lang%3Apt&src=typed_query&f=live"
        )

        tweets: list = []
        while (_ := len(tweets)) == 0:
            try:
                sleep(0.2)
                tweets = driver.find_elements(By.TAG_NAME, "article")
            except Exception as error:
                log.error(f"ERROR: AdaptiveFiltersBar-target not found : {error}")

        data: dict = {"hashtag": hashtag, "comments": []}
        for _ in range(self.n_posts_2_extract + 1):
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
            sleep(1)

            tweets = driver.find_elements(By.TAG_NAME, "article")
            for tweet in tweets:
                try:
                    username = tweet.find_element(
                        By.XPATH,
                        "./div/div/div/div[2]/div[2]/div[1]/div/div/div[1]/div/div/div[2]/div/div[1]/a/div/span",
                    )
                    comment = tweet.find_element(By.XPATH, "./div/div/div/div[2]/div[2]/div[2]")
                    date = tweet.find_element(
                        By.XPATH,
                        "./div/div/div/div[2]/div[2]/div[1]/div/div/div[1]/div/div/div[2]/div/div[3]/a/time",
                    )

                    if username and comment:
                        username_: str = username.text.strip()
                        comment_: str = self.treat_comment(comment.text.strip())
                        date_: Arrow = self.treat_data(date)

                        data["comments"].append(
                            {
                                "hash": sha256(
                                    (f"{username_}|{comment_}").encode("ascii", "ignore")
                                ).hexdigest(),
                                "username": username_,
                                "data": date_.format("DD/MM/YYYY HH:mm"),
                                "timestamp": date_.timestamp(),
                                "comment": comment_,
                            }
                        )
                except Exception as error:
                    log.error(f"ERROR: username or comment not found : {error}")
        driver.close()
        return data
