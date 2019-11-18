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

def hint(x,y):
    gameDisplay.blit(hint8, (x, y))

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

    hint((rect_Width + margin), (rect_Height + margin))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            b.solved = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            if 0 <= pos[0] <= rect_Width and 0 <= pos[1] <= rect_Height:
                if b.puzzle[0][0] == 0:
                    color = black
                    b.puzzle[0][0] = 1
                else:
                    color = white
                    b.puzzle[0][0] = 0
            elif (rect_Width + margin) <= pos[0] <= (rect_Width*2 + margin) and 0 <= pos[1] <= rect_Height:
                if b.puzzle[0][1] == 0:
                    color = black
                    b.puzzle[0][1] = 1
                else:
                    color = white
                    b.puzzle[0][1] = 0
            elif (rect_Width*2 + margin*2) <= pos[0] <= (rect_Width*3 + margin*2) and 0 <= pos[1] <= rect_Height:
                if b.puzzle[0][2] == 0:
                    color = black
                    b.puzzle[0][2] = 1
                else:
                    color = white
                    b.puzzle[0][2] = 0
            elif 0 <= pos[0] <= rect_Width and (rect_Height  + margin) <= pos[1] <= (rect_Height*2 + margin):
                if b.puzzle[1][0] == 0:
                    color = black
                    b.puzzle[1][0] = 1
                else:
                    color = white
                    b.puzzle[1][0] = 0
            elif (rect_Width*2 + margin*2) <= pos[0] <= (rect_Width*3 + margin*2) and (rect_Height + margin) <= pos[1] <= (rect_Height*2 + margin):
                if b.puzzle[1][2] == 0:
                    color = black
                    b.puzzle[1][2] = 1
                else:
                    color = white
                    b.puzzle[1][2] = 0
            elif 0 <= pos[0] <= rect_Width and (rect_Height*2 + margin*2) <= pos[1] <= (rect_Height*3 + margin*2):
                if b.puzzle[2][0] == 0:
                    color = black
                    b.puzzle[2][0] = 1
                else:
                    color = white
                    b.puzzle[2][0] = 0
            elif (rect_Width + margin) <= pos[0] <= (rect_Width*2 + margin) and (rect_Height*2 + margin*2) <= pos[1] <= (rect_Height*3 + margin*2):
                if b.puzzle[2][1] == 0:
                    color = black
                    b.puzzle[2][1] = 1
                else:
                    color = white
                    b.puzzle[2][1] = 0
            elif (rect_Width*2 + margin*2) <= pos[0] <= (rect_Width*3 + margin*2) and (rect_Height*2 + margin*2) <= pos[1] <= (rect_Height*3 + margin*2):
                if b.puzzle[2][2] == 0:
                    color = black
                    b.puzzle[2][2] = 1
                else:
                    color = white
                    b.puzzle[2][2] = 0
            
    
    b.checkSolved()
            



    pygame.display.update()
    fps.tick(60)