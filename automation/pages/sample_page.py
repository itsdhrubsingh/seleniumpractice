from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from configs.config import Config

class SamplePage(BasePage):
    """Page Object for the sample page provided in the script."""

    # Locators
    TEXT_INPUT = (By.ID, "text-input")
    PASSWORD_INPUT = (By.NAME, "passwordInput")
    SUBMIT_BUTTON = (By.CSS_SELECTOR, ".btn")
    LINK = (By.XPATH, "//a[@id='link1']")
    ALERT_BUTTON = (By.ID, "alert-button")
    RIGHT_CLICK_DIV = (By.ID, "right-click-div")
    DOUBLE_CLICK_DIV = (By.ID, "double-click-div")
    HOVER_DIV = (By.ID, "hover-div")
    DRAG_SOURCE = (By.ID, "drag-source")
    DROP_TARGET = (By.ID, "drop-target")
    SAMPLE_IFRAME = (By.ID, "sample-iframe")
    IFRAME_TEXT = (By.ID, "iframe-text")
    DISABLED_INPUT = (By.ID, "disabled-input")
    DATA_ELEMENT = (By.CSS_SELECTOR, "[data-test-id='sample-data']")

    def __init__(self, driver):
        super().__init__(driver)

    def load(self, url=None):
        if url is None:
            url = Config.BASE_URL
        self.navigate_to(url)

    def enter_text(self, text):
        self.type_into(self.TEXT_INPUT, text)

    def find_password_field(self):
        return self.find_element(self.PASSWORD_INPUT)

    def click_submit(self):
        self.click_element(self.SUBMIT_BUTTON)

    def click_link(self):
        self.click_element(self.LINK)

    def trigger_and_accept_alert(self):
        self.click_element(self.ALERT_BUTTON)
        self.handle_alert(accept=True)

    def perform_actions_chains(self):
        self.right_click(self.RIGHT_CLICK_DIV)
        self.double_click(self.DOUBLE_CLICK_DIV)
        self.hover_over(self.HOVER_DIV)
        self.drag_and_drop(self.DRAG_SOURCE, self.DROP_TARGET)

    def get_text_from_iframe(self):
        self.switch_to_iframe(self.SAMPLE_IFRAME)
        text = self.get_text(self.IFRAME_TEXT)
        self.switch_to_default_content()
        return text

    def try_interacting_with_disabled_element(self):
        try:
            self.type_into(self.DISABLED_INPUT, "This should fail")
            return True
        except Exception:
            return False

    def get_data_value(self):
        return self.get_attribute(self.DATA_ELEMENT, "data-value")
