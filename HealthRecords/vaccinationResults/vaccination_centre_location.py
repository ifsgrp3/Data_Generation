import random, sys

vaccination_centre_location_list = ['radin mas community club', 'kolam ayer community club', 'buona vista community club',
                                    'potong pasir community club', 'raffles city convention centre', 'tanjong pagar community club',
                                    'jalan besar community club', 'bishan community club', 'queenstown community centre',
                                    'toa payoh west community club', 'marine parade community club', 'bukit timah community club',
                                    'geylang serai community club', 'tampines east community club', 'bedok community centre',
                                    'pasir ris elias community club', 'arena@ our tampines hub', 'marsiling community club',
                                    'woodlands community club', 'woodlands galaxy community club', 'canberra community club',
                                    'nee soon east community club', 'kebun baru community club', 'punggol 21 community club',
                                    'serangoon community club', 'sengkang community club', 'hougang community club',
                                    'teck ghee community club', 'hong kah north community club', 'yew tee community club',
                                    'former hong kah secondary school', 'taman jurong community club', 'yuhua community club',
                                    'nanyang community club', 'clementi community centre', 'senja-cashew community club',
                                    'chua chu kang community club']


def main():
    count = 0
    sys.stdout = open("vaccinationCentreLocation.csv", "w")
    while count < 5000:
        print(vaccination_centre_location_list[random.randint(0, 36)])
        count += 1
    sys.stdout.close()


main()





