# AMAQ Dictionary

Dictionary implementation using textblob. Amaq(Ask-me-any-question) is a natural language processing implementation using textblob, a python library. Until now, it is capable of finding meanings of normal/daily-use english words. In order to run this on your system, you must have textblob and python3 installed on your system. You can install textblob using the procedures mentioned on <https://textblob.readthedocs.io/>.  

It is still under development.

## Getting started

### Setup

- `python -m virtualenv .venv`
- `source .venv/bin/activate`
- `pip install -r requirements.txt`
- `export NLTK_DATA=$(pwd)/.venv/lib`
- `python -m textblob.download_corpora lite`

### Run

- `export NLTK_DATA=$(pwd)/.venv/lib`
- `python amaq.py`
