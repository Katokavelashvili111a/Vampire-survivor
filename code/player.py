from settings import *

class Player(pygame.sprite.Sprite):
    def __init__(self, pos, groups, collision_sprites):
        super().__init__(groups)
        self.image = pygame.image.load(join('images', 'player', 'down', '0.png')).convert_alpha()
        self.rect = self.image.get_frect(center = pos)
        #pos = position (will be fetched from parameter)
       
       #movement
        self.direction = pygame.Vector2() 
        self.speed = 500
        self.collision_sprites = collision_sprites

    def input(self):
        keys = pygame.key.get_pressed() #i think this means it reads whichever key is inputted, sso pressed....
        self.direction.x = int(keys[pygame.K_RIGHT]) - int(keys[pygame.K_LEFT]) #movement on x axis
        self.direction.y = int(keys[pygame.K_DOWN]) - int(keys[pygame.K_UP]) #movement on y axis
        self.direction = self.direction.normalize() if self.direction else self.direction #the movemetn speed becomes constant so it doesnt move at different speeds depending on the direction
    #def is define for methods. remember
    def move(self, dt):
        self.rect.x += self.direction.x * self.speed * dt #basically new position = old position + direction x speed x time
        self.rect.y += self.direction.y * self.speed * dt

    def collision(self, direstion):
        pass

    def update(self, dt):
        self.input()
        self.move(dt)