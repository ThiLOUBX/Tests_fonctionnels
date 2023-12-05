# Generated by Selenium IDE
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

class TestCration():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_cration(self):
    self.driver.get("https://mohamedmamdouh1999.github.io/Products_CRUDS/")
    self.driver.set_window_size(1696, 1018)
    self.driver.find_element(By.ID, "inputName").click()
    self.driver.find_element(By.ID, "inputName").send_keys("Wow")
    self.driver.find_element(By.ID, "inputPrice").click()
    self.driver.find_element(By.ID, "inputPrice").send_keys("1000")
    self.driver.find_element(By.ID, "inputCondition").click()
    dropdown = self.driver.find_element(By.ID, "inputCondition")
    dropdown.find_element(By.XPATH, "//option[. = 'Excellent']").click()
    self.driver.find_element(By.ID, "btnAdd").click()
    self.driver.find_element(By.ID, "inputName").click()
    self.driver.find_element(By.ID, "inputName").send_keys("Mid")
    self.driver.find_element(By.ID, "inputPrice").click()
    self.driver.find_element(By.ID, "inputPrice").send_keys("500")
    self.driver.find_element(By.CSS_SELECTOR, ".p-2:nth-child(1)").click()
    self.driver.find_element(By.ID, "inputCategory").click()
    dropdown = self.driver.find_element(By.ID, "inputCategory")
    dropdown.find_element(By.XPATH, "//option[. = 'TV']").click()
    self.driver.find_element(By.ID, "inputCondition").click()
    dropdown = self.driver.find_element(By.ID, "inputCondition")
    dropdown.find_element(By.XPATH, "//option[. = 'Good']").click()
    self.driver.find_element(By.ID, "btnAdd").click()
    self.driver.find_element(By.ID, "inputName").click()
    self.driver.find_element(By.ID, "inputName").send_keys("Bad tv")
    self.driver.find_element(By.ID, "inputPrice").click()
    self.driver.find_element(By.ID, "inputPrice").send_keys("50")
    self.driver.find_element(By.ID, "inputCategory").click()
    self.driver.find_element(By.ID, "inputPrice").click()
    self.driver.find_element(By.ID, "inputPrice").send_keys("100")
    self.driver.find_element(By.CSS_SELECTOR, ".p-2:nth-child(1)").click()
    self.driver.find_element(By.ID, "inputCategory").click()
    dropdown = self.driver.find_element(By.ID, "inputCategory")
    dropdown.find_element(By.XPATH, "//option[. = 'TV']").click()
    self.driver.find_element(By.ID, "inputCondition").click()
    dropdown = self.driver.find_element(By.ID, "inputCondition")
    dropdown.find_element(By.XPATH, "//option[. = 'Bad']").click()
    self.driver.find_element(By.ID, "btnAdd").click()
    element = self.driver.find_element(By.ID, "btnAdd")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    element = self.driver.find_element(By.CSS_SELECTOR, "body")
    actions = ActionChains(self.driver)
    actions.move_to_element(element, 0, 0).perform()
    self.driver.find_element(By.ID, "inputName").click()
    self.driver.find_element(By.ID, "inputName").send_keys("Wow laptop")
    self.driver.find_element(By.ID, "inputPrice").click()
    self.driver.find_element(By.ID, "inputPrice").send_keys("1000")
    self.driver.find_element(By.ID, "inputCategory").click()
    dropdown = self.driver.find_element(By.ID, "inputCategory")
    dropdown.find_element(By.XPATH, "//option[. = 'LAPTOB']").click()
    self.driver.find_element(By.ID, "inputCondition").click()
    dropdown = self.driver.find_element(By.ID, "inputCondition")
    dropdown.find_element(By.XPATH, "//option[. = 'Excellent']").click()
    self.driver.find_element(By.ID, "btnAdd").click()
    element = self.driver.find_element(By.ID, "btnAdd")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    element = self.driver.find_element(By.CSS_SELECTOR, "body")
    actions = ActionChains(self.driver)
    actions.move_to_element(element, 0, 0).perform()
    self.driver.find_element(By.CSS_SELECTOR, ".p-2:nth-child(1)").click()
    self.driver.find_element(By.ID, "inputName").click()
    self.driver.find_element(By.ID, "inputName").send_keys("Mid Laptop")
    self.driver.find_element(By.ID, "inputPrice").click()
    self.driver.find_element(By.ID, "inputPrice").send_keys("500")
    self.driver.find_element(By.ID, "inputCategory").click()
    dropdown = self.driver.find_element(By.ID, "inputCategory")
    dropdown.find_element(By.XPATH, "//option[. = 'LAPTOB']").click()
    self.driver.find_element(By.ID, "inputCondition").click()
    dropdown = self.driver.find_element(By.ID, "inputCondition")
    dropdown.find_element(By.XPATH, "//option[. = 'Good']").click()
    self.driver.find_element(By.ID, "btnAdd").click()
    element = self.driver.find_element(By.ID, "btnAdd")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    element = self.driver.find_element(By.CSS_SELECTOR, "body")
    actions = ActionChains(self.driver)
    actions.move_to_element(element, 0, 0).perform()
    self.driver.find_element(By.ID, "inputName").click()
    self.driver.find_element(By.ID, "inputName").send_keys("Bad Laptop")
    self.driver.find_element(By.ID, "inputPrice").click()
    self.driver.find_element(By.ID, "inputPrice").send_keys("100")
    self.driver.find_element(By.ID, "inputCategory").click()
    dropdown = self.driver.find_element(By.ID, "inputCategory")
    dropdown.find_element(By.XPATH, "//option[. = 'LAPTOB']").click()
    self.driver.find_element(By.ID, "inputCondition").click()
    dropdown = self.driver.find_element(By.ID, "inputCondition")
    dropdown.find_element(By.XPATH, "//option[. = 'Bad']").click()
    self.driver.find_element(By.ID, "btnAdd").click()
    element = self.driver.find_element(By.ID, "btnAdd")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    element = self.driver.find_element(By.CSS_SELECTOR, "body")
    actions = ActionChains(self.driver)
    actions.move_to_element(element, 0, 0).perform()
    self.driver.find_element(By.ID, "inputName").click()
    self.driver.find_element(By.ID, "inputCondition").click()
    self.driver.find_element(By.ID, "inputCategory").click()
    self.driver.find_element(By.ID, "inputName").click()
    self.driver.find_element(By.ID, "inputName").send_keys("Wow Mobile")
    self.driver.find_element(By.ID, "inputPrice").click()
    self.driver.find_element(By.ID, "inputPrice").send_keys("1000")
    self.driver.find_element(By.ID, "inputCategory").click()
    dropdown = self.driver.find_element(By.ID, "inputCategory")
    dropdown.find_element(By.XPATH, "//option[. = 'MOBILE']").click()
    self.driver.find_element(By.ID, "inputCondition").click()
    dropdown = self.driver.find_element(By.ID, "inputCondition")
    dropdown.find_element(By.XPATH, "//option[. = 'Excellent']").click()
    self.driver.find_element(By.ID, "btnAdd").click()
    element = self.driver.find_element(By.ID, "btnAdd")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    element = self.driver.find_element(By.CSS_SELECTOR, "body")
    actions = ActionChains(self.driver)
    actions.move_to_element(element, 0, 0).perform()
    self.driver.find_element(By.ID, "inputName").click()
    self.driver.find_element(By.ID, "inputName").send_keys("Mif Mobile")
    self.driver.find_element(By.ID, "inputPrice").click()
    self.driver.find_element(By.ID, "inputPrice").send_keys("500")
    self.driver.find_element(By.ID, "inputCategory").click()
    dropdown = self.driver.find_element(By.ID, "inputCategory")
    dropdown.find_element(By.XPATH, "//option[. = 'MOBILE']").click()
    self.driver.find_element(By.ID, "inputName").click()
    self.driver.find_element(By.ID, "inputName").send_keys("Mid Mobile")
    self.driver.find_element(By.ID, "inputCondition").click()
    dropdown = self.driver.find_element(By.ID, "inputCondition")
    dropdown.find_element(By.XPATH, "//option[. = 'Good']").click()
    self.driver.find_element(By.ID, "btnAdd").click()
    self.driver.find_element(By.ID, "inputName").click()
    self.driver.find_element(By.ID, "inputName").send_keys("Bad Mobile")
    self.driver.find_element(By.ID, "inputPrice").click()
    self.driver.find_element(By.ID, "inputPrice").send_keys("100")
    self.driver.find_element(By.ID, "inputCategory").click()
    dropdown = self.driver.find_element(By.ID, "inputCategory")
    dropdown.find_element(By.XPATH, "//option[. = 'MOBILE']").click()
    self.driver.find_element(By.ID, "inputCondition").click()
    dropdown = self.driver.find_element(By.ID, "inputCondition")
    dropdown.find_element(By.XPATH, "//option[. = 'Bad']").click()
    self.driver.find_element(By.ID, "btnAdd").click()
    element = self.driver.find_element(By.ID, "btnAdd")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    element = self.driver.find_element(By.CSS_SELECTOR, "body")
    actions = ActionChains(self.driver)
    actions.move_to_element(element, 0, 0).perform()
    self.driver.find_element(By.ID, "btnClear").click()
    self.driver.find_element(By.ID, "btnClear").click()
  
