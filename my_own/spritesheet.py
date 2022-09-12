import pygame
import os
import json

# Colors
WHITE = (255,255,255)
RED = (255,0,0)
BLACK = (0,0,0)

class Spritesheet:

    # this function should match with the metadata json
    def get_frame(self, x, y, w, h):
        # create an empty surface. With the same w and h of the sprite img
        sprite = pygame.Surface((w, h))
        # handle transparency (use this or mask?) we will use black
        sprite.set_colorkey(BLACK)
        # cut out the sprite (Taking the empty surface and place the img into it)
        # The img will br the sprite_sheet. The second arg is where. 
        # And the third is the dimensions of the img
        sprite.blit(self.sprite_sheet, (0, 0), (x, y, w, h))
        # return that img back
        return sprite
    
    # metadata json
    def parse_sprite(self):
        # in sprite we wanna store the "frame" info coordinates
        # self.data contains all of the dictionaries
        # the [name] is for example "-0"
        for frameName, frame in self.data['frames'].items():
            print(frameName)
            x, y, w, h = frame['frame']["x"], frame['frame']["y"], frame['frame']["w"], frame['frame']["h"]
            # the get_frame functions draws since I have the coordinates, so:
            image = self.get_frame(x, y, w, h)
            self.spriteImages.append(image)
        
    def get_sprite(self, index):
        return self.spriteImages[index]

    def get_sprite_count(self):
        return self.spriteImages.len()
    
    def animation(self, key):
        animation_list = []
        if key == 'left':
            animation_list.append([self.spriteImages[1], self.spriteImages[5], self.spriteImages[9], self.spriteImages[13]])
        elif key == 'right':
            animation_list.append([self.spriteImages[3], self.spriteImages[7], self.spriteImages[11], self.spriteImages[15]])
        elif key == 'front':
            animation_list.append([self.spriteImages[0], self.spriteImages[4], self.spriteImages[8], self.spriteImages[12]])
        elif key == 'back':
            animation_list.append([self.spriteImages[2], self.spriteImages[6], self.spriteImages[10], self.spriteImages[14]])

        # animation = {
        #     'left': [spriteImages[1], spriteImages[5], spriteImages[9], spriteImages[13]],
        #     'right': [spriteImages[3], spriteImages[7], spriteImages[11], spriteImages[15]],
        #     'front': [spriteImages[0], spriteImages[4], spriteImages[8], spriteImages[12]],
        #     'back': [spriteImages[2], spriteImages[6], spriteImages[10], spriteImages[14]]
        # }


    def __init__(self, filename):
        self.filename = filename
        #self.img_filename = self.filename + '.png'
        # load a spritesheet. Convert to match up with the window size
        self.sprite_sheet = pygame.image.load(os.path.join('assets', self.filename)).convert()
        # new variable for the metadata json
        self.meta_data = os.path.join('assets', self.filename.replace('png', 'json'))

        self.spriteImages = []

        # open the json file
        with open(self.meta_data) as f:
            # new variable to convert all the json info into a python dictionary
            self.data = json.load(f)
        # close the metadata
        f.close()

        self.parse_sprite()