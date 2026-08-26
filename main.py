from selenium import webdriver
import data
import helpers
import pages
import time


class TestUrbanRoutes:
    @classmethod
    # add special method
    def setup_class(cls):
        from selenium.webdriver import DesiredCapabilities
        capabilities = DesiredCapabilities.CHROME
        capabilities["goog:loggingPrefs"] = {'performance': 'ALL'}
        cls.driver = webdriver.Chrome()
        if helpers.is_url_reachable(data.URBAN_ROUTES_URL):
            print("Connected to the Urban Routes server")
        else:
            print("Cannot connect to Urban Routes. Check the server is on and still running")

    """Define 8 functions"""

    # time.sleep() calls are commented out below - uncomment to visually confirm the automation steps
    def test_set_route(self):
        # always retrieve the urban routes server to load the website
        self.driver.get(data.URBAN_ROUTES_URL)
        # create reference to the page
        page = pages.UrbanRoutesPage(self.driver)
        page.enter_from_location(data.ADDRESS_FROM)
        page.enter_to_location(data.ADDRESS_TO)
        # time.sleep(2)
        # Assertions for 1. Setting the address
        assert page.get_from_address() == data.ADDRESS_FROM
        assert page.get_to_address() == data.ADDRESS_TO

    def test_select_plan(self):
        # always retrieve the urban routes server to load the website
        self.driver.get(data.URBAN_ROUTES_URL)
        # create reference to the page
        page = pages.UrbanRoutesPage(self.driver)
        page.enter_from_location(data.ADDRESS_FROM)
        page.enter_to_location(data.ADDRESS_TO)
        page.click_taxi_button()
        page.click_supportive()
        # time.sleep(2)
        # Assertion for 2. Setting Supportive Plan
        assert page.get_supportive() == "Supportive"

    def test_fill_phone_number(self):
        # always retrieve the urban routes server to load the website
        self.driver.get(data.URBAN_ROUTES_URL)
        # create reference to the page
        page = pages.UrbanRoutesPage(self.driver)
        page.enter_from_location(data.ADDRESS_FROM)
        page.enter_to_location(data.ADDRESS_TO)
        page.click_taxi_button()
        page.click_supportive()
        page.click_phone_number()
        page.enter_phone_number(data.PHONE_NUMBER)
        page.click_next_button()
        page.enter_phone_code(helpers.retrieve_phone_code(self.driver))
        page.click_confirm()

        # Assertion for 3. Filling in the phone number
        assert page.get_phone_number() == data.PHONE_NUMBER

    def test_fill_card(self):
        # always retrieve the urban routes server to load the website
        self.driver.get(data.URBAN_ROUTES_URL)
        # create reference to the page
        page = pages.UrbanRoutesPage(self.driver)
        page.enter_from_location(data.ADDRESS_FROM)
        page.enter_to_location(data.ADDRESS_TO)
        page.click_taxi_button()
        page.click_supportive()
        # the steps to fill card
        page.click_payment_method()
        page.click_add_card()
        page.enter_card_number(data.CARD_NUMBER)
        page.enter_card_code(data.CARD_CODE)
        page.click_link()
        page.close()

        # Assertion for 4. Adding a credit card
        assert page.get_card_text() == "Card"

    def test_comment_for_driver(self):
        # always retrieve the urban routes server to load the website
        self.driver.get(data.URBAN_ROUTES_URL)
        # create reference to the page
        page = pages.UrbanRoutesPage(self.driver)
        page.enter_from_location(data.ADDRESS_FROM)
        page.enter_to_location(data.ADDRESS_TO)
        page.click_taxi_button()
        page.click_supportive()
        # the steps to write comment for driver
        page.enter_message(data.MESSAGE_FOR_DRIVER)
        # time.sleep(2)
        # Assertion for 5. Writing a comment for the driver
        assert page.get_message() == data.MESSAGE_FOR_DRIVER

    def test_order_blanket_and_handkerchiefs(self):
        # always retrieve the urban routes server to load the website
        self.driver.get(data.URBAN_ROUTES_URL)
        # create reference to the page
        page = pages.UrbanRoutesPage(self.driver)
        page.enter_from_location(data.ADDRESS_FROM)
        page.enter_to_location(data.ADDRESS_TO)
        page.click_taxi_button()
        page.click_supportive()
        # the steps to order blanket and handkerchiefs
        page.click_toggle()
        # time.sleep(2)
        # Assertion for 6. Ordering a Blanket and handkerchiefs
        assert page.check_toggle_state() == True

    def test_order_2_ice_creams(self):
        # always retrieve the urban routes server to load the website
        self.driver.get(data.URBAN_ROUTES_URL)
        # create reference to the page
        page = pages.UrbanRoutesPage(self.driver)
        page.enter_from_location(data.ADDRESS_FROM)
        page.enter_to_location(data.ADDRESS_TO)
        page.click_taxi_button()
        page.click_supportive()
        number_of_ice_creams = 2
        # time.sleep(2)
        for i in range(number_of_ice_creams):
            page.click_count()
        # time.sleep(2)
        # Assertion for 7. Ordering 2 Ice creams
        assert page.retrieve_count() == '2'

    def test_car_search_model_appears(self):
        # always retrieve the urban routes server to load the website
        self.driver.get(data.URBAN_ROUTES_URL)
        # create reference to the page
        page = pages.UrbanRoutesPage(self.driver)
        page.enter_from_location(data.ADDRESS_FROM)
        page.enter_to_location(data.ADDRESS_TO)
        page.click_taxi_button()
        page.click_supportive()
        page.click_phone_number()
        page.enter_phone_number(data.PHONE_NUMBER)
        page.click_next_button()
        page.enter_phone_code(helpers.retrieve_phone_code(self.driver))
        page.click_confirm()
        # time.sleep(2)
        page.enter_message(data.MESSAGE_FOR_DRIVER)
        page.click_order()
        # time.sleep(2)
        # Assertion for 8. Order a taxi with the "Supportive" tariff
        assert page.retrieve_modal() == True

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
