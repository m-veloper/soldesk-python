from bs4 import BeautifulSoup
import requests
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

mvList=['179181', '186821', '187321', '186613', '181925', '190026', '172816', '176306', '190325', '187350']

with requests.session() as s :
    for mv in mvList:
        urlT="https://movie.naver.com/movie/bi/mi/basic.nhn?code=" +mv
        url = "https://movie.naver.com/movie/bi/mi/pointWriteFormList.nhn?code="+mv+"&type=after&isActualPointWriteExecute=false&isMileageSubscriptionAlready=false&isMileageSubscriptionReject=false&page="
        listP=[]
        scoreP=[]
        run=True
        saveStr=""
        i=1


        rt=s.get(urlT)
        soupT=BeautifulSoup(rt.text,"html.parser")
        mvTitle=str(soupT.select_one("#content > div.article > div.mv_info_area > div.mv_info > h3 > a:nth-child(1)").text)
        #print(mvTitle)

        #평점 추출
        while run :
            urlF=url+str(i)
            r=s.get(urlF)
            soup=BeautifulSoup(r.text, "html.parser")
            list=soup.select("span[id^=_filtered_ment_]") #리뷰글
            score = soup.select("div.star_score > em") #별의 점수
            listP +=list
            scoreP +=score
            i +=1
            if soup.select_one("#pagerTagAnchor" + str(i)) is None:
                run=False
        #출력
        for i in range(len(listP)-1, -1, -1) :
            content = listP[i].text.strip()
            scr=int(scoreP[i].text)
            star = '★'*(scr//2) +'☆'*(scr%2)
            saveStr += "내용 : {}, \n평점 : {}{}\n\n".format(content,star, scr)
        saveStr += "총 리뷰 수 : {}".format(len(listP))
        mvTitle = mvTitle.replace(":","_")
        savePath="D:/python/movie/"+mvTitle+".txt"
        with open(savePath, "wt") as saveFile :
            saveFile.write(saveStr)

print('다운로드 완료')
