# Example using Selenium for web application testing
from selenium import webdriver

def test_login_functionality():
    browser = webdriver.Safari()
    browser.get("http://example.com/login")
    username_field = browser.find_element_by_name("username")
    password_field = browser.find_element_by_name("password")
    username_field.send_keys("user")
    password_field.send_keys("pass")
    login_button = browser.find_element_by_id("login-button")
    login_button.click()
    assert "Dashboard" in browser.page_source
    print("Passed")
