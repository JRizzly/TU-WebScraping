
import urllib2
import selenium
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

file = open('email.txt', 'w', 0)

driver = webdriver.Firefox()

# go to the google home page
driver.get("http://www.utexas.edu/directory/index.php?q=&scope=student&submit=Search")

inputSearchBarElements = driver.find_elements_by_xpath("/html/body/div[@id='main_w_padding']/div[@id='content']/div[@class='content']/table/tbody/tr/td[1]/div[@id='searchField']/form[@id='form1']/input[@id='searchInput']")
inputSearchBar = inputSearchBarElements[0]

#this is where I will make the strings to be searched

inputSearchBar.send_keys("aa")
inputSearchBar.submit()

#time.wait(2)

linkResults = driver.find_elements_by_xpath("/html/body/div[@id='main_w_padding']/div[@id='content']/div[@class='content']/table/tbody/tr/td[1]/div[@id='results']/div[@id='moreinfo']/a")

linkResults[0].click()

emailList = driver.find_elements_by_xpath("/html/body/div[@id='main_w_padding']/div[@id='content']/div[@class='content']/table/tbody/tr/td[1]/div[@id='results']/div[@id='moreinfo']/table/tbody/tr[2]/td[2]")

email = emailList[0]
print email.text
file.write(email.text)

driver.back()


####
#driver.quit()







