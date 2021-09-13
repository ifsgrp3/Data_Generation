import random, sys


def main():
    count = 0
    sys.stdout = open("temperature.csv", "w")
    while count < 5000:
        temperature_value = round(random.uniform(36.0, 38.0), 1)
        print(temperature_value)

        count += 1
    sys.stdout.close()


main()
