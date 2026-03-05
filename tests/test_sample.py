import pytest
from pages.sample_page import SamplePage

def test_page_interactions(driver):
    # Initialize SamplePage
    sample_page = SamplePage(driver)
    
    # Setup - Navigate to page (uses BASE_URL from .env)
    sample_page.load()
    
    # 1. Text input by ID
    sample_page.enter_text("Hello World")
    
    # 2. Find by name (logic check inside SamplePage)
    password_field = sample_page.find_password_field()
    assert password_field is not None
    
    # 3. Click submit by CSS selector
    # Note: Not clicking for this test, as it might navigate away
    # sample_page.click_submit()
    
    # 4. Find/Click link by XPath
    # sample_page.click_link()
    
    # 5. Handle Alert
    # sample_page.trigger_and_accept_alert()
    
    # 6. Action Chains
    # sample_page.perform_actions_chains()
    
    # 7. Iframe handling
    # iframe_text = sample_page.get_text_from_iframe()
    # print(f"Iframe content: {iframe_text}")
    
    # 8. Handling disabled elements (should fail)
    # success = sample_page.try_interacting_with_disabled_element()
    # assert success is False, "Should fail when interacting with disabled input"
    
    # 9. Data attributes
    data_val = sample_page.get_data_value()
    print(f"Data value: {data_val}")
    
    # The original script just print attributes and finishes.
    # In a real test we would add more assertions here.
