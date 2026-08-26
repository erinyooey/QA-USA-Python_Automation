import time

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By



class UrbanRoutesPage:
    # define locators. Describe elements or parts from the page (website)
    FROM_LOCATOR = (By.ID, "from")
    TO_LOCATOR = (By.ID, "to")
    # to click the "Call a taxi" button
    TAXI_LOCATOR = (By.XPATH, "//button[text()='Call a taxi']")
    # to select the "Supportive" option
    SUPPORTIVE_LOCATOR = (By.XPATH, "//div[text()='Supportive']")
    # first click the "Phone number" option
    PHONE_NUMBER_OPTION = (By.CLASS_NAME, "np-text")
    # then click the actual "Phone number" field. has unique id
    PHONE_NUMBER_FIELD = (By.ID, "phone")
    NEXT_BUTTON = (By.XPATH, "//button[text()='Next']")
    PHONE_CODE_FIELD = (By.ID, "code")
    CONFIRM_BUTTON = (By.XPATH, "//button[text()='Confirm']")
    # Credit Card
    PAYMENT_LOCATOR = (By.CLASS_NAME, "pp-text")
    ADD_CARD_LOCATOR = (By.XPATH, "//div[text()='Add card']")
    CARD_FIELD = (By.ID, "number")
    CARD_CODE_FIELD = (By.XPATH, '//input[@name="code"]')
    LINK_BUTTON = (By.XPATH, "//button[text()='Link']")
    CLOSE_BUTTON = (By.XPATH, "(//button[contains(@class, 'section-close')])[3]")
    CARD_TEXT = (By.CLASS_NAME, "pp-value-text") # for assertion text
    # Comment for driver
    COMMENT_FIELD = (By.ID, "comment")
    # toggle button for blanket and handkerchief
    TOGGLE_BUTTON = (By.XPATH, "//div[@class='r-sw-container'][.//div[text()='Blanket and handkerchiefs']]//span[@class='slider round']")
    # to verify checkbox state for blanket and handkerchief
    SELECTED = (By.XPATH, "//div[text()='Blanket and handkerchiefs']/following-sibling::div//input[@class='switch-input']")
    # ice cream locator
    ICE_CREAM_COUNT_LOCATOR = (By.CLASS_NAME, "counter-plus")
    ICE_CREAM_COUNT_DISPLAY = (By.CLASS_NAME, "counter-value")
    # Car modal
    ORDER_BUTTON = (By.CLASS_NAME, "smart-button")
    CAR_MODAL = (By.CLASS_NAME, "order-body")

    def __init__(self, driver):
        self.driver = driver

    # For each element, we can define an action
    def enter_from_location(self, from_text):
        self.driver.find_element(*self.FROM_LOCATOR).send_keys(from_text)

    def enter_to_location(self, to_text):
        self.driver.find_element(*self.TO_LOCATOR).send_keys(to_text)

    # get text for route
    def get_from_address(self):
        return self.driver.find_element(*self.FROM_LOCATOR).get_property("value")

    def get_to_address(self):
        return self.driver.find_element(*self.TO_LOCATOR).get_property("value")

    # methods for selecting plan
    def click_taxi_button(self):
        self.driver.find_element(*self.TAXI_LOCATOR).click()

    def click_supportive(self):
        self.driver.find_element(*self.SUPPORTIVE_LOCATOR).click()

    # get text for selected plan
    def get_supportive(self):
        return self.driver.find_element(*self.SUPPORTIVE_LOCATOR).text

    # methods for testing phone number feature
    def click_phone_number(self):
        self.driver.find_element(*self.PHONE_NUMBER_OPTION).click()

    def enter_phone_number(self, phone_number):
        self.driver.find_element(*self.PHONE_NUMBER_FIELD).send_keys(phone_number)

    def click_next_button(self):
        self.driver.find_element(*self.NEXT_BUTTON).click()

    def enter_phone_code(self, phone_code):
        self.driver.find_element(*self.PHONE_CODE_FIELD).send_keys(phone_code)

    def click_confirm(self):
        self.driver.find_element(*self.CONFIRM_BUTTON).click()

    # get text for phone number features
    def get_phone_number(self):
        return self.driver.find_element(*self.PHONE_NUMBER_OPTION).text

    # methods for adding a credit card
    def click_payment_method(self):
        self.driver.find_element(*self.PAYMENT_LOCATOR).click()

    def click_add_card(self):
        self.driver.find_element(*self.ADD_CARD_LOCATOR).click()

    def enter_card_number(self, card):
        self.driver.find_element(*self.CARD_FIELD).send_keys(card)

    def enter_card_code(self, card_code):
        self.driver.find_element(*self.CARD_CODE_FIELD).send_keys(card_code)
        # simulate user pressing TAB
        self.driver.find_element(*self.CARD_CODE_FIELD).send_keys(Keys.TAB)

    def click_link(self):
        self.driver.find_element(*self.LINK_BUTTON).click()

    def close(self):
        self.driver.find_element(*self.CLOSE_BUTTON).click()

    # get text for adding a card
    def get_card_text(self):
        return self.driver.find_element(*self.CARD_TEXT).text

    # methods for writing a comment for the driver

    def enter_message(self, message):
        self.driver.find_element(*self.COMMENT_FIELD).send_keys(message)

    def get_message(self):
        return self.driver.find_element(*self.COMMENT_FIELD).get_property("value")

    # methods for ordering blanket and handkerchiefs
    def click_toggle(self):
        self.driver.find_element(*self.TOGGLE_BUTTON).click()

    def check_toggle_state(self):
        return self.driver.find_element(*self.SELECTED).get_property("checked")

    # methods for ordering 2 ice creams
    def click_count(self):
        self.driver.find_element(*self.ICE_CREAM_COUNT_LOCATOR).click()

    def retrieve_count(self):
        return self.driver.find_element(*self.ICE_CREAM_COUNT_DISPLAY).text

    # methods for ordering taxi
    def click_order(self):
        self.driver.find_element(*self.ORDER_BUTTON).click()

    def retrieve_modal(self):
        return self.driver.find_element(*self.CAR_MODAL).is_displayed()