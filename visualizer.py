
import sys
from collections import deque

import pygame

size = (width, height) = 640, 480
pygame.init()

window = pygame.display.set_mode(size)
pygame.display.set_caption('BFS')
clock = pygame.time.Clock()

cols, rows = 64, 48

w = width//cols
h = height//rows

grid = []
queue = deque()
visited = []
path = []


class Grid:
    def __init__(self, i, j):
        self.x, self.y = i, j
        self.f, self.g, self.h = 0, 0, 0
        self.neighbors = []

        self.visited = False
        self.prev = None
        self.wall = False

    def show(self, window, col):
        if self.wall == True:
            col = (0, 0, 0)
        pygame.draw.rect(window, col, (self.x*w, self.y*h, w-1, h-1))

    def add_neighbors(self, grid):
        if self.x < cols - 1:
            self.neighbors.append(grid[self.x+1][self.y])
        if self.x > 0:
            self.neighbors.append(grid[self.x-1][self.y])
        if self.y < rows - 1:
            self.neighbors.append(grid[self.x][self.y+1])
        if self.y > 0:
            self.neighbors.append(grid[self.x][self.y-1])


def place(pos):
    i = pos[0] // w
    j = pos[1] // h
    return w, h


for i in range(cols):
    arr = []
    for j in range(rows):
        arr.append(Grid(i, j))
    grid.append(arr)

for i in range(cols):
    for j in range(rows):
        grid[i][j].add_neighbors(grid)


start = grid[cols//2][rows//2]
end = grid[cols-1][rows - cols//2]
start.wall = False
end.wall = False

queue.append(start)
start.visited = True


def main():
    flag = False
    noflag = True
    start = False
    # if startflag:
    # queue.popleft()
    # while queue
    # grid[rows+1][cols+1]

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.K_RETURN:
                # if event.key == pygame.K_RETURN:
                start = True

        window.fill((0, 20, 20))
        for i in range(cols):
            for j in range(rows):
                index = grid[i][j]
                index.show(window, (255, 255, 255))
                if index in path:
                    index.show(window, (25, 120, 250))
                elif index.visited:
                    index.show(window, (255, 0, 0))
                if index in queue:
                    index.show(window, (0, 255, 0))
                if index == end:
                    index.show(window, (0, 120, 255))

        pygame.display.flip()


main()
