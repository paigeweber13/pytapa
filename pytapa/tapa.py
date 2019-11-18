import pygame

pygame.init()

game_Height = 590
game_Width =  590

square_Height = 190
square_Width = 190
margin = 5

black = (0, 0, 0)
white = (255, 255, 255)

gameDisplay = pygame.display.set_mode((game_Width, game_Height))
pygame.display.set_caption('Tapa')

puzzleSolved = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
puzzleDefault = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
puzzle = puzzleDefault

fps = pygame.time.Clock()

solved = False

while not solved:
    
    color = white
    rect = [0, -200, 190, 190]

    for row in puzzle:
        rect[1] += 200
        for col in row:
            pygame.draw.rect(gameDisplay, color, rect)
            rect[0] += 200
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            solved = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()



    pygame.display.update()
    fps.tick(60)