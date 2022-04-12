import sys
import io
from selenium import webdriver

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding='utf-8')

driver = webdriver.Chrome('D:/Python_2022/webdriver/chrome/chromedriver')

driver.get('https://google.com')
driver.save_screenshot('D:/Python_2022/img/Website3.png')

driver.get('https://daum.net')
driver.save_screenshot('D:/Python_2022/img/Website4.png')

driver.quit()

print("스크린샷 성공")
