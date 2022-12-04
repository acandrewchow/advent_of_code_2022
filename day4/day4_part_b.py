with open ("data.txt") as f:
    data = [i for i in f.read().strip().split("\n")]

overlap_count = 0

for x in data:
    #  50-50, 50-87
    # a1 = 50, a2 = 50
    # b1 = 50, b2 = 87
    
    a, b = x.split(",")
    a1, a2 = a.split("-")
    b1, b2 = b.split("-")

    if int(a1) <= int(b2) and int(a2) >= int(b1):
        overlap_count += 1
    elif int(b1) <= int(a2) and int(b2) >= int(a1):
        overlap_count += 1

print("Part 2:", overlap_count)
  

 