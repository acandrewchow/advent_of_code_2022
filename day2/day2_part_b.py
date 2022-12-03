with open ("data.txt") as f:
    data = [i for i in f.read().strip().split("\n")]

# print(data)

# All Game combinations
# Rock = 1
# Paper = 2
# Scissors = 3

# A | X = Draw =  1 + 3 = 4
# A | Y = Win  =  2 + 6 = 8
# A | Z = Loss =  3 + 0 = 3

# B | X = Loss =  1 + 0 = 1
# B | Y = Draw =  2 + 3 = 5
# B | Z = Win  =  3 + 6 = 9

# C | X = Win  =  1 + 6 = 7
# C | Y = Loss =  2 + 0 = 2
# C | Z = Draw =  3 + 3 = 6

# Change the points to the desired outcomes
# X = loss
# Y = Draw
# Z = Win
# Example A X is Draw - 4 points 
# X represents a Loss, therefore the outcome changes
# A X to 3 points to represent a loss

outcomes_part_b = {
    "A X": 3,
    "A Y": 4,
    "A Z": 8,
    "B X": 1,
    "B Y": 5,
    "B Z": 9,
    "C X": 2,
    "C Y": 6,
    "C Z": 7,
}

total_points = 0

for round in data:
    total_points = total_points + outcomes_part_b[round]

print("Part 2:", total_points,"points")