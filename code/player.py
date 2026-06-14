from settings import *

class Player(pygame.sprite.Sprite):
    def __init__(self, pos, groups, collision_sprites):
        super().__init__(groups)
        self.image = pygame.image.load(join('images', 'player', 'down', '0.png')).convert_alpha()
        self.rect = self.image.get_frect(center = pos)
        #pos = position (will be fetched from parameter)
        self.hitbox_rect = self.rect.inflate(-40, 0) #changes hitbox of the rectangel so the annoying white cpace is gone 
       
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
        self.hitbox_rect.x += self.direction.x * self.speed * dt #basically new position = old position + direction x speed x time
        self.collision('horizontal') #checks collision on x axis
        self.hitbox_rect.y += self.direction.y * self.speed * dt
        self.collision('vertical') #checks collision on y axis

    def collision(self, direction):
        for sprite in self.collision_sprites:
            if sprite.rect.colliderect(self.rect):
                if direction == 'horizontal':
                #we are setting the right side of the player to the left side of the obsticle 
                    if self.direction.x > 0: self.rect.right = sprite.rect.left #checks if player is left to right of obsticle and stopt the player  
                    if self.direction.x < 0: self.rect.left = sprite.rect.right
                else:
                    if self.direction.y < 0: self.rect.top = sprite.rect.bottom
                    if self.direction.y > 0: self.rect.bottom = sprite.rect.top



    def update(self, dt):
        self.input()
        self.move(dt)