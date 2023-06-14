import pytest


expected_title = 'Electronics, Cars, Fashion, Collectibles & More | eBay'
base_url = 'https://www.ebay.com'


@pytest.mark.smoketest
def test_title(browser):
    # navigate to ebay.com home page
    browser.get(base_url)
    # verify that website title is eBay
    assert expected_title in browser.title
