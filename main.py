from game import Game
import pygame
import numpy as np
import matplotlib.pyplot as plt

pygame.init()

done = False
play = False
board_size_x = 100
board_size_y = 60
graphics_multiplyer = 15
screen_width  = board_size_x * graphics_multiplyer
screen_height = board_size_y * graphics_multiplyer
fps = 30
clock = pygame.time.Clock()

screen = pygame.display.set_mode([screen_width, screen_height])
pygame.display.set_caption("Game Of Life")

g = Game(board_size_x, board_size_y, [], screen, graphics_multiplyer)

frame_counter = 0
while not done:
    screen.fill((0,0,0))
    g.print_board()

    # event handeling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                done = True
            if event.key == pygame.K_r:
                g.reset()
                play = False
            if event.key == pygame.K_a:
                g.random()
                play = False
            if event.key == pygame.K_s:
                if play:
                    play = False
                else:
                    g.calculate_population()
                    play = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if play == False:
                pos = pygame.mouse.get_pos()
                g.change(pos)
            

    if play and frame_counter % 3 == 0:
        g.step()
    
    frame_counter += 1
    pygame.display.flip()
    clock.tick(fps)

pygame.quit()


x = g.population
y = [n for n in range(len(x))]

plt.bar(y, x, width=1)
plt.legend()
plt.xlabel('time')
plt.ylabel('population')
plt.title("Population per time")
plt.show()
