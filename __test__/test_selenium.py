import time

from selenium import webdriver

wd = webdriver.Chrome('E:\cafe24\chromedriver_win32\chromedriver.exe')
wd.get('https://www.google.com')

time.sleep(2)
html = wd.page_source
print(html)

wd.quit()