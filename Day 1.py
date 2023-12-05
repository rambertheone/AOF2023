# a = "1abc2"
# z = ""
# for c in a:
#     if c.isnumeric():
#         z += str(c)
#         print(z)
# print(z)
# print(int(z)*2)
# Day 1 part 1

a = ["1abc2","pqr3stu8vwx","a1b2c3d4e5f","treb7uchet"]
z = ""
f = 0

with open('input1.txt', 'r') as Lines:
    for line in Lines:
        for char in line:
            if char.isnumeric():
                z += str(char)
        x = z[0] + z[-1]
        f += int(x)
        z = ""
print(f)

# print(line)
# print(Lines)