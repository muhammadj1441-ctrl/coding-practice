board = [["w", "w", "w", "w", "w", "w", "w", "w", "w", "w"],
         ["w", "w", "w", "w", "w", "w", "w", "w", "w", "w"],
         ["w", "w", "w", "w", "w", "w", "w", "w", "w", "w"],
         ["w", "w", "w", "w", "w", "w", "w", "w", "w", "w"],
         ["w", "w", "w", "w", "w", "w", "w", "w", "w", "w"],
         ["w", "w", "w", "w", "w", "w", "w", "w", "w", "w"],
         ["w", "w", "w", "w", "w", "w", "w", "w", "w", "w"],
         ["w", "w", "w", "w", "w", "w", "w", "w", "w", "w"],
         ["w", "w", "w", "w", "w", "w", "w", "w", "w", "w"]]
print(board[8][0])

from pygame import *

init()  # set up pygame
width = 700
height = 700
# surface! - can draw to it
# tuple - like a list/array - cannot change!
screen = display.set_mode((width, height))

endGame = False
column_max = 9
row_max = 8
col_choice = -1
current_row = 8
current_player = "r"
while endGame == False:
    # events
    for e in event.get():
        if e.type == QUIT:  # get all events
            endGame = True
        if e.type == KEYDOWN:
            col_choice = -1
            if e.key == K_1:
                print("key 1 pressed")
                col_choice = 0
            elif e.key == K_2:
                print("key 2 pressed")
                col_choice = 1
        	elif e.key == K_3:
                print("key 3 pressed")
                col_choice = 2
            elif e.key == K_4:
                print("key 4 pressed")
                col_choice = 3
        	elif e.key == K_5:
                print("key 5 pressed")
                col_choice = 4
            elif e.key == K_6:
                print("key 6 pressed")
                col_choice = 5
            elif e.key == K_7:
                print("key 7 pressed")
                col_choice = 6
            elif e.key == K_8:
                print("key 8 pressed")
                col_choice = 7
            elif e.key == K_9:
                print("key 9 pressed")
                col_choice = 8
            elif e.key == K_0:
                print("key 10 pressed")
                col_choice = 9

            if col_choice != -1:
                while current_row > -1:
                    if board[current_row][col_choice] == "w":
                        board[current_row][col_choice] = current_player
                        current_row = -2

                        if current_player == "r":
                            current_player = "y"
                        else:
                            current_player = "r"

                        print(board[current_row][col_choice])

                    current_row = current_row - 1
                current_row = 8
                col_choice = -1

                



    screen.fill((0, 0, 0))  # tuple - RGB
    draw.rect(screen, (0, 0, 255), (20, 20, 660, 600))

    y = 55
    while y <= 55 + (65 * row_max):
        x = 55
        while x <= 55 + (65 * column_max):
            draw.circle(screen, (255, 255, 255), (x, y), 30)
            x = x + 65
        y = y + 65

    row = 0
    while row < len(board):
        col = 0
        while col < len(board[row]):
            cy = 55 + row * 65
            cx = 55 + col * 65

            if board[row][col] == "r":
                draw.circle(screen, (255, 0, 0), (cx, cy), 30)
            elif board[row][col] == "y":
                draw.circle(screen, (255, 255, 0), (cx, cy), 30)
            elif board[row][col] == "w":
                draw.circle(screen, (255, 255, 255), (cx, cy), 30)
            col = col + 1
        row = row + 1

    display.flip()




