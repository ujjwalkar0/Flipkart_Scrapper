from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.button import MDRectangleFlatButton
from kivy.lang import Builder
import helpers
import requests
from bs4 import BeautifulSoup as bs
import urllib.request

class InstagramDownloaderApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Green"
        screen = Screen()

        self.url = Builder.load_string(helpers.url)
        self.video= Builder.load_string(helpers.video)
        button = MDRectangleFlatButton(text='Show',
                                       pos_hint={'center_x': 0.5, 'center_y': 0.4},
                                       on_release=self.show_data)
        screen.add_widget(self.url)
        screen.add_widget(self.video)
        screen.add_widget(button)
        return screen

    def show_data(self,obj):
        r2=self.url.text
        r=requests.get(r2)
        soup=bs(r.content,"html.parser")
        url = soup.find("meta",  property="og:video:secure_url")
        v=self.video.text+".mp4"
        print("hello world",r2,v)
        urllib.request.urlretrieve(url["content"], v)

InstagramDownloaderApp().run()
