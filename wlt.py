from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

driver = webdriver.Chrome(executable_path="C:\chromedriver\chromedriver.exe")
driver.get("http://wlt.ustc.edu.cn/cgi-bin/ip")

driver.find_element_by_name('name').send_keys('edenhu1111')
driver.find_element_by_name('password').send_keys('Edenisme02')
driver.find_element_by_name("set").click()

sleep(0.5)

driver.quit()


