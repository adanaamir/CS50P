from twttr import shorten

def test_str():
    assert shorten("adan") == "dn"
    assert shorten("twitter") == "twttr"

def test_lower_and_upper():
    assert shorten("TWITTER") == "TWTTR"   
    assert shorten("twitter") == "twttr"

def test_int():
    assert shorten("1234") == "1234"

def test_punctuation():
    assert shorten("?!.,") == "?!.,"