import pygame

SCREEN = WIDTH, HEIGHT = (600, 200)

class Ground():
	def __init__(self):
		self.image = pygame.image.load('Assets/ground.png')
		self.rect = self.image.get_rect()

		self.width = self.image.get_width()
		self.x1 = 0
		self.x2 = self.width
		self.y = 150

	def update(self, speed):
		self.x1 -= speed
		self.x2 -= speed

		if self.x1 <= -self.width:
			self.x1 = self.width

		if self.x2 <= -self.width:
			self.x2 = self.width

	def draw(self, win):
		win.blit(self.image, (self.x1, self.y))
		win.blit(self.image, (self.x2, self.y))


class Dino():
	def __init__(self, x, y):
		self.x, self.base = x, y

		self.run_list = []
		self.duck_list = []

		for i in range(1, 4):
			img = pygame.image.load(f'Assets/Dino/{i}.png')
			img = pygame.transform.scale(img, (52, 58))
			self.run_list.append(img)

		for i in range(4, 6):
			img = pygame.image.load(f'Assets/Dino/{i}.png').convert_alpha()
			img = pygame.transform.scale(img, (70, 38))
			self.duck_list.append(img)

		self.index = 0
		self.image = self.run_list[self.index]
		self.rect = self.image.get_rect()
		self.rect.x = self.x
		self.rect.bottom = self.base

		self.counter = 0

		self.vel = 0
		self.gravity = 1
		self.jumpHeight = 15
		self.isJumping = False

	def update(self, jump, duck):
		if not self.isJumping and jump:
			self.vel = -self.jumpHeight
			self.isJumping = True

		self.vel += self.gravity
		if self.vel >= self.jumpHeight:
			self.vel = self.jumpHeight

		self.rect.y += self.vel
		if self.rect.bottom > self.base:
			self.rect.bottom = self.base
			self.isJumping = False

		if duck:
			self.counter += 1
			if self.counter >= 6:
				self.index = (self.index + 1) % len(self.duck_list)
				self.image = self.duck_list[self.index]
				self.rect = self.image.get_rect()
				self.rect.x = self.x
				self.rect.bottom = self.base
				self.counter = 0

		elif self.isJumping:
			self.index = 0
			self.counter = 0
			self.image = self.run_list[self.index]
		else:
			self.counter += 1
			if self.counter >= 4:
				self.index = (self.index + 1) % len(self.run_list)
				self.image = self.run_list[self.index]
				self.rect = self.image.get_rect()
				self.rect.x = self.x
				self.rect.bottom = self.base
				self.counter = 0

	def draw(self, win):
		win.blit(self.image, self.rect)

class Cactus(pygame.sprite.Sprite):
	def __init__(self, type):
		super(Cactus, self).__init__()

		self.image_list = []
		for i in range(4):
			scale = 0.65
			img = pygame.image.load(f'Assets/Cactus/{i+1}.png')
			w, h = img.get_size()
			img = pygame.transform.scale(img, (int(w*scale), int(h*scale)))
			self.image_list.append(img)

		self.image = self.image_list[type-1]
		self.rect = self.image.get_rect()
		self.rect.x = WIDTH + 10
		self.rect.bottom = 165

	def update(self, speed):
		self.rect.x -= speed
		if self.rect.right <= 0:
			self.kill()

	def draw(self, win):
		win.blit(self.image, self.rect)


class Cloud(pygame.sprite.Sprite):
	def __init__(self, x, y):
		super(Cloud, self).__init__()

			# scale = 0.65
		img = pygame.image.load(f'Assets/cloud.png')
			# w, h = img.get_size()
			# img = pygame.transform.scale(img, (int(w*scale), int(h*scale)))
			# self.image_list.append(img)

		self.image = img
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y

	def update(self, speed):
		self.rect.x -= speed
		if self.rect.right <= 0:
			self.kill()

	def draw(self, win):
		win.blit(self.image, self.rect)