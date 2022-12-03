with open ("data.txt") as f:
    data = [i for i in f.read().strip().split("\n")]

# print(rounds)

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