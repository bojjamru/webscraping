# Python program to scrape table from website

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


fields = ['Company', 'LCA', 'Salary']
AllRows = []

# Get the website
for i in range(1, 5):

    driver.get(
        'https://www.myvisajobs.com/Reports/2022-H1B-Visa-Sponsor.aspx?P='+str(i))

    # Make Python sleep for some time
    sleep(2)

    for r in range(2, 25):
        if r == 14:
            r = r+1
        Company = driver.find_element(
            "xpath", '//*[@id="ctl00_ctl00_ContentPlaceHolder1_ContentPlaceHolder1_divcontent"]/table/tbody/tr['+str(r)+']/td[2]/a')
        # print(company.text)
        LCA = driver.find_element(
            "xpath", '//*[@id="ctl00_ctl00_ContentPlaceHolder1_ContentPlaceHolder1_divcontent"]/table/tbody/tr['+str(r)+']/td[3]/a')
        Salary = driver.find_element(
            "xpath", '//*[@id="ctl00_ctl00_ContentPlaceHolder1_ContentPlaceHolder1_divcontent"]/table/tbody/tr['+str(r)+']/td[4]')
        # print(Company.text, "|",
        #       LCA.text, "|", Salary.text)

        row = [Company.text, LCA.text, Salary.text]
        AllRows.append(row)
        # print(row)

# print all rows
# print(AllRows)


# name of csv file
filename = "myjobsvisa.csv"

# writing to csv file
with open(filename, 'w') as csvfile:
    # creating a csv writer object
    csvwriter = csv.writer(csvfile)

    # writing the fields
    csvwriter.writerow(fields)

    # writing the data rows
    csvwriter.writerows(AllRows)


#  read csv
pd.read_csv("./myjobsvisa.csv")

# Use selenium.click


