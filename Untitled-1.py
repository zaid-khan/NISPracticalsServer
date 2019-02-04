#!/usr/bin/python3

import ssl
import pandas as pd
from tkinter import *

methods = [
    ("Symmetric", 1),
    ("Asymmetric", 2)
]




fields = 'Link', 'Table ID', 'File Name'

def fetch(entries):
   i = 0
   for entry in entries:
      
      if i == 0:
        linktext  = entry[1].get() 
      elif i == 1:
        tableidtext = entry[1].get()
      else:
        filename = entry[1].get()
      i = i + 1

   ssl._create_default_https_context = ssl._create_unverified_context
   tables = pd.read_html(linktext)

   print(tables[int(tableidtext)])
   tables[int(tableidtext)].to_csv("/home/zaid/Desktop/"+ filename + ".csv", index=False)

   print('"%s"' % (linktext))
   print('"%s"' % (tableidtext))
     

def makeform(root, fields):
    entries = []
    row = Frame(root)
    var = IntVar()
    var.set(1)
    symmetricradiobutton = Radiobutton(row, width=15, text="Symmetric", variable=var, value=1)
    symmetricradiobutton.pack(anchor=W)
    asymmetricradiobutton = Radiobutton(row, width=15, text="Asymmetric",  variable=var, value=2)
    asymmetricradiobutton.pack(anchor=W)
    row.pack(side=TOP, fill=X, padx=5, pady=5)
    symmetricradiobutton.pack(side=LEFT)
    asymmetricradiobutton.pack(side=LEFT)
    entries.append(("Asymmetric", asymmetricradiobutton)) 
    entries.append(("Symmetric", symmetricradiobutton))
    # entries.append(("Asymmetric", asymmetricradiobutton)) 
    
    for field in fields:
        row = Frame(root)
        # rad = Radiobutton(row, width=15, text=field)
        lab = Label(row, width=15, text=field, anchor='w')
        ent = Entry(row)
        row.pack(side=TOP, fill=X, padx=5, pady=5)
        # rad.pack(side=LEFT)
        lab.pack(side=LEFT)
        ent.pack(side=RIGHT, expand=YES, fill=X)
        entries.append((field, ent))
    return entries

if __name__ == '__main__':
    root = Tk()
    root.title("NIS Practicals")
    ents = makeform(root, fields)
    root.bind('<Return>', (lambda event, e=ents: fetch(e)))   
    b1 = Button(root, text='Save As CSV',
          command=(lambda e=ents: fetch(e)))
    b1.pack(side=LEFT, padx=5, pady=5)
    b2 = Button(root, text='Quit', command=root.quit)
    b2.pack(side=LEFT, padx=5, pady=5)
    root.mainloop()