from selenium import webdriver
import time
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys


class test_sharebus():
    def all_task(self):
        driver = webdriver.Chrome(executable_path="G:\\Software\\chromedriver_win32\\chromedriver.exe")
        driver.get("https://test.sharebus.co/")
        driver.maximize_window()
        time.sleep(5)
        driver.delete_all_cookies()

        signin_button = driver.find_element(By.CSS_SELECTOR,
                                            ".btn.fw-normal.px-3.py-1.rounded-pill.sb-btn-lg.sb-btn-secondary")
        signin_button.click()
        time.sleep(5)

        email_field = driver.find_element(By.ID, "email")
        password_field = driver.find_element(By.ID, "password")
        signin_field = driver.find_element(By.CSS_SELECTOR, ".col-lg-4.col-md-6.col-sm-12 > .col-12.mt-4.mx-auto")

        email_field.send_keys("brainstation23@yopmail.com")
        password_field.send_keys("Pass@1234")
        signin_field.click()
        time.sleep(5)

        driver.delete_all_cookies()

        try:
            # Select role
            dropdown = driver.find_element(By.CSS_SELECTOR,
                                           "div[role='button'] > .p-dropdown-trigger-icon.pi.pi-chevron-down")
            time.sleep(3)
            dropdown.click()
            time.sleep(3)
            driver.find_element(By.CSS_SELECTOR, "ul[role='listbox'] > li:nth-of-type(2)  span").click()
            time.sleep(3)

            # continue
            driver.find_element(By.XPATH, "/html//div[@id='app']/div[@class='body-wrapper']//button").click()
            time.sleep(5)

            # Setup share bus
            driver.find_element(By.XPATH,
                                "/html//div[@id='app']/div[@class='body-wrapper']/div[2]/button").click()

            # From
            # Locate the dropdown element
            driver.find_element(By.ID, "startPoint").send_keys("Oslo, Norway")
            time.sleep(5)
            driver.find_element(By.ID, "startPoint").send_keys(Keys.ARROW_DOWN)
            time.sleep(5)
            driver.find_element(By.ID, "startPoint").send_keys(Keys.ENTER)
            time.sleep(5)
            driver.find_element(By.ID, "startPoint").send_keys(Keys.RETURN)
            driver.find_element(By.ID, "startPoint").send_keys(" ")

            # To
            time.sleep(5)
            driver.find_element(By.ID, "destination").send_keys("Kolbotn, Norway")
            time.sleep(3)
            driver.find_element(By.ID, "destination").send_keys(Keys.ARROW_DOWN)
            time.sleep(5)
            driver.find_element(By.ID, "destination").send_keys(Keys.ENTER)
            time.sleep(5)
            driver.find_element(By.ID, "destination").send_keys(Keys.RETURN)
            driver.find_element(By.ID, "destination").send_keys(" ")




        except:
            time.sleep(10)
            print("Exception")


test_obj = test_sharebus()
test_obj.all_task()
