import random

character="+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
print(character[0:10])

pass_length=int(input("Masukkan panjang sandi: "))
password=""

for i in range(pass_length):
    password += random.choice(character)

print(password)
