from numb3rs import validate

def test_ipv4_true():
    assert validate("192.168.1.1") == True

def test_ipv4_false():
    assert validate("256.0.0.0") == False

def test_ipv4_edge_cases():
    assert validate("0.0.0.0") == True
    assert validate("255.255.255.255") == True
    assert validate("192.168.0.256") == False
    assert validate("192.168.0") == False
    assert validate("192.168.0.1.2") == False
    assert validate("192 .168.0.1") == False
