from selenium import webdriver


class SeleniumDriver:
    def __init__(self, selenium_driver):
        self.driver = selenium_driver


def browser():
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(options=options)
    return driver
