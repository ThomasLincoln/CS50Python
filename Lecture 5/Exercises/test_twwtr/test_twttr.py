from twttr import shorten

def main():
    test_upper_lower_case()
    test_number()
    
def test_upper_lower_case():
    assert shorten('twitter') == 'twttr'
    assert shorten('TWITTER') == 'TWTTR'

def test_number():
    assert shorten('1234') == '1234'
    assert shorten('aa234') == '234'
    assert shorten('AA234') == '234'
    
def test_pontuacao():
    assert shorten('..@?') == '..@?'
