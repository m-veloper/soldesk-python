import pygame
import random
import sys


##함수 선언 부분##


# @2-5 : 매개변수로 받은 객체를 화면에 출력

def paintEntiry(entity, x, y):
    monitor.blit(entity, (x, y))

    pass

def writeScore(score) :
    global r, g, b
    myFont = pygame.font.Font('C:/Windows/Fonts/batang.ttc',40)
    txt = myFont.render(u'파괴한 우주괴물 수 : '+str(score), True, (255-r,255-g,255-b))
    paintEntiry(txt,swidth*0.05,sheight*0.9)


def playGame():
    global monitor, shipX, shipY,r,g,b
    r = random.randrange(0, 256)
    g = random.randrange(0, 256)
    b = random.randrange(0, 256)

    # @기능 2-2 : 우주선의 초기 위치와 키보드 이벤트시 이동량 구현
    shipX = swidth / 2
    shipY = sheight * 0.8

    dx, dy = 0, 0

    # 기능 3-2 : 우주괴물을 무작위로 추출하고 크기와 위치를 설정
    monsterImage = ["monster01.png", "monster02.png", "monster03.png", "monster04.png", "monster05.png",
                    "monster06.png", "monster07.png", "monster08.png", "monster09.png", "monster10.png"]
    mon = pygame.image.load(random.choice(monsterImage))
    monsize = mon.get_rect().size
    monX = 0
    monY = sheight * 0.1
    monSpeedX = random.choice([-12, -9, -6, -3, 3, 6, 9, 12])
    monSpeedY = random.choice([-12, -9, -6, -3, 3, 6, 9, 12])
    pang = pygame.image.load('pang.png')
    # 무한 반복
    while True:
        global misY,i,iE,pangT,score,pKeyL,pKeyR,pKeyU,pKeyD,misP
        (pygame.time.Clock()).tick(80)  # 게임 진행속도(10~100)
        monitor.fill((r, g, b))  # 화면 배경 칠하기

        # 키보드나 마우스 이벤트 체크

        for e in pygame.event.get():
            if e.type in [pygame.QUIT]:  # 창에 닫기버튼(x) 누르면
                pygame.quit()
                sys.exit()

            # @2-3 : 방향키에 따라 우주선이 움직이게 구현
            # 방향키를 누르면 우주선이 이동한다(누르고 있으면 계속 이동).
            if e.type in [pygame.KEYDOWN]:
                if e.key == pygame.K_LEFT:
                    pKeyL=-1
                elif e.key == pygame.K_RIGHT:

                    pKeyR=1
                elif e.key == pygame.K_DOWN:

                    pKeyD=1
                elif e.key == pygame.K_UP:

                    pKeyU=-1
                elif e.key == pygame.K_SPACE:
                    misT = pygame.image.load('missile.png')
                    misPX = shipX + (shipsize[0]-missize[0])*0.5
                    misPY = shipY - missize[1]
                    misP.insert(0,[misT,misPX,misPY])
                    # print(misP)




            # 방향키를 떼면 우주선이 멈춘다
            if e.type in [pygame.KEYUP]:
                if e.key == pygame.K_LEFT :
                    pKeyL = 0
                elif e.key == pygame.K_RIGHT:
                    pKeyR = 0
                elif e.key == pygame.K_UP:
                    pKeyU = 0
                elif e.key == pygame.K_DOWN:
                    pKeyD = 0
        dx = (pKeyL + pKeyR)*shipSpeed
        dy = (pKeyU + pKeyD)*shipSpeed
        # @2-4 : 우주선이 화면안에서만 움직이게 구현
        if (0 <= shipX + dx and shipX + dx <= swidth - shipsize[0]) and (
                sheight / 2 <= shipY + dy and shipY + dy <= sheight - shipsize[1]):  # 범위를 벗어나지 않았다면
            shipX += dx
            shipY += dy
        paintEntiry(ship, shipX, shipY)  # 우주선을 화면에 출력

        # @3-3우주괴물이 자동으로 오른쪽으로..

        monX += monSpeedX
        monY += monSpeedY
        if monX >= swidth - monsize[0] or monX < 0 or monY >= sheight-monsize[1] or monY < 0:
            monT = random.choice([0,1,2])
            if monT == 0 :
                monX = 0
                monY = random.randrange(int(sheight*0.1),int(sheight*0.45))
            elif monT == 1 :
                monY = 0
                monX = random.randrange(0, swidth-monsize[0])
            elif monT == 2:
                monX = swidth-monsize[0]
                monY = random.randrange(int(sheight * 0.1), int(sheight * 0.45))
            # elif monT == 3 :
            #     monY = sheight-monsize[1]
            #     monX = random.randrange(0, swidth-monsize[0])
            mon = pygame.image.load(random.choice(monsterImage))
            monSpeedX = random.choice([-12, -9, -6, -3, 3, 6, 9, 12])
            monSpeedY = random.choice([-12, -9, -6, -3, 3, 6, 9, 12])
        paintEntiry(mon, monX, monY)

        pangT -= 1
        if len(misP)>0 :
            for k in range(len(misP)-1,-1,-1 ) :
                if misP[k][2] < 0 :
                    del(misP[k])
                    continue
                if misP[k][2] >= 0:
                    misP[k][2] -= 15
                    paintEntiry(misP[k][0], misP[k][1], misP[k][2])

                if (monX < misP[k][1] < monX+monsize[0]) and (monY < misP[k][2] < monY+monsize[1]) :
                    pangT = 17
                    pangX = monX
                    pangY = monY
                    monX = swidth+5
                    monY = sheight+5
                    misP[k][1] = swidth+5
                    misP[k][2] = sheight+5
                    score += 1

        if pangT > 0 :
            paintEntiry(pang, pangX, pangY)


        writeScore(score)


        pygame.display.update()  # 실시간 게임 상황 화면에 노출
        # print('업데이트',end='')


## 전역 변수 선언 부분 ##
swidth, sheight = 1000, 700  # 화면 크기
shipX, shipY = 0, 0
shipSpeed = 5
pangX, pangY = 0, 0
r,g,b = 0,0,0
misP = []

pKeyL = 0
pKeyR = 0
pKeyU = 0
pKeyD = 0
score = 0
pangT = 0
misY = -15000

monitor = None  # 게임 화면

##메인 코드 부분 ##

pygame.init()
monitor = pygame.display.set_mode((swidth, sheight))
pygame.display.set_caption("우주괴물 무찌르기")

# @기능 2-1 : 우주선 이미지를 준비하고 크기를 구현

ship = pygame.image.load('ship02.png')
shipsize = ship.get_rect().size  # 가로 인덱스 : 0, 세로 인덱스 : 1

mis = pygame.image.load('missile.png')
missize = mis.get_rect().size

playGame()





