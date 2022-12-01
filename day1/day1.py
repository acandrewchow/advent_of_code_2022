def readFile():
    with open('calories.txt') as f:
        data = [i for i in f.read().strip().split("\n")]
    return data

def main():
    data = readFile()
    calories = []
    total_per_elf = 0
    top_three_elf = 0

    for x in data:
        if x == '':
            total_per_elf = 0
        else:
            temp = int(x)
            total_per_elf += temp
            calories.append(total_per_elf)

    calories.sort()
    max_calories = max(calories)
    top_three_elf = calories[-1] + calories[-2] + calories[-3]

    # answers
    print("Part 1: ", max_calories)
    print("Part 2:", top_three_elf)
 
if __name__ == "__main__":
    main()