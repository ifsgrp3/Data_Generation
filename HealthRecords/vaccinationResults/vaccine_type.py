import random, sys

vaccine_type_list = ["pfizer", "moderna", "sinovac"]


def main():
    count = 0
    sys.stdout = open("vaccineType.csv", "w")

    while count < 5000:
        print(vaccine_type_list[random.randint(0, 2)])
        count += 1

    sys.stdout.close()


main()
