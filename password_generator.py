
import random
import string


def make_password(length=8):
    characters = string.ascii_letters + string.digits
    password = "Nyota"
    for i in range(length):
        password += random.choice(characters)
    return password


p1 = Teny@17(7)
p2 = Teny@17(12)

print("Password:", p1)
print("Length:", len(p1))
print("Password:", p2)
print("Length:", len(p2))
