import os
import sys
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


driver = None

def loginSite(cred):
    global driver
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')
    driver = webdriver.Chrome(chrome_options=chrome_options)
    # logging.info(f"{chrome_options}")
    driver.implicitly_wait(10)
    user = None
    password = None
    try:
        user = cred[0]
        password = cred[1]
        # logging.info(f"Username:{user}")
    except IndexError as e:
<<<<<<< HEAD
        print("Please provide a user name and password")
        return False
=======
        # print("Please provide a user name and password")
        # logging.warning("Not enough data provided")
        return
>>>>>>> 6a707f2029c91e42161d0d125d4db5327d152bb4
    driver.get("https://erp.pgu.ac.ir/Dashboard.aspx")
    # logging.info(f"Postion:https://erp.pgu.ac.ir/Dashboard.aspx")
    login = driver.find_element_by_css_selector(
    "#contentMainContainer > a:nth-child(1)"
    )
    login.click()
    driver.switch_to.frame(driver.find_elements_by_tag_name("iframe")[0])
    # driver.switch_to.frame(driver.find_element_by_css_selector("#iframe_040101"))
    userButton = driver.find_element_by_css_selector(
    "#SSMUsername_txt")
    passwordButton = driver.find_element_by_name("SSMPassword_txt")
    userButton.clear()
    passwordButton.clear()
    userButton.send_keys(str(user))
    passwordButton.send_keys(str(password))
    button = driver.find_element_by_css_selector("#login_btn > input")
    button.click()
    driver.quit()
    print(f"User {user} succesfully logged in")
    return True


def main():
    commands = {
    "login": loginSite,
    }
    try:
        cm = sys.argv[1]
        if cm not in commands:
            print("Invalid command!")
            return
        func = commands[cm]
        func()
    except IndexError as e:
        print("No commands!")
        return

if __name__ == "__main__":
    main()
