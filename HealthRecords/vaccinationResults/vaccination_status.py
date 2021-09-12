import random, sys

# 0 represent not vaccinated, 1 represent partially vaccinated, 2 represent fully vaccinated
vaccination_status_list = [0, 1, 2]


def main():
    count = 0
    sys.stdout = open("vaccinationStatus.csv", "w")
    while count < 5000:
        print(vaccination_status_list[random.randint(0, 2)])
        count += 1
    sys.stdout.close()


main()


