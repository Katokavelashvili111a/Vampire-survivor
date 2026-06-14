from settings import *

class Player(pygame.sprite.Sprite):
    def __init__(self, pos, groups):
        super().__init__(groups)
        self.image = pygame.image.load(join('images', 'player', 'down', '0.png')).convert_alpha()
        self.rect = self.image.get_frect(center = pos)
        #pos = position (will be fetched from parameter)
       
        self.direction = pygame.Vector2() 
        self.speed = 500

    def input(self):
        keys = pygame.key.get_pressed() #i think this means it reads whichever key is inputted, sso pressed....
        self.direction.x = int(keys[pygame.K_RIGHT]) - int(keys[pygame.K_LEFT])
        self.direction.y = int(keys[pygame.K_DOWN]) - int(keys[pygame.K_UP])
        self.direction = self.direction.normalize() if self.direction else self.direction
    #def is define for methods. remember
    def move(self, dt):
        self.rect.center += self.direction * self.speed * dt #basically new position = old position + direction x speed x time

    def update(self, dt):
        self.input()
        self.move(dt)