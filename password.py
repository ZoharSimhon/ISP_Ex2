hash = "$6$EumdVZ0c$kI1t/HYchH3FRUBLrPuV1Na85YGvaq6HC7AmS3Q9H9wS4q0gKuA.Gb8LR/jcViBOGgMHGWrvI.hxTncfocS73."

def cammelCase(lines):
    with open('password.txt', 'a') as file:
        for line in lines:
            fullName = line.strip().split(" ")
            print(fullName,"\n")
            pas = fullName[0].lower() + fullName[1] + "\n"
            file.write(pas)


def cammelCaseUpper(lines):
    with open('password.txt', 'a') as file:
        for line in lines:
            fullName = line.strip().split(" ")
            pas = fullName[0] + fullName[1] + "\n"
            file.write(pas)


def lowerCase(lines):
    with open('password.txt', 'a') as file:
        for line in lines:
            fullName = line.strip().split(" ")
            pas = fullName[0].lower() + fullName[1].lower() + "\n"
            file.write(pas)


with open('names.txt') as f:
    lines = f.readlines()

count = 0
# Strips the newline character
for line in lines:
    count += 1
    line1 = line.strip()
    print(line1)

cammelCase(lines)
cammelCaseUpper(lines)
lowerCase(lines)
