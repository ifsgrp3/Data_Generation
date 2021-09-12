import random, sys

area_list = ["North", "South", "East", "West", "Central"]


def main():
    count = 0
    sys.stdout = open("area.csv", "w")
    while count < 5000:
        print(area_list[random.randint(0, 4)])
        count += 1
    sys.stdout.close()


main()

