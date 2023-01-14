from conf.config import TestData


class TestPage:

    def __init__(self, browser):
        self.browser = browser

    def close_google_vignette(self, el):
        self.browser.switch_to.frame('aswift_3')
        if TestData(self.browser).check_exists(el):
            TestData(self.browser).click_el(el)
        else:
            self.browser.switch_to.frame("ad_iframe")
            TestData(self.browser).click_el(el)
