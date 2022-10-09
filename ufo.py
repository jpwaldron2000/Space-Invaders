# from ast import Or
# from email.headerregistry import HeaderRegistry
# from random import randint
# from secrets import choice
# import pygame as pg
# from pygame.sprite import Sprite, Group
# from laser import Lasers
# from timer import Timer

# class Ufo(Sprite):
#     def __init__(self, game):
#         super().__init__()
#         self.game = game
#         self.screen = game.screen
#         self.side = ''
#         self.screen_width =1200

#         self.image = pg.image.load(f'images/ufo_0.png')
#         self.rect = self.image.get_rect()       
#         self.rect.y = 20
#         self.rect.x = -50

#         self.ship_lasers = game.ship_lasers.lasers


#         self.ufo = pg.sprite.GroupSingle()
#         self.ufo_spawn_time = randint(400,800)
#         self.speed = -3

        

#     def hit(self):
#         self.kill()
#         self.sb.increment_score_ufo()

#     def create_ufo(self, game):
#         sides = ['left','right']
#         c = choice(sides)
#         x = 0
#         if c== 'right':
#             x=self.screen_width + 50
#             speed = -3
#         else:
#             x=-50
#             speed = 3

#             newUfo = Ufo(game)
#             newUfo.speed = speed
#             newUfo.rect.x = x

#             self.ufo.add(newUfo)
#             print('ufo made')

        

#        # game = self.game
#         # newUfo = Ufo(game)
#         # choices = ['left', 'right']
#         # newUfo.side = choice(choices)
#         # if newUfo.side =='right':
#         #     newUfo.rect.x= self.screen_width + 50
#         #     newUfo.speed=-3
#         # else: 
#         #     newUfo.rect.x=-50
#         #     newUfo.speed=3    

#         # newUfo.rect.y = 20
#         # self.ufo.add(newUfo)
#         # print('ufo created')
        
#     def reset(self):
#         self.ufo.remove
#         self.create_ufo(game=self.game)

#     def check_collisions(self):
#         collisions = pg.sprite.groupcollide(self.ufo, self.ship_lasers, False, True)
#         if(collisions):
#             self.ufo.hit

#     def update(self):
#         self.rect.x +=self.speed
#         self.check_collisions()
#         self.ufo_spawn_time -=1
#         if self.ufo_spawn_time <= 0:
#             self.create_ufo(game = self.game)
#             self.ufo_spawn_time = randint(40,80)
    
#         self.draw()

#     def draw(self):
        
#         # rect.x, rect.y = self.rect.x, self.rect.y
#         self.screen.blit(self.image, self.rect)