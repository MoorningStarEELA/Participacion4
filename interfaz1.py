from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button


class Firstapp(App):
    def build(self):
        btn1=  Button(text='Subir archivo',font_size=30,size_hint=(0.5,0.2),pos=(250,250),background_color='blue')
        return btn1
    

        

if __name__ == "__main__":
    Firstapp().run()
