# Python program to scrape data from 'myvisajobs.com'
import csv
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import nltk
# Create webdriver object
driver = webdriver.Chrome()


# Sheet2 - [Company, Job Title, Min Salary, Avg.Salary, Max.Salary]
JobFields = ['Company', 'Job Title', 'Min Salary', 'Avg Salary', 'Max Salary']
JobsData = []


# Companies = ['Amazon.com Services LLC','Cognizant Technology Solutions US Corp','Google LLC','Microsoft Corporation','Tata Consultancy Services Limited','Ernst & Young US LLP','Infosys Limited','Meta Platforms INC','Deloitte Consulting LLP','Amazon Web Services INC','Apple INC','Intel Corporation','Capgemini America INC','Wal Mart Associates INC','Jpmorgan Chase & CO','HCL America INC','Accenture LLP','Qualcomm Technologies INC','Wipro Limited','Compunnel Software Group INC','Tekorg INC','Cisco Systems INC','IBM Corporation','Amazon Development Center US INC','Deloitte & Touche LLP','International Business Machines Corporation','Larsen & Toubro Infotech Limited','Mphasis Corporation','Tech Mahindra Americas INC','Linkedin Corporation','Goldman Sachs & CO LLC','Fidelity Technology Group LLC','Salesforce.com INC','Salesforce INC','Pricewaterhousecoopers Advisory Services LL','CTesla INC','Mindtree Limited','Oracle America INC','Vmware INC','Citibank NA','Paypal INC','Ford Motor Company','Uber Technologies INC','Cummins INC','Atos Syntel INC','Mastech Digital Technologies INC','Facebook INC','CGI Technologies and Solutions INC','Capital One Services LLC',  'Adobe INC']
Companies = ['Amazon.com Services LLC','Cognizant Technology Solutions US Corp','Google LLC','Microsoft Corporation','Tata Consultancy Services Limited','Ernst & Young US LLP','Infosys Limited','Meta Platforms INC','Deloitte Consulting LLP','Amazon Web Services INC','Apple INC']



JobKeyWords = {'Data Scientist': 0, 'Software Developer': 0, 'Software Engineer': 0, 'Analyst': 0, 'Machine': 0, 'DevOps': 0, 'Cloud': 0, 'Software System': 0,
               'Software Quality': 0, 'AWS': 0, 'Azure': 0, 'Google Cloud': 0, 'Software Quality': 0,  'Tableau': 0, 'Automation': 0, 'PowerBi': 0}



def H1B_Url():
    driver.get('https://h1bgrader.com/')


def SearchCompany(i):
    # Search Company Data
    search = driver.find_element(By.ID, 'employer')
    print("Company Name:", i)
    CompanyName = i
    print(CompanyName)
    # search.click()
    search.send_keys(i)
    buttonClick = driver.find_element(By.CLASS_NAME, 'search-button')
    buttonClick.click()
    # Select Job_Title Button
    driver.find_element(By.ID, 'employer-job-tabb').click()
    sleep(2)
    # return (i)

    for j in range(1, 5):
        try:
            page = driver.find_element(By.XPATH, '//*[@id="salary-data-table_paginate"]/ul/li['+str(j)+']')
            # print(page.text)
            page.click()
            # AllJobs()

            for k in range(1, 201):
                try:
                    jobTitle = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/div/div/div[1]/div[7]/div[5]/div[2]/div[2]/div/table/tbody/tr['+str(k)+']/td[1]')
                    MaxSalary = driver.find_element(By.XPATH, '//*[@id="salary-data-table"]/tbody/tr['+str(k)+']/td[2]')
                    AvgSalary = driver.find_element(By.XPATH, '//*[@id="salary-data-table"]/tbody/tr['+str(k)+']/td[3]')
                    MinSalary = driver.find_element(By.XPATH, '//*[@id="salary-data-table"]/tbody/tr['+str(k)+']/td[4]')
                    print(CompanyName, jobTitle.text, MaxSalary.text, AvgSalary.text, MinSalary.text) 
                    row = [CompanyName, jobTitle.text, MaxSalary.text, AvgSalary.text, MinSalary.text]
                    JobsData.append(row)
                except:
                    # print("Failed to Get job item ", i)
                    print("NA at k")

        except:
            print("")





def AllJobs():
    for i in range(1, 201):
        try:
            jobTitle = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/div/div/div[1]/div[7]/div[5]/div[2]/div[2]/div/table/tbody/tr['+str(i)+']/td[1]')
            MaxSalary = driver.find_element(By.XPATH, '//*[@id="salary-data-table"]/tbody/tr['+str(i)+']/td[2]')
            AvgSalary = driver.find_element(By.XPATH, '//*[@id="salary-data-table"]/tbody/tr['+str(i)+']/td[3]')
            MinSalary = driver.find_element(By.XPATH, '//*[@id="salary-data-table"]/tbody/tr['+str(i)+']/td[4]')
            print(jobTitle.text, MaxSalary.text, AvgSalary.text, MinSalary.text) 
            row = [jobTitle.text, MaxSalary.text, AvgSalary.text, MinSalary.text]
            JobsData.append(row)
        except:
            # print("Failed to Get job item ", i)
            print("NA")
            

def Jobs():


    for i in range(1, 5):
        try:
            page = driver.find_element(By.XPATH, '//*[@id="salary-data-table_paginate"]/ul/li['+str(i)+']')
            # print(page.text)
            page.click()
            AllJobs()
        except:
            print("")







# MAIN 
for i in Companies:

    try:
        H1B_Url()
        SearchCompany(i)
        # Jobs()


    except:
        print("NA")


# search.send_keys(Keys.ENTER)


sleep(3)




# Save Data to CSV
JobListFile = "JobsList.csv"
# writing to csv file
with open(JobListFile, 'w') as csvfile:
    # creating a csv writer object
    csvwriter = csv.writer(csvfile)

    # writing the fields
    csvwriter.writerow(JobFields)

    # writing the data rows
    csvwriter.writerows(JobsData)