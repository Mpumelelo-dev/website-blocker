#importing required liberary
from tkinter import *
import tkinter as tk
from PIL import ImageTk, Image
#creating a window
window = Tk()
window.geometry('650x300')
window.minsize(650,400)
window.maxsize(650,400)

# Load the image
image = Image.open("img/bimg.png")  
background_image = ImageTk.PhotoImage(image)

# Create a label with the image
background_label = tk.Label(window, image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)



window.title(" Digital citizen Website Blocker")

# heading=Label(window, text ='Website Blocker' , font ='arial')
# heading.pack()

host_path ='C:\Windows\System32\drivers\etc\hosts'
ip_address = '127.0.0.1'
label5=Label(window, text ='Website blocker/unblocker' , font ='arial 13 bold')
label5.place(x=200 ,y=60)
label1=Label(window, text ='Enter Website :' , font ='arial 13 bold')
label1.place(x=20 ,y=160)

enter_Website = Text(window,font = 'arial',height='2', width = '40')
enter_Website.place(x= 160,y = 150)

def Blocker():
    website_lists = enter_Website.get(1.0,END)
    Website = list(website_lists.split(","))
    with open (host_path , 'r+') as host_file:
        file_content = host_file.read()
        for web in Website:
            if web in file_content:
                display=Label(window, text = 'Already Blocked' , font = 'arial')
                display.place(x=200,y=250)
                pass
            else:
                host_file.write(ip_address + " " + web + '\n')
                Label(window, text = "Blocked", font = 'arial').place(x=230,y =250)

def Unblock():
    website_lists = enter_Website.get(1.0,END)
    Website = list(website_lists.split(","))
    with open (host_path , 'r+') as host_file:
        file_content = host_file.readlines()
    for web in Website:
            if web in website_lists:
                with open (host_path , 'r+') as f:
                    for line in file_content:
                        if line.strip(',') != website_lists:
                            f.write(line)
                            Label(window, text = "Already UnBlocked", font = 'arial').place(x=350,y =250)
                            pass
                        else:
                            display=Label(window, text = 'Already UnBlocked' , font = 'arial')
                            display.place(x=350,y=250)


block_button = Button(window, text = 'Block',font = 'arial',pady = 5,command = Blocker ,width = 6, bg = 'royal blue1', activebackground = 'grey')
block_button.place(x = 230, y = 200)

unblock_button = Button(window, text = 'UnBlock',font = 'arial',pady = 5,command = Unblock ,width = 6, bg = 'royal blue1', activebackground = 'grey')
unblock_button.place(x = 350, y = 200)
window.mainloop()
