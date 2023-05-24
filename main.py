import pygame

# setting up our game window here
pygame.init()
width = 1000
height = 900
screen = pygame.display.set_mode([width, height])
pygame.display.set_caption('Two-Player Chess :)')
font = pygame.font.Font('freesansbold.ttf', 20)
big_font = pygame.font.Font('freesansbold.ttf', 50)

#setting up our framerate here
timer = pygame.time.Clock()
fps = 60

# game variables and images
white_pieces = ['rook', 'knight', 'bishop', 'king', 'queen', 'bishop', 'knight', 'rook',
                'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn']
white_locations = [(0,0), (1,0), (2,0), (3,0), (4,0), (5,0), (6,0), (7,0),
                   (0,1), (1,1), (2,1), (3,1), (4,1), (5,1), (6,1), (7,1)]

black_pieces = ['rook', 'knight', 'bishop', 'king', 'queen', 'bishop', 'knight', 'rook',
                'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn']
black_locations = [(0,7), (1,7), (2,7), (3,7), (4,7), (5,7), (6,7), (7,7),
                   (0,6), (1,6), (2,6), (3,6), (4,6), (5,6), (6,6), (7,6)]

captured_pieces_white = []
captured_pieces_black = []

turn_step = 0
selection = 100
valid_moves = []

# load in game piece images for both white and black pieces
# black pieces below. Load in assets, then create a main piece, then a captured piece
black_queen = pygame.image.load('assets/images/black queen.png')
black_queen = pygame.transform.scale(black_queen, (80, 80))
black_queen_small = pygame.transform.scale(black_queen, (45, 45))

black_king = pygame.image.load('assets/images/black king.png')
black_king = pygame.transform.scale(black_king, (80, 80))
black_king_small = pygame.transform.scale(black_king, (45, 45))

black_knight = pygame.image.load('assets/images/black knight.png')
black_knight = pygame.transform.scale(black_knight, (80, 80))
black_knight_small = pygame.transform.scale(black_knight, (45, 45))

black_rook = pygame.image.load('assets/images/black rook.png')
black_rook = pygame.transform.scale(black_rook, (80, 80))
black_rook_small = pygame.transform.scale(black_rook, (45, 45))

black_bishop = pygame.image.load('assets/images/black bishop.png')
black_bishop = pygame.transform.scale(black_bishop, (80, 80))
black_bishop_small = pygame.transform.scale(black_bishop, (45, 45))

black_pawn = pygame.image.load('assets/images/black pawn.png')
black_pawn = pygame.transform.scale(black_pawn, (65, 65))
black_pawn_small = pygame.transform.scale(black_pawn, (45, 45))

# white pieces below:
white_queen = pygame.image.load('assets/images/white queen.png')
white_queen = pygame.transform.scale(white_queen, (80, 80))
white_queen_small = pygame.transform.scale(white_queen, (45, 45))

white_king = pygame.image.load('assets/images/white king.png')
white_king = pygame.transform.scale(white_king, (80, 80))
white_king_small = pygame.transform.scale(white_king, (45, 45))

white_knight = pygame.image.load('assets/images/white knight.png')
white_knight = pygame.transform.scale(white_knight, (80, 80))
white_knight_small = pygame.transform.scale(white_knight, (45, 45))

white_rook = pygame.image.load('assets/images/white rook.png')
white_rook = pygame.transform.scale(white_rook, (80, 80))
white_rook_small = pygame.transform.scale(white_rook, (45, 45))

white_bishop = pygame.image.load('assets/images/white bishop.png')
white_bishop = pygame.transform.scale(white_bishop, (80, 80))
white_bishop_small = pygame.transform.scale(white_bishop, (45, 45))

white_pawn = pygame.image.load('assets/images/white pawn.png')
white_pawn = pygame.transform.scale(white_pawn, (65, 65))
white_pawn_small = pygame.transform.scale(white_pawn, (45, 45))

# lists of our white piece variables
white_images = [white_pawn, white_queen, white_king, white_bishop, white_knight, white_rook]
small_white_images = [white_pawn_small, white_queen_small, white_king_small, white_bishop_small, white_knight_small, white_rook_small]

black_images = [black_pawn, black_queen, black_king, black_bishop, black_knight, black_rook]
small_black_images = [black_pawn_small, black_queen_small, black_king_small, black_bishop_small, black_knight_small, black_rook_small]

piece_list = ['pawn', 'queen', 'king', 'bishop', 'knight', 'rook']

# check variables here


# draw main game board
def draw_board():
    for row in range(8):
        for column in range(8):
            # column = j
            # row = i
            
            # to make our grid, we need alternating row patterns
            # if the row is odd, then the pattern is black -> white
            # if the row is even, then the pattern is white -> black
            
            if row % 2 == 0:
                if column % 2 == 0:
                    pygame.draw.rect(screen, 'black', [600 - (column * 100), row * 100, 100, 100])
                else:
                    pygame.draw.rect(screen, 'white', [700 - (column * 100), row * 100, 100, 100])
            else:
                if column % 2 == 0:
                    pygame.draw.rect(screen, 'white', [700 - (column * 100), row * 100, 100, 100])
                else:
                    pygame.draw.rect(screen, 'black', [600 - (column * 100), row * 100, 100, 100])
    pygame.draw.rect(screen, 'pink', [0, 800, width, 100])
    pygame.draw.rect(screen, 'gold', [0, 800, width, 100], 5)
    pygame.draw.rect(screen, 'gold', [800, 0, 200, height], 5)
    
    status_text = ['White: Select a piece to move', 'White: Select a destination',
                   'Black: Select a piece to move', 'Black: select a destination']
    screen.blit(big_font.render(status_text[turn_step], True, 'black'), (20, 820))
    
    for i in range(9):
        pygame.draw.line(screen, 'black', (0, 100 * i), (800, 100 * i), 2)
        pygame.draw.line(screen, 'black', (100 * i, 0), (100 * i, 800), 2)
        
# draw pieces onto board
def draw_pieces():
    # white pieces
    for i in range(len(white_pieces)):
        index = piece_list.index(white_pieces[i])
        if white_pieces[i] == 'pawn':
            screen.blit(white_pawn, (white_locations[i][0] * 100 + 22, white_locations[i][1] * 100 + 15))
        else:
            screen.blit(white_images[index], (white_locations[i][0] * 100 + 10, white_locations[i][1] * 100 + 10))

        if turn_step < 2:
            if selection == i:
                pygame.draw.rect(screen, 'red', [white_locations[i][0] * 100 + 1, white_locations[i][1] * 100 + 1, 100, 100], 2)
        
    # black pieces
    for i in range(len(black_pieces)):
        index = piece_list.index(black_pieces[i])
        if black_pieces[i] == 'pawn':
            screen.blit(black_pawn, (black_locations[i][0] * 100 + 22, black_locations[i][1] * 100 + 15))
        else:
            screen.blit(black_images[index], (black_locations[i][0] * 100 + 10, black_locations[i][1] * 100 + 10))

        if turn_step >= 2:
            if selection == i:
                pygame.draw.rect(screen, 'blue', [black_locations[i][0] * 100 + 1, black_locations[i][1] * 100 + 1, 100, 100], 2)
                



# setting up main gameplay loop
run = True

while run:
    timer.tick(fps) #timer ticks at our framerate
    screen.fill('pink')
    
    draw_board()
    draw_pieces()
    
    #this is our event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            x_coordinate = event.pos[0] // 100
            y_coordinate = event.pos[1] // 100
            click_coordinates = (x_coordinate, y_coordinate)
            
            if turn_step <= 1:
                if click_coordinates in white_locations:
                    selection = white_locations.index(click_coordinates)
                    if turn_step == 0:
                        turn_step = 1
                # if click_coordinates in valid_moves and selection != 100:
                    
            
            
            
            
    pygame.display.flip()
pygame.quit()