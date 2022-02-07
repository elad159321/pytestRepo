import pytest
import sys


def setup_module(module):
    print("Before execution")


def teardown_module(module):
    print("teardown")


@pytest.mark.skip
def test_ogin():
    print("login")

@pytest.mark.regression
def test_add():
    print("add products")

@pytest.mark.smoke
def test_logout():
    print("logout")

# test should be skipped if python version is less then 4.0
@pytest.mark.skipif(sys.version_info<(4,0),reason="Python version not supported")
def test_dependOnPythonVer():
    print("logout")
    
@pytest.mark.xfail
def test_xfailExample():
    assert 10==10