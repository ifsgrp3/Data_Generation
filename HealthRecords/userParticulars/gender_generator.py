import random
import sys

gender_list = ["female", "male"]


def main():
    i = 0
    sys.stdout = open("gender.csv", "w")
    while i < 5000:
        print(gender_list[random.randint(0, 1)])
        i += 1


main()

