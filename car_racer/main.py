import sys
import pygame
from utils import scale_image, blit_text_center
from car import PlayerCar, AiCar
from game_info import GameInfo
pygame.font.init()
pygame.mixer.init()

class CarRacer:
    """class to set up game"""
    def __init__(self):
        pygame.init()
        # load track images into variables and scale to size
        self.grass = scale_image(pygame.image.load("car_racer/imgs/grass.jpg"), 2.5)
        self.track = scale_image(pygame.image.load("car_racer/imgs/track.png"), 0.9)
        self.track_border = scale_image(pygame.image.load("car_racer/imgs/track-border.png"), 0.9)
        self.track_border_mask = pygame.mask.from_surface(self.track_border)
        self.finish_line = pygame.image.load("car_racer/imgs/finish.png")
        self.finish_mask = pygame.mask.from_surface(self.finish_line)
        self.finish_position = (130, 250)
        # sound set up
        pygame.mixer.music.load('car_racer/sound/RacingSounds.wav')
        self.lose = pygame.mixer.Sound('car_racer/sound/lose.wav')
        self.win = pygame.mixer.Sound('car_racer/sound/winner.wav')

        # set up window size based on track dimensions
        self.width, self.height = self.track.get_width(), self.track.get_height()
        self.window = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Car Racer    --Controls: W-forward | A-left | S-back | D-right | Q to quit   Beat all 10 Levels!")
        self.FPS = 35
        self.run = True
        self.ai_car_path = [(173, 91), (99, 65), (51, 125), (66, 477), (286, 713), (395, 710), (414, 515), 
                            (505, 471), (596, 534), (607, 709), (696, 740), (740, 651), (742, 439), (713, 357), 
                            (617, 367), (445, 360), (391, 299), (481, 260), (682, 260), (739, 174), (677, 73), 
                            (505, 73), (353, 74), (275, 128), (281, 265), (274, 402), (164, 391), (173, 254)]
        self.timer = pygame.time.Clock()    
        self.images = [(self.grass, (0,0)), (self.track, (0,0)), (self.finish_line, (self.finish_position)), (self.track_border, (0,0))]
        self.player_car = PlayerCar(4, 4)
        self.ai_car = AiCar(2, 4, self.ai_car_path)
        self.main_font = pygame.font.SysFont('cambriacambriamath', 48)
        
    def draw(self, game_info):
        """add level info to the screen"""

        for img, pos, in self.images:
            self.window.blit(img, pos)
        
        level_text = self.main_font.render(
            f'Level {game_info.level}', 1, (255, 255, 255))
        self.window.blit(level_text, (5, self.height - level_text.get_height() - 70))

        time_text = self.main_font.render(
            f'Time: {game_info.get_level_time()}s', 1, (255, 255, 255))
        self.window.blit(time_text, (5, self.height - time_text.get_height() - 40))

        velocity_text = self.main_font.render(
            f'Speed: {round(self.player_car.velocity, 1) * 20} MPH', 1, (255, 255, 255))
        self.window.blit(velocity_text, (5, self.height - velocity_text.get_height() - 10))

        self.player_car.draw(self.window)
        self.ai_car.draw(self.window)
        pygame.display.update()

    def check_events(self):
        '''Check events for movement and quit'''
        keys = pygame.key.get_pressed()
        moved = False

        if keys[pygame.K_a]:
            self.player_car.rotate(left=True)
        if keys[pygame.K_d]:
            self.player_car.rotate(right=True)
        if keys[pygame.K_w]:
            moved = True
            self.player_car.move_forward()
        if keys[pygame.K_s]:
            moved = True
            self.player_car.move_backward()
        if keys[pygame.K_q]:
            sys.exit()
        if not moved:
            self.player_car.reduce_speed()

    def collision_detection(self, game_info):
        '''collision detection for track mask and finish line'''
        if self.player_car.collide(self.track_border_mask) != None:
            self.player_car.bounce()
        
        ai_finish_collision_point = self.ai_car.collide(self.finish_mask, *self.finish_position)

        if ai_finish_collision_point != None:
            blit_text_center(self.window, self.main_font, "You Lost!")
            pygame.mixer.music.stop()
            pygame.mixer.Sound.play(self.lose)
            pygame.display.update()
            pygame.time.wait(5000)
            game_info.reset()
            self.player_car.reset()
            self.ai_car.next_level(game_info.level)

        player_finish_collision_point = self.player_car.collide(self.finish_mask, *self.finish_position)
        
        if player_finish_collision_point != None:
            if player_finish_collision_point[1] == 0:
                self.player_car.bounce()
            else:
                pygame.mixer.music.stop()
                pygame.mixer.Sound.play(self.win)
                game_info.next_level()
                self.player_car.reset()
                self.ai_car.next_level(game_info.level)

    def run_game(self):
        '''run game function'''
        game_info = GameInfo()
        while self.run:
            
            self.timer.tick(self.FPS)
            CarRacer.draw(self, game_info)

            while not game_info.started:
                blit_text_center(self.window, self.main_font, f'Press any key to start level {game_info.level}!')
                pygame.display.update()

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        break
                    if event.type == pygame.KEYDOWN:
                        game_info.start_level()
                        pygame.mixer.music.play(-1)


            for event in pygame.event.get():
                
                if event.type == pygame.QUIT:
                    self.run = False
                    # to store ai_path array
                    # print(self.ai_car.path)
                    pygame.quit()

                """Logic to store ai_car path array"""
                # if event.type == pygame.MOUSEBUTTONDOWN:
                #     pos = pygame.mouse.get_pos()
                #     self.ai_car.path.append(pos)
            self.ai_car.move()
            self.check_events()
            self.collision_detection(game_info)
            
            if game_info.game_finished():
                blit_text_center(self.window, self.main_font, "You Won The Game!")
                pygame.display.update()
                pygame.time.wait(5000)
                game_info.reset()
                self.player_car.reset()
                self.ai_car.reset()

if __name__ == '__main__':
    ai = CarRacer()
    ai.run_game()