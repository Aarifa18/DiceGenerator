# Import the random module 
import random
# Set the minimum vaue the dice can roll
min = 1
# Set the largest value the dice can roll
max = 6
# Set the initial value of sum variable to 0
sum = 0
# Keep looping as long as the user wants to keep running simulations
keepGoing = True
# Use a while loop with the boolean variable to keep looping
while (keepGoing == True):
     # Set the two dice values by choosing a random number between min and max
    die1 = random.randint(min,max)
    die2 = random.randint(min,max)
    # Add the values and print the values of each die and their sum
    sum = die1 + die2
    
    print("\nFirst roll is " + str(die1))
    print("\nSecond roll is " + str(die2))
    print("\nSum of both dice is " + str(sum))

    # While loop keeps going until a valid input is given
    isValid = True
    while (isValid == True):
        # Ask user if they want to keep going
        askUser = str(input("roll again? (y/n)"))
        # Checks to see if user does not want to keep going
        if (askUser == "n" or askUser == 'no'):
            print("\nThank You, Bye!")
            break
        # Checks to make sure the input is valid
        if(askUser != "n" and askUser != "no" and askUser != "y" and askUser != "yes"):
            print ("Please put a valid answer")
        else:
            isValid = False
