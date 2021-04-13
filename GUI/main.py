import tkinter 

class MainWindow(tkinter.Tk):
    """ Ana pencere """

    def __init__(self):
        super().__init__()
        """ Ana pencere ayarları """
        # ana pencere başlığı
        self.title("Cryptographic Ciphers")
        # ana pencere boyutu
        self.geometry("835x490")
        # ana pencere rengi
        self.configure(background = "light blue")
        
    # encryption fonksiyonu
    def encryption(self, message, shifter_key):
        encryption_result = ""
        # go through every character
        for i in range(len(message)):
            letter = message[i]
            if (letter.isupper()):
                encryption_result += chr((ord(letter) + shifter_key - 65)%26 + 65)
            elif(letter.islower()):
                encryption_result += chr((ord(letter) + shifter_key - 97)%26 + 97)
            elif(letter == " "):
                encryption_result += " "
        return encryption_result

    # decryption fonksiyonu    
    def decryption(self, message, shifter_key):
        decryption_result = ""
        # go through every character
        for i in range(len(message)):
            letter = message[i]
            if (letter.isupper()):
                decryption_result += chr((ord(letter) - shifter_key - 65)%26 + 65)
            elif(letter.islower()):
                decryption_result += chr((ord(letter) - shifter_key - 97)%26 + 97)
            elif(letter == " "):
                decryption_result += " "
        return decryption_result
        
root_window = MainWindow()
if __name__ == "__main__":
    root_window.mainloop()