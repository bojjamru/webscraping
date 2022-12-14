from selenium import webdriver
driver = webdriver.Chrome()
driver.get("https://www.myvisajobs.com/Reports/2022-H1B-Visa-Sponsor.aspx")
driver.close() #closes that particular tab
driver.quit() #quits the entire browser


#price = driver.find_element_by_id("priceblock_ourprice")
#print(price.text)

#search_bar= driver.find_element_by_name("q")
#print(search_bar.get_attribute("placeholder"))

# logo=driver.f("python-logo")
# print(logo.size)
# driver.quit()