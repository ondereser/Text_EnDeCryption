### Önder Eser, onder.eser@pru.edu.tr
def encrypted(string, shift):
    cipher = ""
    for char in string:
        if char==" ":
            cipher = cipher + char
        elif char.isupper():
            cipher = cipher + chr((ord(char)+shift-65)%26+65)
        else:
            cipher = cipher + chr((ord(char)+shift-97)%26+97)
    return cipher

def decrypted(encrypted, shift):
    cipher = ""
    for char in encrypted:
        if char==" ":
            cipher = cipher + char
        elif char.isupper():
            cipher = cipher + chr((ord(char)-shift-65)%26+65)
        else:
            cipher = cipher + chr((ord(char)-shift-97)%26+97)
    return cipher

print("If you press q, the program will be terminated")
while True:
    text = input("enter the text:")
    s = int(input("enter the shift key:"))
    print("the original text is:", text)
    print("the encrypted message is:", encrypted(text, s))
    encryption = encrypted(text, s)
    print("the decrypted message is:", decrypted(encryption, s))

    if text == "q":
        break




