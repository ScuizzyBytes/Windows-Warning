from tkinter import messagebox

import customtkinter as ctk

root = ctk.CTk()

root.geometry("500x400")
root.title("Make a Windows Sound")

root.attributes("-alpha", 0.85)

def make_winsound():
    label = entry1.get().strip()
    label2 = entry2.get().strip()

    messagebox.showwarning(label, label2)
    

label =  ctk.CTkLabel(root, text="Name of the Title: ", font=("Arail", 25, "bold")).place(x= 140, y= 20)

entry1 = ctk.CTkEntry(root, font=("Arial", 25, "bold"), width=300, height= 40)
entry1.place(x= 96, y= 70)

label1 =  ctk.CTkLabel(root, text="Wriete text for the Sound: ", font=("Arail", 25, "bold")).place(x= 110, y= 160)

entry2 = ctk.CTkEntry(root, font=("Arial", 25, "bold"), width=300, height= 40)
entry2.place(x= 96, y=210)

Button = ctk.CTkButton(root, text="Click!", font=("Arial", 25, "bold"), width=300, height= 60, command= make_winsound)
Button.place(x= 90, y= 300) 

root.mainloop()
