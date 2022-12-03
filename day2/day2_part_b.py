with open ("data.txt") as f:
    data = [i for i in f.read().strip().split("\n")]

# print(data)

# All Game combinations

# A vs X = Draw =  1 + 3 = 4
# A vs Y = Win  =  2 + 6 = 8
# A vs Z = Loss =  3 + 0 = 3

# B vs X = Loss =  1 + 0 = 1
# B vs Y = Draw =  2 + 3 = 5
# B vs Z = Win  =  3 + 6 = 9

# C vs X = Win  =  1 + 6 = 7
# C vs Y = Loss =  2 + 0 = 2
# C vs Z = Draw =  3 + 3 = 6

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