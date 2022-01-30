import pytest

@pytest.mark.skip
def test_ogin():
    print("login")

@pytest.mark.regression
def test_add():
    print("add products")

@pytest.mark.smoke
def test_logout():
    print("logout")
