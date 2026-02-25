# Selenium Locators Practice Website

This is a comprehensive website designed for practicing Selenium WebDriver locators and commands. It contains various HTML elements organized in sections for easy reference and testing.

## Interactive Learning Features

- **Show Selenium Script Buttons**: Click the "Show Selenium Script" button next to any element to see the JavaScript WebDriver code for interacting with that specific element
- **Dynamic Code Generation**: Code examples include multiple locator strategies (ID, Name, CSS Selector, XPath) and element-specific actions
- **Real-time Examples**: Code snippets are tailored to each element type with appropriate Selenium commands

## Features

- **Input Fields**: Text, password, email, number, date, datetime-local, time, month, week, file, color, range, search, URL, telephone, disabled, readonly, autocomplete, and hidden inputs
- **Buttons**: Different types of buttons (button, input button, submit)
- **Checkboxes & Radio Buttons**: Multiple options with labels
- **Select Dropdowns**: Single and multi-select dropdowns (hold Ctrl/Cmd for multi-select)
- **Textarea**: Multi-line text input
- **Links**: Anchor tags for link testing
- **Images**: Image elements
- **Tables**: Sample table with headers and data
- **Forms**: Form elements
- **Divs and Spans**: Container elements for CSS selector practice
- **JavaScript Popups**: Alert, confirm, and prompt dialogs for handling browser popups
- **Advanced Interactions**: Right-click, double-click, hover, and drag-and-drop elements
- **Advanced Elements**: Iframes, progress bars, meters, collapsible content, modals, SVG, canvas, data attributes, and keyboard events

## Getting Started

1. Clone or download this repository
2. Open a terminal in the project directory
3. Run the local server:
   ```bash
   python -m http.server 8000
   ```
4. Open your browser and navigate to `http://localhost:8000`

## Usage for Selenium Practice

Each element is uniquely identifiable with:
- **ID**: For precise targeting (e.g., `id="text-input"`)
- **Name**: For form-based locators (e.g., `name="textInput"`)
- **Class**: For CSS class selectors
- **Tag Name**: For general element types

### Example Selenium Code

```python
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("http://localhost:8000")

# Find by ID
text_input = driver.find_element(By.ID, "text-input")
text_input.send_keys("Hello World")

# Find by name
password_input = driver.find_element(By.NAME, "passwordInput")

# Find by CSS selector
submit_button = driver.find_element(By.CSS_SELECTOR, ".btn")

# Find by XPath
link = driver.find_element(By.XPATH, "//a[@id='link1']")

# Handle JavaScript alerts
alert_button = driver.find_element(By.ID, "alert-button")
alert_button.click()
alert = driver.switch_to.alert
alert.accept()  # or alert.dismiss() for confirm

# Advanced interactions
from selenium.webdriver.common.action_chains import ActionChains

# Right-click
right_click_element = driver.find_element(By.ID, "right-click-div")
ActionChains(driver).context_click(right_click_element).perform()

# Double-click
double_click_element = driver.find_element(By.ID, "double-click-div")
ActionChains(driver).double_click(double_click_element).perform()

# Hover
hover_element = driver.find_element(By.ID, "hover-div")
ActionChains(driver).move_to_element(hover_element).perform()

# Drag and drop
source = driver.find_element(By.ID, "drag-source")
target = driver.find_element(By.ID, "drop-target")
ActionChains(driver).drag_and_drop(source, target).perform()

# Switch to iframe
iframe = driver.find_element(By.ID, "sample-iframe")
driver.switch_to.frame(iframe)
iframe_element = driver.find_element(By.ID, "iframe-text")
print(iframe_element.text)
driver.switch_to.default_content()

# Handle disabled/readonly elements (should fail)
try:
    disabled_input = driver.find_element(By.ID, "disabled-input")
    disabled_input.send_keys("This should fail")
except Exception as e:
    print(f"Expected error: {e}")

# Data attributes
data_element = driver.find_element(By.CSS_SELECTOR, "[data-test-id='sample-data']")
print(data_element.get_attribute("data-value"))

driver.quit()
```

## Elements Overview

- All elements have unique IDs for easy identification
- Form elements have appropriate `name` attributes
- Buttons and links have classes for CSS selector practice
- Tables include headers and data cells
- Iframe contains inline HTML content for testing frame switching
- Disabled and readonly inputs demonstrate element state handling
- Data attributes show how to select elements by custom attributes
- SVG and Canvas elements allow testing of graphical content interaction
- Images use placeholder URLs
- **Show Selenium Script buttons** provide instant code examples for each element

## Contributing

Feel free to add more elements or improve the styling to enhance the practice experience.

## License

This project is for educational purposes.