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
hint8 = pygame.image.load("8hint.JPG")
solvedImg = pygame.image.load("solved.JPG")

def hint(x,y):
    gameDisplay.blit(hint8, (x, y))

color = white

while not b.done:
    
    for row in range(len(b.rectangles)):
        for col in range(len(b.rectangles[row])):
            if b.puzzle[row][col] == 0:
                pygame.draw.rect(gameDisplay, white, 
                                 b.rectangles[row][col])
            else:
                pygame.draw.rect(gameDisplay, black, 
                                 b.rectangles[row][col])

    hint((rect_Width + margin), (rect_Height + margin))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            b.done = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            y = int(pos[0]/rect_Width) 
            x = int(pos[1]/rect_Height)

            if b.puzzle[x][y] == 0:
                b.puzzle[x][y] = 1
            else:
                b.puzzle[x][y] = 0 
    
    b.checkSolved()
    if b.solved == True:
        gameDisplay.fill(black)
        gameDisplay.blit(solvedImg, (0, 0))
            



    pygame.display.update()
    fps.tick(60)