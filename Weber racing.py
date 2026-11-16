import turtle
import time
import random 

WIDTH, HEIGHT = 500, 500
COLOURS=['RED','blue','cyan','green','orange''yellow','black','purple','brown','pink']
def get_numbers_of_racers():
	racers=0
	while True:
		try:
			racers=int(input("Enter the numbers of racers(2-10): "))
		except ValueError:
			print ("only numbers allowed")
		continue 
		if >=2 racers<=10:
			return racers
		else:
			print("Numbers not in range2-10. Try Again🦹🏼")

def race(colours):
			turtles=create_turtles(colours)
			while True:
				for racer in turtles:
					distance=r.ranrange(1,20)
					racer.foward(distance)
					x,y=racer.pos()
					if y>=HEIGHT//2-10:
						return colours [turtles.indec(racer)]
def create_turtles(colours):
	turtles=[]
	spacingx=WIDTH//(lens(colours)+1 )
	for  i ,colour in enumerate (colours)
	move = turtle.Turtle()
	move.colour(colours)
	move.shape("turtle")
	move.left(90)
	move.penup()
	move.setpos(WIDTH//2,+(i+1)* spacing x,HEIGHT//2+20))
	move.pendown()
	turtles.append(move)
	remain turtles 
	
def make_turles():	
	screen = turtle.Screen()
	screen.setup(WIDTH, HEIGHT)
	screen.title("Weber racing")

racers=9
random.shuffle(COLOURS )
colours=[:racers]
winner=race(colours)
print(f"the winner is turtle{winner}🎖️🏆")
# Keeps the window open so it doesn't flash and close
turtle.done()
