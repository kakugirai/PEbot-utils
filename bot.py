#!/usr/bin/env python
# encoding: utf-8

from selenium import webdriver
from bs4 import BeautifulSoup
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC

URL = "https://wellness.sfc.keio.ac.jp/v3/pc.php"
USERNAME_XPATH = "/html/body/div/div[2]/div/form/table/tbody/tr[1]/td/input"
PASSWORD_XPATH = "/html/body/div/div[2]/div/form/table/tbody/tr[2]/td/input"
SUBMIT_XPATH = "/html/body/div/div[2]/div/form/table/tbody/tr[3]/td[2]/input[3]"
RESERVATION_BAR_XPATH = "/html/body/div/div[2]/ul/li[3]/a"
INNER_ALL_AVAILABLE_CLASSES_XPATH = "/html/body/div/div[3]/ul[1]/li/a"
OUTER_ALL_AVAILABLE_CLASSES_XPATH = "/html/body/div/div[3]/ul[3]/li/a"
CLASS_TABLE_XPATH = "/html/body/div/div[3]/table[2]"
CLASS_XPATH_A = "/html/body/div/div[3]/table[2]/tbody/tr/td[(text()='"
CLASS_XPATH_B = "')]/following-sibling::td[4]/a"
RESERVE_BUTTON_XPATH = "/html/body/div/div[3]/form/p/input[1]"

class Bot(object):
    """PEbot object"""
    ##
    # TODO: error handler
    ##
    def __init__(self):
        super(Bot, self).__init__()
        self.browser = webdriver.Chrome()

    def login(self, username, password):
        """login"""
        try:
            self.browser.get(URL)
            self.browser.find_element_by_xpath(USERNAME_XPATH).send_keys(username)
            self.browser.find_element_by_xpath(PASSWORD_XPATH).send_keys(password)
            self.browser.find_element_by_xpath(SUBMIT_XPATH).click()
            return "Successfully logged in."
        except Exception as err:
            raise err

    def show_available_class(self):
        """generate a HTML table object to show available class"""
        try:
            # check if the user logged in
            # if self.browser.find_element_by_xpath(USERNAME_XPATH).size() > 0:
            #     self.browser.find_element_by_xpath(OUTER_ALL_AVAILABLE_CLASSES_XPATH).click()
            # else:
            #     # switch to reservation page
            self.browser.find_element_by_xpath(RESERVATION_BAR_XPATH).click()
            #     # show all available class
            self.browser.find_element_by_xpath(INNER_ALL_AVAILABLE_CLASSES_XPATH).click()

            class_table = []
            available_class_table = BeautifulSoup(self.browser.page_source, 'lxml').find(attrs={"class" : "cool"})
            rows = available_class_table.find_all('tr')
            for row in rows[1:]:
                cols = row.find_all("td")
                class_table.append([cols[0].get_text(), cols[1].get_text(), cols[2].get_text()])
            return class_table
        except Exception as err:
            raise err

    def reserve_class(self, desired_class):
        """reserve class"""
        try:
            # switch to reservation page
            self.browser.find_element_by_xpath(RESERVATION_BAR_XPATH).click()
            # show all available class
            self.browser.find_element_by_xpath(ALL_AVAILABLE_CLASSES_XPATH).click()
            # Choose class
            class_xpath = CLASS_XPATH_A + desired_class + CLASS_XPATH_B
            self.browser.find_element_by_xpath(class_xpath).click()
            # Reserve class
            self.browser.find_element_by_xpath(RESERVE_BUTTON_XPATH).click()
            # Click again
            self.browser.find_element_by_xpath(RESERVE_BUTTON_XPATH).click()
            return "You've successfully reserved " + desired_class + "."
        except Exception as err:
            raise err

