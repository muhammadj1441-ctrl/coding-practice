from pygame import *
init() # set up pygame
width = 700
height = 700
# surface! - can draw to it
# tuple - like a list/array - cannot change!
screen = display.set_mode((width, height))

endGame = False
while endGame == False:
	# events
	for e in event.get(): # get all events
		if e.type == QUIT:
			endGame = True
	screen.fill((53,137,134)) # tuple - RGB
	draw.rect(screen, (30,41,231), (20,20,660,640))
	draw.circle(screen, (255,0,0), (70,90), 40)
	
	
	
	display.flip()
	# draw
