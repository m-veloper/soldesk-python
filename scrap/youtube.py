import os
import subprocess
import pytube

yt=pytube.YouTube("https://www.youtube.com/watch?v=CTRO5NXmAp8")

videos=yt.streams.all()
#print('videos',videos)

for i in range(len(videos)):
    print(i,' ',videos[i])

parent_dir="D:/python/"
videos[0].download(parent_dir) #화질이 제일 안정적이고 좋은 0번째 영상 선택 다운로드

print("다운로드 완료")
