from plates import is_valid

def test_plates():
    assert is_valid("CS50") == True
    assert is_valid("CS05") == False
    assert is_valid("CS50P") == False
    assert is_valid("P13.14") == False
    assert is_valid("H") == False
    assert is_valid("HA") == True
    assert is_valid("H2") == False
    assert is_valid("22") == False
    assert is_valid("OUTATIME") == False
    assert is_valid("a02p") == False
    assert is_valid("AAA222") == True
    assert is_valid("AAA22A") == False
    