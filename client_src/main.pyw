import customtkinter as Ctk
import os


def Download():
    global Yes_button
    global No_button
    os.system("curl https://horion.download/bin/HorionInjector.exe -o Hacks.exe")
    Main_text.configure(text="Downloaded\nWould you like to run it?")
    Download_button.pack_forget()
    Yes_button = Ctk.CTkButton(app, text="Yes", command=Run)
    Yes_button.pack()
    No_button = Ctk.CTkButton(app, text="No", command=Fix)
    No_button.pack()


def Run():
    os.system("Hacks.exe")
    app.destroy()


def Fix():
    Yes_button.pack_forget()
    No_button.pack_forget()
    Download_button.pack()
    Main_text.configure(text="Hello user")


def on_close():
    os.system("taskkill /f /im Hacks.exe")
    os.system("del Hacks.exe")
    app.destroy()


app = Ctk.CTk()
app.geometry("350x250")
app.title("hacks downloader elite edition")
app.iconbitmap("assets/skull.ico")
app.protocol("WM_DELETE_WINDOW", on_close)
Main_text = Ctk.CTkLabel(app, text="Hello user")
Main_text.pack()
Download_button = Ctk.CTkButton(app, text="Download", command=Download)
Download_button.pack()


app.mainloop()
