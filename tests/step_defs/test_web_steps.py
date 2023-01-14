import time

from pytest_bdd import scenarios, given, when, then, parsers
from selenium.webdriver import ActionChains
from conf.config import TestData
from tests.pages.test_page import TestPage

scenarios('../features/Multiple_lists.feature')


@given(parsers.parse('open the globalsqa "{url}" page'))
def gq_home_page(browser, url):
    browser.get(url)


@when('go to the test page')
def go_to_test_page(browser):
    data = TestData(browser)
    el = data.element_wait(data.TESTERS_HUB)
    action = ActionChains(browser)
    action.move_to_element(el).perform()
    data.click_el(data.SIMPLE_PAGE_TEST)
    data.click_el(data.SORTABLE)
    TestPage(browser).close_google_vignette(data.CLOSE_FRAME)


@when(parsers.parse('reorder elements {section},{iframe},{el1},{el2}'))
def reorder(browser, section, iframe, el1, el2):
    data = TestData(browser)
    data.click_el(section)
    browser.switch_to.frame(data.element_wait(iframe))
    source = data.element_wait(el1)
    target = data.element_wait(el2)
    action = ActionChains(browser)
    action.drag_and_drop(source, target).perform()

"""
@when('reorder MULTIPLE LISTS')
def reorder(browser):
    data = TestData(browser)
    data.click_el(data.MULTIPLE_LISTS)
    browser.switch_to.frame(data.element_wait(data.IFRAME_MULTIPLE_LISTS))
    source = data.element_wait(data.Item1)
    target = data.element_wait(data.Item2)
    action = ActionChains(browser)
    action.drag_and_drop(source, target).perform()


@when('reorder PORTLETS')
def reorder(browser):
    data = TestData(browser)
    browser.switch_to.frame(data.element_wait(data.IFRAME_PORTLETS))
    source = data.element_wait(data.FEEDS)
    target = data.element_wait(data.NEWS)
    action = ActionChains(browser)
    action.drag_and_drop(source, target).perform()
"""

@when(parsers.parse('click {element}'))
def click_element(browser, element):
    data = TestData(browser)
    data.click_el(element)


@then(parsers.parse('the url is contain {text}'))
def check_url(browser, text):
    assert text in browser.current_url


@then(parsers.parse('the element exist {element}'))
def check_elements(browser, element):
    data = TestData(browser)
    assert data.check_exists(element)
