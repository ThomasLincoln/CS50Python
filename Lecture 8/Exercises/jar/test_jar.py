from jar import Jar
import pytest


def test_init():
    with pytest.raises(ValueError):
         jar = Jar(-1)


def test_init_errado():
    jar = Jar(10)
    assert str(jar) == ''


def test_string():
    jar = Jar()
    assert str(jar) == ''

    jar.deposit(1)
    assert str(jar) == '🍪'

    jar.deposit(11)
    assert str(jar) == '🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪'


def test_deposito():
    jar = Jar(10)

    jar.deposit(10)
    assert str(jar) == '🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪'

    with pytest.raises(ValueError):
         jar.deposit(1)


def test_retirada():
    jar = Jar(10)

    jar.deposit(8)
    jar.withdraw(2)
    assert str(jar) == '🍪🍪🍪🍪🍪🍪'

    with pytest.raises(ValueError):
         jar.deposit(8)