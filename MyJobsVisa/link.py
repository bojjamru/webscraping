# import libraries selenium and timepip
import pandas as pd
import csv
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# Create webdriver object
driver = webdriver.Chrome()

driver.get(
    'https://www.myvisajobs.com/Reports/2022-H1B-Visa-Sponsor.aspx?P=1')

link = driver.find_element(
            "xpath",'//*[@id="ctl00_ctl00_ContentPlaceHolder1_ContentPlaceHolder1_divcontent"]/table/tbody/tr[2]/td[2]/a').get_attribute('href')

# link_text = driver.find_element(By.PARTIAL_LINK_TEXT, "Amazon")
# print(link_text)
# link_text.click()

driver.get(link)

# link.click()
print(link)
