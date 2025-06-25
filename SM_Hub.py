# import gpiozero
import requests
from tkinter import *
#mport tkinter as Tk
import time
from PIL import ImageTk, Image, ImageOps
import constants # API KEYS
# This is my custom Smart Home Hub written in python


time_format = 12

# news_country_code = 'us'
date_format = "%b %d, %Y"
latitude = '35.962639'
longitude = '-83.916718'
xlarge_text_size = 94
large_text_size = 48
medium_text_size = 28
small_text_size = 18
very_small_text_size = 10


BASE_BG = "#3F3F3F"
BASE_FG = "#FFD700"

class Clock(Frame):
    def __init__(self, parent):
        super().__init__(parent, bg=BASE_BG)
        self.time1 = ''
        self.timeLbl = Label(self, font=('Helvetica', large_text_size), fg=BASE_FG, bg=BASE_BG)
        self.timeLbl.pack(side=TOP, anchor=E)
        # initialize day of week
        self.day_of_week1 = ''
        self.dayOWLbl = Label(self, text=self.day_of_week1, font=('Helvetica', medium_text_size), fg=BASE_FG, bg=BASE_BG)
        self.dayOWLbl.pack(side=TOP, anchor=E)
        # initialize date label
        self.date1 = ''
        self.dateLbl = Label(self, text=self.date1, font=('Helvetica', small_text_size), fg=BASE_FG, bg=BASE_BG)
        self.dateLbl.pack(side=TOP, anchor=E)
        self.tick()

    def tick(self):
        if time_format == 12:
            time2 = time.strftime('%I:%M %p')

        else:
            time2 = time.strftime('%H:%M')

        day_of_week2 = time.strftime('%A')
        date2 = time.strftime(date_format)
        if time2 != self.time1:
            self.time1 = time2
            self.timeLbl.config(text=time2)
        if day_of_week2 != self.day_of_week1:
            self.day_of_week1 = day_of_week2
            self.dayOWLbl.config(text=day_of_week2)
        if date2 != self.date1:
            self.date1 = date2
            self.dateLbl.config(text=date2)

        self.timeLbl.after(200, self.tick)

class Weather(Frame):
    def __init__(self, parent):
        super().__init__(parent, bg=BASE_BG)
        self.temp = None
        self.currently = ''
        self.forecast = ''
        self.location = 'Knoxville, US'
        self.degreeFrm = Frame(self, bg=BASE_BG)
        self.degreeFrm.pack(side=LEFT, anchor=E)
        self.TempLbl = Label(self.degreeFrm, font=("Helvetica", large_text_size), fg=BASE_FG, bg=BASE_BG)
        self.TempLbl.pack(side = LEFT, anchor = W, padx=10)
        self.CurrentlyLbl = Label(self, font=('Helvetica', medium_text_size), fg=BASE_FG, bg= BASE_BG)
        self.CurrentlyLbl.pack(side = TOP, anchor = W)
        self.LoactionLbl = Label(self, text=self.location, font=('Helvetica', small_text_size), fg=BASE_FG, bg=BASE_BG)
        self.LoactionLbl.pack(side = LEFT, anchor = E)
        self.ForecastLbl = Label(self, font= ("Helvetica", small_text_size), fg=BASE_FG, bg=BASE_BG)
        self.ForecastLbl.pack(side = TOP, anchor = E)
        #self.get_weather()

    def get_weather(self):
        exclude = ['minutely', 'hourly']
        req_url = "https://api.openweathermap.org/data/2.5/onecall?lat=%s&lon=%s&exclude=%s&appid=%s" % (latitude, longitude, exclude, constants.WEATHER_API_KEY)
        params = {'units': 'imperial'}
        try:
            req = requests.request(url = req_url, params=params, method = 'get')
            response = req.json()
            degree_sign = u'\N{DEGREE SIGN}'
            temp2 = '%s%s' % (round(int(response['current']['temp'])), degree_sign)
            currently2 = response['current']['weather'][0]['main']

            while True:
                forecast2 = [response['daily'][0]['weather'][0]['description']]

                for i in range(1, 7):

                    forecast2.append(response['daily'][i]['weather'][0]['description'])

                break


            if self.temp != temp2:
                self.temp = temp2
                self.TempLbl.config(text=temp2)
            if self.currently != currently2:
                self.currently = currently2
                self.CurrentlyLbl.config(text=currently2)

        except Exception as e:
            print(e)
            print("Error getting Weather")
            #exit(0)
        self.after(600000, self.get_weather)

class News(Frame):
    def __init__(self, parent):
        super().__init__(parent, bg=BASE_BG)
        self.headlines = []
        self.newsLbl = Label(self, text="News", font=("Helvetica", large_text_size), bg=BASE_BG, fg=BASE_FG)
        self.newsLbl.pack(side=TOP)
        self.headlineFrm = Frame(self, bg= BASE_BG)
        self.headlineFrm.pack(side=TOP)
        self.get_headlines()

    def get_headlines(self):
        headlineReq = requests.get("https://newsapi.org/v2/top-headlines?country=us&apiKey=%s" % constants.NEWS_API_KEY)
        self.headline_json = headlineReq.json()
        # self.headline_json["articles"][i]["title"]
        # print(self.headlines)
        self.head1Lbl = Label(self, text=self.headline_json["articles"][5]["title"], font=("Helvetica", 10),bg=BASE_BG, fg=BASE_FG)
        self.head1Lbl.pack(side=BOTTOM)
        self.head2Lbl = Label(self, text=self.headline_json["articles"][4]["title"], font=("Helvetica", 10),bg=BASE_BG, fg=BASE_FG)
        self.head2Lbl.pack(side=BOTTOM)
        self.head3Lbl = Label(self, text=self.headline_json["articles"][3]["title"], font=("Helvetica", 10),bg=BASE_BG, fg=BASE_FG)
        self.head3Lbl.pack(side=BOTTOM)
        self.head4Lbl = Label(self, text=self.headline_json["articles"][2]["title"], font=("Helvetica", 10),bg=BASE_BG, fg=BASE_FG)
        self.head4Lbl.pack(side=BOTTOM)
        self.head5Lbl = Label(self, text=self.headline_json["articles"][1]["title"], font=("Helvetica", 10),bg=BASE_BG, fg=BASE_FG)
        self.head5Lbl.pack(side=BOTTOM)
        self.head6Lbl = Label(self, text=self.headline_json["articles"][0]["title"], font=("Helvetica", 10),bg=BASE_BG, fg=BASE_FG)
        self.head6Lbl.pack(side=BOTTOM)

class Menu(Frame):
    def __init__(self, parent):
        super().__init__(parent, bg=BASE_BG)
        self.img = Image.open('images/home.png')
        self.img = self.img.convert("RGB")
        self.img = ImageOps.invert(self.img)
        self.img = self.img.resize((50, 50))
        self.img = ImageTk.PhotoImage(self.img, Image.Resampling.LANCZOS)
        self.btn = Button(self, image=self.img, command=self.Clicked, fg = BASE_BG, bg = BASE_BG)
        self.btn.pack(side= BOTTOM)
    def Clicked(self):
       # Create stage
       self.menuLbl = Label(self, text = "         Menu         ",font= ("Helvetica", large_text_size), bg= BASE_BG, fg = BASE_FG)
       # Return button should be on the bottom
       self.ledBtn = Button(self, font=("Helvetica", small_text_size), bg=BASE_BG, text="Lighting", command=self.lightCtrl)
       self.returnBtn = Button(self, font=("Helvetica", very_small_text_size), bg = BASE_BG,text= "Return", command=self.menuDelete)

       # Pack stage
       self.menuLbl.pack(side = TOP, anchor = E)
       self.returnBtn.pack(side = BOTTOM)
       self.btn.pack_forget()
    def menuDelete(self):
        # Unpacks menu items and return label
        self.menuLbl.pack_forget()
        self.returnBtn.pack_forget()
        self.btn.pack()
    def lightCtrl(self):
        pass

class Window():
    def __init__(self):
        self.tk = Tk()
        self.tk.title("Hub")
        #self.iconphoto(False, ImagePhotoImage(file="home.png"))
        self.tk.configure(bg=BASE_BG)
        self.topFrame = Frame(self.tk, bg=BASE_BG)
        self.bottomFrame = Frame(self.tk, bg=BASE_BG)
        #self.centerFrame = Frame(self, bg=BASE_BG)
        self.topFrame.pack(side= TOP, fill = BOTH, expand = YES)
        self.bottomFrame.pack(side = BOTTOM, fill = BOTH, expand = YES)
        #self.centerFrame.pack(side = TOP, fill = BOTH, expand = YES)
        self.state = False
        self.tk.bind("<Return>", self.toggle_fullscreen)
        self.tk.bind("<Escape>", self.end_fullscreen)
        # Menu Button
        self.button = Menu(self.topFrame)
        self.button.pack(side = RIGHT, anchor = NE)
        # Clock
        self.clock = Clock(self.topFrame)
        self.clock.pack(side = LEFT, anchor = N, padx=40, pady=40)
        # Weather
        self.weather = Weather(self.topFrame)
        self.weather.pack(side=RIGHT, anchor=N, padx=40, pady=40)
        # News
        self.News = News(self.bottomFrame)
        self.News.pack(side = RIGHT, anchor = SE, padx = 40, pady = 40)
        
    def toggle_fullscreen(self, event=None):
        self.state = not self.state  # Just toggling the boolean
        self.tk.attributes("-fullscreen", self.state)
        return "break"

    def end_fullscreen(self, event=None):
        self.state = False
        self.tk.attributes("-fullscreen", False)
        return "break"
    def run(self):
        self.tk.mainloop()

if __name__ == '__main__':
    w = Window()
    w.run()
