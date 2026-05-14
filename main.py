from turtle import *
import random
import time

#### CLASS AND FUNCTION DEFINITIONS #####
def playing_area():
	t = Turtle()
	t.speed(0)
	t.ht()
	t.pu()
	t.goto(-250,250)
	t.color("light blue")
	t.pd()
	t.begin_fill()
	for i in range(4):
		t.forward(500)
		t.right(90)
	t.end_fill()

def updatePoints(t):
	t.clear()
	t.speed(0)
	t.ht()
	t.pu()
	t.color("#FFFFFF")
	t.goto(-300,0)
	t.pd()
	t.write("P1:" + str(p1.points), align="center", font=["Times New Roman","30"])
	t.pu()
	t.goto(300,0)
	t.pd()
	t.write("P2:" + str(p2.points), align="center", font=["Times New Roman","30"])

def spawnDaZombies(prizesCollected):
	for i in range(prizesCollected + 1):
		for p in [p1,p2]:
			randx = random.randint(-250,250)
			randy = random.randint(-250,250)
			while (randx < p.xcor()+100 and randx > p.xcor()-100 and randy < p.ycor()+100 and randy > p.ycor()-100) or (randx<=-250 or randy<=-250 or randx>=250 or randy>=250):
				randx = random.randint(-250,250)
				randy = random.randint(-250,250)
			if i%5 == 0 and i!=0:
				zombies.append(BeefyBoi(randx,randy,p))
			else:
				zombies.append(Zombie(randx,randy,p))


class Player(Turtle):
	def __init__(self,x,y,leftkey,rightkey,shootkey,bombkey,color):
		super().__init__()
		self.ht()
		self.penup()
		self.goto(x,y)
		self.speed(0)
		self.shape("turtle")
		self.color(color)
		self.bullets=[]
		self.bombs=[]
		self.leftkey=leftkey
		self.rightkey=rightkey
		self.shootkey=shootkey
		self.bombkey=bombkey
		self.points=0
		self.st()

	def move(self):
		self.forward(5)
	
	def goleft(self):
		self.left(10)
	
	def goright(self):
		self.right(10)
	
	def fire(self):
		self.bullets.append(Bullet(self))
	
	def bomb(self):
		self.bombs.append(Bomb(self))

	def die(self):
		self.ht()
		dieTurtle = Turtle()
		dieTurtle.home()
		dieTurtle.ht()
		dieTurtle.speed(0)
		dieTurtle.color("#00AA00")
		dieTurtle.write("Game over.\nZombie death!", align="center", font=("Times New Roman",50))

class Bullet(Turtle):
	def __init__(self,player):
		super().__init__()
		self.ht()
		self.speed(0)
		self.penup()
		self.player = player
		self.color(player.color()[0])
		self.goto(player.pos())
		self.setheading(player.heading())
		self.st()
	
	def move(self):
		self.forward(15)
	
	def die(self):
		self.ht()
		self.player.bullets.remove(self)

class Bomb(Turtle):
	def __init__(self,player):
		super().__init__()
		self.ht()
		self.speed(0)
		self.penup()
		self.player = player
		self.shape("circle")
		self.color(player.color()[0])
		self.goto(player.pos())
		self.detonationtimer=0
		self.st()
	
	def BOOM(self):
		self.ht()
		self.goto(self.xcor(),self.ycor()+50)
		self.pendown()
		self.begin_fill()
		self.circle(-50)
		self.end_fill()
		self.penup()
		self.goto(self.xcor(),self.ycor()-50)
		ded=[]
		for i in range(len(zombies)-1):
			if self.xcor()-50 < zombies[i].xcor() and self.ycor()-50 < zombies[i].ycor() and self.xcor()+50 > zombies[i].xcor() and self.ycor()+50 > zombies[i].ycor():
				ded.append(zombies[i])
		for deadzombie in ded:
			deadzombie.die()
		self.clear()
		self.player.bombs.remove(self)

class Zombie(Turtle):
	def __init__(self,x,y,target):
		super().__init__()
		self.ht()
		self.speed(0)
		self.target = target
		self.color("#008800")
		self.shape("turtle")
		self.penup()
		self.goto(x,y)
		self.setheading(self.towards(self.target))
		self.st()
	
	def move(self):
		self.forward(3)
		self.setheading(self.towards(self.target))
	
	def die(self):
		self.ht()
		zombies.remove(self)

class BeefyBoi(Turtle):
	def __init__(self,x,y,target):
		super().__init__()
		self.ht()
		self.speed(0)
		self.target = target
		self.hp=5
		self.color("#008800")
		self.shape("turtle")
		self.shapesize(2)
		self.penup()
		self.goto(x,y)
		self.setheading(self.towards(self.target))
		self.st()
	
	def move(self):
		self.forward(1.5)
		self.setheading(self.towards(self.target))
	
	def die(self):
		self.ht()
		zombies.remove(self)

#### DRIVER CODE ####
screen = Screen()
screen.bgcolor("black")

playing_area()
global p1
p1=Player(10,0,"Left","Right","Up","Down","#FF0000")
global p2
p2=Player(10,0,"a","d","w","s","#0000FF")
pointsTurtle=Turtle()
updatePoints(pointsTurtle)

global zombies
zombies = []

prize = Turtle()
prize.ht()
prize.speed(0)
prize.penup()
prize.shape("circle")
prize.color("#FFFF00")
prize.goto(random.randint(-200,200),random.randint(-200,200))
prize.setheading(random.randint(0,359))
prize.st()
prizesCollected = 0

alive = True
won = False

onkeypress(p1.goleft,p1.leftkey)
onkeypress(p1.goright,p1.rightkey)
onkeypress(p1.fire,p1.shootkey)
onkeypress(p1.bomb,p1.bombkey)
onkeypress(p2.goleft,p2.leftkey)
onkeypress(p2.goright,p2.rightkey)
onkeypress(p2.fire,p2.shootkey)
onkeypress(p2.bomb,p2.bombkey)
screen.listen()

while alive == True and won == False:
	for p in [p1,p2]:
		p.move()
		if p.xcor() > 230 or p.xcor() < -230:
			p.setheading(180 - p.heading())
		if p.ycor() > 230 or p.ycor() < -230:
			p.setheading(-p.heading())
		if p.xcor() > prize.xcor()-30 and p.ycor() > prize.ycor()-30 and p.xcor() < prize.xcor()+30 and p.ycor() < prize.ycor()+30:
			prize.ht()
			p.points+=1
			if p.points == 10:
				won = True
			prizesCollected+=1
			prize.goto(random.randint(-200,200),random.randint(-200,200))
			prize.setheading(random.randint(0,359))
			prize.st()
			spawnDaZombies(prizesCollected)
			updatePoints(pointsTurtle)
		
		for bullet in p.bullets:
			bullet.move()
			if bullet.xcor()<=-250 or bullet.ycor()<=-250 or bullet.xcor()>=250 or bullet.ycor()>=250:
				bullet.die()
			else:
				for zombie in zombies:
					if type(zombie)==Zombie:
						if bullet.xcor() > zombie.xcor()-20 and bullet.ycor() > zombie.ycor()-20 and bullet.xcor() < zombie.xcor()+20 and bullet.ycor() < zombie.ycor()+20:
							bullet.die()
							zombie.die()
							break
					elif type(zombie)==BeefyBoi:
						if bullet.xcor() > zombie.xcor()-40 and bullet.ycor() > zombie.ycor()-40 and bullet.xcor() < zombie.xcor()+40 and bullet.ycor() < zombie.ycor()+40:
							bullet.die()
							if zombie.hp==1:
								zombie.die()
							else:
								zombie.hp-=1
								zombie.color("#FFFFFF")
								time.sleep(0.1)
								zombie.color("#008800")
							break

		for bomb in p.bombs:
			if bomb.detonationtimer == 25:
				bomb.BOOM()
			else:
				bomb.detonationtimer += 1
		
		for zombie in zombies:
			zombie.move()
			if p.xcor() > zombie.xcor()-30 and p.ycor() > zombie.ycor()-30 and p.xcor() < zombie.xcor()+30 and p.ycor() < zombie.ycor()+30:
				p.die()
				alive = False
	
	prize.forward(5)
	if prize.xcor() > 230 or prize.xcor() < -230:
		prize.setheading(180 - prize.heading())
	if prize.ycor() > 230 or prize.ycor() < -230:
		prize.setheading(-prize.heading())
	prize.left(random.randint(0,10))
	prize.right(random.randint(0,10))

if alive == False:
	p1=""
	p2=""
	prize.ht()
	prize=""
	for zombie in zombies:
		zombie.ht()

if won == True:
	p1=""
	p2=""
	prize.ht()
	prize=""
	for zombie in zombies:
		zombie.ht()
	winTurtle = Turtle()
	winTurtle.home()
	winTurtle.ht()
	winTurtle.speed(0)
	winTurtle.color("#00AA00")
	winTurtle.write("Game over.\nPoints win!", align="center", font=("Times New Roman",50))

screen.mainloop()