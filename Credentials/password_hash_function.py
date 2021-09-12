import uuid
import hashlib
import csv
import random, sys

def hashText(text):
    """
        Basic hashing function for a text using random unique salt.
    """
    salt = uuid.uuid4().hex
    return hashlib.sha256(salt.encode() + text.encode()).hexdigest() + ':' + salt


def matchHashedText(hashedText, providedText):
    """
        Check for the text in the hashed text
    """
    _hashedText, salt = hashedText.split(':')
    return _hashedText == hashlib.sha256(salt.encode() + providedText.encode()).hexdigest()

if __name__ == '__main__':
    hashtest = hashText('123')
    print(hashtest)
    hashrs = matchHashedText(hashtest,'123')
    #print("\n")
    #print(hashrs)



with open('password.csv') as csv_file:
    csv_reader = csv.reader(csv_file) #delimiter=''
    sys.stdout = open("password_with_hash1.csv", "w")
    for row in csv_reader:
            hashtest = hashText(row[0])
            _hashedText, salt = hashtest.split(':')
            print(row[0] + "," + _hashedText + "," + salt)
    sys.stdout.close()

