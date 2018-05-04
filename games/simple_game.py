#import the pygame module, and the
#sys module for exiting the window we create
import pygame, sys

#import some useful constants
from pygame.locals import *

BLACK = (0,0,0)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)

ROWS = 10
COLUMNS = 10
TILESIZE = 30

class Player(object):
    
    def __init__(self):
        self.rect = pygame.rect.Rect((150,270,30,30))
        
    def handleMovement(self):
        key = pygame.key.get_pressed()
        
        if key[pygame.K_LEFT] and self.rect.left > 0:
           self.rect.move_ip(-10, 0)
        if key[pygame.K_RIGHT] and self.rect.right < COLUMNS*TILESIZE:
           self.rect.move_ip(10, 0)
           
    def draw(self):
        pygame.draw.rect(screen, BLUE, self.rect)
        
class Rock(object):
    def __init__(self,params):
        self.rect = pygame.rect.Rect(params)
    def fall(self,tiles):
        self.rect.move_ip(0,-10)
    def draw(self):
        pygame.draw.rect(screen, RED, self.rect)

class Point(object):
    def __init__(self,column,tiles):
        self.rect = pygame.rect.Rect(params)
        tiles[0][column] = 
    def fall(self,tiles):
        self.rect.move_ip(0,-10)
    def draw(self):
        pygame.draw.rect(screen, GREEN, self.rect)
        
class backgroundTile(object):
    def __init__(self,params):
        self.rect = pygame.rect.Rect((params[0],params[1],10,10))

#initiating the game tiles


#initialise the pygame module
pygame.init()

#create a new drawing surface, width=300, height=300
screen = pygame.display.set_mode((ROWS*TILESIZE,COLUMNS*TILESIZE))
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
    
def drawTiles(tiles):
    
   
        