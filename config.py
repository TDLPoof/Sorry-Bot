import pygame

BG = (95, 169, 199)

SCALE = 32

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600

map_tile_image = {
    "-": pygame.transform.scale(pygame.image.load("sprites/blank.png"), (SCALE, SCALE)),
    "0": pygame.transform.scale(pygame.image.load("sprites/red_ss.png"), (SCALE, SCALE)),
    "1": pygame.transform.scale(pygame.image.load("sprites/red_s.png"), (SCALE, SCALE)),
    "2": pygame.transform.scale(pygame.image.load("sprites/red_se.png"), (SCALE, SCALE)),
    "3": pygame.transform.scale(pygame.image.load("sprites/blue_ss.png"), (SCALE, SCALE)),
    "A": pygame.transform.scale(pygame.image.load("sprites/blue_s.png"), (SCALE, SCALE)),
    "B": pygame.transform.scale(pygame.image.load("sprites/blue_se.png"), (SCALE, SCALE)),
    "C": pygame.transform.scale(pygame.image.load("sprites/green_ss.png"), (SCALE, SCALE)),
    "D": pygame.transform.scale(pygame.image.load("sprites/green_s.png"), (SCALE, SCALE)),
    "Q": pygame.transform.scale(pygame.image.load("sprites/green_se.png"), (SCALE, SCALE)),
    "W": pygame.transform.scale(pygame.image.load("sprites/ylo_ss.png"), (SCALE, SCALE)),
    "E": pygame.transform.scale(pygame.image.load("sprites/ylo_s.png"), (SCALE, SCALE)),
    "R": pygame.transform.scale(pygame.image.load("sprites/ylo_se.png"), (SCALE, SCALE))
}
