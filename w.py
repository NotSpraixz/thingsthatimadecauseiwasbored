import random
import string

def generate_key():
    letters = string.ascii_uppercase + string.digits
    key = ''.join(random.choice(letters) for i in range(25))
    return key

print("Generating Windows 10 keys...")
for i in range(10):
    print(generate_key())
