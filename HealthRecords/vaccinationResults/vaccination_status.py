import random, sys
from datetime import datetime
from dateutil.relativedelta import relativedelta

# 0 represent not vaccinated, 1 represent partially vaccinated, 2 represent fully vaccinated
vaccination_status_list = [0, 1, 2]
vaccine_type_list = ["pfizer", "moderna", "sinovac"]
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
    sys.stdout = open("vaccinationStatus.csv", "w")
    while count < 5000:
        vaccination_status_bit = vaccination_status_list[random.randint(0, 2)]
        # not vaccinated
        if vaccination_status_bit == 0:
            vaccine_type = "null"
            vaccination_centre_location = "null"
            first_dose_date = "null"
            second_dose_date = "null"
            print(vaccination_status_bit, ",", vaccine_type, ",", vaccination_centre_location, ",", first_dose_date,
                  ",", second_dose_date)
            count += 1
            continue
        # partially vaccinated/fully vaccinated
        else:
            vaccine_type = vaccine_type_list[random.randint(0, 2)]
            vaccination_centre_location = vaccination_centre_location_list[random.randint(0, 36)]
            first_dose_date = datetime.today()
            second_dose_date = first_dose_date + relativedelta(months=6)

            date_format = '%Y/%m/%d'
            first_dose_date_str = first_dose_date.strftime(date_format)
            second_dose_date_str = second_dose_date.strftime(date_format)

            print(vaccination_status_bit, ",", vaccine_type, ",", vaccination_centre_location, ",", first_dose_date_str,
                  ",", second_dose_date_str)
            count += 1
            continue

    sys.stdout.close()


main()


