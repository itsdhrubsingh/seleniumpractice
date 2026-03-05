import pytest
from pages.sample_page import SamplePage

def test_page_interactions(driver):
    sample_page = SamplePage(driver)
    sample_page.load()
    
    # Verify inputs
    sample_page.enter_text("Hello World")
    password_field = sample_page.find_password_field()
    assert password_field.is_enabled()
    
    # Verify data attribute
    data_val = sample_page.get_data_value()
    assert data_val is not None
