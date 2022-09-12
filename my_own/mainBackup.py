import pygame
import os

# Colors
WHITE = (255,255,255)
RED = (255,0,0)

# Set up window
WIDTH, HEIGTH = 900, 500

# Players variables
RECT_PLAYER_WIDTH, RECT_PLAYER_HEIGTH = 50, 50

# Load imgs
MAN_PLAYER = pygame.image.load(os.path.join('assets', 'george.png'))
WOMAN_PLAYER = pygame.image.load(os.path.join('assets', 'betty.png'))

MAN_LASER = pygame.image.load(os.path.join('assets', 'pixel_laser_blue.png'))
WOMAN_LASER = pygame.image.load(os.path.join('assets', 'pixel_laser_red.png'))

# Cats - takes the same image, see it later
BLACK_CAT = pygame.image.load(os.path.join('assets', 'cats_all_black_and_white.png'))
WHITE_CAT = pygame.image.load(os.path.join('assets', 'cats_all_black_and_white.png'))

class Entity():
    def __init__(self,x,y):
        self.x = x
        self.y = y
        
    def draw(self,window):
        pass

class Animals(Entity): # Players or cats
    # Properties of this player
    def __init__(self, x, y, health=100):
        super().__init__(self,x,y)
        self.health = health
        # allow us to draw the player and the laser, when pick woman or man
        self.img = None
    # Player.draw, taking the window as parameter
    def draw(self, window):
        # First draw a rectangle. where, color, 
        # x/y position, rect (dimension) and fill it = 0
        #pygame.draw.rect(window, RED, (self.x, self.y, RECT_PLAYER_WIDTH, RECT_PLAYER_HEIGTH), 0)
        
        # draw proper player, not rect
        window.blit(self.img, (self.x, self.y))

        # draw laser

class Player(Entity):
    # Class variables. For the number of the player and cooldown
    NUMBER_MAP = {
        1: (MAN_PLAYER, MAN_LASER),
        2: (WOMAN_PLAYER, WOMAN_LASER)
    }
    COOLDOWN = 30 # half a second

    def __init__(self, x, y, number, health=100):
        # Call the animals init method
        super().__init__(x, y, health)
        self.img, self.laser_img = self.NUMBER_MAP[number]        
        self.lasers = []
        self.cool_down_counter = 0
        # creating a mask, allow us to do pixel perfect collision
        self.mask = pygame.mask.from_surface(self.img)
        self.max_health = health

class Cat(Animals):
    #  For the type of the cat
    CATS_MAP = {
        0: None,
        1: (BLACK_CAT),
        2: (WHITE_CAT)
    }
    def __init__(self, x, y, number, health=100):
        # Call the animals init method
        super().__init__(x, y, health)        
        self.img = self.CATS_MAP[number]
        self.mask = pygame.mask.from_surface(self.img)
        self.max_health = health

def init_window(): # set up window
    WIN = pygame.display.set_mode((WIDTH, HEIGTH))
    pygame.display.set_caption('My Custom Game')
    return WIN

def draw_window(WIN, player, cat):
    WIN.fill(WHITE)

    # Draw player
    player.draw(WIN)

    # Draw cat
    if cat.img != 0:        
        cat.draw(WIN)


    # to the drawings work, we need to update the display
    pygame.display.update()

def main_game_loop(character_number, cat_number):
    # define variables for the game
    run = True
    WIN = init_window()

    player = Player(10,10, character_number)

    # kind of cat
    cat = Cat(50,50, cat_number)

    while run:
        draw_window(WIN, player, cat)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

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
    cat = input("Would you like a cat? Type 'y' for Yes or 'n' for No.")
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
    character = get_number_of_your_player()
    cat = wanna_cat()
    print(cat)
    main_game_loop(character, cat)
        
