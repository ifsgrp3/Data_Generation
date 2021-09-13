import random, sys

# 0 represents symptoms not visible, 1 represents symptoms visible
covid_symptoms_list = [0, 1]


def main():
    count = 0
    sys.stdout = open("covidSymptoms.csv", "w")
    while count < 5000:
        print(covid_symptoms_list[random.randint(0, 1)])
        count += 1
    sys.stdout.close()


main()

