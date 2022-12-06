with open ("data.txt") as f:
    signal = [i for i in f.read().strip()]
#print(data_signal)

size = len(signal)

# 4 for part 1
# 14 for part 2
n = 4
x = 0

for char in range(0, size):
    # retrieve 4 characters per iteration
    sequence = signal[x:x+n]
    if len(set(list(sequence))) == n:
        # distinct marker found
        x += 4
        break
    # continue iterating
    x += 1

print("Part 1:", x)