from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from time import sleep
import os


USERNAME = os.environ["USERNAME"]
PASSWORD = os.environ["PASSWORD"]
URL = os.environ["URL"]

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.set_window_size(1200, 900)
driver.get(URL)


# "LOG IN"ボタンをクリック
login_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="t2067052097"]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a'))
)
login_button.click()

# "FACEBOOKでログイン"ボタンをクリック
google_login_button = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.XPATH, '//*[@id="t338671021"]/div/div[1]/div/div[1]/div/div/div[2]/div[2]/span/div[3]/button'))
)
google_login_button.click()

# Facebookログイン用のポップアップが表示されるまで待機
WebDriverWait(driver, 10).until(
    EC.number_of_windows_to_be(2)
)

# 新しいウィンドウ（Facebookログイン）に切り替え
driver.switch_to.window(driver.window_handles[1])

# Facebookのメールアドレスとパスワードを入力
email_field = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, 'email'))
)
email_field.send_keys(USERNAME)

password_field = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, 'pass'))
)
password_field.send_keys(PASSWORD)
password_field.send_keys(Keys.RETURN)

# 元のウィンドウ（Tinder）に戻る
WebDriverWait(driver, 10).until(
    EC.number_of_windows_to_be(1)
)
driver.switch_to.window(driver.window_handles[0])

admit_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="t338671021"]/div/div[1]/div/div/div[3]/button[1]'))
)
admit_button.click()
no_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="t338671021"]/div/div[1]/div/div/div[3]/button[2]'))
)
no_button.click()

like_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="t2067052097"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div/div[3]/div/div[4]/button'))
)
like_button.click()

for i in range(99):
    like_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="t2067052097"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div/div[4]/div/div[4]/button'))
    )
    like_button.click()

