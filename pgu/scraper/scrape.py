if __name__ == '__main__':
    import os
    import sys
    sys.path.append(os.getcwd())

import os
import sys
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from pgu.logfiles.logger import logging, setup_logging


setup_logging()
class Scraper():
    """Scraper for pgu.ac.ir
    functions:
    loginSite(cred = List of username and password) returns true or false
    """

    address = {
        "dashboard" : "https://erp.pgu.ac.ir/Dashboard.aspx"
    }
    css_selector = {
        "loginTo" : "#contentMainContainer > a:nth-child(1)" ,
        "usernameField" : "#SSMUsername_txt",
        "passwordField" : "#SSMPassword_txt",
        "loginButton" : "#login_btn > input",

    }


    def __init__(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--disable-gpu')
        logging.info(f"{chrome_options}")
        if __name__ == "__main__":
            self.driver = webdriver.Edge("msedgedriver.exe")
            logging.info(f"driver:msedgedriver.exe")
        else:
            self.driver = webdriver.Chrome(chrome_options=chrome_options)
        self.driver.implicitly_wait(10)


    def get_element(self, name):
        if name not in self.css_selector:
            return None
        return self.driver.find_element_by_css_selector(self.css_selector[name])


    def loginSite(self, cred):

        user = None
        password = None
        try:
            user = cred[0]
            password = cred[1]
            logging.info(f"Username:{user}")
        except IndexError as e:
            # print("Please provide a user name and password")
            logging.warning("Not enough data provided")
            return
        self.driver.get(self.address["dashboard"])
        logging.info(f"Postion:{self.driver.current_url}")
        login = self.get_element("loginTo")
        login.click()

        self.driver.switch_to.frame(
        self.driver.find_elements_by_tag_name("iframe")[0]
        )

        userButton = self.get_element("usernameField")
        passwordButton = self.get_element("passwordField")
        userButton.clear()
        passwordButton.clear()
        userButton.send_keys(str(user))
        passwordButton.send_keys(str(password))

        button = self.get_element("loginButton")
        button.click()
        while 1:
            pass
        # print(f"User {user} succesfully logged in")
        logging.info(f"User:{user} logged in")
        return True


def main():
    scrape = Scraper()
    scrape.loginSite(["970216648","1274473506"])

if __name__ == "__main__":
    main()
