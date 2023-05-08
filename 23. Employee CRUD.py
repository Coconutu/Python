
def insertData():
    id=enterId.get()
    name=enterName.get()
    dept=enterDept.get()
    if(id=="" or name=="" or dept==""):
        messagebox.showwarning("Cannot Insert","All the field are required!")
    else:
        myDB=mysql.connector.connect(host='localhost',user='root',passwd='Coconutu2!',database='employee')
        myCur=myDB.cursor()

        myCur.execute(f"INSERT INTO empdetails VALUES('{id}','{name}','{dept}')")
        myDB.commit()

        enterId.delete(0,"end")
        enterName.delete(0,"end")
        enterDept.delete(0,"end")
        messagebox.showinfo('Insert status','Data inserted successfully')
        myDB.close()
        show()
def updateData():
    id = enterId.get()
    name = enterName.get()
    dept = enterDept.get()
    if (id == "" or name == "" or dept == ""):
        messagebox.showwarning("Cannot Update", "All the field are required!")
    else:
        myDB = mysql.connector.connect(host='localhost', user='root', passwd='Coconutu2!', database='employee')
        myCur = myDB.cursor()
        myCur.execute(f"update empdetails set empName='{name}',empDept='{dept}' where empID='{id}'")
        myDB.commit()

        enterId.delete(0, "end")
        enterName.delete(0, "end")
        enterDept.delete(0, "end")
        messagebox.showinfo('Update status', 'Data Updated successfully')
        myDB.close()
        show()

def getData():
    if (enterId.get()==""):
        messagebox.showwarning('Fetch Status','Please provide the EMP ID to fetch the data')
    else:
        myDB = mysql.connector.connect(host='localhost', user='root', passwd='Coconutu2!', database='employee')
        myCur = myDB.cursor()

        myCur.execute(f"SELECT* FROM empdetails where empID='{enterId.get()}'")
        rows=myCur.fetchall()
        for row in rows:
            enterName.insert(0,row[1])
            enterDept.insert(0,row[2])
        myDB.close()

def deleteData():
    if (enterId.get() == ""):
        messagebox.showwarning('Cannot delete', 'Please provide the EMP ID to delete the data')
    else:
        myDB = mysql.connector.connect(host='localhost', user='root', passwd='Coconutu2!', database='employee')
        myCur = myDB.cursor()

        myCur.execute(f"DELETE FROM empdetails where empID='{enterId.get()}'")
        myDB.commit()
        enterId.delete(0, "end")
        enterName.delete(0, "end")
        enterDept.delete(0, "end")
        messagebox.showinfo('Delete status', 'Data Deleted successfully')
        myDB.close()
        show()
def show():
    myDB = mysql.connector.connect(host='localhost', user='root', passwd='Coconutu2!', database='employee')
    myCur = myDB.cursor()
    myCur.execute('SELECT* FROM empdetails')
    rows=myCur.fetchall()
    showData.delete(0,showData.size())
    for row in rows:
        addData=str(row[0])+' '+row[1]+' '+row[2]
        showData.insert(showData.size()+1,addData)
    myDB.close()

def resetFields():
    enterId.delete(0, "end")
    enterName.delete(0, "end")
    enterDept.delete(0, "end")
    show()


from tkinter import *
from tkinter import messagebox
import mysql.connector

window=Tk()
window.geometry("600x270")
window.title('Employee CRUD App')

empId=Label(window,text='Employee ID',font=('Serif',12))
empId.place(x=20,y=30)

empName=Label(window,text='Employee Name',font=('Serif',12))
empName.place(x=20,y=60)

empDept=Label(window,text='Employee Dept',font=('Serif',12))
empDept.place(x=20,y=90)

enterId=Entry(window)
enterId.place(x=170,y=30)

enterName=Entry(window)
enterName.place(x=170,y=60)

enterDept=Entry(window)
enterDept.place(x=170,y=90)

insertBtn=Button(window,text='Insert',font=('Sans',12),bg='white',command=insertData)
insertBtn.place(x=20,y=160)

updateBtn=Button(window,text='Update',font=('Sans',12),bg='white',command=updateData)
updateBtn.place(x=100,y=160)

getBtn=Button(window,text='Fetch',font=('Sans',12),bg='white',command=getData)
getBtn.place(x=190,y=160)

deleteBtn=Button(window,text='Delete',font=('Sans',12),bg='white',command=deleteData)
deleteBtn.place(x=270,y=160)

resetBtn=Button(window,text='Reset',font=('Sans',12),bg='white',command=resetFields)
resetBtn.place(x=20,y=210)

showData=Listbox(window)
showData.place(x=370,y=30)
#listbox metode
    #delete(first,last=None) -sterge liniile din range first,last. Daca omitem al doilea argument, sterge doar linia indicata de first
    #get(first,last=None) - returneaza o tupla continand textul liniilor indicate de first, last.
    #size() returneaza numarul liniilor
    #insert(index,*elements) - insereaza una sau mai multe liniiin listbox inaintea liniei specificate in index.Se poate folosi END ca si prim argument daca vrem sa adaugam o linie noua la finalul listboxului.


show()
window.mainloop()