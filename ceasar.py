alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


def encrypt(text,shift):
    encrypted_word = ""
    for char in text:
        index = alphabet.index(char)
        en = alphabet[(index+shift)]
        encrypted_word += en
    print(encrypted_word)

def decrypt(text,shit):
 pass

encrypt(text,shift)
