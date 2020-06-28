from bs4 import BeautifulSoup
import bs4
import requests,re
from tkinter import *
root = Tk()
root.config(bg="black")
root.geometry('400x200')
root.title('Corona Cases Detector')
Label(text='Corona cases detector',font=20).pack(fill=BOTH,pady=10)
def searchcases():
    res = requests.get("https://www.worldometers.info/coronavirus/")
    print('success')
    soup = bs4.BeautifulSoup(res.text, 'lxml')
    hi = soup.select('title')
    p=hi[0].getText().replace(',','')
    temp = re.findall(r'\d+', p)
    res = list(map(int, temp))
    Label(text=f"Total {res[0]} \nDeath {res[1]} \nRecovered {res[2]}",font=20).place(y=50,x=150)
    # Label(text=f"ACTIVE CASES {res[0]} \nCLOSED CASES {res[1]} ",font=20).place(y=70,x=170)
Button(text="Search",font=10,command=searchcases).place(x=20,y=50)
root.mainloop()
