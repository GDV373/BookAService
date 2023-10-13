# Generated by Selenium IDE and refined by george attard
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support import expected_conditions as EC


class TestClietnAddDeleteCar:
    def setup_method(self, method):
        self.driver = webdriver.Chrome()
        self.vars = {}

    def teardown_method(self, method):
        self.driver.quit()

    def test_clietnAddDeleteCar(self):
        self.driver.get("https://bookaservice-32a4c779d8fe.herokuapp.com/")
        self.driver.set_window_size(2576, 1408)
        time.sleep(2)
        self.driver.find_element(
            By.XPATH, "//a[contains(text(),\'Log In / Register\')]").click()
        time.sleep(5)
        self.driver.find_element(By.XPATH, "//div/div[3]/div").click()
        time.sleep(1)
        self.driver.find_element(
            By.CSS_SELECTOR, ".col-lg-4:nth-child(3) .text-secondary"
        ).click()
        self.driver.find_element(
            By.NAME, "email").send_keys("test12345@gmail.com")
        self.driver.find_element(By.NAME, "password").send_keys("123456")
        self.driver.find_element(By.NAME, "email").click()
        self.driver.find_element(By.NAME, "password").click()
        self.driver.find_element(
            By.CSS_SELECTOR,
            "button:nth-child(9)").click()
        self.driver.find_element(
            By.CSS_SELECTOR,
            ".nav-item:nth-child(3)").click()
        self.driver.find_element(By.CSS_SELECTOR, ".btn-success").click()
        self.driver.find_element(By.ID, "id_Brand").click()
        self.driver.find_element(By.ID, "id_Brand").send_keys("toyota")
        self.driver.find_element(By.ID, "id_Model").click()
        self.driver.find_element(By.ID, "id_Model").send_keys("yaris")
        self.driver.find_element(By.ID, "id_Fuel_Type").click()
        dropdown = self.driver.find_element(By.ID, "id_Fuel_Type")
        dropdown.find_element(By.XPATH, "//option[. = 'Petrol']").click()
        self.driver.find_element(By.ID, "id_VIN").click()
        self.driver.find_element(By.ID, "id_VIN").send_keys("7418529631547854")
        self.driver.find_element(By.ID, "id_NumPlate").click()
        self.driver.find_element(By.ID, "id_NumPlate").send_keys("TOY333")
        self.driver.find_element(By.CSS_SELECTOR, "form > .btn").click()
        self.driver.find_element(
            By.CSS_SELECTOR,
            "tr:nth-child(2) .btn-danger").click()
        self.driver.find_element(By.CSS_SELECTOR, ".py-4").click()


class TestClientUserSettingUpdate:
    def setup_method(self, method):
        self.driver = webdriver.Chrome()
        self.vars = {}

    def teardown_method(self, method):
        self.driver.quit()

    def test_clientUserSettingUpdate(self):
        self.driver.get("https://bookaservice-32a4c779d8fe.herokuapp.com/")
        self.driver.set_window_size(2576, 1408)
        time.sleep(2)
        self.driver.find_element(By.CSS_SELECTOR, ".py-4").click()
        time.sleep(1)
        self.driver.find_element(
            By.CSS_SELECTOR, ".col-lg-4:nth-child(3) .text-secondary"
        ).click()
        time.sleep(1)
        self.driver.find_element(
            By.NAME, "email").send_keys("test12345@gmail.com")
        self.driver.find_element(By.NAME, "password").send_keys("123456")
        self.driver.find_element(By.NAME, "email").click()
        self.driver.find_element(By.NAME, "password").click()
        self.driver.find_element(
            By.CSS_SELECTOR,
            "button:nth-child(9)").click()
        self.driver.find_element(
            By.CSS_SELECTOR,
            ".nav-item:nth-child(5)").click()
        self.driver.find_element(
            By.CSS_SELECTOR, ".profile:nth-child(2) .btn-warning"
        ).click()
        self.driver.find_element(By.ID, "id_first_name").click()
        self.driver.find_element(By.ID, "id_first_name").clear()
        self.driver.find_element(
            By.ID, "id_first_name").send_keys("Georgetest")
        self.driver.find_element(By.ID, "id_last_name").click()
        self.driver.find_element(By.ID, "id_last_name").clear()
        self.driver.find_element(By.ID, "id_last_name").send_keys("Attardtest")
        self.driver.find_element(
            By.CSS_SELECTOR,
            ".btn-primary:nth-child(4)").click()
        self.driver.find_element(
            By.CSS_SELECTOR, ".profile:nth-child(3) .btn-warning"
        ).click()
        self.driver.find_element(By.ID, "id_Location").click()
        dropdown = self.driver.find_element(By.ID, "id_Location")
        dropdown.find_element(By.XPATH, "//option[. = 'Attard']").click()
        self.driver.find_element(By.ID, "id_Mobile").click()
        self.driver.find_element(By.ID, "id_Mobile").click()
        element = self.driver.find_element(By.ID, "id_Mobile")
        actions = ActionChains(self.driver)
        actions.double_click(element).perform()
        self.driver.find_element(By.ID, "id_Mobile").clear()
        self.driver.find_element(By.ID, "id_Mobile").send_keys("77777777")
        self.driver.find_element(By.ID, "id_ID_number").click()
        self.driver.find_element(By.ID, "id_ID_number").click()
        element = self.driver.find_element(By.ID, "id_ID_number")
        actions = ActionChains(self.driver)
        actions.double_click(element).perform()
        self.driver.find_element(By.ID, "id_ID_number").clear()
        self.driver.find_element(By.ID, "id_ID_number").send_keys("1255566788")
        self.driver.find_element(By.ID, "id_Address").click()
        self.driver.find_element(By.ID, "id_Address").clear()
        self.driver.find_element(By.ID, "id_Address").send_keys(
            "3B Flat 6 Lisle Adamtest"
        )
        self.driver.find_element(By.CSS_SELECTOR, "form > .btn").click()
        self.driver.find_element(
            By.CSS_SELECTOR, ".profile:nth-child(2) .btn-warning"
        ).click()
        self.driver.find_element(By.ID, "id_first_name").click()
        self.driver.find_element(By.ID, "id_first_name").click()
        self.driver.find_element(By.ID, "id_first_name").clear()
        self.driver.find_element(By.ID, "id_first_name").send_keys("George")
        self.driver.find_element(By.ID, "id_last_name").click()
        self.driver.find_element(By.ID, "id_last_name").click()
        self.driver.find_element(By.ID, "id_last_name").clear()
        self.driver.find_element(By.ID, "id_last_name").send_keys("Attard")
        self.driver.find_element(
            By.CSS_SELECTOR,
            ".btn-primary:nth-child(4)").click()
        self.driver.find_element(
            By.CSS_SELECTOR, ".profile:nth-child(3) .btn-warning"
        ).click()
        self.driver.find_element(By.ID, "id_Location").click()
        dropdown = self.driver.find_element(By.ID, "id_Location")
        dropdown.find_element(By.XPATH, "//option[. = 'L-Iklin']").click()
        self.driver.find_element(By.ID, "id_Mobile").click()
        self.driver.find_element(By.ID, "id_Mobile").click()
        element = self.driver.find_element(By.ID, "id_Mobile")
        actions = ActionChains(self.driver)
        actions.double_click(element).perform()
        self.driver.find_element(By.ID, "id_Mobile").clear()
        self.driver.find_element(By.ID, "id_Mobile").send_keys("88888888")
        self.driver.find_element(By.ID, "id_ID_number").click()
        self.driver.find_element(By.ID, "id_ID_number").click()
        element = self.driver.find_element(By.ID, "id_ID_number")
        actions = ActionChains(self.driver)
        actions.double_click(element).perform()
        self.driver.find_element(By.ID, "id_ID_number").click()
        self.driver.find_element(By.ID, "id_ID_number").clear()
        self.driver.find_element(By.ID, "id_ID_number").send_keys("1555566788")
        self.driver.find_element(By.ID, "id_Address").click()
        self.driver.find_element(By.ID, "id_Address").click()
        self.driver.find_element(By.ID, "id_Address").clear()
        self.driver.find_element(
            By.ID, "id_Address").send_keys("3B Flat 6 Lisle Adam")
        self.driver.find_element(By.CSS_SELECTOR, "form > .btn").click()
        self.driver.find_element(By.CSS_SELECTOR, ".py-4").click()


class TestClientNewAccountNewPassDeleteAcc:
    def setup_method(self, method):
        self.driver = webdriver.Chrome()
        self.vars = {}

    def teardown_method(self, method):
        self.driver.quit()

    def test_clientNewAccountNewPassDeleteAcc(self):
        self.driver.get("https://bookaservice-32a4c779d8fe.herokuapp.com/")
        self.driver.set_window_size(2576, 1408)
        time.sleep(2)
        self.driver.find_element(By.CSS_SELECTOR, ".py-4").click()
        time.sleep(2)
        self.driver.find_element(By.LINK_TEXT, "Click Here").click()
        self.driver.find_element(By.ID, "email").send_keys(
            "selentestcust@gmail.com")
        self.driver.find_element(By.ID, "pass1").send_keys("1234")
        self.driver.find_element(By.ID, "fname").click()
        self.driver.find_element(By.ID, "fname").send_keys("TestRegName")
        self.driver.find_element(By.ID, "lname").click()
        self.driver.find_element(By.ID, "lname").send_keys("TetsRegLname")
        self.driver.find_element(By.ID, "email").click()
        self.driver.find_element(By.ID, "location").click()
        dropdown = self.driver.find_element(By.ID, "location")
        dropdown.find_element(By.XPATH, "//option[. = 'Birkirkara']").click()
        self.driver.find_element(By.ID, "address").click()
        self.driver.find_element(By.ID, "address").send_keys("test adress 3b")
        self.driver.find_element(By.ID, "number").click()
        self.driver.find_element(By.ID, "number").send_keys("36925814")
        self.driver.find_element(By.ID, "id_number").click()
        self.driver.find_element(By.ID, "id_number").send_keys("12345644TS")
        self.driver.find_element(By.ID, "pass1").click()
        self.driver.find_element(By.ID, "pass1").click()
        self.driver.find_element(By.ID, "pass1").click()
        element = self.driver.find_element(By.ID, "pass1")
        actions = ActionChains(self.driver)
        actions.double_click(element).perform()
        self.driver.find_element(By.ID, "pass2").click()
        self.driver.find_element(By.ID, "pass2").send_keys("1234")
        time.sleep(1)
        self.driver.find_element(By.CSS_SELECTOR, ".btn:nth-child(12)").click()
        self.driver.find_element(
            By.CSS_SELECTOR,
            ".nav-item:nth-child(5)").click()
        self.driver.find_element(By.CSS_SELECTOR, ".btn-info").click()
        self.driver.find_element(By.ID, "id_old_password").click()
        self.driver.find_element(By.ID, "id_old_password").send_keys("1234")
        self.driver.find_element(By.ID, "id_new_password1").click()
        self.driver.find_element(
            By.ID, "id_new_password1").send_keys("sel12345!")
        self.driver.find_element(By.CSS_SELECTOR, "li:nth-child(1)").click()
        self.driver.find_element(By.ID, "id_new_password2").click()
        self.driver.find_element(By.ID, "id_new_password2").click()
        self.driver.find_element(
            By.ID, "id_new_password2").send_keys("sel12345!")
        self.driver.find_element(By.CSS_SELECTOR, "form > .btn").click()
        self.driver.find_element(By.CSS_SELECTOR, ".py-4").click()
        self.driver.find_element(By.CSS_SELECTOR, ".py-4").click()
        time.sleep(2)
        self.driver.find_element(
            By.CSS_SELECTOR, ".col-lg-4:nth-child(3) .text-secondary"
        ).click()
        self.driver.find_element(By.NAME, "email").send_keys(
            "selentestcust@gmail.com")
        self.driver.find_element(By.NAME, "password").send_keys("1234")
        self.driver.find_element(By.NAME, "email").click()
        self.driver.find_element(By.NAME, "email").click()
        self.driver.find_element(By.NAME, "password").click()
        self.driver.find_element(By.NAME, "password").click()
        self.driver.find_element(By.NAME, "password").click()
        element = self.driver.find_element(By.NAME, "password")
        actions = ActionChains(self.driver)
        actions.double_click(element).perform()
        self.driver.find_element(
            By.CSS_SELECTOR,
            "button:nth-child(9)").click()
        self.driver.find_element(By.NAME, "email").send_keys(
            "selentestcust@gmail.com")
        self.driver.find_element(By.NAME, "password").send_keys("1234")
        self.driver.find_element(By.NAME, "password").click()
        self.driver.find_element(By.NAME, "password").click()
        self.driver.find_element(By.NAME, "password").click()
        element = self.driver.find_element(By.NAME, "password")
        actions = ActionChains(self.driver)
        actions.double_click(element).perform()
        self.driver.find_element(By.NAME, "password").click()
        self.driver.find_element(By.NAME, "password").clear()
        self.driver.find_element(By.NAME, "password").send_keys("sel12345!")
        time.sleep(2)
        self.driver.find_element(
            By.CSS_SELECTOR,
            "button:nth-child(9)").click()
        time.sleep(2)
        self.driver.find_element(
            By.CSS_SELECTOR,
            ".nav-item:nth-child(5)").click()
        time.sleep(2)
        self.driver.find_element(By.ID, "deleteAccountButton").click()
        time.sleep(2)
        self.driver.find_element(By.ID, "confirmDeleteButton").click()
        time.sleep(2)
        self.driver.find_element(By.CSS_SELECTOR, ".py-4").click()
        time.sleep(2)
        self.driver.find_element(
            By.CSS_SELECTOR, ".col-lg-4:nth-child(3) .text-secondary"
        ).click()
        self.driver.find_element(By.NAME, "email").send_keys(
            "selentestcust@gmail.com")
        self.driver.find_element(By.NAME, "password").send_keys("1234")
        self.driver.find_element(By.NAME, "email").click()
        self.driver.find_element(By.NAME, "email").click()
        self.driver.find_element(By.NAME, "password").click()
        self.driver.find_element(By.NAME, "password").click()
        self.driver.find_element(By.NAME, "password").click()
        element = self.driver.find_element(By.NAME, "password")
        actions = ActionChains(self.driver)
        actions.double_click(element).perform()
        self.driver.find_element(By.NAME, "password").send_keys("sel12345!")
        self.driver.find_element(
            By.CSS_SELECTOR,
            "button:nth-child(9)").click()
        self.driver.find_element(By.NAME, "email").send_keys(
            "selentestcust@gmail.com")
        self.driver.find_element(By.NAME, "password").send_keys("1234")
        self.driver.find_element(By.CSS_SELECTOR, ".alert").click()
        self.driver.find_element(By.CSS_SELECTOR, ".alert").click()
        element = self.driver.find_element(By.CSS_SELECTOR, ".alert")
        actions = ActionChains(self.driver)
        actions.double_click(element).perform()
        self.driver.find_element(By.CSS_SELECTOR, ".alert").click()


class TestClientLoginAndTabsLoading:
    def setup_method(self, method):
        self.driver = webdriver.Chrome()
        self.vars = {}

    def teardown_method(self, method):
        self.driver.quit()

    def test_clientLoginAndTabsLoading(self):
        self.driver.get("https://bookaservice-32a4c779d8fe.herokuapp.com/")
        self.driver.set_window_size(2576, 1408)
        self.driver.find_element(By.CSS_SELECTOR, ".py-4").click()
        time.sleep(2)
        self.driver.find_element(
            By.CSS_SELECTOR, ".col-lg-4:nth-child(3) .text-secondary"
        ).click()
        self.driver.find_element(
            By.NAME, "email").send_keys("test12345@gmail.com")
        self.driver.find_element(By.NAME, "password").send_keys("123456")
        self.driver.find_element(By.NAME, "email").click()
        self.driver.find_element(By.NAME, "password").click()
        self.driver.find_element(
            By.CSS_SELECTOR,
            "button:nth-child(9)").click()
        self.driver.find_element(
            By.CSS_SELECTOR,
            ".nav-item:nth-child(2)").click()
        self.driver.find_element(
            By.CSS_SELECTOR,
            ".nav-item:nth-child(3)").click()
        self.driver.find_element(
            By.CSS_SELECTOR,
            ".nav-item:nth-child(5)").click()
        self.driver.find_element(By.CSS_SELECTOR, ".py-4").click()


class TestClientCreateBooking:
    def setup_method(self, method):
        self.driver = webdriver.Chrome()
        self.vars = {}

    def teardown_method(self, method):
        self.driver.quit()

    def test_clientCreateBooking(self):
        self.driver.get("https://bookaservice-32a4c779d8fe.herokuapp.com/")
        self.driver.set_window_size(2576, 1408)
        self.driver.find_element(By.CSS_SELECTOR, ".py-4").click()
        time.sleep(2)
        self.driver.find_element(
            By.CSS_SELECTOR, ".col-lg-4:nth-child(3) .ps-4"
        ).click()
        time.sleep(2)
        self.driver.find_element(
            By.CSS_SELECTOR, ".col-lg-4:nth-child(3) .text-secondary"
        ).click()
        self.driver.find_element(
            By.NAME, "email").send_keys("test12345@gmail.com")
        self.driver.find_element(By.NAME, "password").send_keys("123456")
        self.driver.find_element(By.NAME, "email").click()
        self.driver.find_element(By.NAME, "password").click()
        time.sleep(2)
        self.driver.find_element(
            By.CSS_SELECTOR,
            "button:nth-child(9)").click()
        time.sleep(2)
        self.driver.find_element(
            By.CSS_SELECTOR,
            ".nav-item:nth-child(2)").click()
        time.sleep(1)
        self.driver.find_element(By.ID, "provider").click()
        dropdown = self.driver.find_element(By.ID, "provider")
        dropdown.find_element(
            By.XPATH, "//option[. = 'D_Service_Stop']").click()
        time.sleep(2)
        self.driver.find_element(By.ID, "service").click()
        time.sleep(1)
        dropdown = self.driver.find_element(By.ID, "service")
        element = self.driver.find_element(
            By.XPATH, '//*[@id="service"]/option[3]')
        element.click()
        time.sleep(1)
        self.driver.find_element(By.ID, "car").click()
        dropdown = self.driver.find_element(By.ID, "car")
        element = self.driver.find_element(
            By.XPATH, '//*[@id="car"]/option[2]')
        element.click()
        time.sleep(1)
        self.driver.find_element(By.NAME, "date").click()
        self.driver.find_element(By.CSS_SELECTOR, ".table .next > .fa").click()
        self.driver.find_element(By.CSS_SELECTOR, ".table .next > .fa").click()
        element = self.driver.find_element(
            By.CSS_SELECTOR, ".table .next > .fa")
        actions = ActionChains(self.driver)
        actions.double_click(element).perform()
        self.driver.find_element(By.CSS_SELECTOR, ".table .next > .fa").click()
        self.driver.find_element(By.CSS_SELECTOR, ".table .next > .fa").click()
        self.driver.find_element(By.NAME, "details").click()
        self.driver.find_element(By.NAME, "details").send_keys("Battery test")
        self.driver.find_element(By.CSS_SELECTOR, ".py-4").click()