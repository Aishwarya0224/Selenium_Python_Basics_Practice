import pytest


@pytest.fixture(scope="class")
def setup():
    print("I will be executing first")
    yield
    print(" I will execute last")
    
@pytest.fixture()
def dataLoad():
    print("user profile data is being created")
    return["rahul", "shetty", "rahulshettyacademy.com"]

@pytest.fixture(params=["chrome", "firefox", "IE"])
def crossBrowser(request):
    return request.param