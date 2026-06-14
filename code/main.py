from settings import *
from player import Player
from sprites import *

from random import randint

class Game:
    def __init__(self):
        #setup
        pygame.init()
        self.display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption('Survivor')
        self.clock = pygame.time.Clock()
        self.running = True

        #groups? <-- figure out what this means!!
        self.all_sprites = pygame.sprite.Group()
        #these are the parameters that player is fetching
        #sprites
        self.player = Player((400, 300), self.all_sprites)
        for i in range(6): # will place 6 collisions
            x,y = randint(0, WINDOW_WIDTH), randint(0, WINDOW_HEIGHT) #will place collisions at random locations on the x and y axis
            w,h = randint(60,100), randint(50,100)
            CollisionSprite((x,y), (w,h), self.all_sprites) 

    def run(self):
        while self.running:
            #delta ttime
            dt = self.clock.tick() / 1000

            #event loop 
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
            
            #update
            #this will make the sprites update with delta time so the time that passes between every frame will be very short
            self.all_sprites.update(dt)
            #draw
            self.display_surface.fill('black')
            self.all_sprites.draw(self.display_surface)
            pygame.display.update()
        pygame.quit()

if __name__ == '__main__':
    game = Game()
    game.run()
            

