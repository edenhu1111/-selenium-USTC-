from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

driver = webdriver.Chrome(executable_path="C:\chromedriver\chromedriver.exe")
driver.get("http://wlt.ustc.edu.cn/cgi-bin/ip")

<<<<<<< HEAD
driver.find_element_by_name('name').send_keys('YourUSRNAME')
driver.find_element_by_name('password').send_keys('YourPW')
=======
driver.find_element_by_name('name').send_keys('yourusername')
driver.find_element_by_name('password').send_keys('yourpassword')
>>>>>>> bd08aabdafe59f210a99de67d80e439fcd1d4f92
driver.find_element_by_name("set").click()

sleep(0.5)

driver.quit()


