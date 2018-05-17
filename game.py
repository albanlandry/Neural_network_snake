import pygame
import time

class snake:
	'Player class'
	direction = 3
	
	def __init__(self, length = 3, step = 10):
		self.step = step
		self.x = []
		self.y = []
		self.length = length
		
		for i in range(self.length-1, -1, -1):
			self.x.append(i * self.step)
			self.y.append(0)
			
		print(self.x)
	
	def move_up(self, step):
		direction = 0
		self.y[0] -= step
	
	def move_down(self, step):
		direction = 1
		self.y[0] += step
		
	def move_left(self, step):
		direction = 2
		self.x[0] -= step
	
	def move_right(self, step):
		direction = 3
		self.x[0] += step
		
	def update(self):
		print("update")

class food:
	'The food to be eaten by the snake, the player'
	def __init__(self, x, y):
		self.x = x
		self.y = y
		
class SnakeGame:
	gameName = "Neural Network SNAKE"
	step = 10
	speed = 50.0/1000.0

	def __init__(self):
		self.isRunning = True
		self.player = snake()
		self.gameDisplay = None
		self.size = self.weight, self.height = 640, 400
		self.time = pygame.time.Clock()
		
	def on_init(self):
		pygame.init()
		self.gameDisplay = pygame.display.set_mode(self.size, pygame.HWSURFACE | pygame.DOUBLEBUF)
		pygame.display.set_caption(self.gameName)
		self.isRunning = True
	
	'Handle game and player events'
	def on_event(self, event):
		if event.type == pygame.constants.QUIT:
			self.isRunning = False
		
		'Handle key pressed'
		pressed = pygame.key.get_pressed()
		if pressed[pygame.K_UP]:
			self.player.move_up(self.step)
			
		if pressed[pygame.K_DOWN]:
			self.player.move_down(self.step)
			
		if pressed[pygame.K_LEFT]:
			self.player.move_left(self.step)
			
		if pressed[pygame.K_RIGHT]:
			self.player.move_right(self.step)
		
	def on_execute(self):
		if self.on_init () == False:
			self.isRunning = False
		
		self.time.tick(60)
		
		while(self.isRunning):
			for event in pygame.event.get():
				self.on_event(event)
			self.on_loop()
			self.on_render()
			
			time.sleep(self.speed)
		self.on_cleanup()
		
	def on_loop(self):
		self.player.update()
		pass
		
	def on_render(self):
		self.gameDisplay.fill((255, 255, 255))
		
		'Rendering of the snake, the player'
		pygame.draw.rect(self.gameDisplay, (255, 0, 0), pygame.Rect(self.player.x[0], self.player.y[0], 10, 10))
		
		pygame.display.flip()
		
	def on_cleanup(self):
		pygame.quit()
		
	def start(self):
		game_init()
		
		
	
	
if __name__ == "__main__" :
	app = SnakeGame()
	app.on_execute()