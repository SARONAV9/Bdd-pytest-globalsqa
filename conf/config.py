from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from re import search
from selenium.webdriver.support import expected_conditions as ec


class TestData:
    TESTERS_HUB = "menu-item-2822"
    SIMPLE_PAGE_TEST = "menu-item-2846"
    SORTABLE = "//*[text()='Sortable']"
    DRAG_AND_DROP = "menu-item-2804"
    CLOSE_FRAME = '//*[@id="dismiss-button"]'
    MULTIPLE_LISTS = '//*[@id="Multiple Lists"]'
    IFRAME_MULTIPLE_LISTS = '//*[@id="post-2675"]/div[2]/div/div/div[2]/p/iframe'
    IFRAME_PORTLETS = '//*[@id="post-2675"]/div[2]/div/div/div[1]/p/iframe'
    """
     '[class="newtabs horizontal"]>div:nth-child(2)>div:nth-child(4) iframe'
    """
    # SIMPLE_LIST
    SIMPLE_LIST = 'Simple List'
    Item1 = '//*[@id="sortable1"]/li[1]'
    Item2 = '//*[@id="sortable2"]/li[1]'

    # PORTLETS
    PORTLETS = 'Portlets'
    FEEDS = '//*[text()="Feeds"]'
    NEWS = '//*[text()="Images"]'

    def __init__(self, browser):
        self.browser = browser

    def click_el(self, el):
        self.element_wait(el).click()

    def element_wait(self, locator):
        if search("//\*", locator):
            return WebDriverWait(self.browser, 10).until(ec.visibility_of_element_located((By.XPATH, locator)))
        elif search("css=", locator):
            return WebDriverWait(self.browser, 10).until(ec.visibility_of_element_located((By.CSS_SELECTOR, locator)))
        else:
            return WebDriverWait(self.browser, 10).until(ec.visibility_of_element_located((By.ID, locator)))

    def check_exists(self, el):
        try:
            self.browser.find_element(By.XPATH, el)
        except NoSuchElementException:
            return False
        return True
