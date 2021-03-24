from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time
chrome_options = Options()
chrome_options.add_argument('start-maximized')
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://mail.ru/")
elem = driver.find_element_by_name("login")
elem.send_keys('study.ai_172')
elem = driver.find_element_by_class_name("svelte-1eyrl7y")
elem.click()
time.sleep(1)
elem = driver.find_element_by_name("password")
elem.send_keys("NextPassword172")
elem.send_keys(Keys.ENTER)
#elem.find_element_by_xpath("//button[@class='second-button svelte-1eyrl7y']")
#elem.find_element_by_class_name("second-button")
elem.click()
time.sleep(3)
#links_list = driver.find_elements_by_class_name("llc js-tooltip-direction_letter-bottom js-letter-list-item llc_normal")
links_list = driver.find_elements_by_xpath("//")
print(links_list)