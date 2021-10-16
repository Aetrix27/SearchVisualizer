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

# Initializes grid class with cells, where each cell can be accessed
class Grid:
    def __init__(self, i, j):
        self.x = i
        self.y = j
        self.neighbors = []

        self.visited = False
        self.prev = None
    # Show the grid

    def show(self, window, col):
        pygame.draw.rect(window, col, (self.x*w, self.y*h, w-1, h-1))
    # Add all grid locations

    def add_neighbors(self, grid):
        if self.x < cols - 1:
            self.neighbors.append(grid[self.x+1][self.y])
        if self.x > 0:
            self.neighbors.append(grid[self.x-1][self.y])
        if self.y < rows - 1:
            self.neighbors.append(grid[self.x][self.y+1])
        if self.y > 0:
            self.neighbors.append(grid[self.x][self.y-1])


for i in range(cols):
    arr = []
    for j in range(rows):
        arr.append(Grid(i, j))
    grid.append(arr)

for i in range(cols):
    for j in range(rows):
        grid[i][j].add_neighbors(grid)


start = grid[cols//2][rows//2]

queue.append(start)
start.visited = True


def main():
    end = grid[cols-30][rows - cols//2]

    found = False
    searchStarted = False

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                searchStarted = True
            # If user clicks on cell, the end node is now the chosen cell
            if event.type == pygame.MOUSEBUTTONDOWN:
                if pygame.mouse.get_pressed(3):
                    position = pygame.mouse.get_pos()
                    print(position[0])
                    end = grid[position[0]//w][position[1]//h]

        # performs BFS by checking each level
        if searchStarted:
            if len(queue) > 0:
                current = queue.popleft()
                if current == end:
                    print("Found")
                    found = True

                if current is not None and found == False:
                    for i in current.neighbors:
                        if not i.visited:
                            i.visited = True
                            queue.append(i)
            elif found == False:
                print("No Solution")

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
