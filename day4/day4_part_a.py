with open ("data.txt") as f:
    data = [i for i in f.read().strip().split("\n")]

count = 0

for x in data:
    #  50-50, 50-87
    # a1 = 50, a2 = 50
    # b1 = 50, b2 = 87
    
    # Case 1
    # b1 ---------------- b2
    #   a1 ------------ a2

    # Case 2
    #    b1 ------ b2
    # a1 ------------- a2
    
    a, b = x.split(",")
    a1, a2 = a.split("-")
    b1, b2 = b.split("-")
    
    # case 2
    if int(a1) <= int(b1) and int(a2) >= int(b2):
        count += 1
    # case 1
    elif int(a1) >= int(b1) and int(a2) <= int(b2):
        count += 1

print("Part 1: ", count)
  

 
