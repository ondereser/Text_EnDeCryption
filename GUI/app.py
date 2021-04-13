import main as mn

""" Logical fonksiyonlar"""

# encryption işlemi gerçekleşiyor 
def move_text_to_decrypt_box():
    space = "\n"
    moving_text = encryption_box.get("1.0", mn.tkinter.END)
    empty_message = "ERROR! The en/decryption box or shifter key box is empty!\n"
    shifter_key_number = shifter_key_box.get("1.0", mn.tkinter.END)
    
    if empty_message in moving_text:
        encryption_box.delete("1.0", mn.tkinter.END)
    
    elif (len(moving_text)< 2 or len(shifter_key_number)< 2):
        # text box dolu mu boş mu kontrol ediyoruz
        decryption_box.insert("1.0", empty_message)
    else:
        # encryption işlemi gerçekleşiyor ve decryption kutusuna yazılıyor
        decryption_box.insert("1.0", space)
        decryption_box.insert("1.0", mn.MainWindow.encryption(moving_text, moving_text, int(shifter_key_number)))
        encryption_box.delete("1.0", mn.tkinter.END)

# decryption işlemi gerçekleşiyor 
def move_text_to_encrypted_box():
    moving_text = decryption_box.get("1.0", mn.tkinter.END)
    empty_message = "ERROR! The en/decryption box or shifter key box is empty!\n"
    shifter_key_number = shifter_key_box.get("1.0", mn.tkinter.END)

    # text box dolu mu boş mu kontrol ediyoruz
    if empty_message in moving_text:
        decryption_box.delete("1.0", mn.tkinter.END)
    elif (len(moving_text) <2 or len(shifter_key_number)< 2):
        encryption_box.insert("1.0", empty_message)
    # mesajı decrypt edip diğer kutuya gönderme işlemi
    else:
        encryption_box.insert("1.0", mn.MainWindow.decryption(moving_text, moving_text, int(shifter_key_number)))
        decryption_box.delete("1.0", mn.tkinter.END)
# tüm kutular yenilenir
def refresh_all():
    encryption_box.delete("1.0", mn.tkinter.END)
    decryption_box.delete("1.0", mn.tkinter.END)
    shifter_key_box.delete("1.0", mn.tkinter.END)

# başlık 
placeholder_label = mn.tkinter.Label(text = "                                ", font = ("times", 20), bg = "light blue")
placeholder_label.grid(row =0, column =0)

title_label = mn.tkinter.Label(text = "Cryptographic Ciphers", font = ("times", 20), bg = "light blue")
title_label.grid(row =0, column =1)

placeholder_label = mn.tkinter.Label(text = "                                               ", font = ("times", 20), bg = "light blue")
placeholder_label.grid(row =0, column =2)

# encryption mesajı
encryption_message = mn.tkinter.Label(text = "Encrypt", font = ("times", 17), pady = 20, bg = "light green")
encryption_message.grid(row = 1, column = 0, sticky = mn.tkinter.W)

# decryption mesajı
decryption_message = mn.tkinter.Label(text = "Decrypt", font = ("times", 17), pady = 20, bg = "light green")
decryption_message.grid(row = 1, column = 2, sticky = mn.tkinter.E)

# encryption kutusu
encryption_box = mn.tkinter.Text(height = 20, width = 30)
encryption_box.grid(row = 2, column= 0, sticky = mn.tkinter.W)

# shifter key
shifter_key = mn.tkinter.Label(text = "Shifter Key =", font = ("times", 15), bg = "green", fg = "white")
shifter_key.grid(row = 1, column= 1, sticky = mn.tkinter.W)

# shifter key kutusu
shifter_key_box = mn.tkinter.Text(height=2, width=5)
shifter_key_box.grid(row=1,column=1)

# encryption butonu
encryption_button = mn.tkinter.Button(text = "              ENCRYPT              ", 
                                        font = ("times", 15), pady = 10, command = move_text_to_decrypt_box, bg = "green")
encryption_button.grid(row = 3, column = 0, sticky = mn.tkinter.W)

# decryption kutusu
decryption_box = mn.tkinter.Text(height = 20, width = 30)
decryption_box.grid(row = 2, column= 2, sticky = mn.tkinter.E)

# decryption butonu
decryption_button = mn.tkinter.Button(text = "             DECRYPT              ",
                                         font = ("times", 15), pady = 10, command = move_text_to_encrypted_box, bg = "green")
decryption_button.grid(row = 3, column = 2, sticky = mn.tkinter.E)

# refresh butonu
refresh_button = mn.tkinter.Button(text = "RESET", font = ("times", 15), pady = 2,command = refresh_all, fg = "white", bg = "blue")
refresh_button.grid(row = 1, column = 1, sticky = mn.tkinter.E)

# loop the program
if __name__ == "__main__":
    mn.root_window.mainloop()