import pytest
import sys
@pytest.mark.skip
def test_ogin():
    print("login")

@pytest.mark.regression
def test_add():
    print("add products")

@pytest.mark.smoke
def test_logout():
    print("logout")


@pytest.mark.skipif(sys.version_info<(4,0),reason="Python version not supported")
def test_dependOnPythonVer():
    print("logout")