# finds the lowest, highest and average score from a list
def get_stats(stats_list):
    pass
    # sort the lists.
    stats_list.sort()

    # find lowest, highest and average scores...

    lowest_score = stats_list[0]
    highest_score = stats_list[-1]
    average_score = sum(stats_list) / len(stats_list)

    return [lowest_score, highest_score, average_score]


# Create lists to hold user and computer scores
user_score = [10, 0, 13, 10, 10, 11]
comp_score = [10, 11, 0, 0, 10, 11]

# Loop six times - for testing purposes, ask the user to enter the 
# score for the user and the computer for each round
# for item in range(0, 6):
#     user_score = int(input("Enter the user score:  "))
#     comp_score = int(input("Enter the computer score:  "))
#
#     # add user score to list of user scores!
#     user_scores.append(user_score)
#     comp_scores.append(comp_score)

# calculate the lowest, highest and average
# scores and display time

user_stats = get_stats(user_score)
comp_stats = get_stats(comp_score)

print(" Game Statistics ")
print(f"User - Lowest Score: {user_stats[0]}\t"
      f"Highest Score: {user_stats[1]}\t "
      f"Average Scores: {user_stats[2]}")

print(f"Computer - Lowest Score: {comp_stats[0]}\t"
      f"Highest Score: {comp_stats[1]}\t "
      f"Average Scores: {comp_stats[2]}")
