import re


def clean_text(text: str) -> str:
    text = text.lower().strip()
    text = re.sub(r"[^A-Za-z ]+", "", text)
    return re.sub(r"\s+", " ", text)
