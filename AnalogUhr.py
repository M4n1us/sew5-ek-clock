import math
import os

import pygame as pygame
import datetime

from Strategy import Uhr


class AnalogUhr(Uhr):
    """
    Pygame rendering for an analog clock containing hour, minute and second hands
    """
    def __init__(self):
        """
        Sets up the main Window and the background image
        """
        super().__init__()
        self.continuous_zeiger = None
        self.screen = pygame.display.set_mode((640, 640), pygame.HWSURFACE | pygame.DOUBLEBUF)
        self.background = pygame.Surface(self.screen.get_size())
        self.background = self.background.convert()
        self.image, self.rect = load_png('background.jpg')
        self.image = pygame.transform.scale(self.image, (640, 640))
        self.screen.blit(self.image, (0, 0))
        pygame.display.flip()

    def draw_second(self, time):
        """
        Draws the second hand of the clock
        :param time: time for calculating the angle
        :return: none
        """
        angle_sec = calc_second_angle(time, self.continuous_zeiger)
        point = rotate_point((320, 320), (320, 20), angle_sec)
        pygame.draw.line(self.screen, (250, 0, 0), (320, 320), point, width=3)

    def draw_minute(self, time):
        """
        Draws the minute hand of the clock
        :param time: time for calculating the angle
        :return: none
        """
        angle_minute = calc_minute_angle(time)
        point = rotate_point((320, 320), (320, 40), angle_minute)
        pygame.draw.line(self.screen, (0, 250, 0), (320, 320), point, width=6)

    def draw_hour(self, time):
        """
        Draws the hour hand of the clock
        :param time: time for calculating the angle
        :return: none
        """
        angle_hour = calc_hour_angle(time)
        point = rotate_point((320, 320), (320, 120), angle_hour)
        pygame.draw.line(self.screen, (0, 250, 0), (320, 320), point, width=10)

    def render(self, params=None):
        """
        Renders the hands on the background image
        :param params: Continuous flag needs to be set as true or false, affects rendering of second hand
        :return: none
        """
        if params is None:
            self.continuous_zeiger = True
        else:
            self.continuous_zeiger = params["continuous"]

        time = datetime.datetime.now()
        self.image = pygame.transform.scale(self.image, (640, 640))
        self.screen.blit(self.image, (0, 0))
        self.draw_second(time)
        self.draw_minute(time)
        self.draw_hour(time)
        pygame.draw.circle(self.image, (0, 250, 0), (320,320), 20, width=0)
        pygame.display.flip()

def calc_hour_angle(time):
    """
    Calculates the radians rotation of the hour hand based on the time handed to the function
    :param time: datetime.datetime on which the radian will be calculated
    :return: angle for hour hand in radians
    """
    hour = time.hour
    minute = time.minute
    second = time.second
    seconds = (hour * 60 * 60) + (minute * 60) + second
    percentage = seconds / (12*60*60)
    return 2*math.pi * percentage

def calc_minute_angle(time):
    """
    Calculates the radians rotation of the minute hand based on the time handed to the function
    :param time: datetime.datetime on which the radian will be calculated
    :return: angle for minute hand in radians
    """
    minute = time.minute
    second = time.second
    seconds = (minute * 60) + second
    percentage = seconds / (60*60)
    return 2*math.pi * percentage

def calc_second_angle(time, continuous=True):
    """
    Calculates the radians rotation of the minute hand based on the time handed to the function
    :param time: datetime.datetime on which the radian will be calculated
    :param continuous: boolean flag setting if angle should include microseconds or ignore smaller measurements
    :return: angle for minute hand in radians
    """
    second = time.second
    microsecond = time.microsecond
    percentage = None
    if continuous:
        percentage = (second + microsecond/1000000) / 60
    else:
        percentage = second / 60
    return 2*math.pi * percentage

def rotate_point(point_axis, point, angle_rad):
    """
    Function to rotate a point around another point given an angle in radius
    :param point_axis:  (x,y) tuple point around which should be rotated
    :param point: (x,y) tuple point to rotate around
    :param angle_rad: angle in radians
    :return: (x,y) tuple point with new coordinates
    """
    sin = math.sin(angle_rad)
    cos = math.cos(angle_rad)
    p1x, p1y = point_axis
    p2x, p2y = point
    p2x -= p1x
    p2y -= p1y
    newx = p2x * cos - p2y * sin
    newy = p2x * sin + p2y * cos
    return newx+p1x, newy + p1y


def load_png(name):
    """
    Load image and return image object
    :param name: name for the file
    :return: image object
    """
    fullname = os.path.join('data', name)
    try:
        image = pygame.image.load(fullname)
        if image.get_alpha is None:
            image = image.convert()
        else:
            image = image.convert_alpha()
    except pygame.error as message:
        print('Cannot load image: %s', str(fullname))
        raise SystemExit(message)
    return image, image.get_rect()