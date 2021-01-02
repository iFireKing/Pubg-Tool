from sys import exit
from requests import get
from pytube import YouTube
from tkinter import *
from tkinter import messagebox


version = "0.2"


def checkforupdates():
    try:
        gitversion = get("https://raw.githubusercontent.com/iFireKing/Youtube-Downloader/main/verison.txt").text
        if f'{version}\n' != gitversion:
            messagebox.showwarning(f"New Update {gitversion}V",
                                   f"Your version is old.\nYour version: {version}\nLatest version: {gitversion}\nGet "
                                   f"latest version in the link "
                                   f"below\nhttps://github.com/iFireKing/Youtube-Downloader/releases/tag "
                                   f"/{version}")

        exit(0)
    except:
        exit(0)


if f'{version}\n' != get("https://raw.githubusercontent.com/iFireKing/Youtube-Downloader/master/verison.txt").text:
    checkforupdates()
else:
    app = Tk()
    app.title(f"Youtube Downloader-{version}V")
    app.geometry("1200x250")
    Label(app, text="Put Your Link", height=2, font=("Arial", 20)).pack()
    link = StringVar()
    link.set("Link")
    Entry(app, width=55, font=("Arial", 30), textvariable=link).pack()
    Label(app, text="By FireKing", height=2, font=("Arial", 20)).pack()


    def Download():
        adv = link.get()
        vi = YouTube(adv).streams.filter(progressive=True, file_extension='mp4').get_by_itag("22")
        vi.download()
        messagebox.showinfo("Success", "Downloaded Has Done!")


    Button(app, text="Download", width=20, height=2, bg="#e91e63", fg="white", borderwidth=1,
           command=Download).pack()

    app.resizable(False, False)
    app.mainloop()
