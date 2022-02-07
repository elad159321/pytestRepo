def pytest_runtest_setup(item):
    print ("pytest_runtest_setup")

def pytest_runtest_teardown(item):
    print(("pytest_runtest_teardown"),item)