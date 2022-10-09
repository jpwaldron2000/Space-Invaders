import pygame as pg
from settings import Settings
import game_functions as gf

from laser import Lasers, LaserType
from alien import Aliens, Alien, Ufo
from ship import Ship
from sound import Sound
from scoreboard import Scoreboard
from barrier import Barriers
import sys
from button import Button


class Game:
    def __init__(self):
        pg.init()
        self.settings = Settings()
        size = self.settings.screen_width, self.settings.screen_height   # tuple
        self.screen = pg.display.set_mode(size=size)
        pg.display.set_caption("Alien Invasion")

        self.sound = Sound(bg_music="sounds/startrek.wav")
        self.scoreboard = Scoreboard(game=self)  

        self.ship_lasers = Lasers(settings=self.settings, type=LaserType.SHIP)
        self.alien_lasers = Lasers(settings=self.settings, type=LaserType.ALIEN)
        
        self.barriers = Barriers(game=self)
        self.ufo = Ufo(game=self, side = 'right')
        self.ship = Ship(game=self)
        self.aliens = Aliens(game=self)
        self.settings.initialize_speed_settings()
        BG = pg.image.load

    def reset(self):
        print('Resetting game...')
        # self.lasers.reset()
        self.barriers.reset()
        self.ship.reset()
        self.aliens.reset()
        # self.scoreboard.reset()

    def game_over(self):
        print('All ships gone: game over!')
        self.sound.gameover()
        pg.quit()
        sys.exit()

    def play(self):
        self.sound.play_bg()
        while True:     # at the moment, only exits in gf.check_events if Ctrl/Cmd-Q pressed

            gf.check_events(settings=self.settings, ship=self.ship)
            self.screen.fill((13,55,13))
            self.ship.update()
            self.aliens.update()
            self.barriers.update()
            self.ufo.update()
            # self.lasers.update()
            self.scoreboard.update()
            pg.display.flip()

    def menu(self):
        pg.display.set_caption("Menu")

        while True:
            self.screen.blit(pg.image.load("images/Menu.png"), (0,0))
            menu_mouse_pos = pg.mouse.get_pos()

            file = open('highscore.txt','r')
            score = file.read()
            strin= ("High Score: ")
            bstrin = strin+score
            file.close()
             
            
            text = pg.font.Font(f'images/font.ttf', 50).render(bstrin,True,'White')
            text_rec = text.get_rect(center = (250,50))
            self.screen.blit(text, text_rec)
            
            PLAY_BUTTON = Button(image=None, pos=(600,700),text_input = "Play", font=pg.font.Font(f'images/font.ttf', 75), base_color="#d7fcd4", hovering_color="White")

            for button in [PLAY_BUTTON]:
                button.changeColor(menu_mouse_pos)
                button.update(screen=self.screen)
            
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    sys.exit()
                if event.type ==pg.MOUSEBUTTONDOWN:
                    if PLAY_BUTTON.checkForInput(menu_mouse_pos):
                        g = Game()
                        g.play()
            pg.display.update()


def main():
    g = Game()
    g.menu()


if __name__ == '__main__':
    main()
