from turtle import *
from random import randint, choice

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

'''
Player() Class

Constructor( def __init__(self)):
- player should be shaped like a turtle.
- will take in the x and y coordinates for where the player will initially appear.
- will take in a color for the player
- will take in keys to turn left, turn right and shoot bullets.
- player will have an attribute that is a list that stores bullets


move(self):
- moves object forward five pixels

fire(self):
- creates a Bullet object
- appends the Bullet object to the players's bullet list
'''
class Player(Turtle):
	def __init__(self,x,y,leftkey,rightkey,shootkey):
		super().__init__()
		self.ht()
		self.penup()
		self.goto(x,y)
		self.speed(0)
		self.shape("turtle")
		self.color("#FF0000")
		self.bullets=[]
		self.leftkey=leftkey
		self.rightkey=rightkey
		self.shootkey=shootkey
		self.st()

	def move(self):
		self.forward(5)
	
	def goleft(self):
		self.left(10)
	
	def goright(self):
		self.right(10)
	
	def fire(self):
		self.bullets.append(Bullet(self))

'''
Bullet() Class
Constructor ( def __init__(self) ):
- Input: player object
- Attributes:
	- Position: same as player
	- Heading: same as player
	- Player: the player
 
move(self):
- move 15 or more pixels forward
- should call on the die() method when the bullet leaves the playing area

die()
- hides the object. 
- removes object from the player's bullet list
'''

class Bullet(Turtle):
	def __init__(self,player):
		super().__init__()
		self.ht()
		self.speed(0)
		self.penup()
		self.player = player
		self.color = player.color()
		self.goto(player.pos())
		self.setheading(player.heading())
		self.st()
	
	def move(self):
		self.forward(15)
	
	def die(self):
		self.ht()
		self.player.bullets.remove(self)

#### DRIVER CODE ####
screen = Screen()
screen.bgcolor("black")

playing_area()
p1=Player(0,0,"Left","Right","Up")

onkeypress(p1.goleft,p1.leftkey)
onkeypress(p1.goright,p1.rightkey)
onkeypress(p1.fire,p1.shootkey)
screen.listen()

while True:
	p1.move()
	for bullet in p1.bullets:
		bullet.move()
		if bullet.xcor()<=-250 or bullet.ycor()<=-250 or bullet.xcor()>=250 or bullet.ycor()>=250:
			bullet.die()

screen.mainloop()