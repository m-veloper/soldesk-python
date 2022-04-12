import sys
import io
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import pyperclip
import time

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding='utf-8')


class NcafeWriteAtt:
    # 초기화 실행(webdriver 설정)
    def __init__(self):
        chrome_options = Options()
        self.driver = webdriver.Chrome('D:/Python_2022/webdriver/chrome/chromedriver')
        self.driver.implicitly_wait(5)

    # 네이버 카페 로그인 && 출석 체크
    def writeAttendCheck(self):
        self.driver.get('https://nid.naver.com/nidlogin.login')

        pyperclip.copy('516smile')
        self.driver.find_element_by_name('id').click()
        webdriver.ActionChains(self.driver).key_down(Keys.CONTROL).send_keys('v').key_up(Keys.CONTROL).perform()

        pyperclip.copy('jb030625@')
        self.driver.find_element_by_name('pw').click()
        webdriver.ActionChains(self.driver).key_down(Keys.CONTROL).send_keys('v').key_up(Keys.CONTROL).perform()

        self.driver.find_element_by_xpath('//*[@id="log.login"]').click()
        time.sleep(3)

        self.driver.get(
            'http://cafe.naver.com/paramsx?iframe_url=/AttendanceView.nhn%3Fsearch.clubid=19756449%26search.menuid=103')
        self.driver.implicitly_wait(5)
        self.driver.switch_to_frame('cafe_main')
        self.driver.find_element_by_xpath('//*[@id="cmtinput"]').send_keys('한주 홧팅!!^^~~')
        self.driver.find_element_by_xpath('//*[@id="btn-submit-attendance"]').click()
        time.sleep(3)

    # 소멸
    def __del__(self):
        self.driver.quit()
        print("Remove driver Object")


# 실행
if __name__ == '__main__':
    # 객체 생성
    a = NcafeWriteAtt()
    # 시작 시간
    start_time = time.time()  # 현재시간
    # 프로그램 호출
    a.writeAttendCheck()
    # 종료시간
    print("--total %s sconds---" % (time.time() - start_time))
    # 객체 소멸
    del a
