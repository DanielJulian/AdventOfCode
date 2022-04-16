commands = open('day2_input.txt', 'r').readlines()

print("Solution 1")

depth = 0
forward = 0

for line in commands:
    l = line.strip().split(" ")
    command = l[0]
    amount = l[1]
    if (command == "forward"):
        forward += int(amount)
    elif (command == "down"):
        depth += int(amount)
    elif (command == "up"):
        depth -= int(amount)

print(forward*depth)


print("Solution 2")

depth = 0
forward = 0
aim = 0

for line in commands:
    l = line.strip().split(" ")
    command = l[0]
    amount = l[1]
    if (command == "forward"):
        forward += int(amount)
        depth += aim * int(amount)
    elif (command == "down"):
        aim += int(amount)
    elif (command == "up"):
        aim -= int(amount)

print(forward*depth)