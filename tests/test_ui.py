import pytest
import re
from playwright.sync_api import Page, expect


@pytest.mark.ui
@pytest.mark.acme_bank
def test_acmebank_login(page:Page):

    # Arrange
    page.goto("https://demo.applitools.com/")

    # Act
    # PLAYWRIGHT will automatically wait for the elements to load before sending the interactions below
    page.locator("id=username").fill("GeadKee")
    page.locator("id=password").fill("ggk1212")
    page.locator("id=log-in").click()

    # Assert
    # "expect" follows concept web-first assertion
    expect(page.locator("tag=div").get_by_text("logo-w")).to_be_visible
    expect(page.locator("tag=div").get_by_text("form-group")).to_be_visible
    expect(page.get_by_text("Add Account")).to_be_visible()
    expect(page.get_by_text("Make Payment")).to_be_visible()
    expect(page.get_by_text("View Statement")).to_be_visible()
    expect(page.get_by_text("Request Increase")).to_be_visible()
    expect(page.get_by_text("Pay Now")).to_be_visible()

    warning_msg = re.compile(r'Your nearest branch closes in:( \d+[hms])+')
    expect(page.locator('id=time')).to_have_text(warning_msg)
    
    acceptable_statuses = ['Complete', 'Pending', 'Declined']
    actual_statuses = page.locator('span.status-pill + span').all_text_contents()
    for status in actual_statuses:
        assert status in acceptable_statuses
