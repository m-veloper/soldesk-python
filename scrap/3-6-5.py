import sys
import io
from selenium import webdriver
from selenium.webdriver.firefox.options import Options

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding='utf-8')

# CLI(command line interface)로 브라우져 제어
options = Options()
options.binary_location = r'C:/Program Files/Mozilla Firefox/firefox.exe'
options.headless = True
driver = webdriver.Firefox(options=options, executable_path=r'D:/Python_2022/webdriver/firefox/geckodriver.exe')

driver.get('https://google.com')
driver.save_screenshot('D:/Python_2022/img/Website9.png')

driver.get('https://daum.net')
driver.save_screenshot('D:/Python_2022/img/Website10.png')
driver.quit()

print("스크린샷 성공")
