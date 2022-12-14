# Python program to scrape table from website

# import libraries selenium and time
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# Create webdriver object
driver = webdriver.Chrome()

# Get the website
driver.get(
    "https://www.myvisajobs.com/Reports/2022-H1B-Visa-Sponsor.aspx")

# Make Python sleep for some time
sleep(2)

# Obtain the number of rows in body
# rows = driver.find_element("xpath", '//*[@id="ctl00_ctl00_ContentPlaceHolder1_ContentPlaceHolder1_divcontent"]/table/tbody/tr[3]/td[2]/a')
# print(rows.text)


for r in range(2, 25):
#    error = driver.find_element(By.CLASS_NAME, 'adsbygoogle')
#    if(error != ""):
#         print("Error")
#    else:



        if r == 14:
            r = r+1
        value = driver.find_element(
        "xpath", '//*[@id="ctl00_ctl00_ContentPlaceHolder1_ContentPlaceHolder1_divcontent"]/table/tbody/tr['+str(r)+']/td[2]/a')
        print(value.text)

# Use selenium.click