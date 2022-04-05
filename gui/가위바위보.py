import random


def convertRCP(val1):
    if val1 == 1:
        result = "가위"
    elif val1 == 2:
        result = "바위"
    elif val1 == 3:
        result = "보"
    return result


def RSPgame():
    rsp = {"가위": "보", "바위": "가위", "보": "바위"}
    player = input("값을 입력해주세요(가위/바위/보) : ")
    cpu = convertRCP(random.randrange(1, 4))

    if rsp[player] == cpu:
        winner = "승자는 player 입니다"
    elif rsp[cpu] == player:
        winner = "승자는 cpu 입니다"
    else:
        winner = "비겼습니다."

    print("player : {}\n cpu : {}\n {} ".format(player, cpu, winner))
