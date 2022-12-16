# Python program to scrape data from 'myvisajobs.com'
import pandas as pd
import csv
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# Create webdriver object
driver = webdriver.Chrome()


CompanyFields = ['Company', 'LCA', 'Salary']
AllCompanyList = []

JobFields = ['Company', 'Jon Title', 'Occupation']
AllJobsAndOccupationList =[]

# Get the website
for i in range(1, 5):

    # driver.get(
    #     'https://www.myvisajobs.com/Reports/2022-H1B-Visa-Sponsor.aspx?P='+str(i))

    # # Make Python sleep for some time
    # sleep(2)

    for r in range(2, 25):
        driver.get(
            'https://www.myvisajobs.com/Reports/2022-H1B-Visa-Sponsor.aspx?P='+str(i))

        # Make Python sleep for some time
        sleep(2)
        if r == 14:
            r = r+1
        Company = driver.find_element(
            "xpath", '//*[@id="ctl00_ctl00_ContentPlaceHolder1_ContentPlaceHolder1_divcontent"]/table/tbody/tr['+str(r)+']/td[2]/a')
        # print(company.text)
        LCA = driver.find_element(
            "xpath", '//*[@id="ctl00_ctl00_ContentPlaceHolder1_ContentPlaceHolder1_divcontent"]/table/tbody/tr['+str(r)+']/td[3]/a')
        Salary = driver.find_element(
            "xpath", '//*[@id="ctl00_ctl00_ContentPlaceHolder1_ContentPlaceHolder1_divcontent"]/table/tbody/tr['+str(r)+']/td[4]')

        row = [Company.text, LCA.text, Salary.text]
        AllCompanyList.append(row)
        print(row)

        temp = Company.text

        # click  Company Link
        CompanyLink = Company.get_attribute('href')
        driver.get(CompanyLink)
        OccupationLink = driver.find_element(
            "xpath", '//*[@id="toc"]/li[5]/a').get_attribute('href')
        driver.get(OccupationLink)

        # list of jobs and occupations
        for j in range(2, 11):
            Jobs = driver.find_element(
                "xpath", '//*[@id="ctl00_ctl00_ContentPlaceHolder1_ContentPlaceHolder1_divContent"]/div/table/tbody/tr[1]/td[1]/table/tbody/tr['+str(j)+']/td[2]')
            Occupation = driver.find_element(
                "xpath", '//*[@id="ctl00_ctl00_ContentPlaceHolder1_ContentPlaceHolder1_divContent"]/div/table/tbody/tr[1]/td[2]/table/tbody/tr['+str(j)+']/td[2]')

            jobsOccupation = [temp, Jobs.text, Occupation.text]
            print(jobsOccupation)
            AllJobsAndOccupationList.append(jobsOccupation)
            # print(Jobs.text, Occupation.text)



        # driver.get(
        # 'https://www.myvisajobs.com/Reports/2022-H1B-Visa-Sponsor.aspx?P='+str(i))


# print all rows
# print(AllRows)

# Company, LCA, Avg. Salary CSV
# name of csv file
CompanyListFile = "MyJobsVisa.csv"
# writing to csv file
with open(CompanyListFile, 'w') as csvfile:
    # creating a csv writer object
    csvwriter = csv.writer(csvfile)

    # writing the fields
    csvwriter.writerow(CompanyFields)

    # writing the data rows
    csvwriter.writerows(AllCompanyList )



# Write Jobs and occupation csv
JobsAndOccupationsFile = "JobsAndOccupations.csv"
with open(JobsAndOccupationsFile, 'w') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(JobFields)
    csvwriter.writerows(AllJobsAndOccupationList)



#  read csv
# pd.read_csv("./myjobsvisa.csv")

# Use selenium.click


# //*[@id="toc"]/li[5]/a
# //*[@id="toc"]/li[5]/a
