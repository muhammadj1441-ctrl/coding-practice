board = [["r", "w", "y", "r", "r", "r", "w", "y", "y"],
         ["w", "w", "y", "r", "y", "r", "y", "y", "w"],
         ["r", "y", "y", "w", "r", "r", "w", "y", "w"],
         ["w", "y", "y", "w", "r", "y", "w", "y", "y"],
         ["r", "w", "w", "r", "r", "r", "y", "r", "r"],
         ["w", "y", "y", "w", "w", "r", "r", "y", "w"],
         ["y", "w", "y", "w", "r", "r", "w", "y", "y"],
         ["y", "w", "y", "w", "y", "r", "w", "y", "w"],
         ["w", "w", "y", "y", "r", "r", "w", "y", "r"],
         ["w", "r", "y", "w", "r", "y", "w", "r", "y"]]

print(board[0][2])

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
while endGame == False:
    # events
    for e in event.get():  # get all events
        if e.type == QUIT:
            endGame = True
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

            cx = 55 + row * 65
            cy = 55 + col * 65


            if board[row][col] == "r":
                draw.circle(screen, (255, 0, 0), (cx, cy), 30)
            elif board[row][col] == "y":
                draw.circle(screen, (255, 255, 0), (cx, cy), 30)
            elif board[row][col] == "w":
                draw.circle(screen, (255, 255, 255), (cx, cy), 30)
            col = col + 1
        row = row + 1


    display.flip()
