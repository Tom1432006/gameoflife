import pygame
from random import randint

class Game:
    field = []

    field_width = 5
    field_height = 5
    checked_fields = []
    screen = None
    graphics_multiplyer = 10
    infinite = True

    population = []
    def __init__(self, field_width, field_height, checked_fields, screen, graphics_multiplyer, infinite):
        self.field_width = field_width
        self.field_height = field_height
        self.checked_fields = checked_fields
        self.screen = screen
        self.graphics_multiplyer = graphics_multiplyer
        self.infinite = infinite
        self.construct_field()

    def construct_field(self):
        for n in range(self.field_width*self.field_height):
            if n in self.checked_fields:
                self.field.append(1)
            else:
                self.field.append(0)
    
    def step(self):
        old_board = list(self.field)

        for x in range(len(self.field)):
            neighbours = self.check_neighbours(x, old_board)

            if old_board[x] == 1:
                if neighbours < 2 or neighbours > 3:
                    self.field[x] = 0
            else:
                if neighbours == 3:
                    self.field[x] = 1
        
        self.calculate_population()
    
    def check_neighbours(self, x, board):
        neighbours = 0

        directions = [
            x-self.field_width-1,
            x-self.field_width,
            x-self.field_width+1,
            x-1, x+1,
            x+self.field_width-1,
            x+self.field_width,
            x+self.field_width+1
        ]

        for n in directions:
            # sides
            if x % self.field_width == self.field_width-1 and n % self.field_width == 0: 
                if not self.infinite: continue
                n -= self.field_width
            elif x % self.field_width == 0 and n % self.field_width == self.field_width-1: 
                if not self.infinite: continue
                n += self.field_width

            # bottom and top
            if int(x / self.field_width) == 0 and n < 0:
                if not self.infinite: continue
                n += self.field_width * self.field_height
            elif int(x / self.field_width) == self.field_height-1 and n > (self.field_width * self.field_height)-1:
                if not self.infinite: continue
                n -= self.field_width * self.field_height

            neighbours += board[n%(self.field_width*self.field_height)]
        
        return neighbours
    
    def showNeighbours(self, pos):
        # get index
        x = pos[0]
        x = int(x/self.graphics_multiplyer)

        y = pos[1]
        y = int(y/self.graphics_multiplyer)

        x = self.field_width * y + x

        directions = [
            x-self.field_width-1,
            x-self.field_width,
            x-self.field_width+1,
            x-1, x+1,
            x+self.field_width-1,
            x+self.field_width,
            x+self.field_width+1
        ]

        for n in directions:
            # sides
            if x % self.field_width == self.field_width-1 and n % self.field_width == 0: 
                if not self.infinite: continue
                n -= self.field_width
            elif x % self.field_width == 0 and n % self.field_width == self.field_width-1: 
                if not self.infinite: continue
                n += self.field_width

            # top and bottom
            if int(x / self.field_width) == 0 and n < 0:
                if not self.infinite: continue
                n += self.field_width * self.field_height
            elif int(x / self.field_width) == self.field_height-1 and n > (self.field_width * self.field_height)-1:
                if not self.infinite: continue
                n -= self.field_width * self.field_height

            left = n % self.field_width
            top = int(n / self.field_width)
            rect = pygame.Rect(left*self.graphics_multiplyer, top*self.graphics_multiplyer, self.graphics_multiplyer, self.graphics_multiplyer)
            pygame.draw.rect(self.screen, (255,0,0), rect, 1)
        
    def print_board(self):
        for n in range(len(self.field)):
            rect = pygame.Rect((n%self.field_width)*self.graphics_multiplyer, int(n/self.field_width)*self.graphics_multiplyer, self.graphics_multiplyer, self.graphics_multiplyer)
            if self.field[n] == 1:
                pygame.draw.rect(self.screen, (255,255,255), rect, 0)
            # else: 
            #     pygame.draw.rect(self.screen, (255,255,255), rect, 1)

    def change(self, pos):
        # get index
        x = pos[0]
        x = int(x/self.graphics_multiplyer)

        y = pos[1]
        y = int(y/self.graphics_multiplyer)

        num = self.field_width * y + x
        
        if self.field[num] == 1:
            self.field[num] = 0
        else:
            self.field[num] = 1

    def reset(self):
        for n in range(self.field_width*self.field_height):
            if n in self.checked_fields:
                self.field[n] = 1
            else:
                self.field[n] = 0
    
    def random(self):
        for n in range(self.field_width*self.field_height):
            self.field[n] = randint(0, 1) % 2 

    def calculate_population(self):
        population = 0
        for n in self.field:
            population += n
        
        self.population.append(population)
