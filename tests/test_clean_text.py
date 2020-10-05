from helper import clean_text


def test_clean_text_no_special_char() -> None:
    text = clean_text("hello world")
    assert text == "hello world"


def test_clean_text_digits() -> None:
    text = clean_text("hello world123")
    assert text == "hello world"


def test_clean_text_special_char() -> None:
    text = clean_text("hello world#$%")
    assert text == "hello world"


def test_clean_text_multiple_spaces() -> None:
    text = clean_text("hello world   ")
    assert text == "hello world"
