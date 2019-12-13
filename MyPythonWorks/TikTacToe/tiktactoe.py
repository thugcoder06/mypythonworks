import random
#variables
first=" "
second=' '
decider=0
toggle=1
looping=' '
selection=' '
marker=' '
marker1=' '
marker2=' '
avail=True
position=0
winner=0
valid_input=False
test_board = ['#',' ',' ',' ',' ',' ',' ',' ',' ',' ']
#creating the board
def display_board(game):
    print( "   |   |   |  \n {} | {} | {} |  \n   |   |   |  \n_ _ _ _ _ _ __\n   |   |   |  \n {} | {} | {} |  \n   |   |   |  \n_ _ _ _ _ _ __ \n   |   |   |  \n {} | {} | {} |  \n   |   |   |  ".format(game[1],game[2],game[3],game[4],game[5],game[6],game[7],game[8],game[9]))
#taking player input
def player_input():
    global marker1
    global marker2
    starter = ' '
    while(starter!="X" and starter!="x" and starter!="o" and starter!="O"):
        starter = input("{} : Enter your choice (X or O) : ".format(first))
        if starter!="X" and starter!="x" and starter!="o" and starter!="O":
            print("Invalid input, please try again!!!")
    if starter=="X" or "x":
        marker1='X'
        marker2 = 'O'
    if starter == "X" or "x":
        marker1='O'
        marker2 = 'X'
# updating sign on the board
def place_marker(board, marker, position):
    board[position]=marker
    display_board(test_board)
#checking the winner
def win_check(game, mark):
    global looping,winner
    count=0
    i=1
    horizontal = 1
    const = 1

    while(i<=9 and winner==0):
        if(game[i]==mark):
            count=count+1
        else:
            count=0
        if(i==3 or i==6 or i==9):
            if(count==3):
                winner=1
            count=0
        if(winner==1):
            print("{} is winner".format(looping))
            break
        i+=1

    if winner==0:
        i=1

    while (i <= 9 and winner == 0):
        if(game[horizontal]==mark):
            count+=1
        else:
            count=0
        if (horizontal == 7 or horizontal == 8 or horizontal == 9):
            if (count == 3):
                winner = 1
            count = 0
            const+=1
            horizontal=const-3
        if (winner == 1):
            print("{} is winner".format(looping))
            break
        i += 1
        horizontal=horizontal+3

    if(game[1]==mark and game[5]==mark and game[9]==mark):
        winner=1
        print("{} is winner".format(looping))
    else:
        if(game[3]== mark and game[5]==mark and game[7]==mark):
            print("{} is winner".format(looping))
            winner = 1
#toss
def choose_first():
    decider=random.randint(1,2)
    global first,second
    if decider==1:
        print("Player 1: Go First")
        first="Player 1"
        second="Player 2"
    else:
        print("Player 2: Go First")
        first = "Player 2"
        second = "Player 1"
#check if position is available on board
def space_check(game, position):
    global toggle
    if game[position]==" ":
        toggle += 1
        return 1
    else:
        print(" OOPS!! This place is occupied, try again!!")
        player_choice(test_board)
#cheking if board is full
def full_board_check(game):
    global avail
    for i in range(len(game)):
        if game[i] != " ":
            avail=False
        else:
            avail=True
            break
    return avail
#Write a function that asks for a player's next position (as a number 1-9) and then uses the function from step 6 to check if it's a free position. If it is, then return the position for later use.
def player_choice(game):
    global position,toggle,looping,marker,marker1,marker2,position,valid_input
    if toggle%2!=0:
        looping=first
        marker=marker1
    else:
        looping=second
        marker = marker2
    while True:
        global valid_input
        position=int(input("{} Chose your position : ".format(looping)))
        for i in range(1,10):
            if position==i:
               valid_input=True
               break
        if valid_input:
            valid_input=False
            break
        if not valid_input:
            print("OOPS!! Invalid Input. Please try again.")
            continue
    free=space_check(test_board,position)
    if free==1:
        return position
#Replay
def replay():
    rplay=input("Would you like to play again? (Y or N) : ")
    if rplay=="Y":
        print('\n' * 50)
        global first,second,decider,toggle,looping,selection,marker,marker1,marker2,avail,position,winner,valid_input,test_board
        first = " "
        second = ' '
        decider = 0
        toggle = 1
        looping = ' '
        selection = ' '
        marker = ' '
        marker1 = ' '
        marker2 = ' '
        avail = True
        position = 0
        winner = 0
        valid_input = False
        test_board = ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
        return True
#applying the game
while True:
    print("Welcome to Tik Tac Toe !!!")
    display_board(test_board)
    choose_first()
    player_input()
    while avail:
        print('\n' * 18)
        pos=player_choice(test_board)
        place_marker(test_board, marker, position)
        win_check(test_board, marker)
        full_board_check(test_board)
        if winner==1:
            break
    if(avail==False and winner==0):
        print("Game Draw!!")
    if not replay():
        print('\n' * 50)
        print("Game Over")
        break







