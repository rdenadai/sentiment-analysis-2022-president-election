#!/bin/bash

python -m pip install -r ./requirements.txt --upgrade

python -m nltk.downloader stopwords
python -m nltk.downloader punkt
python -m nltk.downloader rslp
python -m nltk.downloader perluniprops
python -m spacy download en_core_web_sm
python -m spacy download pt_core_news_sm