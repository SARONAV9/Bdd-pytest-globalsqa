import pytest
from selenium import webdriver


@pytest.fixture
def browser():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--incognito")
    b = webdriver.Chrome(chrome_options=chrome_options)
    b.maximize_window()
    b.implicitly_wait(4)
    yield b
    b.quit()
