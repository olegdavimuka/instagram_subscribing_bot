import os
import time

from selenium import webdriver
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.webdriver.common.by import By

INSTAGRAM_USERNAME = os.environ.get("INSTAGRAM_USERNAME")
INSTAGRAM_PASSWORD = os.environ.get("INSTAGRAM_PASSWORD")
chrome_driver_path = "C:\Coding\chromedriver.exe"
instagram_path = "https://www.instagram.com"
instagram_account = "therock"


class InstagramFollowingBot:
    def __init__(self, web_driver):
        self.driver = webdriver.Chrome(executable_path=web_driver)

    def login(self):
        self.driver.get(instagram_path)
        time.sleep(2)
        login_input = self.driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[1]/div/label/input')
        password_input = self.driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[2]/div/label/input')
        login_button = self.driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[3]/button')
        login_input.send_keys(INSTAGRAM_USERNAME)
        password_input.send_keys(INSTAGRAM_PASSWORD)
        login_button.click()
        time.sleep(5)

    def find_followers(self):
        self.driver.get(f"{instagram_path}/{instagram_account}")
        time.sleep(5)
        followers_button = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/section/main/div/header/section'
                                                              '/ul/li[3]/a')
        followers_button.click()
        time.sleep(2)
        modal = self.driver.find_element(By.XPATH, '/html/body/div[4]/div/div/div[2]')
        for i in range(10):
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", modal)
            time.sleep(2)

    def follow(self):
        all_buttons = self.driver.find_element(By.CSS_SELECTOR, "li button")
        for button in all_buttons:
            try:
                button.click()
                time.sleep(1)
            except ElementClickInterceptedException:
                cancel_button = self.driver.find_element(By.XPATH, '/html/body/div[5]/div/div/div/div[3]/button[2]')
                cancel_button.click()


instagram_bot = InstagramFollowingBot(chrome_driver_path)
instagram_bot.login()
instagram_bot.find_followers()
instagram_bot.follow()
