from bank import value

def test_words():
    assert value("Hello") == "$0"
    assert value("How are you doing?") == "$20"
    assert value("What's Up") == "$100"