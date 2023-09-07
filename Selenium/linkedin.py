from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import time
driver = webdriver.Chrome()
driver.get("https://www.linkedin.com")
username = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='session_key']")))
password = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='session_password']")))

#enter username and password
username.clear()
username.send_keys("urmail")
password.clear()
password.send_keys("urpass")

#target the login button and click it
button = WebDriverWait(driver, 2).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))).click()
driver.get("https://www.linkedin.com/search/results/people/?network=%5B%22S%22%5D&origin=FACETED_SEARCH&page=3&sid=dzV")
time.sleep(20)
conn_btns = driver.find_elements(By.CSS_SELECTOR ,"button[type='button']")
time.sleep(2)
btns = [btn for btn in conn_btns if btn.text == "Connect"]
#btn = btns[0]
for btn in btns :
    driver.execute_script("arguments[0].click();", btn)
    time.sleep(2)
    sen_btns = conn_btns = driver.find_elements(By.CSS_SELECTOR ,"button[aria-label='Send now']")
    sen_btn = sen_btns[0]
    driver.execute_script("arguments[0].click();", sen_btn)
    time.sleep(2)