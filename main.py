from game import Game
import pygame
import matplotlib.pyplot as plt

pygame.init()

######## SETTINGS ########
board_size_x = 100
board_size_y = 60
graphics_multiplyer = 10
fps = 30
infinite = True

screen_width  = board_size_x * graphics_multiplyer
screen_height = board_size_y * graphics_multiplyer
clock = pygame.time.Clock()
done = False
play = False
debug_mode = False

screen = pygame.display.set_mode([screen_width, screen_height])
pygame.display.set_caption("Game Of Life")

g = Game(board_size_x, board_size_y, [], screen, graphics_multiplyer, infinite)

frame_counter = 0
while not done:
    screen.fill((0,0,0))
    g.print_board()
    pos = pygame.mouse.get_pos()
    if debug_mode:
        g.showNeighbours(pos)

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
            if event.key == pygame.K_d:
                debug_mode = not debug_mode
            if event.key == pygame.K_1:
                fps = 10
            if event.key == pygame.K_2:
                fps = 20
            if event.key == pygame.K_3:
                fps = 30
            if event.key == pygame.K_4:
                fps = 40
            if event.key == pygame.K_5:
                fps = 50
            if event.key == pygame.K_i:
                infinite = not infinite
                g.infinite = infinite
                g.reset()
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
