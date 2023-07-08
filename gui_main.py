import pygame
from sys import exit

from constantes import *
from animaciones import *

from Player import Player
from Level import Level
from menu import MainMenu, LevelsMenu, PauseMenu

pygame.init()

# Configuración screen
screen = pygame.display.set_mode((WIDTH_PANTALLA, HEIGHT_PANTALLA))
clock = pygame.time.Clock()
pygame.display.set_caption('Alice in Worderland')
icono = pygame.image.load('./images/alice/idle/rigth.png').convert_alpha()
pygame.display.set_icon(icono)

def play(level_play="level_1"):
    player = Player()

    list_level = []

    level = Level(player, level_play)
    list_level.append(level.level)
    running_game = True
    game_over = False
    is_paused = False
    return_to_play = False

    while running_game:

        if is_paused:
            pygame.display.update()
            continue

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running_game = False
                exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    player.saltar()
                if event.key == pygame.K_ESCAPE:
                    is_paused = True
                    return_to_play = pause_menu(level_play)

        player.eventos(level.bubbles_group)
        if level_play == "level_2":
            player.transition_dark = True
        elif level_play == "level_3":
            player.dark = True

        if not game_over:
            if player.muerto or level.time_restante == 0:
                game_over = True

            level.draw(screen)
            level.update(screen)

            if level.next_level == "level_2":
                level_play = "level_2"
                level = Level(player, level_play)
                list_level.append(level.level)
            elif level.next_level == "level_3":
                level_play = "level_3"
                level = Level(player, level_play)
                list_level.append(level.level)

        else:
            ambient_suspence.stop()
            game_over_sound.play()
            screen.blit(game_over_image, (0, 0))

        pygame.display.update()
        clock.tick(FPS)

        if return_to_play:
            is_paused = False
            return_to_play = False

def main_menu():
    alice_intro.play()

    while True:
      main_menu = MainMenu()
      ejecutar =  main_menu.update()
      main_menu.draw(screen)
      if ejecutar == "play":
        alice_intro.stop()
        play()
      elif ejecutar == "levels_menu":
        levels_menu()
      pygame.display.update()

def levels_menu():
    alice_intro.stop()
    click_magic.play()

    while True:
      levels_menu = LevelsMenu()
      ejecutar = levels_menu.update()
      levels_menu.draw(screen)
      if ejecutar == "play_1":
        play("level_1")
      elif ejecutar == "play_2":
        play("level_2")
      elif ejecutar == "play_3":
        play("level_3")
      pygame.display.update()

def pause_menu(level_play):
  alice_intro.stop()
  click_magic.play()

  while True:
    pause_menu = PauseMenu()
    ejecutar = pause_menu.update()
    pause_menu.draw(screen)
    if ejecutar == "continue":
      return True
    elif ejecutar == "restart":
      play(level_play)
    elif ejecutar == "main_menu":
      main_menu()
    pygame.display.update()

main_menu()
