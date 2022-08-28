from functools import lru_cache
from string import punctuation
from typing import Any, Iterator
from unicodedata import normalize

import nltk
import spacy
from nltk.corpus import stopwords


def chunks(l_iter: list, n: int) -> Iterator[list]:
    # looping till length l
    for i in range(0, len(l_iter), n):
        yield l_iter[i : i + n]


@lru_cache(maxsize=256)
def is_number(value: Any) -> bool:
    try:
        complex(value)  # for int, long, float and complex
    except ValueError:
        return False
    return True


@lru_cache(maxsize=256)
def get_stopwords() -> tuple[list[str], list[str]]:
    stpwords = stopwords.words("portuguese")
    punkt = [pk for pk in punctuation]
    rms = ["um", "não", "mais", "muito", "sem", "estou", "sou"]
    for rm in rms:
        del stpwords[stpwords.index(rm)]
    for rm in ["?"]:
        del punkt[punkt.index(rm)]
    return stpwords, punkt


def remover_acentos(txt: str) -> str:
    return normalize("NFKD", txt).encode("ASCII", "ignore").decode("ASCII")


def normalizar(phrase: str, sort: bool = True) -> str:
    if phrase:
        phrase = remover_acentos(phrase.lower())
        for punkt in punctuation:
            phrase = phrase.replace(punkt, " ")
        phrase = phrase.split()
        if sort:
            phrase = sorted(phrase)
        phrase = "".join(phrase).strip()
    return phrase


# GLOBALS
NLP_LEMMATIZER = spacy.load("pt_core_news_sm")
RSLP_STEMMER = nltk.stem.RSLPStemmer()
SNOWBALL_STEMMER = nltk.stem.SnowballStemmer("portuguese")
STOPWORDS, PUNCT = get_stopwords()
