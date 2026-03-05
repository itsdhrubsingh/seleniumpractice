from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from configs.config import Config

class BasePage:
    """Base class for all Page Objects in the POM."""

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, Config.EXPLICIT_WAIT)
        self.actions = ActionChains(self.driver)

    def navigate_to(self, url):
        self.driver.get(url)

    def find_element(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))

    def click_element(self, locator):
        self.find_element(locator).click()

    def type_into(self, locator, text):
        element = self.find_element(locator)
        element.clear()
        element.send_keys(text)

    def get_text(self, locator):
        return self.find_element(locator).text

    def get_attribute(self, locator, attribute):
        return self.find_element(locator).get_attribute(attribute)

    def is_element_enabled(self, locator):
        return self.find_element(locator).is_enabled()

    def handle_alert(self, accept=True):
        alert = self.driver.switch_to.alert
        if accept:
            alert.accept()
        else:
            alert.dismiss()

    def right_click(self, locator):
        element = self.find_element(locator)
        self.actions.context_click(element).perform()

    def double_click(self, locator):
        element = self.find_element(locator)
        self.actions.double_click(element).perform()

    def hover_over(self, locator):
        element = self.find_element(locator)
        self.actions.move_to_element(element).perform()

    def drag_and_drop(self, source_locator, target_locator):
        source_element = self.find_element(source_locator)
        target_element = self.find_element(target_locator)
        self.actions.drag_and_drop(source_element, target_element).perform()

    def switch_to_iframe(self, locator):
        iframe = self.find_element(locator)
        self.driver.switch_to.frame(iframe)

    def switch_to_default_content(self):
        self.driver.switch_to.default_content()
