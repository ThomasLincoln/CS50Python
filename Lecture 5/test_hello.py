from hello import hello

def test_hello():
    assert hello("Thomas") == "hello, Thomas"
    assert hello() == "hello, world"