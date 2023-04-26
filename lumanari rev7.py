from tkinter import *
from tkinter import ttk
import datetime
from datetime import date


w=Tk()
w.title('Biserica Cermei')
width=w.winfo_screenwidth()
height=w.winfo_screenheight()
w.geometry(f'{width}x{height}')
pret_lum_mica=1
pret_lum_mare=3
pret_liturghie_prescuri=10
pret_cult_pe_persoana=50
nr_lum_mici=0
nr_lum_mari=0
nr_prescuri=0
ron_donatii=0
ron_cult=0
total_Plata=0
raport_lum_mici=0
raport_lum_mari=0
raport_prescuri=0
raport_donatii=0
raport_cult=0
raport_total_general=0
raport_tas=0

def Vizualizare_cos():
	global nr_lum_mici
	global nr_lum_mari
	global nr_prescuri
	global ron_donatii
	global ron_cult
	global total_Plata
	global pret_lum_mica
	global pret_lum_mare
	global pret_liturghie_prescuri
	global pret_cult_pe_persoana

	nr_lum_mici=int(comboLummici.get())
	lab_cos_Lummici.config(text=f"Cos lum.mici : {nr_lum_mici} X {pret_lum_mica} RON = "+str(nr_lum_mici*pret_lum_mica)+" RON")

	nr_lum_mari =int(comboLummari.get())
	lab_cos_Lummari.config(text=f"Cos lum.mari : {nr_lum_mari} X {pret_lum_mare} RON = "+str(nr_lum_mari*pret_lum_mare)+" RON")

	nr_prescuri =int(comboPrescuri.get())
	lab_cos_Prescuri.config(text=f"Cos Prescuri : {nr_prescuri} X {pret_liturghie_prescuri} RON = "+str(nr_prescuri*pret_liturghie_prescuri)+" RON")

	ron_donatii=int(comboDonatii.get())
	lab_cos_Donatii.config(text=f"Cos Donatii : {ron_donatii} RON")

	ron_cult=int(comboCult.get())
	lab_cos_Cult.config(text=f"Cos Cult : {comboCult.get()}X{pret_cult_pe_persoana} RON = "+str(ron_cult*pret_cult_pe_persoana)+" RON")

	total_Plata=nr_lum_mici*pret_lum_mica+nr_lum_mari*pret_lum_mare+nr_prescuri*pret_liturghie_prescuri+ron_donatii+ron_cult*pret_cult_pe_persoana
	lab_total_Plata.config(text=f"Cos Total : {total_Plata} RON")
def Adauga_la_raport():
	global raport_lum_mici
	global raport_lum_mari
	global raport_prescuri
	global raport_donatii
	global raport_cult
	global raport_total_general
	global pret_lum_mica
	global pret_lum_mare
	global pret_liturghie_prescuri
	global pret_cult_pe_persoana
	global raport_tas

	raport_lum_mici = raport_lum_mici+int(comboLummici.get())
	raport_lum_mari = raport_lum_mari + int(comboLummari.get())
	lab_raport_lum_mici_mari.config(text=f"Lum:{raport_lum_mici}X{pret_lum_mica}="+str(raport_lum_mici*pret_lum_mica)+f" / {raport_lum_mari}X{pret_lum_mare}="+str(raport_lum_mari*pret_lum_mare)+f' ->{str(raport_lum_mici*pret_lum_mica+raport_lum_mari*pret_lum_mare)} RON')

	raport_prescuri =raport_prescuri+int(comboPrescuri.get())
	lab_raport_prescuri.config(text=f"Prescuri:{raport_prescuri}X{pret_liturghie_prescuri}=" + str(raport_prescuri*pret_liturghie_prescuri) + " RON")

	raport_donatii = raport_donatii+int(comboDonatii.get())
	lab_raport_donatii.config(text=f"Donatii: {raport_donatii} RON")

	raport_cult = raport_cult+int(comboCult.get())
	lab_raport_cult.config(text=f"Cult:{raport_cult}X{pret_cult_pe_persoana} RON=" + str(raport_cult*pret_cult_pe_persoana) + " RON")
	raport_tas=raport_tas+int(entry_tas.get())
	lab_raport_tas.config(text=f' Tas : {raport_tas} RON')
		

	raport_total_general = (raport_lum_mici * pret_lum_mica) + (raport_lum_mari * pret_lum_mare) + (raport_prescuri * pret_liturghie_prescuri) + (raport_donatii + raport_cult*pret_cult_pe_persoana)+raport_tas
	lab_raport_total_general.config(text=f"Total GENERAL:{raport_total_general} RON")
	reseteaza_combo_cos()
	actualizeazaOra()

def actualizeazaOra():
	ora=datetime.datetime.now()
	lab_sumar.configure(text=f"Vanzari la ora {ora.hour}:{ora.minute}:{ora.second}")
	data=date.today()
	labTitlu.configure(text=f'Vanzare in {data}')
	
def reseteaza_combo_cos():
	comboLummici.current(1)
	comboLummari.current(1)
	comboPrescuri.current(1)
	comboDonatii.current(1)
	comboCult.current(1)
	lab_cos_Lummici.config(text='Cos lum.mici:')
	lab_cos_Lummari.config(text='Cos lum.mari:')
	lab_cos_Prescuri.config(text='Cos Prescuri:')
	lab_cos_Donatii.config(text='Cos Donatii:')
	lab_cos_Cult.config(text='Cos Cult:')
	lab_total_Plata.config(text='Cos Total:')
	entry_tas.delete(0,END)
	entry_tas.insert(0,"0")

marime_font=11

labTitlu=Label(w,text='Vanzare ',font=('Serif',marime_font+4,'bold'),fg='blue')
labLummici=Label(w,text='Lumanari mici:',font=('Serif',marime_font))
labLummari=Label(w,text='Lumanari MARI:',font=('Serif',marime_font))
labPrescuri=Label(w,text='L. Prescuri:',font=('Serif',marime_font))
labDonatii=Label(w,text='Donatii:',font=('Serif',marime_font))
labCult=Label(w,text='Cult[nr.persoane]:',font=('Serif',marime_font))
lab_cos_Lummici=Label(w,text='Cos lum.mici:',font=('Serif',marime_font))
lab_cos_Lummari=Label(w,text='Cos lum.mari:',font=('Serif',marime_font))
lab_cos_Prescuri=Label(w,text='Cos Prescuri:',font=('Serif',marime_font))
lab_cos_Donatii=Label(w,text='Cos Donatii:',font=('Serif',marime_font))
lab_cos_Cult=Label(w,text='Cos Cult:',font=('Serif',marime_font))
lab_total_Plata=Label(w,text='Cos Total:',font=('Serif',marime_font))
lab_sumar=Label(w,text='SUMAR : ',font=('Serif',marime_font,'bold'),bg='orange')
lab_raport_lum_mici_mari=Label(w,text='Lum. vandute:0',font=('Serif',marime_font),bg='yellow')
lab_raport_prescuri=Label(w,text='Prescuri:0',font=('Serif',marime_font),bg='yellow')
lab_raport_donatii=Label(w,text='Donatii:0',font=('Serif',marime_font),bg='yellow')
lab_raport_cult=Label(w,text='Cult:0',font=('Serif',marime_font),bg='yellow')
lab_raport_tas=Label(w,text='Tas : 0',font=('Serif',marime_font),bg='yellow')
lab_raport_total_general=Label(w,text='Total GENERAL:0',font=('Serif',marime_font,'bold'),bg='pink')
lab_tas=Label(w,text='Tas :',font=('Serif',marime_font))
entry_tas=Entry(w,bg='yellow',width=8,font=('Serif',marime_font))
entry_tas.insert(0,"0")


stil=ttk.Style()
stil.theme_use('alt')    #('winnative', 'clam', 'alt', 'default', 'classic', 'vista', 'xpnative')
stil.configure("TCombobox",fieldbackground= "white",arrowsize=70)
valori=[]
for i in range(-1,31):
	valori.append(i)
comboLummici=ttk.Combobox(w,values=valori,width=5,font=('Serif',marime_font),height=25)
comboLummici.current(1)
comboLummari=ttk.Combobox(w,values=valori,width=5,font=('Serif',marime_font),height=25)
comboLummari.current(1)
prescuri=[]
for i in range (-1,20):
	prescuri.append(i)
comboPrescuri=ttk.Combobox(w,values=prescuri,width=5,font=('Serif',marime_font),height=21)
comboPrescuri.current(1)
donatii=[]
for i in range(-50,1050,50):
	donatii.append(i)
comboDonatii=ttk.Combobox(w,values=donatii,width=5,font=('Serif',marime_font),height=25)
comboDonatii.current(1)
nr_persoane=[]
for i in range(-1,11):
	nr_persoane.append(i)
comboCult=ttk.Combobox(w,values=nr_persoane,width=5,font=('Serif',marime_font),height=11)
comboCult.current(1)


Adauga_in_cos=Button(w,text='Actualizare cos',font=('Serif',marime_font,'bold'),command=Vizualizare_cos)
Vandut=Button(w,text='Vandut!',font=('Serif',marime_font,'bold'),command=Adauga_la_raport)


if __name__ == '__main__':
	X_comb=250 #laptop Samsung, valoarea 250, telefon 430
	Yref=40#laptop Samsung, valoarea 37,telefon 70
	labTitlu.pack()
	labLummici.place(x=10,y=Yref)
	comboLummici.place(x=X_comb,y=Yref)
	labLummari.place(x=10,y=2*Yref)
	comboLummari.place(x=X_comb,y=2*Yref)
	labPrescuri.place(x=10,y=3*Yref)
	comboPrescuri.place(x=X_comb,y=3*Yref)
	labDonatii.place(x=10,y=4*Yref)
	comboDonatii.place(x=X_comb,y=4*Yref)
	labCult.place(x=10,y=5*Yref)
	comboCult.place(x=X_comb,y=5*Yref)
	lab_tas.place(x=10,y=6*Yref)
	entry_tas.place(x=X_comb,y=6*Yref)
	
	Adauga_in_cos.place(x=10,y=7*Yref)
	Vandut.place(x=X_comb,y=7*Yref)
	lab_cos_Lummici.place(x=10,y=8*Yref)
	lab_cos_Lummari.place(x=10,y=9*Yref)
	lab_cos_Prescuri.place(x=10,y=10*Yref)
	lab_cos_Donatii.place(x=10,y=11*Yref)
	lab_cos_Cult.place(x=10,y=12*Yref)
	lab_total_Plata.place(x=10,y=13*Yref)
	lab_sumar.place(x=10,y=14*Yref)
	lab_raport_lum_mici_mari.place(x=10,y=15*Yref)
	lab_raport_prescuri.place(x=10,y=16*Yref)
	lab_raport_donatii.place(x=10,y=17*Yref)
	lab_raport_cult.place(x=10,y=18*Yref)
	lab_raport_tas.place(x=10,y=19*Yref)
	lab_raport_total_general.place(x=10,y=20*Yref)
	w.mainloop()