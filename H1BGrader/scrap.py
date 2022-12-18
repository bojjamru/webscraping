# Python program to scrape data from 'myvisajobs.com'
import csv
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# Create webdriver object
driver = webdriver.Chrome()


# Sheet1 - [Company, LCA Count]
CompanyFields = ['Company', 'LCA']
CompanyData = []


# Sheet2 - [Company, Job Title, Min Salary, Avg.Salary, Max.Salary]
JobFields = ['Company', 'Jon Title', 'Min Salary', 'Avg Salary', 'Max Salary']
JobsData = []


JobKeyWords = ['Data Scientist', 'Software', 'Analyst', 'Machine', 'DevOps', 'Cloud', 'Software System',
               'Software Quality', 'AWS', 'Azure', 'Google Cloud', 'Software Quality',  'Tableau', 'Automation', 'PowerBi']



# Get URL
driver.get('https://h1bgrader.com/reports/sponsors/lca/2022?utm_source=website&utm_medium=banner&utm_campaign=sidebar_track&utm_term=reports')



# Get Company, LCA info
for i in range(1, 51):
    company = driver.find_element(By.XPATH, '//*[@id="content"]/div/div/div[1]/table/tbody[2]/tr['+str(i)+']/td[2]/a')
    LCA = driver.find_element(By.XPATH, '//*[@id="content"]/div/div/div[1]/table/tbody[2]/tr['+str(i)+']/td[3]')
    row = [company.text, LCA.text]
    CompanyData.append(row)
    print(row)








# Save Data to CSV
CompanyListFile = "CompanyLCAList.csv"
# writing to csv file
with open(CompanyListFile, 'w') as csvfile:
    # creating a csv writer object
    csvwriter = csv.writer(csvfile)

    # writing the fields
    csvwriter.writerow(CompanyFields)

    # writing the data rows
    csvwriter.writerows(CompanyData)

