from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button

class Fereastra(GridLayout):
    def __init__(self,**kwargs):
        super(Fereastra,self).__init__(**kwargs)
        self.cols=2
        self.add_widget(Label(text='coconutu'))
        self.add_widget(Label(text='reali'))
        self.add_widget(Button(text="Buton stanga"))
        self.add_widget(Button(text='Buton dreapta'))

class MyApp(App):
    def build(self):
        return Fereastra()

if __name__=='__main__':
    MyApp().run()