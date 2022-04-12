import sys
import io
from selenium import webdriver

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding='utf-8')

driver = webdriver.PhantomJS('D:/Python_2022/webdriver/phantomjs/bin/phantomjs')

# load가 되지 않은 상태에서 진행시 오류를 발생시키므로 대기시간이 필요
driver.implicitly_wait(5)  # 5초

driver.get('https://google.com')
# 스샷
driver.save_screenshot('D:/Python_2022/img/Website1.png')
driver.implicitly_wait(5)  # 5초

driver.get('https://daum.net')

# 스샷
driver.save_screenshot('D:/Python_2022/img/Website2.png')
driver.quit()

print("스크린샷 성공")
