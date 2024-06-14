'''
Yousef Sprint 1:
# Define a Player class
    # Initialize with game settings, position (x, y)
    # Define player properties (e.g., speed, health, etc.)
    # Implement an update method
        # Update player logic based on key presses (e.g., move left, right, jump)
    # Implement a draw method
        # Draw the player on the screen
'''
import pygame as pg
import os

class Player(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.images = self.load_images()
        self.direction = 'R'
        self.image = self.images['R1']
        self.rect = self.image.get_rect(center = (640,360))
        self.speed = 3
        self.animation_index = 0

    def load_images(self):
        images = {}
        dir_path = 'assets/images/player/'

        # Load images for all positions
        directions = ['R', 'L', 'U', 'D']
        for direction in directions:
            direction_images = {}
            # Load the 3 images for each direction (for walking animation)
            for i in range(1,4):
                image_path = os.path.join(dir_path, f"{direction}/{direction}{i}.png")
                image = pg.image.load(image_path).convert_alpha()
                image_resized = pg.transform.scale(image, (32,43)) 
                direction_images[f'{direction}{i}'] = image_resized
            images.update(direction_images)
        return images
    
    def player_input(self):
        keys = pg.key.get_pressed()
        if keys[pg.K_RIGHT]:
            self.rect.x += self.speed
            self.direction = 'R'
            self.animate_movement()
        elif keys[pg.K_LEFT]:
            self.rect.x -= self.speed
            self.direction = 'L'
            self.animate_movement()
        elif keys[pg.K_UP]:
            self.rect.y -= self.speed
            self.direction = 'U'
            self.animate_movement()
        elif keys[pg.K_DOWN]:
            self.rect.y += self.speed
            self.direction = 'D'
            self.animate_movement()
        
    def animate_movement(self):
        # Update animation frame based off index
        self.animation_index += 0.2
        if self.animation_index >= 3:
            self.animation_index = 0
        self.image = self.images[f'{self.direction}{int(self.animation_index) + 1}']
    
    def update(self):
        self.player_input()
    