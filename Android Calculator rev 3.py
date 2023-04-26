#pylint:disable=C0301
# pylint:disable=W0123
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label


expresie = ''
valoare=0
erase = False

class Calculator(App):

    def build(self):
        global x
        marime_font = 60
        shy=0.30
        red=0
        green=0.5
        blue=1
        superBox = BoxLayout(orientation='vertical')
        HBR = BoxLayout(orientation='horizontal',size_hint=(1.0,shy))
        HBM = BoxLayout(orientation='horizontal',size_hint=(1.0,shy))
        HB0 = BoxLayout(orientation='horizontal')
        HB1 = BoxLayout(orientation='horizontal',size_hint=(1.0,shy))
        HB2 = BoxLayout(orientation='horizontal',size_hint=(1.0,shy))
        HB3 = BoxLayout(orientation='horizontal',size_hint=(1.0,shy))
        HB4 = BoxLayout(orientation='horizontal',size_hint=(1.0,shy))
        Ecran = TextInput(multiline=True, font_size=marime_font + 20, foreground_color=(1, 0.9,0.1), background_color=(red, green, blue))
        Rezultat = Label(text='', font_size=marime_font + 20)
        b7 = Button(text="7", font_size=marime_font)
        b7.bind(on_press=lambda x: scrie('7'))
        b8 = Button(text='8', font_size=marime_font)
        b8.bind(on_press=lambda x: scrie('8'))
        b9 = Button(text='9', font_size=marime_font)
        b9.bind(on_press=lambda x: scrie('9'))
        b_inmultire = Button(text='X', font_size=marime_font)
        b_inmultire.bind(on_press=lambda x: scrie('*'))
        b4 = Button(text='4', font_size=marime_font)
        b4.bind(on_press=lambda x: scrie('4'))
        b5 = Button(text='5', font_size=marime_font)
        b5.bind(on_press=lambda x: scrie('5'))
        b6 = Button(text='6', font_size=marime_font)
        b6.bind(on_press=lambda x: scrie('6'))
        b_minus = Button(text='-', font_size=marime_font + 10)
        b_minus.bind(on_press=lambda x: scrie('-'))
        b1 = Button(text='1', font_size=marime_font)
        b1.bind(on_press=lambda x: scrie('1'))
        b2 = Button(text='2', font_size=marime_font)
        b2.bind(on_press=lambda x: scrie('2'))
        b3 = Button(text='3', font_size=marime_font)
        b3.bind(on_press=lambda x: scrie('3'))
        b_plus = Button(text='+', font_size=marime_font + 10)
        b_plus.bind(on_press=lambda x: scrie('+'))
        b0 = Button(text='0', font_size=marime_font)
        b0.bind(on_press=lambda x: scrie('0'))
        b_virgula = Button(text='.', font_size=marime_font)
        b_virgula.bind(on_press=lambda x: scrie('.'))
        b_egal = Button(text='=', font_size=marime_font + 10)
        b_egal.bind(on_press=lambda x: apasa_egal())
                            
        b_rdeschis = Button(text='(', font_size=marime_font)
        b_rdeschis.bind(on_press=lambda x: scrie('('))
        b_rinchis = Button(text=')', font_size=marime_font)
        b_rinchis.bind(on_press=lambda x: scrie(')'))
        b_impartire = Button(text='/', font_size=marime_font)
        b_impartire.bind(on_press=lambda x: scrie('/'))
        b_reset = Button(text='CE', font_size=marime_font)
        b_reset.bind(on_press=lambda x: curataecran())
        b_backspace = Button(text='<-', font_size=marime_font)
        b_backspace.bind(on_press=lambda x: backspace())
        bmplus = Button(text='M+', font_size=marime_font)
        bmplus.bind(on_press=lambda x: mPlus())
        bmmr = Button(text='MR', font_size=marime_font)
        bmmr.bind(on_press=lambda x: mR())
        b_cat = Button(text='CAT \nIMP. (//)', font_size=marime_font-10, halign='center')
        b_cat.bind(on_press=lambda x: scrie('//'))
        b_rest = Button(text='REST \n IMP. (%)', font_size=marime_font -10, halign='center')
        b_rest.bind(on_press=lambda x: scrie('%'))
        b_ridputere = Button(text='X^Y',font_size=marime_font - 5, halign='center')
        b_ridputere.bind(on_press=lambda x: scrie('**'))
        HB0.add_widget(Ecran)
        HBR.add_widget(Rezultat)
        HBM.add_widget(bmplus)
        HBM.add_widget(bmmr)
        HBM.add_widget(b_reset)
        HBM.add_widget(b_backspace)
        HBM.add_widget(b_ridputere)
        HB1.add_widget(b7)
        HB1.add_widget(b8)
        HB1.add_widget(b9)
        HB1.add_widget(b_cat)
        HB1.add_widget(b_rest)
        HB2.add_widget(b4)
        HB2.add_widget(b5)
        HB2.add_widget(b6)
        HB2.add_widget(b_rdeschis)
        HB2.add_widget(b_rinchis)
        HB3.add_widget(b1)
        HB3.add_widget(b2)
        HB3.add_widget(b3)
        HB3.add_widget(b_minus)
        HB3.add_widget(b_plus)
        HB4.add_widget(b_virgula)
        HB4.add_widget(b0)
        HB4.add_widget(b_impartire)
        HB4.add_widget(b_inmultire)
        
        HB4.add_widget(b_egal)
        superBox.add_widget(HB0)
        superBox.add_widget(HBR)
        superBox.add_widget(HBM)
        superBox.add_widget(HB1)
        superBox.add_widget(HB2)
        superBox.add_widget(HB3)
        superBox.add_widget(HB4)

        def scrie(text):
            global expresie
            global erase
            if erase == True:
                curataecran()
                erase = False
            expresie = expresie + text
            Ecran.text = expresie
            calculeaza()

        def curataecran():
            global expresie
            Ecran.text = ''
            expresie = ''
            Rezultat.text = ''

        def backspace():
            global expresie
            expresie = expresie[:-1]
            Ecran.text = expresie

        def calculeaza():
            global erase
            global expresie
            global raspuns
            try:
                raspuns = eval(expresie)
                Rezultat.text ='='+ f'{raspuns:,}'.replace(',', ' ')
                raspuns = str(raspuns)
            except:
                Rezultat.text = ''

        def apasa_egal():
            global erase
            global expresie
            global raspuns
            try:
                raspuns = eval(expresie)
                Rezultat.text ='='+f'{raspuns:,}'.replace(',', ' ')
                raspuns=str(raspuns)
                erase = True
            except:
                Rezultat.text = ''

        def mPlus():
            global raspuns
            global valoare
            valoare = raspuns

        def mR():
            global raspuns
            try:
                scrie(valoare)
            except:
                Rezultat.text = ''

        return superBox

root = Calculator()
root.run()

