import os
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
	browser = webdriver.Chrome()

	browser.get("http://suninjuly.github.io/explicit_wait2.html")
	#button = browser.find_element_by_css_selector("button:not([disabled])")
	button = WebDriverWait(browser, 14).until(
        	EC.text_to_be_present_in_element((By.ID, "price"), "$100")
   		)
	button = browser.find_element(By.CLASS_NAME, "btn.btn-primary")
	button.click()
	#message = browser.find_element(By.ID, "verify_message")
	#message = browser.find_element(By.ID, "verify_message")

	#assert "successful" in message.text
	x_element = browser.find_element(By.CSS_SELECTOR, '#input_value')
	x = x_element.text
	y = calc(x)
	print(y)
	input1 = browser.find_element(By.ID, "answer")
	input1.send_keys(y)
	button = browser.find_element(By.ID, "solve")
	button.click()

finally:
    
    time.sleep(15)
   
    browser.quit()