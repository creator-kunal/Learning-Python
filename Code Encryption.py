import random

import string

chars = " " + string.punctuation + string.digits + string.ascii_letters

chars = list(chars)

key = chars.copy()

random.shuffle(key)


#ENCRYPT#
MESSAGE = input("Enter a message to Encrypt: ")

CODE = ""

for letter in MESSAGE:
    index = chars.index(letter)
    CODE += key[index]

print(f"original message : {MESSAGE}")

print(f"Encrypted message: {CODE}")


#DECRYPT#
CODE = input("Enter a message to Decrypt: ")
MESSAGE = ""

for letter in CODE:
    index = key.index(letter)
    MESSAGE += chars[index]

print(f"Encrypted message: {CODE}")
print(f"original message : {MESSAGE}")