import pygame
import time
from random import randint
from Observer import Subject
import numpy as np
import csv
from keras.models import Sequential
from keras.layers import Dense, Activation

' Classes responsible for drawing elements on the surface'
class Drawer:
	DEFAULT_WIDTH = 10
	DEFAULT_HEIGHT = 10

	def draw(self, surface):
		pass
''' Game Elements '''
class Labyrinth(Drawer):
	'Labyrinth use inside the game'
	DEFAULT_PATTERN = [
					  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
					  [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
					  [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
					  [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
					  [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
					  [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
					  [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
					  [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
					  [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
					  [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
					  [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
					  [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
					  [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
					  [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
					  [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
					  [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
					  [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
					  [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
					  [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
					  [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
					  [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
					  [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
					  [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
					  [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
					  [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
					  [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
					  [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
					  [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
					  [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
					  [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
					  [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
					  [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
					  [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
					  [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
					  [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
					  [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
					  [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
					  [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
					  [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
					  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
	]
	
	''' pattern : table 40,40 
		1 = there is a block
		0 = there is no block
	''' 
	def __init__(self, pattern = []):
		self.pattern = pattern
		self.height = len(pattern)
		self.width = len(pattern[0])
		
	def draw(self, surface):
		for i in range(0, len(self.pattern)):
			for j in range(0, len(self.pattern[i])):
				if self.pattern[i][j] == 1:
					pygame.draw.rect(surface, (150, 150, 150), pygame.Rect(j * self.DEFAULT_HEIGHT, i * self.DEFAULT_HEIGHT, self.DEFAULT_HEIGHT, self.DEFAULT_WIDTH))

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
		self.isAlive = True
		
		for i in range(self.length-1, -1, -1):
			self.x.append(i * self.step)
			self.y.append(self.DEFAULT_WIDTH)
	
	def move_up(self):
		self.direction = self.DIRECTION_UP
		# print("up")
		
	def move_down(self):
		self.direction = self.DIRECTION_DOWN
		# print("down")
		
	def move_left(self):
		self.direction = self.DIRECTION_LEFT
		# print("left")
		
	def move_right(self):
		self.direction = self.DIRECTION_RIGHT
		# print("right")
		
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
		pygame.draw.rect(surface, (0, 0, 0), pygame.Rect(self.x[0], self.y[0], 10, 10)) 
		
		for i in range(1, self.length):
			pygame.draw.rect(surface, (255, 0, 0), pygame.Rect(self.x[i], self.y[i], 10, 10)) 

class Food(Drawer):
	'The food to be eaten by the snake, the player'
	def __init__(self, x, y):
		self.x = x
		self.y = y
		
	def draw(self, surface):
		pygame.draw.rect(surface, (0, 0, 250), pygame.Rect(self.x, self.y, self.DEFAULT_WIDTH, self.DEFAULT_HEIGHT)) 
		
class TextDrawer(Drawer):
	DEFAULT_SIZE = 15
	
	def __init__(self, font, x= 0, y=0, text='', color=(0, 0, 0)):
		self.font = font
		self.text = font.render(text, True, color)
		self.color = color
		self.x = x
		self.y = y
		
	def draw(self, surface):
		surface.blit(self.text, (self.x, self.y))
		

class GameLogic:
	def isCollision(self,x1,y1,x2,y2, bsize = 0):
		if (x1 < x2 + bsize and x1 + bsize > x2 and y1 < y2 + bsize and bsize + y1 > y2):
			return True
		return False		
	
		
class SnakeGame(Subject):
	gameName = "Neural Network SNAKE"
	step = 10
	speed = 100.0/1000.0
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
		self.score = None
		self.score_point = 0
		self.input_data = []
		self.count = 150
		self.model = None
		
	def on_init(self):
		pygame.init()
		self.gameDisplay = pygame.display.set_mode(self.size, pygame.HWSURFACE | pygame.DOUBLEBUF)
		pygame.display.set_caption(self.gameName)
		self.labyrinth = Labyrinth(Labyrinth.DEFAULT_PATTERN)
		self.food = Food(20, 20)
		self.isRunning = True
		self.gameLogic = GameLogic()
		self.score = TextDrawer(pygame.font.Font(None, TextDrawer.DEFAULT_SIZE),
								TextDrawer.DEFAULT_SIZE,
								self.HEIGHT + TextDrawer.DEFAULT_SIZE,
								"Score : " + str(self.score_point))
	
	'Handle game and player events'
	def on_event(self, event):
		if event.type == pygame.constants.QUIT:
			self.isRunning = False
		
		'Handle key pressed'
		pressed = pygame.key.get_pressed()
		if pressed[pygame.K_RETURN]:
			self.start_pause()
			
		if pressed[pygame.K_UP] and self.player.direction != 1:
			self.player.move_up()
			
		if pressed[pygame.K_DOWN] and self.player.direction != 0:
			self.player.move_down()
			
		if pressed[pygame.K_LEFT] and self.player.direction != 3:
			self.player.move_left()
			
		if pressed[pygame.K_RIGHT] and self.player.direction != 2:
			self.player.move_right()
		
	def on_execute(self):
		if self.on_init () == False:
			self.isRunning = False
		
		self.time.tick(24)
		
		self.model = self.learn()
		
		while(self.isRunning):
			pygame.event.pump()
			for event in pygame.event.get():
				self.on_event(event)
			
			if self.isStarted and self.count > 0:
				self.on_loop()
				
			self.on_render()
			
			time.sleep(self.speed)
		self.on_cleanup()
		
	def on_loop(self):
		# Add the selected action to the inputs array 
		self.input_data = self.get_board_state(self.player, np.array(self.labyrinth.pattern))
		# Automatic action selection
		action = self.generate_action()
		self.input_data.append(action)
		
		isDirectionOk = self.predict(np.array([self.input_data]), self.model)
		
		if isDirectionOk:
			self.get_action(action)
			self.player.update()
		
		
		# print(self.input_data, isDirectionOk)	
		
		#print(self.player.x[0], self.player.y[0])
		
		# Update snake position 

		
		if self.isCollisionWithLabyrinth(self.player, self.labyrinth) or self.isCollisionWithSnake(self.player):
			self.player.isAlive = False
		
		# if the player is Alive he maybe able to eat
		if self.player.isAlive:
			# Detect if the snake eat the food
			for i in range(0,self.player.length):
				if self.gameLogic.isCollision(self.food.x,self.food.y,self.player.x[i], self.player.y[i], 10):
					self.score_point += 1
					food_x = randint(0,self.labyrinth.width - 1)
					food_y = randint(0,self.labyrinth.height - 1)
					
					# Make sure that the food does not appear at a place occupied by a block
					while self.labyrinth.pattern[food_y][food_x] == 1:
						food_x = randint(0,self.labyrinth.width - 1)
						food_y = randint(0,self.labyrinth.width - 1)						
					
					self.food.x, self.food.y = food_x * self.player.DEFAULT_WIDTH, food_y * self.player.DEFAULT_HEIGHT
					self.player.grow()
			self.input_data.append(1)
		else:
			self.input_data.append(0)
			self.on_reset()
			self.count -=1
		
		# print(self.input_data)
		# self.write_in_file("test_data.csv", self.input_data)
	
	def on_render(self):
		self.gameDisplay.fill((255, 255, 255))
		
		'Rendering of the snake, the player'
		self.food.draw(self.gameDisplay)
		self.player.draw(self.gameDisplay)
		self.labyrinth.draw(self.gameDisplay)
		
		'Render the actual score of the player'
		self.score.draw(self.gameDisplay)
		
		pygame.display.flip()
		
	def on_cleanup(self):
		pygame.quit()
		
	def on_reset(self):
		self.player = Snake()
		self.gameDisplay = pygame.display.set_mode(self.size, pygame.HWSURFACE | pygame.DOUBLEBUF)
		pygame.display.set_caption(self.gameName)
		self.labyrinth = Labyrinth(Labyrinth.DEFAULT_PATTERN)
		self.food = Food(20, 20)
		self.gameLogic = GameLogic()

	'Game utility functions'
	#write in csv file
	def write_in_file(self, filename, line):
		with open(filename, 'a+') as myfile:
			wr = csv.writer(myfile)
			wr.writerow(line)
	
	# Detect whether the snake collides with himself
	def isCollisionWithSnake(self, player):
		for i in range(1, player.length):
			if self.gameLogic.isCollision(player.x[0], player.y[0], player.x[i], player.y[i], 10):
				return True
				
		return False

	# Check whether the snake collides with the labyrinth's block
	def isCollisionWithLabyrinth(self, snake, labyrinth):
		for i in range(0, len(labyrinth.pattern)):
			for j in range(0, len(labyrinth.pattern[i])):
				if labyrinth.pattern[j][i] == 1 and self.gameLogic.isCollision(snake.x[0], snake.y[0], i * 10, j * 10, 10):
					return True
					
		return False
		
	'API used for the machine learning program'
	def start_pause(self):
		self.isStarted = not self.isStarted
		
	def generate_action(self):
		action = randint(0,2) - 1
		return action

	def get_action(self, action):
		if action == -1:
			if self.player.direction == 0:
				self.player.move_left()
			elif self.player.direction == 1:
				self.player.move_right()
			elif self.player.direction == 2:
				self.player.move_down()
			elif self.player.direction == 3:
				self.player.move_up()
		elif action == 1:
			if self.player.direction == 0:
				self.player.move_right()
			elif self.player.direction == 1:
				self.player.move_left()
			elif self.player.direction == 2:
				self.player.move_up()
			elif self.player.direction == 3:
				self.player.move_down()
		else:
			pass

	def get_board_state(self, snake, labyrinth):
		# Retrieve the occupied positions
		'''
		for i in range(1, snake.length-1):
			player_x = snake.x[i] // snake.DEFAULT_WIDTH 
			player_y = snake.y[i] // snake.DEFAULT_HEIGHT
			
			labyrinth[player_y, player_x] = 1
		'''
		directions = []
		player_x = snake.x[0] // snake.DEFAULT_WIDTH 
		player_y = snake.y[0] // snake.DEFAULT_HEIGHT
				
		if player_x < 39 and player_y < 39:
			if snake.direction == 0: # the snake goes up
				directions.append(labyrinth[player_y, player_x-1]) # left block
				directions.append(labyrinth[player_y-1, player_x]) # front block
				directions.append(labyrinth[player_y, player_x+1]) # right block
			elif snake.direction == 1: # the snake goes down
				directions.append(labyrinth[player_y, player_x+1]) # left block
				directions.append(labyrinth[player_y+1, player_x]) # front block
				directions.append(labyrinth[player_y, player_x-1]) # right block
			elif snake.direction == 2: # the snake goes left
				directions.append(labyrinth[player_y+1, player_x]) # left block
				directions.append(labyrinth[player_y, player_x-1]) # front block
				directions.append(labyrinth[player_y-1, player_x]) # right block
			else:# The snake goes right
				directions.append(labyrinth[player_y-1, player_x]) # left block
				directions.append(labyrinth[player_y, player_x+1]) # front block
				directions.append(labyrinth[player_y+1, player_x]) # right block		
		
		return directions
	
	def build_model(self):
		# The model
		model = Sequential()
		model.add(Dense(4, input_dim=4, activation='relu'))
		model.add(Dense(4, activation='relu'))
		model.add(Dense(1, activation='sigmoid'))
		
		return model
		
	def train(self, model):
		np.random.seed(7)
		dataset = np.loadtxt("dataset.csv", delimiter=",")
		X = dataset[:,0:4]
		Y = dataset[:,4]
		# Compile model#
		model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
		# Fit the model
		model.fit(X, Y, epochs=10, batch_size=10)
		
		return model
	
	def test_model(self, model):
		# evaluate the model
		test_dataset = np.loadtxt("test_data.csv", delimiter=",")
		TEST_X = test_dataset[:,0:4]
		TEST_Y = test_dataset[:,4]
		
		#Predict
		PREDICTED_Y = model.predict_classes(TEST_X)
		
		for i in range(len(TEST_X)):
			print("X=%s, Predicted=%s" % (TEST_X[i], PREDICTED_Y[i]))
		
		# evaluate the model
		scores = model.evaluate(TEST_X, TEST_Y)
		print("\n%s: %.2f%%" % (model.metrics_names[1], scores[1]*100))
		
	def predict(self, input, model):
		y = model.predict_classes(input)
		
		if int(y[0, 0]) == 1:
			return True
		# print(input, int(y[0, 0]))
		return False
		
	'Learning API'
	def learn(self):
		model = self.build_model()
		model = self.train(model)
		'''
		value = np.array([[1., 0., 0., 0.]])
		self.predict(value, model)
		'''
		return model
		# self.test_model(model)
if __name__ == "__main__" :
	app = SnakeGame()
	app.on_execute()
