with open ("data.txt") as f:
    data = [i for i in f.read().strip().split("\n")]

points_part_one = 0

# priorities    
# from a to z is 1 - 26
# from A to Z is 27 - 52

for compartment in data:
    if len(compartment) % 2 == 0:
        x = len(compartment) // 2
        # split the sack
        sack, = set(compartment[:x]) & set(compartment[x:])

        if sack.islower():
            points_part_one += ord(sack) - ord('a') + 1
        else:
            points_part_one += ord(sack) - ord('A') + 27

print("Part 1:", points_part_one)
    
      
        


