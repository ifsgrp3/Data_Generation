import random, sys

# 0 represent ART, 1 represent PCR
covid19_test_type_list = [0, 1]


def main():
    count = 0
    sys.stdout = open("covid19TestType.csv", "w")
    while count < 5000:
        print(covid19_test_type_list[random.randint(0, 1)])
        count += 1
    sys.stdout.close()


main()
