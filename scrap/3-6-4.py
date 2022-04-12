import sys
import io
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding='utf-8')

# CLI(command line interface)로 브라우져 제어
chrome_options = Options()
chrome_options.add_argument("--headless")
# 모니터 출력없이 접속
driver = webdriver.Chrome(chrome_options=chrome_options,
                          executable_path=r'D:/Python_2022/webdriver/chrome/chromedriver')
# 눈으로 확이하면서 크롤링
# driver=webdriver.Chrome('D:/Python_2022/webdriver/chrome/chromedriver')

driver.get('https://google.com')
driver.save_screenshot('D:/Python_2022/img/Website7.png')

driver.get('https://daum.net')
driver.save_screenshot('D:/Python_2022/img/Website8.png')
driver.quit()

print("스크린샷 성공")
