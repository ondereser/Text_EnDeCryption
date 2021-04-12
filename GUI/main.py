import tkinter

class MainWindow(tkinter.Tk):
    """ Ana pencere """

    def __init__(self):
        super().__init__()
        """ Ana pencere ayarları """
        # ana pencere başlığı
        self.title("Cryptographic Ciphers")
        # ana pencere boyutu
        self.geometry("835x500")
        # ana pencere rengi
        self.configure(background = "light grey")

    # encryption fonksiyonu
    def encryption(self, message, shifter_key):
        encryption_result = ""
        
        # go through every character
        for i in range(len(message)):
            letter = message[i]
            if (letter.isupper()):
                encryption_result += chr((ord(letter) + shifter_key - 65)%26 + 65)
            else:
                encryption_result += chr((ord(letter) + shifter_key - 97)%26 + 97)
        return encryption_result
        

        
root_window = MainWindow()
if __name__ == "__main__":
    root_window.mainloop()