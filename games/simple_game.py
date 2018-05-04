#import the pygame module, and the
#sys module for exiting the window we create
import pygame, sys

#import some useful constants
from pygame.locals import *

class Player(object):
    
    def __init__(self):
        self.rect = pygame.rect.Rect((150,280,20,20))
        
    def handleMovement(self):
        key = pygame.key.get_pressed()
        
        if key[pygame.K_LEFT] and self.rect.left > 0:
           self.rect.move_ip(-10, 0)
        if key[pygame.K_RIGHT] and self.rect.right < 300:
           self.rect.move_ip(10, 0)
           
    def draw(self):
        pygame.draw.rect(screen, (0,255,255), self.rect)
        
class Rock(object):
    def __init__(self,params):
        self.rect = pygame.rect.Rect(params)
    def fall(self):
        self.rect.move_ip(0,-10)
    def draw(self):
        pygame.draw.rect(screen, (0,255,0), self.rect)

class Point(object):
    def __init__(self,params):
        self.rect = pygame.rect.Rect(params)
    def fall(self):
        self.rect.move_ip(0,-10)
    def draw(self):
        pygame.draw.rect(screen, (255,255,0), self.rect)
    def draw(self):
        pygame.draw.rect(screen, (0,0,0), self.rect)
        
class backgroundTile(object):
    def __init__(self,params):
        self.rect = pygame.rect.Rect((params[0],params[1],10,10))

#initiating the game tiles
tiles = [[backgroundTile for i in range(10)] for j in range(10)]

#initialise the pygame module
pygame.init()

#create a new drawing surface, width=300, height=300
screen = pygame.display.set_mode((300,300))
#give the window a caption
pygame.display.set_caption('My First Game')

clock = pygame.time.Clock()

#create player square
player = Player()
#loop (repeat) forever
while True:

    #get all the user events
    for event in pygame.event.get():
        #if the user wants to quit
        if event.type == QUIT:
            #end the game and close the window
            pygame.quit()
            sys.exit()
            
    screen.fill((0,0,0))
    player.draw()
    player.handleMovement()
    #update the display        
    pygame.display.update()
    
    clock.tick(20)
    
   
        