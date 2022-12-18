# Python program to scrape data from 'myvisajobs.com'
import csv
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
# Create webdriver object
driver = webdriver.Chrome()


# Sheet2 - [Company, Job Title, Min Salary, Avg.Salary, Max.Salary]
JobFields = ['Company', 'Job Title', 'Min Salary', 'Avg Salary', 'Max Salary']
JobsData = []


Companies = ['Amazon.com Services LLC','Cognizant Technology Solutions US Corp','Google LLC','Microsoft Corporation','Tata Consultancy Services Limited','Ernst & Young US LLP','Infosys Limited','Meta Platforms INC','Deloitte Consulting LLP','Amazon Web Services INC','Apple INC','Intel Corporation','Capgemini America INC','Wal Mart Associates INC','Jpmorgan Chase & CO','HCL America INC','Accenture LLP','Qualcomm Technologies INC','Wipro Limited','Compunnel Software Group INC','Tekorg INC','Cisco Systems INC','IBM Corporation','Amazon Development Center US INC','Deloitte & Touche LLP','International Business Machines Corporation','Larsen & Toubro Infotech Limited','Mphasis Corporation','Tech Mahindra Americas INC','Linkedin Corporation','Goldman Sachs & CO LLC','Fidelity Technology Group LLC','Salesforce.com INC','Salesforce INC','Pricewaterhousecoopers Advisory Services LL','CTesla INC','Mindtree Limited','Oracle America INC','Vmware INC','Citibank NA','Paypal INC','Ford Motor Company','Uber Technologies INC','Cummins INC','Atos Syntel INC','Mastech Digital Technologies INC','Facebook INC','CGI Technologies and Solutions INC','Capital One Services LLC',  'Adobe INC']



JobKeyWords = {'Data Scientist': 0, 'Software Developer': 0, 'Software Engineer': 0, 'Analyst': 0, 'Machine': 0, 'DevOps': 0, 'Cloud': 0, 'Software System': 0,
               'Software Quality': 0, 'AWS': 0, 'Azure': 0, 'Google Cloud': 0, 'Software Quality': 0,  'Tableau': 0, 'Automation': 0, 'PowerBi': 0}





def H1B_Url():
    driver.get('https://h1bgrader.com/')


def SearchCompany(i):
        # Search Company Data
    search = driver.find_element(By.ID, 'employer')
    print(i)
    # search.click()
    search.send_keys(i)
    buttonClick = driver.find_element(By.CLASS_NAME, 'search-button')
    buttonClick.click()
    # Select Job_Title Button
    driver.find_element(By.ID, 'employer-job-tabb').click()



def Jobs():
    for i in range(1, 11):
        # get Job Title
        job = driver.find_element(By.XPATH, '//*[@id="salary-data-table"]/tbody/tr['+str(i)+']/td[1]/a')
        # print(job.text)

        try:
            if job in JobKeyWords:
                print(job.text)
                JobKeyWords[job] += 1
                print(JobKeyWords[job])
                print("Job KeyBoards", JobKeyWords)
            else:
                print("Job title Doesn't match in", JobKeyWords )
        except:
            print("Job title Doesn't match")



for i in Companies:

    try:
        H1B_Url()
        SearchCompany(i)
        Jobs()


    except:
        print("Error Occured")


# search.send_keys(Keys.ENTER)


sleep(30)
