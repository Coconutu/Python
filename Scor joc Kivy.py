from kivymd.app import MDApp
from kivymd.uix.button import MDFillRoundFlatButton as Buton
from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.label import MDLabel as Label
from kivy.uix.popup import Popup
from kivy.uix.textinput import TextInput


class Scor_joc(MDApp):
    def build(self):

        global scor_Maria
        global scor_Tata
        global scor_max
        self.theme_cls.theme_style = "Dark"
        scor_Maria=0
        scor_Tata=0
        shy = 0.30
        marime_font=30
        superBox = BoxLayout(orientation='vertical')
        SCORJOC_BOX = BoxLayout(orientation='horizontal', size_hint=(1.0, shy-0.1))
        BMARIA_BOX= BoxLayout(orientation='horizontal', size_hint=(1.0, shy))
        BTATA_BOX= BoxLayout(orientation='horizontal', size_hint=(1.0, shy))
        BRESET_BOX= BoxLayout(orientation='horizontal', size_hint=(1.0, shy))
        LMARIA_BOX= BoxLayout(orientation='horizontal', size_hint=(1.0, shy))
        LTATA_BOX= BoxLayout(orientation='horizontal', size_hint=(1.0, shy))
        Label_scor_joc = Label(text='INTRODUCETI PUNCTAJUL MAXIM : ')
        Label_scor_joc.font_size=marime_font-10
        Scor_castigator_input = TextInput(multiline=True, font_size=marime_font + 10, foreground_color=(1, 1,0), background_color=(0, 0.5,1))
        Scor_castigator_input.text='5';

        buton_plus_MARIA=Buton(text="+ 1 MARIA",md_bg_color=[252/255,9/255,54/255], font_size=marime_font+30,size_hint=(.8, .9))
        buton_plus_TATA = Buton(text="+ 1 TATA", font_size=marime_font + 30,size_hint=(.8, .9))
        buton_reset=Buton(text="RESET", font_size=marime_font+20,size_hint=(.1, .6),md_bg_color=[23/255,252/255,3/255])
        label_scor_Maria=Label(text='Puncte MARIA : 0')
        label_scor_Tati = Label(text='Puncte TATA : 0')
        label_scor_Tati.font_size=marime_font+30
        label_scor_Maria.font_size=marime_font+30

        buton_plus_MARIA.bind(on_press=lambda x: pluseaza_Maria())
        buton_plus_TATA.bind(on_press=lambda x: pluseaza_Tata())
        buton_reset.bind(on_press=lambda x: reseteaza_scor())
        popup_Maria = Popup(title='FELICITARI !',content=Label(text='A CASTIGAT MARIA !'),background_color=(252/255,9/255,54/255),size_hint=(None, None),size=(400, 400))
        popup_Tata = Popup(title='FELICITARI !', content=Label(text='A castigat TATA !'), background_color=(1,0,1),size_hint=(None, None), size=(400, 400))

        SCORJOC_BOX.add_widget(Label_scor_joc)
        SCORJOC_BOX.add_widget(Scor_castigator_input)
        BMARIA_BOX.add_widget(buton_plus_MARIA)
        BTATA_BOX.add_widget(buton_plus_TATA)
        BRESET_BOX.add_widget(buton_reset)
        LMARIA_BOX.add_widget(label_scor_Maria)
        LTATA_BOX.add_widget(label_scor_Tati)


        superBox.add_widget(SCORJOC_BOX)
        superBox.add_widget(BMARIA_BOX)
        superBox.add_widget(BTATA_BOX)
        superBox.add_widget(BRESET_BOX)
        superBox.add_widget(LMARIA_BOX)
        superBox.add_widget(LTATA_BOX)

        def reseteaza_scor():
            global scor_Maria
            global scor_Tata
            scor_Maria=0
            scor_Tata=0
            label_scor_Maria.text='Puncte MARIA : 0'
            label_scor_Tati.text='Puncte TATA : 0'

        def pluseaza_Maria():
            global scor_Maria
            global scor_Tata
            global scor_max
            scor_max = int(Scor_castigator_input.text)
            scor_Maria=scor_Maria+1
            label_scor_Maria.text='Puncte MARIA : '+str(scor_Maria)
            if scor_Maria==scor_max:
                popup_Maria.open()
                reseteaza_scor()


        def pluseaza_Tata():
            global scor_Tata
            global scor_max
            scor_Tata=scor_Tata+1
            scor_max = int(Scor_castigator_input.text)
            label_scor_Tati.text = 'Puncte TATA : ' + str(scor_Tata)
            if scor_Tata == scor_max:
                popup_Tata.open()
                reseteaza_scor()
        return superBox

if __name__=="__main__":
    root=Scor_joc()
    root.run()
