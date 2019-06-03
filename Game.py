#Import additional features
import random
import time

#This function is the start menu
def start_menu():
    choice = 0
    print("\nWelcome!\n")
    while choice != -1:
        print("1) Start Game\n"
              "2) How to play\n"
              "3) Scoreboard\n"
              "-1) Quit")
        choice = int(input("CHOICE #"))
        if choice == 1:
            #This will go to the start_game() function which will start the game
            start_game()
        elif choice == 2:
            #This will go to the how_to() function which will print out instructions
            how_to()
        elif choice == 3:
            #This will go to the scoreboard() function which will print out the scores
            scoreboard()
        elif choice != -1:
            #This message will print whenever an integer that is not listed is entered
            print ("Enter an option")

#Main function that will run everything before the game is to startW
def main():
    start_menu()

#This function is to print out the instructions to the game
def how_to():
    print("*************\n"
          "Hello\n"
          "Welcome to my game\n"
          "It is a simple text-based puzzle game.\n"
          "All you have to do is find the key.\n"
          "If you encounter something, "
          "a prompt will appear asking you whether to want to do something.\n"
          "You will not know how big the place is, but you are given coordinate.\n"
          "Enjoy!\n"
          "************\n")

#This function reads the text file
def scoreboard():
    print("\nCurrent Scores:")
    file = open("Scoreboard.txt",'r+')
    string = file.read()
    print(string)
    file.close()
    print()

#Function is to write to the text file for scores
def file_write(name, time):
    file = "Scoreboard.txt"
    with open (file, "a") as f:
        f.write("\n" + name + " - " + time + " secs")
    f.close()

#A class for the player
class Player:
    def __init__(self, name):
        self.name = name

#Function to allow the user to enter their name into a object
def record_name(time):
    p1 = Player(input("Enter name: "))
    player_name = str(p1.name)
    player_time = str(time)

    #Passes the user name and time to the file write function
    file_write(player_name, player_time)

#Function that is the entire game
def start_game():
    #Size of grid
    grid_size = 10
    #Boolean variable for loop to continue
    game_continue = True

    #Contraptions that are switches when encountered
    door_lock =  True
    cabinet_lock = True
    has_crowbar = False

    # This creates the 2D array
    room = []
    for rows in range(grid_size):
        room.append([0])
        for columns in range(grid_size):
                room[rows].append(0)
    print()

    #The starting position of the player
    #It will choose a number between the set value
    current_y = random.randint(3,5)
    current_x = random.randint(3,6)

    #Give values to objects
    #This is help identify the position they are are
    door = 1
    box = 2
    desk = 3
    cabinet = 4
    box_with_key = 5
    desk_with_key = 6
    cabinet_with_crowbar = 7

    #Placing objects with randomize locations
    #This will randomly choose an index of the 2D array
    #And will change its value to whatever the object value is
    #This for loop changes the value to the box
    for x in range (6):
        room[random.randint(1,9)][random.randint(7,8)] = box
        room[random.randint(6, 9)][random.randint(1, 8)] = box
        room[random.randint(1, 9)][random.randint(1, 2)] = box
    #This specific box is place randomly
    #It holds the key to which opens the door
    room[random.randint(1, 9)][random.randint(1, 8)] = box_with_key
    #This for loop places and changes the value to that of the desk
    for x in range (3):
        room[random.randint(1,9)][9] = desk
    #This specific desk is place randomly on column 9
    #It holds the key to open the cabinet
    room[random.randint(1, 9)][9] = desk_with_key
    #This for loop places dummy cabinets
    for x in range (4):
        room[random.randint(1,9)][0] = cabinet
    #This cabinet hols the crowbar which will help user to open the boxes
    room[random.randint(1, 9)][0] = cabinet_with_crowbar
    #The door is place randomly along the first row [0]
    room[0][random.randint(0, 9)] = door


    #This loop will print out the 2D array will everything on it
    """
    for rows in range(grid_size):
        room.append([])
        for columns in range(grid_size):
            room[rows].append(0)
            if rows == current_x and columns == current_y:
                print('P', end=" ")
            else:
                print(room[rows][columns], end=" ")
        print()
    """

    # Prompt
    print("""Waking up in a large, barely lit room. Seeing some desks, cabinets, and lots of boxes.
    There seems to be a door all the way in the back.
    Got to get out of here.\n""")

    # This start_time variable is to record the time it takes to complete the game
    start_time = time.time()

    #The while loop goes on until game_continue is False
    while game_continue:
        # This prints out the current location of the player
        print("Position:")
        print(current_x, current_y)

        #User is to input the direction they want to go
        movement = input("Enter W(up), A(left), S(down), D(right): ")
        #.lower() is used in case of CAPS
        if movement.lower() == 'w':
            #The if-then statements ensures user wiil not go out of bounds
            if current_x > 0:
                current_x -= 1
            else:
                print("It's a wall")
        elif movement.lower() == 's':
            #Ensures user not to go out of bounds
            #It is grid-size-1 because the first index is 0, not 1
            if current_x < (grid_size-1):
                current_x += 1
            else:
                print("It's a wall")
        elif movement.lower() == 'a':
            if current_y > 0:
                current_y -= 1
            else:
                print("It's a wall")
        elif movement.lower() == 'd':
            if current_y < (grid_size-1):
                current_y += 1
            else:
                print("It's a wall")

        """
        for rows in range(grid_size):
            room.append([])
            for columns in range(grid_size):
                room[rows].append(0)
                if rows == current_x and columns == current_y:
                    print('P', end=" ")
                else:
                    print(room[rows][columns], end=" ")
            print()
        """

        #All these if-then statements checks the user position value
        #And if they meet the value, then the following will happen
        #This checks if position value is the door
        if room[current_x][current_y] == 1:
            print("Door is locked")
            #The if-else checks if the door_lock is false to open
            if door_lock == True:
                    print("Looks like you need a key...")
            elif door_lock == False:
                #Ask user to do something
                decision = input("Do you want to insert the key? (Y/N): ")
                if decision.lower() == 'y':
                    "The door is now unlocked"
                    decision = input("Walk out? (Y/N): ")
                    if decision.lower() == 'y':
                        print("You escaped!\n")
                        #This will finish the game and stop the loop
                        game_continue = False
                        #The end_time will be record
                        end_time = time.time()
                        #Calculate the total time it took
                        total_time = end_time - start_time
                        #Pass the total time to the record_name function which user can record their name to the file
                        record_name(total_time)
                    elif decision.lower() != 'y':
                        print("You don't have a choice right now.")
                        print("You escaped!\n")
                        game_continue = False
                        end_time = time.time()
                        total_time = end_time - start_time
                        record_name(total_time)
                elif decision.lower() == 'n':
                    print("You decided to look around some more.")
        #Checks if the position value is a box
        elif room[current_x][current_y] == 2:
            print("There is a box")
            #If-else statements if user has found the crowbar
            if has_crowbar == True:
                decision = input("Do you want to break the box? (Y/N): ")
                if decision.lower() == 'y':
                    print("Nothing is inside.")
                    #This will change the value to 0
                    #which is an empty space
                    room[current_x][current_y] = 0
                elif decision.lower() == 'n':
                    print("You decided to do something else.")
            elif has_crowbar == False:
                decision = input("Do you want to break the box? (Y/N): ")
                if decision.lower() == 'y':
                    print("You punched the box and only injured yourself.")
                elif decision.lower() == 'n':
                    print("You decided to do something else.")
        #Checks if position value is a desk
        elif room[current_x][current_y] == 3:
            print("There is a desk here.")
            decision = input("Do you want to check the desk? (Y/N): ")
            if decision.lower() == 'y':
                print("There is nothing there.")
            elif decision.lower() == 'n':
                print("You decided to do something else.")
        #If the position space is a cabinet
        elif room[current_x][current_y] == 4:
            print("There is a cabinet here.")
            if cabinet_lock == True:
                    print("Looks like you need a key...")
            elif cabinet_lock == False:
                decision = input("Do you want to insert the key? (Y/N): ")
                if decision.lower() == 'y':
                    print("The cabinet is now unlocked")
                    print("There is nothing there.")
                    room[current_x][current_y] = 0
                elif decision.lower() == 'n':
                    print("You decided to look around some more.")
        #Checks if the postion value is the box with key
        elif room[current_x][current_y] == 5:
            print("There is a box")
            #Will only open if user has found the crowbar
            if has_crowbar == True:
                decision = input("Do you want to break the box? (Y/N): ")
                if decision.lower() == 'y':
                    print("There is a key inside!")
                    room[current_x][current_y] = 0
                    door_lock = False
                elif decision.lower() == 'n':
                    print("You decided to do something else.")
            elif has_crowbar == False:
                decision = input("Do you want to break the box? (Y/N): ")
                if decision.lower() == 'y':
                    print("You punched the box and only injured yourself.")
                elif decision.lower() == 'n':
                    print("You decided to do something else.")
        #Check if the value is the desk with key
        elif room[current_x][current_y] == 6:
            print("There is a desk here.")
            decision = input("Do you want to check the desk? (Y/N): ")
            if decision.lower() == 'y':
                print("There is a key!")
                #Changes the lock to false
                cabinet_lock = False
            elif decision.lower() == 'n':
                print("You decided to do something else.")
        #Checks the value to cabinet with the crowbar
        elif room[current_x][current_y] == 7:
            print("There is a cabinet here.")
            if cabinet_lock == True:
                print("Looks like you need a key...")
            elif cabinet_lock == False:
                decision = input("Do you want to insert the key? (Y/N): ")
                if decision.lower() == 'y':
                    print("The cabinet is now unlocked")
                    print("There is a crowbar!")
                    room[current_x][current_y] = 0
                    has_crowbar = True;
                elif decision.lower() == 'n':
                    print("You decided to look around some more.")

#Main Function
if __name__ == '__main__':
    main()