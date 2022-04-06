from tkinter import *
import random
import time
brick_ = 43
class Ball:
    def __init__(self,color):
        for z in range(1, brick_):
            exec('''self.brick%d = brick%d
self.__brick%d__ = 0''' %(z, z, z))
        self.canvas = canvas
        self.paddle = paddle
        self.id = canvas.create_oval(10,10,25,25,fill=color)
        self.canvas.move(self.id,245,100)
        starts = [-3,-2,-1,1,2,3]
        random.shuffle(starts)
        self.x = starts[0]
        self.y = -3
        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width = self.canvas.winfo_width()
        self.hit_bottom = False

    def hit_paddle(self,pos):
        self.pos = pos
        paddle_pos = self.canvas.coords(self.paddle.id)
        if self.pos[2] >= paddle_pos[0] and self.pos[0] <= paddle_pos[2]:
            if self.pos[3] >= paddle_pos[1] and self.pos[3] <= paddle_pos[3]:
                return True
            
        return False
    for z in range(1, brick_):
        exec('''def hit_brick%d(self, pos):
    self.pos = pos
    brick%d_pos = self.canvas.coords(self.brick%d.id)
    if self.pos[2] >= brick%d_pos[0] and self.pos[0] <= brick%d_pos[2]:
        if self.pos[3] >= brick%d_pos[1] and self.pos[1] <= brick%d_pos[3]:
            self.__brick%d__ = 1
            score.count()''' %(z, z, z, z, z, z, z, z))
    def draw(self):
        if paddle.s:
            self.canvas.move(self.id,self.x,self.y)
        self.pos = self.canvas.coords(self.id)
        if self.pos[1] <=0:
            self.y = 3
        if self.pos[3] >= self.canvas_height:
            self.hit_bottom = True
        if self.hit_paddle(self.pos) == True:
            self.y = -3
        if self.pos[0] <= 0:
            self.x = 3
        if self.pos[2] >= self.canvas_width:
            self.x = -3
        for z in range(1, brick_):
            exec('self.hit_brick%d(self.pos)' %z)
class Paddle:
    def __init__(self,canvas,color):
        self.canvas = canvas
        self.s = 0
        self.st = self.canvas.create_text(250,200,text = '시작하려면 스페이스바를 누르세요.',state='hidden',font=('Courier',15))
        self.canvas.itemconfig(self.st,state='normal')
        self.id = canvas.create_rectangle(0,0,100,10,fill=color) #3번째는 막대좌우길이, 4번째는 막대상하길이
        self.canvas.move(self.id,200,300) #3번째는 좌우위치, 4번째는 상하위치
        self.x = 0
        #self.y = 0
        self.canvas_width = self.canvas.winfo_width()
        self.canvas_height = self.canvas.winfo_height()
        self.canvas.bind_all('<KeyPress-Left>',self.left)
        self.canvas.bind_all('<KeyPress-Right>',self.right)
        #self.canvas.bind_all('<KeyPress-Up>',self.up)
        #self.canvas.bind_all('<KeyPress-Down>',self.down)
        #self.canvas.bind_all('<space>',self.stop)
        self.canvas.bind_all('<space>',self.start)
    def left(self,evt):
        if self.p0 and self.s:
            self.x = -9 #좌
    def right(self,evt):
        if self.p2 and self.s:
            self.x = 9 #우
    #def up(self, evt):
    #    if self.p1 and self.s:
    #        self.y = -10 #위
    #def down(self, evt):
    #    if self.p3 and self.s:
    #        self.y = 10 #아래
    #def stop(self, evt):
    #    self.x = 0 #멈춤
        #self.y = 0 #멈춤
    def start(self, evt):
        if self.s and ball.hit_bottom == False and brick.game:
            self.s = 0
            self.canvas.itemconfig(self.st,state='normal')
        elif self.s == 0 and ball.hit_bottom == False and brick.game:
            self.s = 1
            self.canvas.itemconfig(self.st,state='hidden')
    def draw(self):
        if self.s:
            self.canvas.move(self.id, self.x, 0)
        self.pos = self.canvas.coords(self.id)
        if self.pos[0] <= 0:
            self.x = 0
            self.p0 = 0
        else:
            self.p0 = 1
        if self.pos[2] >= self.canvas_width:
            self.x = 0
            self.p2 = 0
        else:
            self.p2 = 1
        #if self.pos[1] <= 0:
        #    self.y = 0
        #    self.p1 = 0
        #else:
        #    self.p1 = 1
        #if self.pos[3] >= self.canvas_height:
        #    self.y = 0
        #    self.p3 = 0
        #else:
        #    self.p3 = 1
        self.x = 0
a1 = 5
a2 = 5
a3 = 35
for x in range(1, brick_):
    exec('''class Brick%d:
    def __init__(self, canvas, score, color):
        self.canvas = canvas
        self.id = canvas.create_rectangle(0,0,%d,10,fill=color) #3번째는 막대좌우길이, 4번째는 막대상하길이
        self.canvas.move(self.id,%d,%d) #3번째는 좌우위치, 4번째는 상하위치
    def draw(self):
        if ball.__brick%d__:
            self.canvas.move(self.id, -100, -100)''' %(x, a3, a1, a2, x))
    a1+=35
    if x%14==0:
        a1 = 5
        a2+=10
class Score:
    def __init__(self,canvas,color):
        self.canvas = canvas
        self.score = 0
        self.id = canvas.create_text(450,60,text = self.score, fill = color,font=('Courier',20)) #초기 때 스코어 나타내는 크기

    def count(self, a=10):
        self.score = self.score + a #스코어 + 늘리기
        self.canvas.itemconfig(self.id,text = self.score,font=('Courier',20)) #이 함수를 호출했을 때 스코어 나타내는 크기
tk = Tk()
tk.title("Game")
tk.resizable(0,0)
tk.wm_attributes("-topmost",1)
canvas = Canvas(tk,width = 500, height=400, bd=0, highlightthickness=0)
canvas.pack()
tk.update()
score = Score(canvas,'green')
paddle = Paddle(canvas,'blue')
for x in range(1, brick_):
    exec("brick%d = Brick%d(canvas, score, random.choice(['red', 'orange', 'yellow', 'green', 'blue', 'navy', 'purple', 'violet', 'pink', 'white', 'black']))" %(x, x))
class Brick:
    def __init__(self):
        self.game = 1
    def draw(self):
        self.a = 1
        for x in range(1, brick_):
            exec('''brick%d.draw()
if not ball.__brick%d__==1:
    self.a = 0''' %(x, x))
        if self.a:
            self.game = 0
brick = Brick()
ball = Ball('red')
game_over_text = canvas.create_text(250,200,text = '실패!',state='hidden',font=('Courier',40)) #Game Over 숨기기, Game Over 크기
_ = canvas.create_text(250,200,text = '성공!',state='hidden',font=('Courier',40))
while 1:
    if ball.hit_bottom == False:
        if brick.game:
            ball.draw()
            paddle.draw()
            brick.draw()
        else:
            canvas.itemconfig(_,state='normal')
    else:
        canvas.itemconfig(game_over_text,state='normal')
    tk.update_idletasks()
    tk.update()
    time.sleep(0.01)
