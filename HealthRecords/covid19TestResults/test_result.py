import random, sys

# 0 represent negative, 1 represent positive
test_result_list = [0, 1]


def main():
    count = 0
    sys.stdout = open("testResult.csv", "w")
    while count < 5000:
        print(test_result_list[random.randint(0, 1)])
        count += 1
    sys.stdout.close()


main()

