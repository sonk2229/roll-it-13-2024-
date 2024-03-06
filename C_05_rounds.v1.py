import random


# generates an integer between 0 and 6
# to simulate a roll of a die
def roll_die():
    result = random.randint(1, 6)
    return result

# rolls two dice and returns total and whether we
# had a double roll


def two_rolls():
    double_score = "no"

    # roll two dice
    roll_1 = roll_die()
    roll_2 = roll_die()

    # check if we have a double score opportunity
    if roll_1 == roll_2:
        double_score = "yes"

    # Find the total points (so far)
    user_points = roll_1 + roll_2

    # Show the user the result
    print(f"Die 1:{roll_1} \t Die 2: {roll_2} ")

    return user_points, double_score

# Main Routine starts here


print("press <enter> to begin this round: ")
input()
# Get initial dice rolls for user
user_first = two_rolls()
user_points = user_first[0]
double_points = user_first[1]


# Tell the user if they are eligible for double points
if double_points == "no":
    double_feedback = ""
else:
    double_feedback = "If you win this round, you gain double points"


# output initial move results
print(f"You rolled a total of {user_points}. {double_feedback}")
print()

# Get initial dice rolls for computer
computer_first = two_rolls()
computer_points = computer_first[0]

print(f"The computer rolled a total of {computer_points}.")


# Loop (while both user / computers have <= 13 points)...
while computer_points < 13 and user_points < 13:

    # ask user if they want to roll again, update
    # points /status
    print()
    roll_again = input("Do you want to roll the dice (type 'no' to pass): ")
    if roll_again == "yes":
        user_move = roll_die()
        user_points += user_move
        print(f"You rolled a {user_move}. You now have {user_points} points.")

    # If user goes over 13 points, tell them that they lose and set points to 0
    if user_points > 13:
        print(f"Oops! you rolled a {user_move} so your total is {user_points}."
              f"Which is over 13 points .")

        # reset user points to zero so that when we update their
        # score at the end of round it is correct.
        user_points = 0

        break

    else:
        print(f"You rolled a {user_move} and have a total score of {user_points}.")

# Roll die for computer and update computer points
    computer_move = roll_die()
    computer_points += computer_move
    print(f"The computer rolled a {computer_move}.   The computer"
          f" now has {computer_points}.")
    # check computer has not gone over...
    if computer_points > 13:
        print(f"The computer rolled a {computer_move}, taking their points"
              f" to {computer_points}.  This is over 13 points so the computer loses!")
        computer_points = 0
        break

    else:
        print(f"The computer rolled a {computer_move}.  The computer"
              f" now has {computer_points}. ")
        
    print()
    if user_points > computer_points:
        result = "You are ahead."
    else:
        result = "The computer is ahead!"

    print(f"***Round Update****:{result}  ")
    print(f"User Score: {user_points} \t | \t Computer Score: {computer_points}")


# Outside loop - double user points if they won and are eligible

# Show rounds results
if user_points < computer_points:
    print("Sorry - you lost this round and no points "
          "have been added to your total score. The computer's score has"
          f"increased by {computer_points} points.")

# currently does not include double points!
else:
    print(f"Yay! you won the round and {user_points} points have  "
          f"been added to your score")
