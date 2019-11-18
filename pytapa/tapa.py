import pygame, puzzle

pygame.init()

game_Height = 590
game_Width =  590

rect_Height = 190
rect_Width = 190
margin = 10

black = (0, 0, 0)
white = (255, 255, 255)

gameDisplay = pygame.display.set_mode((game_Width, game_Height))
pygame.display.set_caption('Tapa')

b = puzzle.Board()

for i in range(len(b.puzzle)):
    b.rectangles.append([])
    for j in range(len(b.puzzle[i])):
        b.rectangles[i].append([j*(rect_Width + margin), i*(rect_Height + margin), rect_Width, rect_Height])

fps = pygame.time.Clock()

color = white

while not b.solved:

    for row in range(len(b.rectangles)):
        for col in range(len(b.rectangles[row])):
            if b.puzzle[row][col] == 0:
                pygame.draw.rect(gameDisplay, white, 
                                 b.rectangles[row][col])
            else:
                pygame.draw.rect(gameDisplay, black, 
                                 b.rectangles[row][col])
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            solved = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            if 0 <= pos[0] <= 190 and 0 <= pos[1] <= 190:
                color = black
                b.puzzle[0][0] = 1
    
    b.checkSolved()
            



    pygame.display.update()
    fps.tick(60)