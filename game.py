import pygame
import time
from random import randint

' Classes responsible for drawing elements on the surface'
class Drawer:
	DEFAULT_WIDTH = 10
	DEFAULT_HEIGHT = 10

	def draw(self, surface):
		pass
''' Game Elements '''
class Labyrinth(Drawer):
	'Labyrinth use inside the game'
	height = 40
	width = 40
	DEFAULT_PATTERN = [
					  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
					  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
					  [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
					  [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
					  [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
					  [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
					  [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
					  [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
					  [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
					  [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
					  [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
					  [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
					  [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
					  [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
					  [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
					  [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
					  [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
					  [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
					  [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
					  [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
					  [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
					  [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
					  [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
					  [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
					  [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
					  [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
					  [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
					  [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
					  [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
					  [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
					  [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
					  [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
					  [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
					  [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
					  [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
					  [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
					  [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
					  [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
					  [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
					  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
	]
	
	''' pattern : table 40,40 
		1 = there is a block
		0 = there is no block
	''' 
	def __init__(self, pattern = []):
		self.pattern = pattern
		
	def draw(self, surface):
		for i in range(0, len(self.pattern)):
			for j in range(0, len(self.pattern[i])):
				if self.pattern[i][j] == 1:
					pygame.draw.rect(surface, (50, 50, 50), pygame.Rect(j * self.DEFAULT_HEIGHT, i * self.DEFAULT_HEIGHT, self.DEFAULT_HEIGHT, self.DEFAULT_WIDTH))

class Snake(Drawer):
	'Player class'
	DIRECTION_UP = 0
	DIRECTION_DOWN = 1
	DIRECTION_LEFT = 2
	DIRECTION_RIGHT = 3
	
	def __init__(self, length = 3, step = 10):
		self.step = step
		self.x = []
		self.y = []
		self.length = length
		self.direction = 3
		
		for i in range(self.length-1, -1, -1):
			self.x.append(i * self.step)
			self.y.append(self.DEFAULT_WIDTH)
	
	def move_up(self, step):
		self.direction = self.DIRECTION_UP
		
	def move_down(self, step):
		self.direction = self.DIRECTION_DOWN
		
	def move_left(self, step):
		self.direction = self.DIRECTION_LEFT
		
	def move_right(self, step):
		self.direction = self.DIRECTION_RIGHT
		
	def update(self):
		previousX = self.x[0]
		previousY = self.y[0]
	
		if self.direction == 0:
			self.y[0] -= self.step
		if self.direction == 1:
			self.y[0] += self.step
		if self.direction == 2:
			self.x[0] -= self.step
		if self.direction == 3:
			self.x[0] += self.step
		
		for i in range(self.length-1, 0, -1):
			if(i == 1): 
				self.x[i] = previousX
				self.y[i] = previousY
			else:
				self.x[i] = self.x[i-1]
				self.y[i] = self.y[i-1]
				
	def grow(self):
		self.x.append(0)
		self.y.append(0)
		self.length += 1
			
	def draw(self, surface):
		for i in range(0, self.length):
			pygame.draw.rect(surface, (255, 0, 0), pygame.Rect(self.x[i], self.y[i], 10, 10)) 

class Food(Drawer):
	'The food to be eaten by the snake, the player'
	def __init__(self, x, y):
		self.x = x
		self.y = y
		
	def draw(self, surface):
		pygame.draw.rect(surface, (0, 0, 250), pygame.Rect(self.x, self.y, self.DEFAULT_WIDTH, self.DEFAULT_HEIGHT)) 

class GameLogic:
	def isCollision(self,x1,y1,x2,y2, bsize = 0):
		if x1 == x2 and y1==y2:
			return True
		return False
		
class SnakeGame:
	gameName = "Neural Network SNAKE"
	step = 10
	speed = 150.0/1000.0
	WIDTH = 400
	HEIGHT = 500

	def __init__(self):
		self.isRunning = False #Used for the main loop
		self.isStarted = False #Used to have the player start moving
		self.player = Snake()
		self.food = None
		self.gameDisplay = None
		self.size = self.WIDTH, self.HEIGHT
		self.labyrinth = None
		self.time = pygame.time.Clock()
		self.game = None
		
	def on_init(self):
		pygame.init()
		self.gameDisplay = pygame.display.set_mode(self.size, pygame.HWSURFACE | pygame.DOUBLEBUF)
		pygame.display.set_caption(self.gameName)
		self.labyrinth = Labyrinth(Labyrinth.DEFAULT_PATTERN)
		self.food = Food(20, 20)
		self.isRunning = True
		self.gameLogic = GameLogic()
	
	'Handle game and player events'
	def on_event(self, event):
		if event.type == pygame.constants.QUIT:
			self.isRunning = False
		
		'Handle key pressed'
		pressed = pygame.key.get_pressed()
		if pressed[pygame.K_RETURN]:
			self.isStarted = not self.isStarted
			
		if pressed[pygame.K_UP] and self.player.direction != 1:
			self.player.move_up(self.step)
			
		if pressed[pygame.K_DOWN] and self.player.direction != 0:
			self.player.move_down(self.step)
			
		if pressed[pygame.K_LEFT] and self.player.direction != 3:
			self.player.move_left(self.step)
			
		if pressed[pygame.K_RIGHT] and self.player.direction != 2:
			self.player.move_right(self.step)
		
	def on_execute(self):
		if self.on_init () == False:
			self.isRunning = False
		
		self.time.tick(24)
		
		while(self.isRunning):
			pygame.event.pump()
			for event in pygame.event.get():
				self.on_event(event)
			
			if self.isStarted:
				self.on_loop()
			
			self.on_render()
			
			time.sleep(self.speed)
		self.on_cleanup()
		
	def on_loop(self):
		# Check whether the snake reaches the boundaries
		if (self.player.x[0] == (self.labyrinth.width - 1) * self.player.DEFAULT_WIDTH) and self.player.direction == self.player.DIRECTION_RIGHT:
			self.player.x[0] = 0
			
		if (self.player.y[0] == (self.labyrinth.height - 1) * self.player.DEFAULT_HEIGHT) and self.player.direction == self.player.DIRECTION_DOWN:
			self.player.y[0] = 0
			
		if self.player.x[0] < 0:
			self.player.x[0] = (self.labyrinth.width - 1) * self.player.DEFAULT_WIDTH
			
		if self.player.y[0] < 0:
			self.player.y[0] = (self.labyrinth.height - 1) * self.player.DEFAULT_HEIGHT
		
		# Update snake position 
		self.player.update()
		
		# Detect if the snake eat the food
		for i in range(0,self.player.length):
			if self.gameLogic.isCollision(self.food.x,self.food.y,self.player.x[i], self.player.y[i]):
				self.food.x = randint(1,self.labyrinth.width - 2) * 10
				self.food.y = randint(1,self.labyrinth.width - 2) * 10
				self.player.grow()

		# Detect whether the snake eats himself
		for i in range(1, self.player.length):
			if self.gameLogic.isCollision(self.player.x[0], self.player.y[0], self.player.x[i], self.player.y[i]):
				self.isStarted = False
		
	def on_render(self):
		self.gameDisplay.fill((255, 255, 255))
		
		'Rendering of the snake, the player'
		self.food.draw(self.gameDisplay)
		self.player.draw(self.gameDisplay)
		self.labyrinth.draw(self.gameDisplay)
		
		pygame.display.flip()
		
	def on_cleanup(self):
		pygame.quit()
	
if __name__ == "__main__" :
	app = SnakeGame()
	app.on_execute()
