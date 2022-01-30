import pytest

@pytest.fixture
def setup():
    ''''this function will run before each test that gets it as arguemnt'''
    print("start browser")

def test_1(setup):
    print("test 1 executed")
    print("close browser")

def test_2(setup):
    print("test 2 executed")
    print("close browser")

def test_3(setup):
    print("test 3 executed")
    print("close browser")