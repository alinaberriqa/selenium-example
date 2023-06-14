import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC


@pytest.mark.parametrize("year, make, model, submodel", [
    ('2022', 'BMW', 'F850GS', 'Adventure')])
@pytest.mark.regressiontest
def test_ebay_search_motorcycle(browser, year, make, model, submodel):
    base_url = 'https://www.ebay.com/'
    expected_title = 'Electronics, Cars, Fashion, Collectibles & More | eBay'
    browser.get(base_url)
    assert expected_title in browser.title
    assert base_url in browser.current_url

    browser.find_element(By.LINK_TEXT, 'Motors').click()
    WebDriverWait(browser, 5).until(EC.title_contains('eBay Motors'))
    browser.find_element(By.NAME, 'MOTORCYCLE').click()

    year_dropdown = Select(WebDriverWait(browser, 3).until(EC.element_to_be_clickable(browser.find_element(By.NAME, 'Year'))))
    year_dropdown.select_by_visible_text(year)

    make_dropdown = Select(WebDriverWait(browser, 3).until(EC.element_to_be_clickable(browser.find_element(By.NAME, 'Make'))))
    make_dropdown.select_by_visible_text(make)

    model_dropdown = Select(WebDriverWait(browser, 3).until(EC.element_to_be_clickable(browser.find_element(By.NAME, 'Model'))))
    model_dropdown.select_by_visible_text(model)

    submodel_dropdown = Select(WebDriverWait(browser, 3).until(EC.element_to_be_clickable(browser.find_element(By.NAME, 'Submodel'))))
    submodel_dropdown.select_by_visible_text(submodel)

    browser.find_element(By.XPATH, "//button[text()='Find Parts']").click()

    assert 'My Garage' in browser.title
    assert 'F850GS' in browser.current_url
    page_heading = browser.find_element(By.CSS_SELECTOR, '.x-my-vehicle-info-title')
    assert '2022 BMW F850GS' in page_heading.text
