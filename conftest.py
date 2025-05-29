import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

@pytest.fixture(scope="session")
def browser():
    options = Options()
    # options.add_argument("--headless")  # или закомментируй для UI
    service = Service(executable_path="D:/Programs/chromedriver-win64/chromedriver.exe")  # путь к скачанному chromedriver.exe
    driver = webdriver.Chrome(service=service, options=options)
    driver.maximize_window()
    yield driver
    driver.quit()

@pytest.fixture()
def home_page(browser):
    from pages.home_page import HomePage
    page = HomePage(browser)
    page.load()
    return page

@pytest.fixture()
def product_page(browser):
    from pages.product_page import ProductPage
    page = ProductPage(browser)
    return page

@pytest .fixture()
def registration_data():
    return {
        "first_name": "name",
        "last_name": "name",
        "email": "name@gmail.ru",
        "pass": "123456"
    }
