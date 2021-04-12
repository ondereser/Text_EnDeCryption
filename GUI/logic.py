

def encryption(message, shifter_key):
    encryption_result = ""
    
    # go through every character
    
    for i in range(len(message)):
        letter = message[i]
    
        if (letter.isupper()):
            encryption_result += chr((ord(letter) + shifter_key - 65)%26 + 65)
        else:
            encryption_result += chr((ord(letter) + shifter_key - 97)%26 + 97)

    return encryption_result


message = input("mesajınızı giriniz:")
shifter_key = int(input("key seçiniz:"))
print("Encrypted message:", encryption(message, shifter_key))