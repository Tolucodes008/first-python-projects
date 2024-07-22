char_1 = "x"
char_2 = "o"
grid = [["_","_","_"],
        ["_","_","_"], 
        ["_","_","_"]]

lose = True
win = True
def draw_grid():
    for i in grid:
        print(" ".join(i))

def choose_char():
    print("Welcome to tic-tac-to \n")
    print("choose character 1(x) or character 2(y) \n")
    print("Take turn in inputting your character coordinates")


def win_lose(char1, char2):
    num_x = 0
    num_y = 0
    for row1 in range(len(grid)):
        if grid[row1-1][0] == char1:
            num_x += 1
        if grid[row1-1][0] == char2:
            num_y += 1
    if num_y < 3:
        num_y = 0
    if num_x < 3:
        num_x = 0
    for row2 in range(len(grid)):
        if grid[row2-1][1] == char1:
            num_x += 1
        if grid[row2-1][1] == char2:
            num_y += 1
    if num_y < 3:
        num_y = 0
    if num_x < 3:
        num_x = 0
    for row3 in range(len(grid)):
        if grid[row3-1][2] == char1:
            num_x += 1
        if grid[row3-1][2] == char2:
            num_y += 1
    if num_y < 3:
        num_y = 0
    if num_x < 3:
        num_x = 0
    if num_x == 3:
        print("Player one wins")
        return win
    if num_y == 3:
        print("Player two wins")
        return win 
    
    
        


def main_game(char_1, char_2):
    while "x" not in grid or "y" not in grid:
        char_1_row = int(input("Character 1 enter your row number: "))
        while char_1_row > 3 or char_1_row < 1:
            char_1_row = int(input("Character 1 enter your row number: "))
        char_1_coloumn = int(input("Character 1 enter your coloumn number: "))
        while char_1_coloumn > 3 or char_1_coloumn < 1:
            char_1_coloumn = int(input("Character 1 enter your row number: "))
        if grid[char_1_row-1][char_1_coloumn-1] != char_2:
            grid[char_1_row-1][char_1_coloumn-1] = char_1
        else:
            continue
        draw_grid()
        if win_lose(char_1, char_2) == win:
            break
        char_2_row = int(input("Character 2 enter your row number: "))
        while char_2_row > 3 or char_2_row < 1:
            char_2_row = int(input("Character 1 enter your row number: "))
        char_2_coloumn = int(input("Character 2 enter your coloumn number: "))
        while char_2_coloumn > 3 or char_2_row < 1:
            char_2_coloumn = int(input("Character 1 enter your row number: "))
        if grid[char_2_row-1][char_2_coloumn-1] != char_1:
            grid[char_2_row-1][char_2_coloumn-1] = char_2
        else:
            continue
        draw_grid()
        if win_lose(char_1, char_2) == win:
            break

choose_char()
main_game(char_1, char_2)

