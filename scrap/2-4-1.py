import os
import subprocess
import pytube

yt=pytube.YouTube("https://youtu.be/yE_m9kBh_vg?list=RDyE_m9kBh_vg")
vids=yt.streams.all()

for i in range(len(vids)):
    print(i,' ',vids[i])

vnum = int(input("다운로드 받을 화질을 선택하세요 (0~21) : "))

parent_dir="D:/python/"
vids[vnum].download(parent_dir)

new_filename = input("변환할 파일명을 입력하세요 : ")

#기본 파일명 저장
default_filename = vids[vnum].default_filename

subprocess.call(['ffmpeg', '-i',
os.path.join(parent_dir, default_filename),
os.path.join(parent_dir, new_filename)])

print('동영상 다운로드 및 mp3 Convert 완료!')
