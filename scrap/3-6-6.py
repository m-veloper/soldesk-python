import sys
import io
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding='utf-8')

# CLI(command line interface)로 브라우져 제어
chrome_options = Options()
driver = webdriver.Chrome('D:/Python_2022/webdriver/chrome/chromedriver')
driver.set_window_size(1920, 1280)
driver.implicitly_wait(5)

driver.get('https://www.wishket.com/accounts/login/')
time.sleep(5)
driver.implicitly_wait(3)
driver.find_element_by_name('identification').send_keys('smile516')
driver.implicitly_wait(3)
driver.find_element_by_name('password').send_keys('jinbin516@')
driver.implicitly_wait(3)

# 로그인버튼
driver.find_element_by_xpath('//*[@id="submit"]').click()
