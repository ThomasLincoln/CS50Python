from twttr import shorten

def test_words():
    assert shorten("aeiou") == ""
    assert shorten("palavra") == "plvr"
    assert shorten("1 BATATA") == "1 btt"
    assert shorten("12182918921") == "12182918921"
    assert shorten("") == ""