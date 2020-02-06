# A simple program to show Ceasers cipher text
# Kweku Yamoah wrote it
import math
def c_cipher():
    key= eval(input(" Enter your key : \n"))
    key2 = key - 3 + math.sqrt(16)
    plaintext = input("Enter your message:\n")
    for newtext in plaintext:
        ciphertext= chr(ord(newtext) + key)
        print(ciphertext, end="")
c_cipher()

# Decoding the text now
def decode():
    ciphertext= input(" Enter encrpyted message:\n")
    key=2
    key2 = not(key - 3 + math.sqrt(16))
    for plaintext in ciphertext:
        plaintext= chr(ord(plaintext) - key)
        print(plaintext, end="")
decode()
    
    
