import pytest


@pytest.mark.one
def test_method1():
    x = 5
    y = 10
    assert x == y


@pytest.mark.two
def test_method2():
    a = 15
    b = 20
    assert a + 5 == b


class TestCase:

    def test_one(self):
        x = "hello"
        assert "l" in x

    def test_two(self):
        x = "abc"
        assert hasattr(x, "check")


@pytest.fixture
def numbers():
    a = 10
    b = 20
    c = 25
    return [a, b, c]


@pytest.mark.xfail
def test_method1(numbers):
    x = 15
    assert numbers[0] == x


@pytest.mark.skip
def test_method2(numbers):
    y = 20
    assert numbers[1] == y


def test_method3(numbers):
    z = 25
    assert numbers[2] == z


@pytest.mark.parametrize("x, y, z", [(10, 20, 200), (20, 40, 200)])
def test_method(x, y, z):
    assert x*y == z
