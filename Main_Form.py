import tkinter as tk
from tkinter import messagebox
from SymmetricCiphers.caesar import caesar_decryption
from SymmetricCiphers.hillcipher import HillCipherDecryptWrapper
from SymmetricCiphers.playfair import PlayFairDecrypt
from SymmetricCiphers.sdes import SDESDecrypt

from server import get_data_from_server
from server import get_data_from_file
import tkinter as tk
from tkinter.font import Font



root = tk.Tk()
text = tk.Text(root)
myFont = Font(family="FreeSans", size=10, weight="bold")



data_counter = 0

root.title("NIS Practicals Server")
v = tk.IntVar()
v.set(0)  # initializing the choice, i.e. Symmetric

languages = [
    "Symmetric",
    "Asymmetric"
]
def Pass_Text():
    global data_counter
    if v.get() == 0:
        if tkvarsymmetric.get() == "Caesar":
            try:
                key_value = int(ent1.get())
                key_value = key_value % 26
            except ValueError:
                messagebox.showerror("Error", "Please enter a number")
                return
                
            print (data_counter)
            cipher = get_data_from_file(data_counter)
            cipher = cipher.replace("\n", "")
            if cipher == "":
                messagebox.showerror("Error", "Nothing to read")
                return
            data_counter += 1
            ent2.config(state='normal')
            ent2.delete(0, 'end')
            ent.delete(0, 'end')
            ent2.insert(0, cipher)
            ent2.config(state='disabled')
            plain = caesar_decryption(cipher, key_value)
            ent.insert(0, plain)

        elif tkvarsymmetric.get() == "Hill":
            try:
                key_value = ent1.get()
                if len(key_value) != 9:
                    raise ValueError("Length not equal to : 9")
            except ValueError:
                messagebox.showerror("Error", "Please enter key of length : 9")
                return

            print (data_counter)
            cipher = get_data_from_file(data_counter)
            cipher = cipher.replace("\n", "")
            if cipher == "":
                messagebox.showerror("Error", "Nothing to read")
                return
            data_counter += 1
            ent2.config(state='normal')
            ent2.delete(0, 'end')
            ent.delete(0, 'end')
            ent2.insert(0, cipher)
            ent2.config(state='disabled')
            plain = HillCipherDecryptWrapper(cipher, key_value)
            ent.insert(0, plain)

        elif tkvarsymmetric.get() == "Playfair":
            try:
                key_value = ent1.get()
                if len(key_value) == 0:
                    raise ValueError("Key Length should not be equal to : 0")
            except ValueError:
                messagebox.showerror("Error", "Key Length should not be equal to : 0")
                return

            print (data_counter)
            cipher = get_data_from_file(data_counter)
            cipher = cipher.replace("\n", "")
            if cipher == "":
                messagebox.showerror("Error", "Nothing to read")
                return
            data_counter += 1
            ent2.config(state='normal')
            ent2.delete(0, 'end')
            ent.delete(0, 'end')
            ent2.insert(0, cipher)
            ent2.config(state='disabled')
            plain = PlayFairDecrypt(cipher, key_value)
            ent.insert(0, plain)
        
        elif tkvarsymmetric.get() == "S-DES":
            try:
                key_value = ent1.get()
                if len(key_value) != 10:
                    raise ValueError("Key is invalid")
               
            except ValueError:
                messagebox.showerror("Error", "Key is invalid")
                return

            print (data_counter)
            cipher = get_data_from_file(data_counter)
            cipher = cipher.replace("\n", "")
            if cipher == "":
                messagebox.showerror("Error", "Nothing to read")
                return
            data_counter += 1
            ent2.config(state='normal')
            ent2.delete(0, 'end')
            ent.delete(0, 'end')
            ent2.insert(0, cipher)
            ent2.config(state='disabled')
            plain = SDESDecrypt(key_value, cipher)
            ent.insert(0, plain)

    print(ent.get())

mainFrame = tk.Frame(root)
mainFrame.pack(side=tk.BOTTOM, fill=tk.X, padx=20, pady=20)
mainFrame2 = tk.Frame(root)
mainFrame2.pack(side=tk.BOTTOM, fill=tk.X, padx=20, pady=20)
mainFrame3 = tk.Frame(root)
mainFrame3.pack(side=tk.BOTTOM, fill=tk.X, padx=20, pady=20)

optionFrame = tk.Frame(root)
optionFrame.pack(side=tk.BOTTOM, fill=tk.X, padx=20, pady=20)

tkvarsymmetric = tk.StringVar()
# List with options
choicessy = {'Caesar', 'Hill', 'Playfair', 'S-DES'}
tkvarsymmetric.set('Caesar')
popupMenuSy = tk.OptionMenu(optionFrame, tkvarsymmetric, *choicessy)
popupMenuSy.pack(side=tk.TOP, padx=20, pady=20)
popupMenuSy.configure(font=myFont)


tkvarasy = tk.StringVar()
# List with options
choicesasy = {'Diffie Hellman', 'xyz'}
tkvarasy.set('Diffie Hellman')
popupMenuAsy = tk.OptionMenu(optionFrame, tkvarasy, *choicesasy)
popupMenuAsy.pack(side=tk.TOP, padx=20, pady=20)
popupMenuAsy.pack_forget()
popupMenuAsy.configure(font=myFont)
# popupMenuSy.pack_forget()

lab = tk.Label(mainFrame, width=15, text="Decrypted Data: ", anchor='w')
lab.configure(font=myFont)
ent = tk.Entry(mainFrame)
lab.pack(side=tk.LEFT)
ent.configure(font=myFont)
ent.pack(side=tk.RIGHT, expand=tk.YES, fill=tk.X)


lab1 = tk.Label(mainFrame2, width=15, text="Key: ", anchor='w')
ent1 = tk.Entry(mainFrame2)
lab1.pack(side=tk.LEFT)
ent1.pack(side=tk.RIGHT, expand=tk.YES, fill=tk.X)
lab1.configure(font=myFont)
ent1.configure(font=myFont)

lab2 = tk.Label(mainFrame3, width=15, text="Received Data: ", anchor='w')
ent2 = tk.Entry(mainFrame3)
lab2.pack(side=tk.LEFT)
ent2.pack(side=tk.RIGHT, expand=tk.YES, fill=tk.X)
ent2.config(state='disabled')
lab2.configure(font=myFont)
ent2.configure(font=myFont)
# ent.pack(side=tk.BOTTOM, expand=tk.YES, fill=tk.X)
# ent2 = tk.Entry(mainFrame)
# ent2.pack(side=tk.BOTTOM, expand=tk.YES, fill=tk.X)

buttonFrame = tk.Frame(root)
buttonFrame.pack(side=tk.RIGHT, fill=tk.X, padx=20, pady=20)

b1 = tk.Button(buttonFrame, text='Quit', command=root.quit)
b1.pack(side=tk.LEFT, padx=5, pady=5)    
b1.configure(font=myFont)
b2 = tk.Button(root, text='Decrypt',
          command=(Pass_Text))
b2.pack(side=tk.RIGHT, padx=5, pady=5)
b2.configure(font=myFont)

def ShowChoice():
    print(v.get())
    if v.get() == 0:
        popupMenuAsy.pack_forget()
        popupMenuSy.pack(side=tk.TOP, padx=20, pady=20)
    elif v.get() == 1:
        popupMenuSy.pack_forget()
        popupMenuAsy.pack(side=tk.TOP, padx=20, pady=20)
    

        

row = tk.Frame(root)

for val, language in enumerate(languages):
    tk.Radiobutton(row, 
                  text=language,
                  padx = 20, 
                  variable=v, 
                  command=ShowChoice,
                  value=val,font=myFont).pack(side=tk.LEFT)
row.pack(side=tk.TOP, fill=tk.X, padx=5, pady=5)


root.mainloop()