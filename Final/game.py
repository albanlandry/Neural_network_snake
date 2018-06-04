import pygame
import time
from random import randint
import numpy as np
import csv
import math
from keras.models import Sequential
from keras.layers import Dense, Activation
from keras.models import model_from_json
from ann_visualizer.visualize import ann_viz;
import os
' Classes responsible for drawing elements on the surface'
class Drawer:
	DEFAULT_WIDTH = 10
	DEFAULT_HEIGHT = 10

	def draw(self, surface):
		pass
''' Game Elements '''
class Labyrinth(Drawer):
	'Labyrinth use inside the game'
	''' pattern : table 40,40 
		1 = there is a block
		0 = there is no block
	''' 
	DEFAULT_PATTERN = [
					  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
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
					  [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
					  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
	]

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
		self.nb_steps = 0
		
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
		
		self.nb_steps +=1
		
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
	DEFAULT_SIZE = 20
	
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
	
		
class SnakeGame():
	gameName = "Neural Network SNAKE"
	step = 10
	speed = 30.0/1000.0
	WIDTH = 400
	HEIGHT = 450

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
		self.steps = None
		self.score_point = 0
		self.input_data = []
		self.count = 1		
		self.model = self.load_model()
		self.visualize_model(self.model)
		
	def on_init(self):
		pygame.init()
		self.gameDisplay = pygame.display.set_mode(self.size, pygame.HWSURFACE | pygame.DOUBLEBUF)
		pygame.display.set_caption(self.gameName)
		self.labyrinth = Labyrinth(Labyrinth.DEFAULT_PATTERN)
		self.food = Food(20, 20)
		self.isRunning = True
		self.gameLogic = GameLogic()
		self.score = TextDrawer(pygame.font.Font(None, TextDrawer.DEFAULT_SIZE),
								10, self.labyrinth.height * 10 + 10,
								"Score : " + str(self.score_point))

		self.steps = TextDrawer(pygame.font.Font(None, TextDrawer.DEFAULT_SIZE),
								10,self.labyrinth.height * 10 + 30,
								"Steps : " + str(self.score_point))
								
		self.total_games = TextDrawer(pygame.font.Font(None, TextDrawer.DEFAULT_SIZE),
								self.labyrinth.width *10 // 2, self.labyrinth.height * 10 + 10,
								"Game : " + str(self.count))
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
		if self.count <= 1000:
			# Add the state of the board to the input
			board_state = self.get_board_state(self.player, np.array(self.labyrinth.pattern))
			self.input_data = board_state
			# Adding the current direction to the inputs
			self.input_data.append(self.player.direction/3)
			# Adding the angle
			angle = self.compute_angle(self.player, self.food) / 180
			self.input_data.append(angle)
			self.input_data.append(self.food.x / 380)
			self.input_data.append(self.food.y / 380)
			self.input_data.append(self.player.x[0] / 380)
			self.input_data.append(self.player.y[0] / 380)
			# Make prediction
			action = self.predict(self.input_data, self.model)
			self.input_data.append(action)
			
			# Update snake position 
			self.player.direction = action
			self.player.update()
			# print(angle)
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
			else:
				# Save the results each time the snake dies
				data = [self.count, self.score_point, self.player.nb_steps, self.player.length]
				self.write_in_file("results.csv", data)
				self.on_reset()
				self.count +=1
			
			print("Predicted action : " + self.get_action(action))
			
	def on_render(self):
		self.gameDisplay.fill((255, 255, 255))
		
		'Rendering of the snake, the player'
		self.food.draw(self.gameDisplay)
		self.player.draw(self.gameDisplay)
		self.labyrinth.draw(self.gameDisplay)
		
		'Render the actual score and steps of the player'		
		self.score.text = self.score.font.render("Score : "+str(self.score_point),True,(0, 0, 0))
		self.steps.text = self.score.font.render("Steps : "+str(self.player.nb_steps),True,(0, 0, 0))
		self.total_games.text = self.score.font.render("Game : "+str(self.count),True,(0, 0, 0))
		
		self.score.draw(self.gameDisplay)
		self.steps.draw(self.gameDisplay)
		self.total_games.draw(self.gameDisplay)
		
		pygame.display.flip()
		
	def on_cleanup(self):
		pygame.quit()
		
	def on_reset(self):
		self.player = Snake()
		self.gameDisplay = pygame.display.set_mode(self.size, pygame.HWSURFACE | pygame.DOUBLEBUF)
		pygame.display.set_caption(self.gameName)
		self.labyrinth = Labyrinth(Labyrinth.DEFAULT_PATTERN)
		self.food = Food(20, 20)
		self.score_point = 0
		self.player.snake = 0
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
		
	
	def get_action(self, action):
		direction = ["UP", "DOWN", "LEFT", "RIGHT"]
		return direction[action[0]]
	
	'API used for the machine learning program'
	def start_pause(self):
		self.isStarted = not self.isStarted
		
	def get_board_state(self, snake, labyrinth):
		# Retrieve the occupied positions
		
		for i in range(1, snake.length-1):
			player_x = snake.x[i] // snake.DEFAULT_WIDTH 
			player_y = snake.y[i] // snake.DEFAULT_HEIGHT
			
			labyrinth[player_y, player_x] = 1
		
		directions = []
		player_x = snake.x[0] // snake.DEFAULT_WIDTH 
		player_y = snake.y[0] // snake.DEFAULT_HEIGHT

		directions.append(labyrinth[player_y-1, player_x]) # up block
		directions.append(labyrinth[player_y+1, player_x]) # down block
		directions.append(labyrinth[player_y, player_x-1]) # left block
		directions.append(labyrinth[player_y, player_x+1]) # right block

		return directions
		
	def compute_angle(self, snake, food):
		if(snake.direction == 2 or snake.direction == 3):
			return math.degrees(math.atan2(- food.y + snake.y[0], food.x - snake.x[0]))
		return math.degrees(math.atan2(food.x - snake.x[0], food.y - snake.y[0]))
	
	def build_model(self):
		# The model
		model = Sequential()
		model.add(Dense(25, input_dim=10, activation='relu'))
		model.add(Dense(25, activation='relu'))
		model.add(Dense(6, activation='sigmoid'))
		return model
		
	def train(self, model):
		np.random.seed(123)
		dataset = np.loadtxt("dataset.csv", delimiter=",")
		X = dataset[:,0:10]
		X[:,4] /= 3.0
		Y = dataset[:,10]
		# Compile model#
		model.compile(loss='sparse_categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
		# Fit the model
		model.fit(X, Y, epochs=100, batch_size=100)
		
		return model
	
	def test_model(self, model):
		# evaluate the model
		test_dataset = np.loadtxt("test_data.csv", delimiter=",")
		TEST_X = test_dataset[:,0:10]
		TEST_X[:,4] /= 3.0
		TEST_Y = test_dataset[:,10]
		
		#Predict
		PREDICTED_Y = model.predict_classes(TEST_X)
		
		for i in range(len(TEST_X)):
			print("X=%s, Predicted=%s" % (TEST_X[i], PREDICTED_Y[i]))
		
		# evaluate the model
		scores = model.evaluate(TEST_X, TEST_Y)
		print("\n%s: %.2f%%" % (model.metrics_names[1], scores[1]*100))
		
	def predict(self, input, model):
		return model.predict_classes(np.array([input]))
		
	def save_model(self, model):
		# serialize model to JSON
		model_json = model.to_json()
		with open("model.json", "w") as json_file:
			json_file.write(model_json)
		# serialize weights to HDF5
		model.save_weights("model.h5")
		print("Saved model to disk")
	
	def load_model(self):
		# load json and create model
		json_file = open('model.json', 'r')
		loaded_model_json = json_file.read()
		json_file.close()
		loaded_model = model_from_json(loaded_model_json)
		# load weights into new model
		loaded_model.load_weights("model.h5")
		print("Loaded model from disk")
		
		return loaded_model
	
	def visualize_model(self, model):
		ann_viz(model, title="Snake Artificial Neural Network")
	
	'Learning API'
	def learn(self):
		model = self.build_model()
		model = self.train(model)

		return model
		# self.test_model(model)
if __name__ == "__main__" :
	app = SnakeGame()
	app.on_execute()
