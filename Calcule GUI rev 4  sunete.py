from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.popup import Popup
import random
import winsound



class Matematica(App):
    def genereaza_expresie(self):
        global expresie
        expresie=''
        a = random.randint(7, 10)
        b = random.randint(0, 6)
        int_semn = random.randint(0, 1)
        if int_semn == 0:
            semn = '+'
        else:
            semn = '-'
        expresie = str(a) + semn + str(b)

        return expresie


    def build(self):
        global expresie
        global puncte
        global incercari
        puncte=0
        incercari=0
        marime_font=60
        Container_principal=BoxLayout(orientation='vertical')
        Container1=BoxLayout(orientation='horizontal', size_hint=(1.0, 0.1))
        Container2=BoxLayout(orientation='horizontal', size_hint=(1.0, 0.1))
        Container3=BoxLayout(orientation='vertical', size_hint=(1.0, 0.6))
        Container_taste1=BoxLayout(orientation='horizontal', size_hint=(1.0, 0.1))
        Container_taste2 = BoxLayout(orientation='horizontal', size_hint=(1.0, 0.1))
        eticheta_titlu=Label(text='Adunări si scăderi',pos_hint={'center_x':0.5,'center_y':0.5},
                             font_size=marime_font,color='blue')

        self.genereaza_expresie()
        eticheta_expresie=Label(text=expresie+'=',pos_hint={'center_x': 0.5, 'center_y': 0.5},
                                font_size=marime_font+20,color='yellow')
        eticheta_corect = Label(text='',pos_hint={'center_x': 0.5, 'center_y': 0.5},font_size=marime_font+10)
        eticheta_punctaj=Label(text=f'Puncte : {puncte}',pos_hint={'center_x': 0.5, 'center_y': 0.5},
                               font_size=marime_font+30,color='yellow')
        rezultat = Label(text='',font_size=marime_font+20)

        buton_verifica=Button(text='<_|',font_size=marime_font,background_color='green')
        buton_verifica.bind(on_press=lambda x: verifica())

        b0 = Button(text='0', font_size=marime_font,background_color='cyan')
        b0.bind(on_press=lambda x: scrie(str('0')))
        b1 = Button(text='1', font_size=marime_font,background_color='cyan')
        b1.bind(on_press=lambda x: scrie(str('1')))
        b2 = Button(text='2', font_size=marime_font,background_color='cyan')
        b2.bind(on_press=lambda x: scrie(str('2')))
        b3 = Button(text='3', font_size=marime_font,background_color='cyan')
        b3.bind(on_press=lambda x: scrie(str('3')))
        b4 = Button(text='4', font_size=marime_font,background_color='cyan')
        b4.bind(on_press=lambda x: scrie(str('4')))
        b5 = Button(text='5', font_size=marime_font,background_color='cyan')
        b5.bind(on_press=lambda x: scrie(str('5')))
        b6 = Button(text='6', font_size=marime_font,background_color='cyan')
        b6.bind(on_press=lambda x: scrie(str('6')))
        b7 = Button(text='7', font_size=marime_font,background_color='cyan')
        b7.bind(on_press=lambda x: scrie(str('7')))
        b8 = Button(text='8', font_size=marime_font,background_color='cyan')
        b8.bind(on_press=lambda x: scrie(str('8')))
        b9 = Button(text='9', font_size=marime_font,background_color='cyan')
        b9.bind(on_press=lambda x: scrie(str('9')))
        b_sterge = Button(text='<-', font_size=marime_font,background_color='red')
        b_sterge.bind(on_press=lambda x: sterge())

        Container_taste1.add_widget(b0)
        Container_taste1.add_widget(b1)
        Container_taste1.add_widget(b2)
        Container_taste1.add_widget(b3)
        Container_taste1.add_widget(b4)
        Container_taste1.add_widget(b_sterge)
        Container_taste2.add_widget(b5)
        Container_taste2.add_widget(b6)
        Container_taste2.add_widget(b7)
        Container_taste2.add_widget(b8)
        Container_taste2.add_widget(b9)

        Container_taste2.add_widget(buton_verifica)

        eticheta_titlu.font_size=marime_font
        Container1.add_widget(eticheta_titlu)
        Container2.add_widget(eticheta_expresie)
        Container2.add_widget(rezultat)

        Container3.add_widget(eticheta_corect)
        Container3.add_widget(eticheta_punctaj)

        Container_principal.add_widget(Container1)
        Container_principal.add_widget(Container2)
        Container_principal.add_widget(Container_taste1)
        Container_principal.add_widget(Container_taste2)
        Container_principal.add_widget(Container3)

        def guinea_fericit():
            try:

                filename = 'guinea_fericit.wav'
                winsound.PlaySound(filename, winsound.SND_FILENAME)


            except:
                pass
        def guinea_suparat():
            try:
                filename = 'guinea_suparat.wav'
                winsound.PlaySound(filename, winsound.SND_FILENAME)

            except:
                pass
        def verifica():
            global puncte
            global incercari

            if str(eval(expresie)) == rezultat.text:
                guinea_fericit()
                eticheta_corect.color = 'green'
                eticheta_corect.text=f'CORECT!\n{expresie} = {eval(expresie)}\nAi +1 punct!'
                puncte=puncte+1
                eticheta_punctaj.text='Puncte : '+str(puncte)+'/10'
                rezultat.text=''
            else:
                guinea_suparat()
                eticheta_corect.color='red'
                eticheta_corect.text = f'GREȘIT!\n{expresie} = {eval(expresie)}\n'
                eticheta_punctaj.text = 'Puncte : ' + str(puncte)+'/10'
                rezultat.text = ''
            incercari = incercari + 1
            if incercari==10:
                if puncte>8:
                    mesaj = Popup(title='FELICITARI :', content=Label(text=f'Ai facut {puncte} din 10!'),
                                    background_color=(252 / 255, 9 / 255, 54 / 255), size_hint=(None, None),
                                    size=(400, 400))
                else:
                    mesaj = Popup(title='REZULTATE :', content=Label(text=f'Ai facut {puncte} din 10!'),
                              background_color=(252 / 255, 9 / 255, 54 / 255), size_hint=(None, None),
                              size=(400, 400))
                mesaj.open()
                puncte=0
                eticheta_punctaj.text = 'Puncte : ' + str(puncte) + '/10'
                eticheta_corect.color='yellow'
                eticheta_corect.text='Incepe alt joc!'
                incercari=0

            else:
                self.genereaza_expresie()

            eticheta_expresie.text=expresie+'='
        def scrie(x):
            rezultat.text=rezultat.text+x
        def sterge():
            rezultat.text=rezultat.text[:-1]

        return Container_principal

if __name__=='__main__':
    mate=Matematica()
    mate.run()
