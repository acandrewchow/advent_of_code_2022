with open ("data.txt") as f:
    data = [i for i in f.read().strip().split("\n")]

points_part_two = 0 

# priorities 
# from a to z is 1 - 26
# from A to Z is 27 - 52

# 3 sacks per
for i in range(0, len(data), 3):
    sack_one, sack_two, sack_three = set(data[i]), set(data[i+1]), set(data[i+2])
    common_badges = set.intersection(sack_one, sack_two, sack_three)

    for x in common_badges:
        if x.islower():
            points_part_two += ord(x) - ord('a') + 1
        else:
            points_part_two += ord(x) - ord('A') + 27
    
print("Part 2:", points_part_two)
      
