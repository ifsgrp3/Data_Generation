import random
import string
import sys

def id_generator(size=256, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

sys.stdout = open("BLE_ROLE_ADMIN.csv", "w")
for i in range(5000):
    ble = id_generator()
    role = id_generator(1,"123")
    admin = id_generator(1,"1234")

    print(ble + "," + role + "," + admin)
sys.stdout.close()
