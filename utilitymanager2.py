from tkinter import *
from customtkinter import *
import os, csv, time, requests, pathlib
from config import keys, logincreds, settings

set_appearance_mode("Dark")
set_default_color_theme("green")
deactivate_automatic_dpi_awareness()

print(keys['scraperapi'])

#----------------
loginpage = CTk()
loginpage.geometry("300x300")
loginpage.resizable(False, False)
loginpage.title("LOGIN - "+os.getlogin())
loginpage.bind('<Return>', lambda event:login())

#STRINGS
username = StringVar()
password = StringVar()

Administrator = StringVar(value = 'Administrator')
Guest = StringVar(value = 'Guest')
Personal = StringVar(value = 'Personal')
Owner = StringVar(value = 'Owner')
initialcustom = StringVar(value = 'Guest')

#ENTRYES
entryusername = CTkEntry(loginpage, textvariable = username).place(x = 83, y = 28)
entrypassword = CTkEntry(loginpage, textvariable = password, show = '*').place(x = 83, y = 83)

#LABELS
labelusername = CTkLabel(loginpage, text = 'Username:').place(x = 80, y = 0)
labelpassword = CTkLabel(loginpage, text = 'Password:').place(x = 80, y = 55)

#OTHER WIDGETS

#FUNCTIONS
def mainwindow():

    windowmain = CTk()
    windowmain.title("Utility Manager | "+username.get())
    windowmain.geometry("560x300")
    windowmain.resizable(False, False)

    #STRINGS
    searchstring = StringVar()

    #ENTRYES
    searchbarentry = CTkEntry(windowmain, textvariable = searchstring, width=420).place(x = 0, y = 0)

    #FUNCTIONS
    def utility1():
        utility1 = CTk()
        utility1.geometry('300x55')
        utility1.resizable(False, False)
        utility1.title('PROXY SCRAPER')

        type = StringVar()

        linklabel = CTkLabel(utility1, text = 'TYPE: ').place(x = 0, y = 0)

        def scrape(choice):

            proxies = 'proxies.txt'

            with open(proxies, 'w') as f:
                f.truncate(0)
                f.close()

            url = 'https://api.proxyscrape.com/v2/?request=displayproxies&protocol='+choice+'&timeout=10000&country=all&ssl=all&anonymity=all'

            payload={}
            headers = {}
            response = requests.request("GET", url, headers=headers, data=payload)

            with open(proxies, 'w') as f:
                f.write(response.text) 
                f.close()
            os.startfile("proxies.txt")

            utility1.destroy()

        proxytype = CTkComboBox(utility1, values = ['http', 'https', 'socks4', 'socks5'],variable = settings['proxyinitialoption'], command = scrape, width = 300).place(x = 0, y = 27)

        utility1.mainloop()

    def utility2():
        print('utility2')
    def utility3():
        print('utility3')
    def utility4():
        print('utility4')
    def utility5():
        print('utility5')
    def utility6():
        print('utility6')
    def utility7():
        print('utility7')
    def utility8():
        print('utility8')

    #BUTTONS & WIDGETS
    buttonsearch = CTkButton(windowmain, text = "Search").place(x = 420,y = 0)
    button1 = CTkButton(windowmain, text = "PROXIES", command = utility1).place(x = 0, y = 28)
    button2 = CTkButton(windowmain, text = "Utility 2", command = utility2).place(x = 0, y = 56)
    button3 = CTkButton(windowmain, text = "Utility 3", command = utility3).place(x = 140, y = 28)
    button4 = CTkButton(windowmain, text = "Utility 4", command = utility4).place(x = 140, y = 56)
    button5 = CTkButton(windowmain, text = "Utility 5", command = utility5).place(x = 280, y = 28)
    button6 = CTkButton(windowmain, text = "Utility 6", command = utility6).place(x = 280, y = 56)
    button7 = CTkButton(windowmain, text = "Utility 7", command = utility7).place(x = 420, y = 28)
    button8 = CTkButton(windowmain, text = "Utility 8", command = utility8).place(x = 420, y = 56)

    windowmain.mainloop()

#LOGIN PAGE
def login():
    if not username.get():
        messagebox.showerror('ERROR!', 'USER OR PASSWORD LABELS ARE EMPTY')
        return

    if username.get() == logincreds['username'] and password.get() == logincreds['password']:
        loginpage.destroy()
        mainwindow()
    else:
        messagebox.showerror('ERROR!', 'USER OR PASSWORD INCORRECT !')

#BUTTON
loginbutton = CTkButton(loginpage, text = 'LOGIN', command = login, fg_color = "purple").place(x = 83, y = 125)

loginpage.mainloop()
