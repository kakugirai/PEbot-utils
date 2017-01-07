"""PEbot core module"""

import time
import random
from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup

URL = "https://wellness.sfc.keio.ac.jp/v3/pc.php"
USERNAME_XPATH = "/html/body/div/div[2]/div/form/table/tbody/tr[1]/td/input"
PASSWORD_XPATH = "/html/body/div/div[2]/div/form/table/tbody/tr[2]/td/input"
SUBMIT_XPATH = "/html/body/div/div[2]/div/form/table/tbody/tr[3]/td[2]/input[3]"
RESERVATION_BAR_XPATH = "/html/body/div/div[2]/ul/li[3]/a"
INNER_ALL_AVAILABLE_CLASSES_XPATH = "/html/body/div/div[3]/ul[1]/li/a"
OUTER_ALL_AVAILABLE_CLASSES_XPATH = "/html/body/div/div[3]/ul[3]/li/a"
CLASS_TABLE_XPATH = "/html/body/div/div[3]/table[2]"
RESERVE_BUTTON_XPATH = "/html/body/div/div[3]/form/p/input[1]"
CANCEL_BUTTON_XPATH = "/html/body/div/div[3]/form/p/input"

class Bot(object):
    """PEbot object"""
    ##
    # refactor error handler
    ##
    def __init__(self):
        super(Bot, self).__init__()
        self.browser = webdriver.Chrome()

    def tear_down(self):
        """close webdriver"""
        self.browser.quit()
        return

    def login(self, username, password, delay=None):
        """login"""
        if delay is None:
            delay = [1, 2]
        self.browser.get(URL)
        self.browser.find_element_by_xpath(USERNAME_XPATH).send_keys(username)
        # time.sleep(random.uniform(delay[0], delay[1]))
        self.browser.find_element_by_xpath(PASSWORD_XPATH).send_keys(password)
        # time.sleep(random.uniform(delay[0], delay[1]))
        self.browser.find_element_by_xpath(SUBMIT_XPATH).click()
        # time.sleep(random.uniform(delay[0], delay[1]))
        print("Successfully logged in.")
        return

    def show_available_class(self):
        """generate an available class list"""
        self.browser.get(URL)
        self.browser.find_element_by_xpath(OUTER_ALL_AVAILABLE_CLASSES_XPATH).click()
        available_class_list = []
        available_class_table = BeautifulSoup(
            self.browser.page_source, 'lxml').find("table", attrs={"class" : "cool"})
        rows = available_class_table.find_all('tr')
        for row in rows[1:]:
            cols = row.find_all("td")
            available_class_list.append(
                [cols[i].get_text() for i in range(4)] + [cols[5].get_text()])
        return available_class_list

    def show_registered_class(self):
        """generate an reserved classes list"""
        registered_class_list = []
        available_class_table = BeautifulSoup(
            self.browser.page_source, 'lxml').find("table", attrs={"class" : "cool"})
        rows = available_class_table.find_all('tr')
        for row in rows[1:]:
            cols = row.find_all("td")
            registered_class_list.append([cols[i].get_text() for i in range(4)])
        return registered_class_list

    def register_class(self, date, period, classname, delay=None):
        """register class"""
        if delay is None:
            delay = [1, 2]
        # switch to reservation page
        self.browser.find_element_by_xpath(RESERVATION_BAR_XPATH).click()
        # time.sleep(random.uniform(delay[0], delay[1]))
        # get available class list
        self.browser.find_element_by_xpath(INNER_ALL_AVAILABLE_CLASSES_XPATH).click()
        # time.sleep(random.uniform(delay[0], delay[1]))
        # Choose class
        class_xpath = '''
        /html/body/div/div[3]/table[2]/tbody/tr[
        td[1]/text()[contains(., "{0}")] and 
        td[2]/text()[contains(., "{1}")] and 
        td[3]/text()[contains(., "{2}")]]/td[7]/a
        '''.format(date, period, classname)
        self.browser.find_element_by_xpath(class_xpath).click()
        # time.sleep(random.uniform(delay[0], delay[1]))
        # Register class
        self.browser.find_element_by_xpath(RESERVE_BUTTON_XPATH).click()
        # time.sleep(random.uniform(delay[0], delay[1]))
        # Click again
        self.browser.find_element_by_xpath(RESERVE_BUTTON_XPATH).click()
        error = self.browser.find_element_by_xpath("/html/body/div/div[3]/p[2]")
        if "reserved" in error.text:
            print("You've successfully registered %s class." % classname)
        else:
            print("Oops. The class was not registered.")
        return

    def cancel_class(self, date, period, classname, delay=None):
        """register class"""
        if delay is None:
            delay = [1, 2]

        class_xpath = '''
        /html/body/div/div[3]/form/table/tbody/tr[
        td[1]/text()[contains(., "{0}")] and 
        td[2]/text()[contains(., "{1}")] and 
        td[3]/text()[contains(., "{2}")]]/td[9]/input
        '''.format(date, period, classname)
        self.browser.find_element_by_xpath(class_xpath).click()
        time.sleep(random.uniform(delay[0], delay[1]))
        self.browser.find_element_by_xpath(CANCEL_BUTTON_XPATH).click()
        error = self.browser.find_element_by_xpath("/html/body/div/div[3]/p[1]")
        if "canceled" in error.text:
            print("You've successfully canceled %s class." % classname)
        else:
            print("Oops. The class was not canceled.")
        return
