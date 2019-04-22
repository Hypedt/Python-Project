#This function is the start menu
def start_menu():
    choice = 0
    print("\nWelcome!\n"
          "1) Start Game\n"
          "2) How to play\n"
          "3) Scoreboard\n"
          "-1) Quit")
    while choice != -1:
        choice = int(input("CHOICE #"))
        if choice == 1:
            start_game()
            print ("1) Start Game")
        elif choice == 2:
            #how_to
            print("2) How To Play")
            how_to()
        elif choice == 3:
            #Scoreboard
            print("3) Scoreboard")
            #scoreBoard()
        elif choice != -1:
            print ("Enter an option")

#Main function that will run everything before the game is to startW
def main():
    start_menu()

#This function is to print out the instructions to the game
def how_to():
    print("*************\n"
          "Hello\n"
          "Welcome to my game\n"
          "It is a simple text based puzzle game.\n"
          "All you have to do is explore and find the key that is hidden.\n"
          "If you encounter something, "
          "a prompt will appear asking you whether to want to do something.\n"
          "It is that simple.\n"
          "Enjoy!\n"
          "************\n")

#This function reads the text file
def scoreboard():
    #fileWrite()
    file = open(r"Scoreboard.txt","r+")
    for line in file:
        print (line)
    file.close()

#Function is to write to the text file for scores
"""
def file_write():
    file = "Scoreboard.txt"
    with open (file, "w+") as f:
        f.write(input());
    f.close()
"""


#This function will print out a map
def grid_map():

    #This creates the room
    room = []
    for rows in range(5):
        room.append([])
        for columns in range(5):
            room[rows].append(0)
    print()

    print ("Modified")

    #legend of the assest in the game
    door = 'D'
    box = 'B'
    switch = 'S'
    table = 'T'
    playerPOS = 'X'

    current_x = 3
    current_y = 2

    room[4][2] = door
    room[2][1] = box
    room[0][1] = switch
    room[0][3] = table
    room[0][4] = table
    room[current_x][current_y] = playerPOS

    #Modified the room and prints it out
    for rows in range(5):
        room.append([])
        for columns in range(5):
            room[rows].append(0)
            print(room[rows][columns], end=" ")
        print()

def start_game():
    grid_map()
    game_continue = True

    # This creates the 2D array
    room = []
    for rows in range(5):
        room.append([])
        for columns in range(5):
            room[rows].append(0)
    print()

    #The starting position of the player
    current_y = 3
    current_x = 2

    #Gives position for each variable
    position_player = room[current_x][current_y]
    position_door = room[4][2]

    while game_continue:
        movement = input()
        if movement == 'w':
            current_y -= 1
        elif movement == 's':
            current_y += 1
        elif movement == 'a':
            current_x -= 1
        elif movement == 'd':
            current_x += 1

        #Checks if movement is working properly
        for rows in range(5):
            room.append([])
            for columns in range(5):
                room[rows].append(0)
                if rows == current_y and columns == current_x:
                    print('X', end=" ")
                else:
                    print(room[rows][columns], end=" ")
            print()


#Main Function
if __name__ == '__main__':
    main()