import pygame, puzzle

pygame.init()

def hint(img, x,y):
    img = pygame.transform.scale(img, (rect_Width, rect_Height))
    gameDisplay.blit(img, (x, y))

# Display the rectangles
def displayTiles():
    for row in range(len(b.rectangles)):
        for col in range(len(b.rectangles[row])):
            if b.puzzle[row][col] == 0:
                pygame.draw.rect(gameDisplay, white, 
                                 b.rectangles[row][col])
            elif b.puzzle[row][col] == 8:
                hint(hint8, (rect_Width * col + margin * col), (rect_Height * row + margin * row))
            elif b.puzzle[row][col] == 4:
                hint(hint4, (rect_Width * col + margin * col), (rect_Height * row + margin * row))
            elif b.puzzle[row][col] == 1111:
                hint(hint1111, (rect_Width * col + margin * col), (rect_Height * row + margin * row))
            elif b.puzzle[row][col] == 7:
                hint(hint7, (rect_Width * col + margin * col), (rect_Height * row + margin * row))
            else:
                pygame.draw.rect(gameDisplay, black, 
                                 b.rectangles[row][col])

# Constants
black = (0, 0, 0)
white = (255, 255, 255)
fps = pygame.time.Clock()
b = puzzle.Board()

# Rectangle Dimensions
rect_Height = 150
rect_Width = 150
margin = 5

# Build list of rectangles
for i in range(len(b.puzzle)):
    b.rectangles.append([])
    for j in range(len(b.puzzle[i])):
        b.rectangles[i].append([j*(rect_Width + margin), i*(rect_Height + margin), rect_Width, rect_Height])

# Build the game screen
numCol = len(b.rectangles)
numRow = len(b.rectangles[0])
game_Height = rect_Height * numCol + margin * (numCol - 1)
game_Width = rect_Width * numRow + margin * (numRow - 1)
gameDisplay = pygame.display.set_mode((game_Width, game_Height))
pygame.display.set_caption('Tapa')

# Images
hint1111 = pygame.image.load("hint1111.JPG")
hint8 = pygame.image.load("8hint.JPG")
hint4 = pygame.image.load("hint4.JPG")
hint7 = pygame.image.load("hint7.JPG")
solvedImg = pygame.image.load("solved.JPG")
solvedImg = pygame.transform.scale(solvedImg, (rect_Width*2, game_Height // 4))

# Run the puzzle loop
while not b.done:
 
    # Check for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            b.done = True
        ## Makes clicks interact with the rectangles
        elif event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            y = int(pos[0]/rect_Width) 
            x = int(pos[1]/rect_Height)

            if b.puzzle[x][y] == 0:
                b.puzzle[x][y] = 1
            elif b.puzzle[x][y] == 1:
                b.puzzle[x][y] = 0 
    
    displayTiles()
    b.checkSolved()

    # Display solved screen when finished
    if b.solved == True:
        gameDisplay.fill(black)
        gameDisplay.blit(solvedImg, (game_Width // 2 - rect_Width, game_Height // 2 - game_Height // 8))
            
    pygame.display.update()
    fps.tick(60)