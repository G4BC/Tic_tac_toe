def hasWon(matrix, n):
    """
    Returns whether someone has won or not.
    n is 1 (player) or 2 (computer).
    """
    c1 = 0
    c2 = 0
    # horizontal and vertical
    for i in range(0, 3):
        c1 = 0
        c2 = 0
        for j in range(0, 3):
            if matrix[i][j] == n:
                c1 += 1
            if matrix[j][i] == n:
                c2 += 1
        if c1==3 or c2==3:
            return 1
    
    # diagonal
    if matrix[1][1] == n and ((matrix[0][0]==n and matrix[2][2]==n) or (matrix[0][2]==n and matrix[2][0]==n)):
        return 1
    return 0


def on_click(i, j, matrix):
    matrix[i][j] = 1

    # Checking if the player has won
    if hasWon(matrix, 1) == 1:
        result = 1
        closed = 1            


    if not closed:
        #Computer's Turn -*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
        played = 0
        i = y - 1  
        j = x - 1

        #Idea to improve the CPU's skill: Firstly, check if in any row, column or diagonal the player is almost winning (with two symbols). If not, make the tradicional play.

        # It tries to play at the sides of the player's symbol 
        if i+1 < 3 and matrix[i+1][j]==0:
            matrix[i+1][j] = 2
            played = 1
        elif i-1 >= 0 and matrix[i-1][j]==0:
            matrix[i-1][j] = 2
            played = 1
        elif j+1 < 3 and matrix[i][j+1]==0:
            matrix[i][j+1] = 2
            played = 1
        elif j-1 >= 0 and matrix[i][j-1]==0:
            matrix[i][j-1] = 2
            played = 1
        # Now at the diagonals
        elif i+1<3 and j+1<3 and matrix[i+1][j+1]==0:
            matrix[i+1][j+1] = 2
            played = 1
        elif i+1<3 and j-1>=0 and matrix[i+1][j-1]==0:
            matrix[i+1][j-1] = 2
            played = 1
        elif i-1>=0 and j+1<3 and matrix[i-1][j+1]==0:
            matrix[i-1][j+1] = 2
            played = 1
        elif i-1>=0 and j-1>=0 and matrix[i-1][j-1]==0:
            matrix[i-1][j-1] = 2
            played = 1
        # Then, it tries every possible play.
        else:
            for i in range(0, 3):
                for j in range(0, 3):
                    if matrix[i][j]==0:
                        matrix[i][j] = 2
                        played = 1

        # Lastly, if nothing works, it's a tie.
        if not played:
            result = 0
            closed = 1

    if not closed and hasWon(matrix, 2)==1:
        result = -1
        closed = 1

    print_table(matrix)


    if result == 1:
        print()
        print("Congrats!! You won!")
    elif result == 0:
        print()
        print("It's a tie.")
    elif result == -1:
        print()
        print("What a shame. You lost.")

    digited = 0
    while not digited:
        print("Wanna play again? (Y or N)")

        x = input()
        if x == 'Y':
            digited = 1
        elif x == 'N':
            digited = 1
            finish = 1
        else:
            print("Input incorrect. Try again.")

