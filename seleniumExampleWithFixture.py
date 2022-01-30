import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
driver=None

@pytest.fixture
def setup():
    ''''Before the yield - its the pre condition
    After the yield its the post condition '''
    print("start browser")
    global driver
    driver=webdriver.Chrome(ChromeDriverManager().install())
    driver.maximize_window()
    yield
    driver.quit()
    print("close browser")

def test_1(setup):
    driver.get("https://www.facebook.com/")
    print("test 1 executed")

def test_2(setup):
    driver.get("https://www.facebook.com/")
    print("test 2 executed")

def test_3(setup):
    driver.get("https://www.facebook.com/")
    print("test 3 executed")
