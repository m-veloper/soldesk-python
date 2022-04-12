import sys
import io
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding='utf-8')

# CLI(command line interface)로 브라우져 제어
chrome_options = Options()
# 브라우져 보이기
# driver = webdriver.Chrome('D:/Python_2022/webdriver/chrome/chromedriver')
# 브라우져 숨김
driver = webdriver.Chrome(chrome_options=chrome_options,
                          executable_path=r'D:/Python_2022/webdriver/chrome/chromedriver')

driver.get("http://www.encar.com/dc/dc_carsearchlist.do?carType=kor&searchType=model&TG.R=A#!")
driver.implicitly_wait(3)

carClsP = driver.find_elements_by_class_name("cls")
carDtlP = driver.find_elements_by_class_name("dtl")

for i in range(len(carClsP)):
    print("{}번째 차 : {} {} \n".format(i + 1, carClsP[i].text, carDtlP[i].text))

driver.quit()
