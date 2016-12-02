"""PEbot core module"""

import random
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
RESERVE_BUTTON_XPATH = "/html/body/div/div[3]/form/p/input[1]"

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

    def login(self, username, password, delay=None):
        """login"""
        if delay is None:
            delay = [0.5, 1.5]
        try:
            self.browser.get(URL)
            self.browser.find_element_by_xpath(USERNAME_XPATH).send_keys(username)
            self.browser.implicitly_wait(random.uniform(delay[0], delay[1]))
            self.browser.find_element_by_xpath(PASSWORD_XPATH).send_keys(password)
            self.browser.implicitly_wait(random.uniform(delay[0], delay[1]))
            self.browser.find_element_by_xpath(SUBMIT_XPATH).click()
            self.browser.implicitly_wait(random.uniform(delay[0], delay[1]))
            print("Successfully logged in.")
            return
        except Exception as err:
            raise err

    def show_available_class(self):
        """generate an available class list"""
        try:
            self.browser.get(URL)
            self.browser.find_element_by_xpath(OUTER_ALL_AVAILABLE_CLASSES_XPATH).click()
            class_list = []
            available_class_table = BeautifulSoup(
                self.browser.page_source, 'lxml').find("table", attrs={"class" : "cool"})
            rows = available_class_table.find_all('tr')
            for row in rows[1:]:
                cols = row.find_all("td")
                class_list.append([cols[i].get_text() for i in range(3)])
            print(class_list)
            return
        except Exception as err:
            raise err

    def reserve_class(self, date, period, classname, delay=None):
        """reserve class"""
        if delay is None:
            delay = [0.5, 1.5]
        try:
            # switch to reservation page
            self.browser.find_element_by_xpath(RESERVATION_BAR_XPATH).click()
            self.browser.implicitly_wait(random.uniform(delay[0], delay[1]))
            # show all available class
            self.browser.find_element_by_xpath(INNER_ALL_AVAILABLE_CLASSES_XPATH).click()
            self.browser.implicitly_wait(random.uniform(delay[0], delay[1]))
            # Choose class
            class_xpath = '''
            /html/body/div/div[3]/table[2]/tbody/tr[
            td[1]/text()[contains(., "{0}")] and 
            td[2]/text()[contains(., "{1}")] and 
            td[3]/text()[contains(., "{2}")]]/td[7]/a
            '''.format(date, period, classname)
            self.browser.find_element_by_xpath(class_xpath).click()
            self.browser.implicitly_wait(random.uniform(delay[0], delay[1]))
            # Reserve class
            self.browser.find_element_by_xpath(RESERVE_BUTTON_XPATH).click()
            self.browser.implicitly_wait(random.uniform(delay[0], delay[1]))
            # Click again
            self.browser.find_element_by_xpath(RESERVE_BUTTON_XPATH).click()
            print("You've successfully reserved %s class." % classname)
            return
        except Exception as err:
            raise err
