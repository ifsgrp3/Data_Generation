import random, sys

vaccination_centre_location_list = ['Radin Mas Community Club', 'Kolam Ayer Community Club', 'Buona Vista Community Club',
                                    'Potong Pasir Community Club', 'Raffles City Convention Centre', 'Tanjong Pagar Community Club',
                                    'Jalan Besar Community Club', 'Bishan Community Club', 'Queenstown Community Centre',
                                    'Toa Payoh West Community Club', 'Marine Parade Community Club', 'Bukit Timah Community Club',
                                    'Geylang Serai Community Club', 'Tampines East Community Club', 'Bedok Community Centre',
                                    'Pasir Ris Elias Community Club', 'Arena@ Our Tampines Hub', 'Marsiling Community Club',
                                    'Woodlands Community Club', 'Woodlands Galaxy Community Club', 'Canberra Community Club',
                                    'Nee Soon East Community Club', 'Kebun Baru Community Club', 'Punggol 21 Community Club',
                                    'The Serangoon Community Club', 'Sengkang Community Club', 'Hougang Community Club',
                                    'Teck Ghee Community Club', 'Hong Kah North Community Club', 'Yew Tee Community Club',
                                    'Former Hong Kah Secondary School', 'Taman Jurong Community Club', 'Yuhua Community Club',
                                    'Nanyang Community Club', 'Clementi Community Centre', 'Senja-Cashew Community Club',
                                    'Chua Chu Kang Community Club']


def main():
    count = 0
    sys.stdout = open("vaccinationCentreLocation.csv", "w")
    while count < 5000:
        print(vaccination_centre_location_list[random.randint(0, 36)])
        count += 1
    sys.stdout.close()


main()

