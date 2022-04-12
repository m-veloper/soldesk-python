import sys
import io
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from bs4 import BeautifulSoup
import pyperclip
import time

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding='utf-8')


class NcafeMemberExr:
    # 초기화 실행(webdriver 설정)
    def __init__(self):
        chrome_options = Options()
        self.driver = webdriver.Chrome('D:/Python_2022/webdriver/chrome/chromedriver')
        self.driver.implicitly_wait(5)

    # 네이버 카페 로그인 && 출석 체크
    def getMemberList(self):
        self.driver.get('https://nid.naver.com/nidlogin.login')

        pyperclip.copy('516smile')
        self.driver.find_element_by_name('id').click()
        webdriver.ActionChains(self.driver).key_down(Keys.CONTROL).send_keys('v').key_up(Keys.CONTROL).perform()

        pyperclip.copy('jb030625@')
        self.driver.find_element_by_name('pw').click()
        webdriver.ActionChains(self.driver).key_down(Keys.CONTROL).send_keys('v').key_up(Keys.CONTROL).perform()

        self.driver.find_element_by_xpath('//*[@id="log.login"]').click()
        time.sleep(3)

        self.driver.get('https://cafe.naver.com/CafeMemberViewTab.nhn?defaultSearch.clubid=19756449')
        self.driver.implicitly_wait(5)
        # sancheon_popup_iframe = self.driver.find_element_by_id("cafe_main")
        self.driver.switch_to.frame("cafe_main")
        # print('test',self.driver.page_source)
        self.driver.implicitly_wait(5)
        # print('test',self.driver.page_source)
        soup = BeautifulSoup(self.driver.page_source, 'html.parser')
        # 선택자 추출
        return soup.select('div.mem_list_wrap > ul > li > div.ellipsis.m-tcol-c')
        time.sleep(3)

    # 네이버 회원 리스트 출력 및 저장
    def printMemberList(self, list):
        f = open("D:/python/memberList.txt", 'wt')
        for i in list:
            f.write(i.string.strip() + "\n")
            print(i.string.strip())
        f.close()

    # 소멸
    def __del__(self):
        self.driver.quit()
        print("Remove driver Object")


# 실행
if __name__ == '__main__':
    # 객체 생성
    a = NcafeMemberExr()
    # 시작 시간
    start_time = time.time()  # 현재시간
    # 프로그램 호출
    a.printMemberList(a.getMemberList())
    # 종료시간
    print("--total %s sconds---" % (time.time() - start_time))
    # 객체 소멸
    del a
