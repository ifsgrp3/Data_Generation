import random, sys


def generate_postal_code():
    postal_code = []
    postal_code.append(random.randint(1, 9))
    i = 0
    while i < 5:
        postal_code.append(random.randint(0, 9))
        i += 1

    return postal_code


def main():
    my_set = set()
    count = 0

    while count < 5000:
        my_set.add(''.join(map(str, generate_postal_code())))
        count += 1

    sys.stdout = open("zipCode.csv", "w")
    for n in my_set:
        print(n)
    sys.stdout.close()

main()

