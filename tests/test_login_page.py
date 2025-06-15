from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
import time

class TestLoginPage:

    def test_valid_login(self,driver):
        driver.get("https://www.saucedemo.com/")

        username = driver.find_element(By.ID,"user-name")
        password = driver.find_element(By.ID,"password")
        login_btn = driver.find_element(By.ID,"login-button")

        username.send_keys("standard_user")
        password.send_keys("secret_sauce")
        login_btn.click()

        actual_url = driver.current_url
        print("Actual url:",actual_url)
        expected_url = "https://www.saucedemo.com/inventory.html"
        assert actual_url == expected_url

        time.sleep(4)

    @pytest.mark.parametrize("username,password,error",[("locked_out_user","secret_sauce","Epic sadface: Sorry, this user has been locked out."),("invalidUser","invalidPass","Epic sadface: Username and password do not match any user in this service")])
    def test_invalid_login(self,driver,username,password,error):
        driver.get("https://www.saucedemo.com/")

        username_input = driver.find_element(By.ID,"user-name")
        password_input = driver.find_element(By.ID,"password")
        login_btn = driver.find_element(By.ID,"login-button")

        username_input.send_keys(username)
        password_input.send_keys(password)
        login_btn.click()

        # actual_url = driver.current_url
        # print("Actual url:",actual_url)
        # expected_url = "https://www.saucedemo.com/inventory.html"
        # assert actual_url == expected_url

        error_msg_h3 = driver.find_element(By.TAG_NAME,"h3")
        error_msg_txt = error_msg_h3.text

        assert error_msg_txt == error

        time.sleep(4)
    


        