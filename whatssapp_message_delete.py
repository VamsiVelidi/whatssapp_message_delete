from selenium import webdriver
import time


driver = webdriver.Chrome('/home/vamsi/Downloads/chromedriver')
driver.maximize_window()
driver.get('https:web.whatsapp.com')
time.sleep(15)
home_search = driver.find_element_by_xpath('//*[@id="side"]/div[1]/div/label/input')
home_search.click()
home_search.send_keys('Gokila Kalai')
Gokila_Kalai = driver.find_element_by_xpath('//*[@id="pane-side"]/div[1]/div/div/div[2]/div/div/div[2]')
Gokila_Kalai.click()
Gokila_Kalai_search = driver.find_element_by_xpath('//*[@id="main"]/header/div[3]/div/div[1]/div')
Gokila_Kalai_search.click()
Gokila_Kalai_search_input = driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div[3]/span/div/div/div[1]/div/label/input')
Gokila_Kalai_search_input.send_keys('Good morning')
