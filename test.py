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







    # error = driver.find_element(
    #     "xpath", '//*[@id="banner-large-eta-vanilla"]/div')
 

    # if error:
    #     r = r+1
    # else:
    #     print("no error")

    # print(value.text)
    # if value != driver.find_element("xpath", '//*[@id="ctl00_ctl00_ContentPlaceHolder1_ContentPlaceHolder1_divcontent"]/table/tbody/tr['+str(r)+']/td[2]/a'):
    #     print(value + ": NA")
    #     r = r + 1
    # else:
    #     print(value.text)


# wait = WebDriverWait(driver, 10)
# element = wait.until(EC.element_to_be_clickable(
#     ("xpath", '//*[@id="ctl00_ctl00_ContentPlaceHolder1_ContentPlaceHolder1_divcontent"]/table/tbody/tr[3]/td[2]/a')))
# print(element.text)


# row = driver.find_element(By.CLASS_NAME, 'tbl a')
# print(row.text)


# heading1 = driver.find_element(By.TAG_NAME, 'td')
# print(heading1.text)


# players = driver.find_element("xpath", '//*[@id="post-395571"]/div[4]/figure/table/tbody/tr[1]/td[1]/a"]')
# print(players.text)


# players_list = []
# for p in range(len(players)):
#     players_list.append(players[p].text)


# Obtain the number of columns in table
# cols = len(driver.find_element("xpath",	"/html/body/div[3]/div[2]/div/div[1]/div/div/div/article/div[3]/div/table/tbody/tr[1]/td"))

# Print rows and columns
# print(rows)
# print(cols.text)

# Printing the table headers
# print("Locators		 "+"			 Description")

# Printing the data of the table
# for r in range(2, rows+1):
# 	for p in range(1, cols+1):

# 		# obtaining the text from each column of the table
# 		value = driver.find_element_by_xpath(
# 			"/html/body/div[3]/div[2]/div/div[1]/div/div/div/article/div[3]/div/table/tbody/tr["+str(r)+"]/td["+str(p)+"]").text
# 		print(value, end='	 ')
# 	print()
