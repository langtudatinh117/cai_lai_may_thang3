# coding=utf-8


from pyvirtualdisplay import Display
from selenium import webdriver

query = "Thiện và ác là hai cái mâu th"
URL = 'http://coccoc.vn/search#query=%22cai+gi%22'
display = Display(visible=0, size=(1024, 768))
display.start()
ff = "/home/daoan/Documents/install/geckodriver"
browser = webdriver.Firefox( executable_path=ff)
browser.get(URL)
id = browser.find_element_by_class_name("snippet-result")
print (id.text)
browser.quit()
display.stop()
