file = open("input.txt", "r")

lines = file.readlines()

count = len(lines)

first_two = lines[:2]

file.close()


output = open("output.txt", "w")

output.writelines(first_two)

output.close()

print("Number of lines:", count)
print("First two lines written to output.txt")