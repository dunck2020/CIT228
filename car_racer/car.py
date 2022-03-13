import math
import pygame
from utils import scale_image, blit_rotate_center

red_car = scale_image(pygame.image.load("car_racer/imgs/red-car.png"), 0.55)
purple_car = scale_image(pygame.image.load("car_racer/imgs/purple-car.png"), 0.55)


class AbstractCar:
    '''base car class'''
    def __init__ (self, max_velocity, rotation_velocity):
        self.car_image = self.car_img
        self.max_velocity = max_velocity
        self.velocity = 0
        self.rotation_velocity = rotation_velocity
        self.angle = 0
        self.x, self.y = self.start_position
        self.acceleration = 0.1

    def rotate(self, left=False, right=False):
        '''function to rotate car left and right'''
        if left:
            self.angle += self.rotation_velocity
        elif right:
            self.angle -= self.rotation_velocity
    
    def draw(self, window):
        '''function to draw the cars'''
        blit_rotate_center(window, self.car_image, (self.x, self.y), self.angle)
    
    def move_forward(self):
        '''function to move the car forward'''
        self.velocity = min(self.velocity + self.acceleration, self.max_velocity)
        self.move()

    def move_backward(self):
        '''backwards movement'''
        self.velocity = max(self.velocity - self.acceleration, -self.max_velocity/2)
        self.move()

    def move(self):
        '''movement to maintain speed at an angle'''
        radians = math.radians(self.angle)
        vertical = math.cos(radians) * self.velocity
        horizontal = math.sin(radians) * self.velocity
        self.y -= vertical
        self.x -= horizontal

    def reduce_speed(self):
        '''method for deceleration'''
        self.velocity = max(self.velocity - self.acceleration / 2, 0)
        self.move()

    def collide(self, mask, x=0, y=0):
        '''collision location for car'''
        car_mask = pygame.mask.from_surface(self.car_image)
        offset = (int(self.x - x), int(self.y - y))
        collision_point = mask.overlap(car_mask, offset)
        return collision_point

    def bounce(self):
        '''velocity change when car hits a wall'''
        self.velocity = -self.velocity /2

    def reset(self):
        '''resets cars to original position'''
        self.x, self.y = self.start_position
        self.angle = 0
        self.velocity = 0

class PlayerCar(AbstractCar):
    """Player car class inherits from Abstract Car class"""
    car_img = red_car
    start_position = (180, 200)

class AiCar(AbstractCar):
    '''Computer controlled car'''
    car_img = purple_car
    start_position = (150, 200)

    def __init__ (self, max_velocity, rotation_velocity, path=[]):
        super().__init__(max_velocity, rotation_velocity)
        self.path = path
        self.current_location = 0
        self.velocity = max_velocity

    def next_level(self, level):
        '''ai car increases speed every level'''
        self.reset()
        self.velocity = self.max_velocity + (level - 1) * 0.2
        self.current_location = 0

    def draw_points(self, window):
        '''function to draw point on map for ai car direction array position'''
        for point in self.path:
            pygame.draw.circle(window, (255,0,0), point, 5)

    def draw(self, window):
        super().draw(window)
        # draw points to define ai_car path
        # self.draw_points(window)

    def calculate_angle(self):
        '''determine angles at which ai car will drive towards points on path'''
        target_x, target_y = self.path[self.current_location]
        x_gap = target_x - self.x
        y_gap = target_y - self.y

        if y_gap == 0:
            radian_angle = math.pi / 2
        else:
            radian_angle = math.atan(x_gap / y_gap)

        if target_y > self.y:
            radian_angle += math.pi
        
        diff_in_angle = self.angle - math.degrees(radian_angle)
        if diff_in_angle >= 180:
            diff_in_angle -= 360
        
        if diff_in_angle > 0:
            self.angle -= min(self.rotation_velocity, abs(diff_in_angle))
        else:
            self.angle += min(self.rotation_velocity, abs(diff_in_angle))

    def update_path_point(self):
        target = self.path[self.current_location]
        rect = pygame.Rect(self.x, self.y, self.car_img.get_width(), self.car_img.get_height())
        if rect.collidepoint(*target):
            self.current_location += 1

    def move(self):
        if self.current_location >= len(self.path):
            return
        self.calculate_angle()
        self.update_path_point()
        super().move()




