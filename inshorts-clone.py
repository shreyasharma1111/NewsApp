import os
import requests
import io
import webbrowser
from tkinter import *
from urllib.request import urlopen
from PIL import Image, ImageTk
from datetime import datetime
from dotenv import load_dotenv

class NewsApp:
    def __init__(self):
        # 1. fetch data, 2. initial gui load, 3. load the first news item
        self.data=requests.get(f'https://newsapi.org/v2/everything?q=India&language=en&apiKey=e3a48c8d05ee42f69e970e3990228d34').json()
        #print(data) to check whether json is output or not
        #to load newest news first:
        # self.data['articles'].sort(key=lambda x: datetime.fromisoformat(x['publishedAt'].replace('Z','')),reverse=True)
        self.loadGUI()
        self.load_news_item(0)

    def loadGUI(self):
        self.root=Tk()
        self.root.geometry('350x600')
        self.root.resizable(0,0)
        self.root.title("News Inshorts")
        self.root.config(bg='black')

    def clear(self):
        for i in self.root.pack_slaves():
            i.destroy()    

    def load_news_item(self, index):
        self.clear()  #clear the screen for next news item
        try:
            img_url=self.data['articles'][index]['urlToImage']
            raw_data=urlopen(img_url).read()
            im=Image.open(io.BytesIO(raw_data)).resize((350,250))
            photo=ImageTk.PhotoImage(im)        
            label=Label(self.root, image=photo)
            label.pack(pady=2, padx=2)
        except:
            img_url='https://jcrsj.wlulaw.wlu.edu/wp-content/uploads/2018/10/placeholder.jpg'   #to load a default image where image cannot be loaded
            raw_data=urlopen(img_url).read()
            im=Image.open(io.BytesIO(raw_data)).resize((350,250))
            photo=ImageTk.PhotoImage(im)        
            label=Label(self.root, image=photo)
            label.pack(pady=2, padx=2)

        heading=Label(self.root, text=self.data['articles'][index]['title'], bg='black', fg='white', wraplength=300, justify='center')
        heading.pack(pady=(20,30))
        heading.config(font=('Cambria', 14))

        details=Label(self.root, text=self.data['articles'][index]['description'], bg='black', fg='white', wraplength=330, justify='left')
        details.pack(pady=(2,20))
        details.config(font=('Cambria', 12))

        frame=Frame(self.root, bg='black')
        frame.pack(expand=True, fill='both')

        if index!=0:
            prev=Button(frame, text='Prev', width=16, height=3, highlightcolor='yellow', command=lambda :self.load_news_item(index-1))
            prev.pack(side='left')

        read_more=Button(frame, text='Read More', width=16, height=3, highlightcolor='yellow', command=lambda :self.open_link(self.data['articles'][index]['url']))
        read_more.pack(side='left')

        if index!=len(self.data['articles'])-1:
            next=Button(frame, text='Next', width=16, height=3, highlightcolor='yellow', command=lambda :self.load_news_item(index+1))
            next.pack(side='left')

        self.root.mainloop()
    
    def open_link(self, url):
        webbrowser.open(url)
    
obj=NewsApp()