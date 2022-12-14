import gc
from concurrent.futures import ProcessPoolExecutor
from functools import partial
from multiprocessing import cpu_count
from time import perf_counter

from peewee import DoesNotExist

from src.data.processing.utils import chunks
from src.data.scraping.hashtags import HASHTAGS
from src.data.scraping.models import TwitterTagsClient
from src.database.conn import db
from src.database.models import HashtagComments
from src.logger import log


def run_hashtag(n_posts_2_extract: int, hashtag: str) -> dict:
    print(f"- Collecting hashtag : {hashtag}")
    tw = TwitterTagsClient(n_posts_2_extract=n_posts_2_extract)
    return tw.load_tags(hashtag)


def run_save_hashtag(item: dict) -> dict:
    num_saved_comments = 0
    hashtag = item["hashtag"]
    for comment in item["comments"]:
        try:
            _ = HashtagComments.get(HashtagComments.hash == comment["hash"])
        except DoesNotExist:
            HashtagComments(hashtag=hashtag, **comment).save(force_insert=True)
            num_saved_comments += 1
    return {"hashtag": hashtag, "num_saved_comments": num_saved_comments}


def main(hashtags: tuple[str, ...]) -> int:
    n_chunks: int = 5
    n_posts_2_extract: int = 2

    with ProcessPoolExecutor(max_workers=cpu_count() * 2) as executor:
        for hashtags_ in chunks(hashtags, n_chunks):
            start_time = perf_counter()
            contents = list(executor.map(partial(run_hashtag, n_posts_2_extract), hashtags_, chunksize=1))
            log.info(f"--- Load tweets took {round(perf_counter() - start_time, 2)}s ---")
            with db.atomic() as txn:
                saved = list(executor.map(run_save_hashtag, contents, chunksize=25))
                txn.commit()
            print(f"--- Save tweets took {round(perf_counter() - start_time, 2)}s ---")
            for i, item in enumerate(saved):
                print(
                    f"--- # of tweets for : {item['hashtag']} => {len(contents[i]['comments'])}/{item['num_saved_comments']}"
                )

    return 0


if __name__ == "__main__":
    gc.set_threshold(100_000, 1_000, 1_000)
    gc.freeze()
    raise SystemExit(main(HASHTAGS))
