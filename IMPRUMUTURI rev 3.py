'''
DESCRIBE NUME
'+---------------------+--------------+------+-----+---------+-------+
| Field               | Type         | Null | Key | Default | Extra |
+---------------------+--------------+------+-----+---------+-------+
| ID                  | int          | NO   | PRI | NULL    |       |
| IMPRUMUT_RESTITUIRE | varchar(25)  | YES  |     | NULL    |       |
| NUME                | varchar(50)  | YES  |     | NULL    |       |
| SUMA                | int          | YES  |     | NULL    |       |
| ZI                  | varchar(12)  | YES  |     | NULL    |       |
| LUNA                | varchar(12)  | YES  |     | NULL    |       |
| AN                  | varchar(12)  | YES  |     | NULL    |       |
| OBSERVATII          | varchar(250) | YES  |     | NULL    |       |
+---------------------+--------------+------+-----+---------+-------+
'''

import tkinter.ttk
from tkinter import *
import mysql.connector
from tkinter import messagebox


def formatare(text,l_finala):
	text=f'{text:<{l_finala}}'

	text=text+'|'
	return text

def insertData():
    id = entryID.get()
    imprumut_restituire = comboboxIMPRUMUT_RESTITUIRE.get()
    nume=entryNUME.get()
    suma=entrySUMA.get()
    zi=comboboxZI.get()
    luna=comboboxLUNA.get()
    an=comboboxAN.get()
    observatii=entryOBSERVATII.get()
    id=id.upper()
    nume=nume.upper()
    observatii=observatii.upper()

    if (id == "" or imprumut_restituire == "" or nume == "" or suma=="" or zi=="" or luna=="" or an==""):
        messagebox.showwarning("Nu pot introduce !", "Toate campurile sunt obligatorii(exceptand OBSERVATII )!")
    else:
        try:
            myDB = mysql.connector.connect(host='localhost', user='root', passwd='Coconutu2!', database='imprumuturi')
            myCur = myDB.cursor()
            if imprumut_restituire=='IMPRUMUT':
                suma='-'+suma
            myCur.execute(f"INSERT INTO nume VALUES('{id}','{imprumut_restituire}','{nume}','{suma}','{zi}','{luna}','{an}','{observatii}')")

            entryID.delete(0, "end")
            entryNUME.delete(0, "end")
            entrySUMA.delete(0, "end")
            entryOBSERVATII.delete(0, "end")
            messagebox.showinfo('Status inserare', 'Datele au fost introduse cu succes!')
            myDB.commit()
            myDB.close()
        except mysql.connector.Error as err:
            messagebox.showerror('Failure in executing query. Error:',err)
    show()

def updateData():
    id = entryID.get()
    imprumut_restituire = comboboxIMPRUMUT_RESTITUIRE.get()
    nume = entryNUME.get()
    suma = entrySUMA.get()
    zi = comboboxZI.get()
    luna = comboboxLUNA.get()
    an = comboboxAN.get()
    observatii = entryOBSERVATII.get()
    id=id.upper()
    nume=nume.upper()
    observatii=observatii.upper()

    if (id == "" or imprumut_restituire == "" or nume == "" or suma == "" or zi == "" or luna == "" or an == ""):
        messagebox.showwarning("Nu pot introduce !", "Toate campurile sunt obligatorii(exceptand OBSERVATII )!")
    else:
        try:
            myDB = mysql.connector.connect(host='localhost', user='root', passwd='Coconutu2!', database='imprumuturi')
            myCur = myDB.cursor()
            if imprumut_restituire=='IMPRUMUT':
                suma='-'+suma
            myCur.execute(f"UPDATE nume SET IMPRUMUT_RESTITUIRE='{imprumut_restituire}',NUME='{nume}',SUMA='{suma}',ZI='{zi}',LUNA='{luna}',AN='{an}',OBSERVATII='{observatii}' WHERE id='{id}'")
            entryID.delete(0, "end")
            entryNUME.delete(0, "end")
            entrySUMA.delete(0, "end")
            entryOBSERVATII.delete(0, "end")
            messagebox.showinfo('Status actualizare', 'Datele au fost actualizate cu succes!')
            myDB.commit()
            myDB.close()
        except mysql.connector.Error as err:
            messagebox.showerror('Failure in executing query. Error:', err)
    show()


def deleteData():
    if (entryID.get() == ""):
        messagebox.showwarning('Status afisare', 'Te rog adauga ID ca sa sterg datele')
    else:
        try:
            showData.delete(0, showData.size())
            myDB = mysql.connector.connect(host='localhost', user='root', passwd='Coconutu2!', database='imprumuturi')
            myCur = myDB.cursor()
            myCur.execute(f"DELETE FROM NUME WHERE ID='{entryID.get()}'")
            myDB.commit()
            rows = myCur.fetchall()
            showData.delete(0, showData.size())
            for row in rows:
                addData = str(row[0]) + '--->' + row[1] + '   ' + row[2] + '     ' + str(
                    row[3]) + ' RON  IN DATA :' + str(row[4]) + '-' + str(row[5]) + '-' + str(row[6]) + '  OBS.:' + row[
                              7]
                showData.insert(showData.size() + 1, addData)

            myDB.close()
        except mysql.connector.Error as err:
            messagebox.showerror('Failure in executing query. Error:', err)
    show()
    resetFields()

def resetFields():
    entryID.delete(0, "end")
    entryNUME.delete(0, "end")
    entrySUMA.delete(0, "end")
    entryOBSERVATII.delete(0, "end")
    show()

def show():
    try:
        balanta=0
        myDB = mysql.connector.connect(host='localhost', user='root', passwd='Coconutu2!', database='imprumuturi')
        myCur = myDB.cursor()
        myCur.execute('SELECT* FROM nume')
        rows = myCur.fetchall()
        showData.delete(0, showData.size())
        item_index=0
        for row in rows:
            addData = (str(row[0]).zfill(3))+'|' + formatare(row[1],10)+ formatare(row[2],15)+formatare(str(row[3]),6) +'RON |' + formatare(str(row[4]).zfill(2)+'/'+str(row[5][:3])+'/'+str(row[6]),11) +'OBS.:' + row[7]
            showData.insert(showData.size() + 1, addData)
            showData.itemconfig(item_index, bg='white' if str(row[1])=='IMPRUMUT' else 'pink')
            item_index=item_index+1

            balanta = balanta + row[3]
            labelBalanta.config(text=balanta)
            if row[2] not in lista_nume:
                lista_nume.append(row[2])
            lista_nume.sort()


        myDB.close()
    except mysql.connector.Error as err:
        messagebox.showerror('Failure in executing query. Error:', err)
def selectNume():
    try:
        balanta=0
        showData.delete(0, showData.size())
        myDB = mysql.connector.connect(host='localhost', user='root', passwd='Coconutu2!', database='imprumuturi')
        myCur = myDB.cursor()
        myCur.execute(f"SELECT* FROM NUME WHERE NUME='{combobox_nume.get()}'")
        rows = myCur.fetchall()
        showData.delete(0, showData.size())
        item_index = 0
        for row in rows:
            addData = (str(row[0]).zfill(3))+'|' + formatare(row[1],10)+ formatare(row[2],15)+formatare(str(row[3]),6) +'RON |' + formatare(str(row[4]).zfill(2)+'/'+str(row[5][:3])+'/'+str(row[6]),11) +'OBS.:' + row[7]
            showData.insert(showData.size() + 1, addData)
            showData.itemconfig(item_index, bg='white' if str(row[1]) == 'IMPRUMUT' else 'pink')
            item_index = item_index + 1
            balanta = balanta + row[3]
            labelBalanta.config(text=balanta)
        messagebox.showwarning(f'Status pentru {combobox_nume.get()}',f'{combobox_nume.get()}-->DE RESTITUIT \n {str(-balanta)} RON')

        myDB.close()
    except mysql.connector.Error as err:
        messagebox.showerror('Failure in executing query. Error:',err)



window=Tk()
window.title('Baza de date imprumuturi')
window.config(bg='Yellow')
width=window.winfo_screenwidth()
height=window.winfo_screenheight()
window.geometry(f'{width}x{height}')

labelID=Label(window,bg='Yellow',text='ID',font=('Serif',12))
labelID.place(x=20,y=30)
entryID=Entry(window)
entryID.place(x=280,y=30)

labelIMPRUMUT_RESTITUIRE=Label(window,bg='Yellow',text='IMPRUMUT/RESTITUIRE',font=('Serif',12))
labelIMPRUMUT_RESTITUIRE.place(x=20,y=60)
textcombobox=['IMPRUMUT','RESTITUIRE']
comboboxIMPRUMUT_RESTITUIRE=tkinter.ttk.Combobox(window,values=textcombobox,width=17)
comboboxIMPRUMUT_RESTITUIRE.current(0)
comboboxIMPRUMUT_RESTITUIRE.place(x=280,y=60)


labelNUME=Label(window,bg='Yellow',text='NUME',font=('Serif',12))
labelNUME.place(x=20,y=90)
entryNUME=Entry(window)
entryNUME.place(x=280,y=90)

labelSUMA=Label(window,bg='Yellow',text='SUMA',font=('Serif',12))
labelSUMA.place(x=20,y=120)
entrySUMA=Entry(window)
entrySUMA.place(x=280,y=120)

labelZI=Label(window,bg='Yellow',text='ZI',font=('Serif',12))
labelZI.place(x=20,y=150)
zilelelunii=[]
for x in range(1, 32):
    zilelelunii.append(x)
comboboxZI=tkinter.ttk.Combobox(window,values=zilelelunii,width=3)
comboboxZI.current(0)
comboboxZI.place(x=280,y=150)

labelLUNA=Label(window,bg='Yellow',text='LUNA',font=('Serif',12))
labelLUNA.place(x=20,y=180)
lunileanului=['Ianuarie','Februarie','Martie','Aprilie','Mai','Iunie','Iulie','August','Septembrie','Octombrie','Noiembrie','Decembrie']
comboboxLUNA=tkinter.ttk.Combobox(window,values=lunileanului,width=10)
comboboxLUNA.current(6)
comboboxLUNA.place(x=280,y=180)

labelAN=Label(window,bg='Yellow',text='AN',font=('Serif',12))
labelAN.place(x=20,y=210)
ani=[]
for x in range(2010, 2050):
    ani.append(x)
comboboxAN=tkinter.ttk.Combobox(window,values=ani,width=6)
comboboxAN.current(10)
comboboxAN.place(x=280,y=210)



labelOBSERVATII=Label(window,bg='Yellow',text='OBSERVATII',font=('Serif',14))
labelOBSERVATII.place(x=20,y=240)
entryOBSERVATII=Entry(window)
entryOBSERVATII.place(x=20,y=270,width=425)


insertBtn=Button(window,text=' Insert ',fg='blue',font=('Sans',14),bg='white',command=insertData)
insertBtn.place(x=20,y=320)

updateBtn=Button(window,text='Update',fg='blue',font=('Sans',14),bg='white',command=updateData)
updateBtn.place(x=120,y=320)

getBtn=Button(window,text='Filtrare dupa nume',fg='blue',font=('Sans',14),bg='white',command=selectNume)
getBtn.place(x=20,y=540)

deleteBtn=Button(window,text=' Delete',fg='red',font=('Sans',14),bg='white',command=deleteData)
deleteBtn.place(x=20,y=370)

resetBtn=Button(window,text=' Reset ',fg='blue',font=('Sans',14),bg='white',command=resetFields)
resetBtn.place(x=120,y=370)

scrollbar=tkinter.Scrollbar()
showData=Listbox(window,width=130,height=45,font=('Courier',11),yscrollcommand=scrollbar.set,selectmode='multiple')

scrollbar.grid(row=0,column=2,sticky='ns')
showData.place(x=450,y=30)


scrollbar.pack(side=RIGHT, fill=BOTH)
labelSumar=Label(window,text='Status balanta (RON) : ',font=('Serif',14))
labelSumar.place(x=20,y=600)

labelBalanta=Label(window,borderwidth=3, relief="ridge",text='balanta',font=('Serif',14))
labelBalanta.place(x=280,y=600)

lista_nume=[]
show()

label_Selectare=Label(window,text='Selecteaza numele din lista :')
label_Selectare.place(x=20,y=460)

combobox_nume = tkinter.ttk.Combobox(window, values=lista_nume, width=22)
combobox_nume.place(x=20, y=500)
combobox_nume.current(0)

window.mainloop()