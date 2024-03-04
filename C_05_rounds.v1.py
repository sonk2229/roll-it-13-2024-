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

# Tell the user if they are eligible for double points

# Get initial dice rolls for computer

# Loop (while both user / computers have <= 13 points)...
# ask user if they want to roll again, update
# points /status

# Roll die for computer and update computer points

# Outside loop - double user points if they won and are eligible

# Show rounds results
