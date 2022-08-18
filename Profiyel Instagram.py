from tkinter import *
import instaloader
from urllib.request import urlopen
from PIL import Image, ImageTk
import io

def get_imag_and_information():
    L = instaloader.Instaloader()
    profile = instaloader.Profile.from_username(L.context, f"{input_user.get()}")
    a = urlopen(profile.get_profile_pic_url())
    data = a.read()
    a.close()
    image = Image.open(io.BytesIO(data))
    pic = ImageTk.PhotoImage(image)
    img.config(image=pic)
    img.image = pic
    img.place(x=100, y=260)
    followers = profile.followers
    followess = profile.followees
    Biography = profile.biography
    name = profile.full_name
    information.config(text=f"FullName: {name}\nfollowers:{followers}\nfollowing: {followess}\nBiography: {Biography}")
    information.place(x=20, y=80)

window = Tk()
window.geometry("520x600")
window.maxsize(520, 600)
window.minsize(520, 600)
window.configure(bg="red")
Label(text="Profile Insta Loder")



input_user = Entry(window, font=('arial', 13, "bold"), bd=8, width=25)
input_user.place(x=90, y=20)

btn_serche = Button(window,text="Search" , padx=15, pady=1, bd=7, fg="black", bg="yellow", command=get_imag_and_information)
btn_serche.place(x=340, y=20)

information = Button(window, padx=110, pady=40, bd=9, fg="black", font=("arial", 10, "bold"))
information.place(x=130, y=80)

img = Label(window, padx=160, pady=140)

window.mainloop()

