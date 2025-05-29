import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

@pytest.fixture(scope="session")
def browser():
    # options = webdriver.ChromeOptions()
    # # options.add_argument("--headless")  # Уберите, если нужен браузер с UI
    # driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    # driver.maximize_window()
    # yield driver
    # driver.quit()
    options = Options()
    # options.add_argument("--headless")  # или закомментируй для UI
    service = Service(executable_path="D:/Programs/chromedriver-win64/chromedriver.exe")  # путь к скачанному chromedriver.exe
    driver = webdriver.Chrome(service=service, options=options)
    yield driver
    driver.quit()
