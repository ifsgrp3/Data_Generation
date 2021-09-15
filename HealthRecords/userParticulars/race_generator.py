import random
import sys

race_list = ["chinese", "malay", "indian", "others"]


def main():
    count = 0
    sys.stdout = open("race.csv", "w")

    while count != 5000:
        print(race_list[random.randint(0, 3)])
        count += 1

    sys.stdout.close()


main()
