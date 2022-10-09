from email.mime import image
from re import X
from tkinter import Y
import pygame as pg
from pygame.sprite import Sprite, Group

class Barrier(Sprite):
    color = 255, 0, 0
    black = 0, 0, 0

    barrier_image0 = [pg.transform.rotozoom(pg.image.load(f'images/barrier__00.png'), 0, 2.0)]

    def __init__(self, game, rect):
        super().__init__()
        self.screen = game.screen
        self.image = pg.image.load(f'images/barrier__00.png')
        self.rect = self.image.get_rect()
        self.rect.y = self.rect.height
        self.x = float(self.rect.x)
        self.settings = game.settings
        self.width = self.rect.width
        

        # self.settings = game.settings
        # self.image = pg.image.load('images/alien0.bmp')
        # self.rect = self.image.get_rect()
        # self.rect.y = self.rect.height
        # self.x = float(self.rect.x)
        
    def hit(self): 
        pass
        #self.kill()
    def update(self):
         self.draw()
    def draw(self): 
       self.screen.blit(self.image, self.rect)

class Barriers:

    def __init__(self, game):
        self.game = game
        self.image = pg.image.load(f'images/barrier__00.png')
        self.settings = game.settings
        self.aliens_lasers = game.alien_lasers
        self.ship_lasers = game.ship_lasers

        self.shape = [
        'xxxx'
        'xxxx'    
        ]

        self.barriers = pg.sprite.Group()
        self.create_barriers(self.barriers)

    def create_barriers(self, barriers): 
        
        barrier = Barrier(game = self.game, rect = self.image.get_rect())
        #self.barriers = Group()
        
        # for row_index, row in enumerate(self.shape):
        #     for col_index, col in enumerate(row):
        #         if col =='x':
        #             barrier.rect.x=col_index * barrier.width
        #             barrier.rect.y=row_index * barrier.width
        #             self.barriers.add(barrier)



        #top = self.settings.screen_height - 2.1 * height
        #rects = [pg.Rect(x * 2 * width + 1.5 * width, top, width, height) for x in range(4)]   # SP w  3w  5w  7w  SP

        for i in range(6):
            barrier = Barrier(game = self.game, rect = self.image.get_rect())
            if i <4:
                barrier.rect.x = 1000+ i*barrier.rect.width
                barrier.rect.y = 700+barrier.rect.height
            else:
                barrier.rect.x = 1000+ (i-3)*barrier.rect.width
                barrier.rect.y = 700

            self.barriers.add(barrier)

        for i in range(6):
            barrier = Barrier(game = self.game, rect = self.image.get_rect())
            if i <4:
                barrier.rect.x = 800+ i*barrier.rect.width
                barrier.rect.y = 700+barrier.rect.height
            else:
                barrier.rect.x = 800+ (i-3)*barrier.rect.width
                barrier.rect.y = 700

            self.barriers.add(barrier)

        for i in range(6):
            barrier = Barrier(game = self.game, rect = self.image.get_rect())
            if i <4:
                barrier.rect.x = 600+ i*barrier.rect.width
                barrier.rect.y = 700+barrier.rect.height
            else:
                barrier.rect.x = 600+ (i-3)*barrier.rect.width
                barrier.rect.y = 700

            self.barriers.add(barrier)

        for i in range(6):
            barrier = Barrier(game = self.game, rect = self.image.get_rect())
            if i <4:
                barrier.rect.x = 400+ i*barrier.rect.width
                barrier.rect.y = 700+barrier.rect.height
            else:
                barrier.rect.x = 400+ (i-3)*barrier.rect.width
                barrier.rect.y = 700

            self.barriers.add(barrier)

        for i in range(6):
            barrier = Barrier(game = self.game, rect = self.image.get_rect())
            if i <4:
                barrier.rect.x = 200+ i*barrier.rect.width
                barrier.rect.y = 700+barrier.rect.height
            else:
                barrier.rect.x = 200+ (i-3)*barrier.rect.width
                barrier.rect.y = 700

            self.barriers.add(barrier)

    def check_collisions(self):
        collisions = pg.sprite.groupcollide(self.barriers, self.aliens_lasers.lasers, True, True)
        if collisions:
            for barrier in collisions:
                barrier.hit()

        collisions = pg.sprite.groupcollide(self.ship_lasers.lasers,self.barriers, True, True)
        if collisions:
            for barrier in collisions:
                barrier.hit()

        # collisions = pg.sprite.spritecollide(self.barriers, self.ship_lasers, True)
        # if collisions:
        #     for barrier in collisions:
        #         barrier.hit()

    def hit(self):
        print("Barrier hit")
        self.kill()

    def reset(self):
        self.barriers.empty()
        self.create_barriers(self.barriers)
        
        

    def update(self):
        for barrier in self.barriers: 
            barrier.update()
            self.check_collisions()
            

    def draw(self):
         for barrier in self.barriers: barrier.draw()

