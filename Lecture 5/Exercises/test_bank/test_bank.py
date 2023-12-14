from bank import value

def main():
    test_return_zero()
    test_return_20()
    test_value_100()
        
def test_return_zero():
    assert value("Hello") == 0
    assert value('hello') == 0
    assert value("heLlO Thomas") == 0
    
def test_return_20():
    assert value("How are you doing?") == 20
    
def test_value_100():
    assert value("What's Up") == 100