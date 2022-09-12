import pygame
import os
from spritesheet import Spritesheet
import time

# Colors
WHITE = (255,255,255)
RED = (255,0,0)
BLACK = (0,0,0)

# Set up window
WIDTH, HEIGHT = 621, 425 # +10% 621,5 , 425,7 # +20% 678 , 464,4 of the gnome_house

# Players variables
RECT_PLAYER_WIDTH, RECT_PLAYER_HEIGHT = 50, 50

# Load imgs
# MAN_PLAYER = pygame.image.load(os.path.join('assets', 'george.png'))
# WOMAN_PLAYER = pygame.image.load(os.path.join('assets', 'betty.png'))

MAN_LASER = pygame.image.load(os.path.join('assets', 'pixel_laser_blue.png'))
WOMAN_LASER = pygame.image.load(os.path.join('assets', 'pixel_laser_red.png'))

# Cats - takes the same image, see it later
BLACK_CAT = pygame.image.load(os.path.join('assets', 'cats_all_black_and_white.png'))
WHITE_CAT = pygame.image.load(os.path.join('assets', 'cats_all_black_and_white.png'))

# House - Scaled Backgrounds
EXTERIOR_HOUSE = pygame.transform.scale(pygame.image.load(os.path.join('assets', 'exterior_house.jpg')), (WIDTH, HEIGHT))
GNOME_HOUSE = pygame.transform.scale(pygame.image.load(os.path.join('assets', 'gnome_house_conv.png')), (WIDTH, HEIGHT))
#GNOME_HOUSE = pygame.image.load(os.path.join('assets', 'gnome_house_conv.png')) # 565, 387
RETRO_HOUSE = pygame.transform.scale(pygame.image.load(os.path.join('assets', 'retro_house.jpg')), (WIDTH, HEIGHT))

class Entity():
    def __init__(self,x,y):
        self.x = x
        self.y = y
        
    def draw(self, window):
        pass

    def update(self):
        pass

class Animals(Entity): # Players or cats
    # Properties of this player
    def __init__(self, x, y, health=100):
        super().__init__(x, y)
        self.health = health
        # allow us to draw the player and the laser, when pick woman or man
        self.img = None
    
    # Player.draw, taking the window as parameter
    # def draw(self, window):
    #     # First draw a rectangle. where, color, 
    #     # x/y position, rect (dimension) and fill it = 0
    #     #pygame.draw.rect(window, RED, (self.x, self.y, RECT_PLAYER_WIDTH, RECT_PLAYER_HEIGHT), 0)
        
    #     # draw proper player, not rect
    #     window.blit(self.img, (self.x, self.y))

    #     # draw laser

class Player(Entity):
    # Class variables. For the number of the player and cooldown
    # NUMBER_MAP = {
    #     1: (MAN_PLAYER, MAN_LASER),
    #     2: (WOMAN_PLAYER, WOMAN_LASER)
    # }
    COOLDOWN = 30 # half a second

    def __init__(self, x, y, imageName, health=100):
        # Call the animals init method
        super().__init__(x, y)
        self.lasers = []
        self.cool_down_counter = 0
        # creating a mask, allow us to do pixel perfect collision
        #self.mask = pygame.mask.from_surface(self.img)
        self.max_health = health
        self.spritesheet = Spritesheet(imageName)
        self.imageIndex = 0

    def draw(self, window):
        # draw proper player, not rect
        window.blit(self.spritesheet.get_sprite(self.imageIndex), (self.x, self.y))

    def update(self):
        keys = pygame.key.get_pressed()
        if (keys[pygame.K_a] or keys[pygame.K_LEFT]): 
            self.imageIndex = (self.imageIndex + 1) % 16
            print(self.imageIndex)


class Cat(Animals):
    #  For the type of the cat
    CATS_MAP = {
        1: (BLACK_CAT),
        2: (WHITE_CAT)
    }
    def __init__(self, x, y, number, health=100):
        # Call the animals init method
        super().__init__(x, y, health)        
        self.img = self.CATS_MAP[number]
        self.mask = pygame.mask.from_surface(self.img)
        self.max_health = health

    def draw(self, window):
        # draw proper player, not rect
        window.blit(self.img, (self.x, self.y))


def init_window(): # set up window
    WIN = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption('My Custom Game')
    return WIN

def draw_window(WIN, entities):
    #WIN.fill(WHITE)
    # Instead of white, give a house background
    WIN.blit(GNOME_HOUSE, (0,0))

    for e in entities:
        e.draw(WIN)        

    # # Draw player
    # player.draw(WIN)

    # # Draw cat
    # if cat.img != 0:        
    #     cat.draw(WIN)

    # -------------- TESTING DRAW SPRITESHEET --------------
    # set to wherever trainer we are at
    # WIN.blit(man_trainer[i], (0, HEIGHT - 128))
    # WIN.blit(woman_trainer[i], (128, HEIGHT - 128))  


    # to the drawings work, we need to update the display
    pygame.display.update()

def main_game_loop():

    character_image=""    
    character = 0
    # while character != 1 or character !=2
    character = get_number_of_your_player()

    if character==1:
        character_image="george.png"
    elif character==2:
        character_image="betty.png"

    catN = wanna_cat()
    
    # define variables for the game
    run = True
    FPS = 60
    clock = pygame.time.Clock()
    WIN = init_window()

    entities = []
    player = Player(10,10, character_image)

    entities.append(player)
    # kind of cat
    if catN!=0:
        cat = Cat(50,50, catN)
        entities.append(cat)

    while run:
        clock.tick(FPS)


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            # if event.type == pygame.KEYDOWN:
            #     # update sprite if space is pressed
            #     if event.key == pygame.K_SPACE:
            #         pass
            #         # reassign index value
            #         # then go to draw

        for e in entities:
            e.update()

        draw_window(WIN, entities)

    pygame.quit()


def get_number_of_your_player():
    character = 0
    # the while loop is because I want continue 
    # to ask which player the user want
    while True:
        character = input ('Enter the number of your character (1 or 2): ')
        # check if this input is a number
        if character.isdigit():
            # now, I can convert this into an integer
            character = int(character)
        # if it is not a digit
        else:
            print('Invalid input... Try Again!')
            # the continue imediatelly brings 
            # the code back to the while loop
            continue

        # now if the input is a digit, we need to 
        # check if it is 1 or 2
        if 1 <= character <= 2:
            # if it is 1 or 2, return which one it is
            return character
        # if it is not 1 or 2
        else:
            print('The number is not either 1 or 2... Try again!')
            # now, I don't need the continue, because by default it goes there

def wanna_cat():
    cat = 0
    cat = input("Would you like a cat? Type 'y' for Yes or 'n' for No. ")
    # check if yes or no
    if cat.lower() == 'y' or cat.lower() == 'yes':
        while True:          
            cat = input('Which color will be your cat (1 or 2)? ')
            # check if the input is a number
            if cat.isdigit():
                # now, I can convert this number into an integer
                cat = int(cat)
            # if it is not a digit
            else:
                print('Invalid input... Try again!')
                # continue will bring the code to the beginnin of the while loop
                continue

            # check if the digit is 1 or 2
            if 1 <= cat <= 2:
                return cat
            # if it is not 1 or 2
            else:
                print('The number is not either 1 or 2... Try again!')
    elif cat.lower() == 'n' or cat.lower() == 'no':
        cat = 0
        return cat
    # if the input is neither y or n
    else:
        print('You should say if you want a cat or not. Try again')
        

if __name__ == '__main__':
    main_game_loop()
        
