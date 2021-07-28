import requests
from bs4 import BeautifulSoup
from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivy.lang import Builder
from kivymd.uix.button import MDRectangleFlatButton, MDFlatButton
from kivymd.uix.dialog import MDDialog

username_helper = """
MDTextField :
    hint_text: "Enter product url"
    pos_hint: {"center_x" : 0.5, "center_y" : 0.8}
    size_hint_x:None
    width : 300 
    
"""
headers = {
        "User-Agent": ' '       # Copy And Paste your User-Agent 
}


class Amazon_price_trackerApp(MDApp):

    def build(self):
        screen = Screen()
        button = MDRectangleFlatButton(text="Get Product Price", pos_hint={"center_x": 0.5, "center_y": 0.7},
                                       on_release=self.show_data)
        self.username = Builder.load_string(username_helper)
        screen.add_widget(self.username)
        screen.add_widget(button)
        return screen


     def show_data(self, obj):
        close_buttons = MDFlatButton(text="Close", on_release=self.close_dialog)
        more_buttons = MDFlatButton(text="More")
        url = self.username.text
        if "amazon.in" in url:
            page = requests.get(url, headers=headers)
            soup = BeautifulSoup(page.content, "html.parser")
            price = soup.find(id="priceblock_dealprice")
            if price == None:
                price = soup.find(id="priceblock_ourprice")
            final_price = price.getText()
        elif "flipkart.com" in url:
            page = requests.get(url, headers=headers)
            soup = BeautifulSoup(page.content, "html.parser")
            price = soup.find("div", {"class", "_30jeq3 _16Jk6d"})
            final_price = price.getText()

        self.dialog = MDDialog(title="Product price", text=final_price,
                               size_hint=(0.5, 1),
                               buttons=[close_buttons, more_buttons])
        self.dialog.open()

    def close_dialog(self, obj):
        self.dialog.dismiss()


Amazon_flipkart_price_track().run()




