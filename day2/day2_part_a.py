with open ("data.txt") as f:
    data = [i for i in f.read().strip().split("\n")]

# print(rounds)

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

outcomes_part_a = {
    "A X": 4,
    "A Y": 8,
    "A Z": 3,
    "B X": 1,
    "B Y": 5,
    "B Z": 9,
    "C X": 7,
    "C Y": 2,
    "C Z": 6,
}

total_points = 0

for round in data:
    total_points = total_points + outcomes_part_a[round]

print("Part 1:", total_points, "points")