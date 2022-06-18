from tkinter import *
import sqlite3
from tkinter import messagebox
from PIL import ImageTk, Image

root=Tk()
conn=sqlite3.connect("facebook.db")
my_image=ImageTk.PhotoImage(Image.open("abcd.jpg"))
my_label=Label(image=my_image)
my_label.place(x=0,y=0)

c=conn.cursor()
c.execute(""" CREATE TABLE User(
    first_name text,
    last_name text,
    address text,
    age integer,
    password text,
    father_name text,
    city text,
    zipcode integer
)""")

print("Table created succcessfully")


def delete():
    conn=sqlite3.connect("facebook.db")
    c=conn.cursor()
    c.execute("DELETE from user WHERE oid = " + delete_box.get())
    print("Deleted successfully")    
    conn.commit()
    conn.close()

def update():
    
    conn=sqlite3.connect("facebook.db")
    c=conn.cursor()
    
    record_id=delete_box.get()
    
    c.execute("""UPDATE user SET 
            first_name=:first,
            last_name=:last,
            address=:address,
            age=:ages,
            password=:password,
            father_name=:father,
            city=:city,
            zipcode=:zipcode
    
            WHERE oid =:oid""",
             {
              "first":f_name_editor.get(),
              "last":l_name_editor.get(),
              "address":address_editor.get(),
              "age":age_editor.get(),
              "password":password_editor.get(),
              "father_name":father_name_editor.get(),
              "city":city_editor.get(),
              "zipcode":zipcode_editor.get(),
              "oid":record_id
            } 
        )
    messagebox.showinfo("Data Updated successfully")
    conn.commit()
    conn.close()

def edit():
    
    global editor
    editor=Toplevel()
    editor.title("update data")
    conn=sqlite3.connect("facebook.db")
    c=conn.cursor()
    record_id=delete_box.get()
    c.execute("SELECT * FROM user WHERE  oid =" + record_id)
    records = c.fetchall()
    
    
    global first_name_editor
    global last_name_editor
    global address_editor
    global age_editor
    global password_editor
    global father_name_editor
    global city_editor
    global zipcode_editor
    
    first_name_editor=Entry(editor,width=30)
    first_name_editor.grid(row=0,column=1,padx=20,pady=10)
    
    last_name_editor=Entry(editor,width=30)
    last_name_editor.grid(row=1,column=1)
    
    address_editor=Entry(editor,width=30)
    address_editor.grid(row=2,column=1)
    
    age_editor=Entry(editor,width=30)
    age_editor.grid(row=3,column=1)
    
    password_editor=Entry(editor,width=30)
    password_editor.grid(row=4,column=1)
    
    father_name_editor=Entry(editor,width=30)
    father_name_editor.grid(row=5,column=1)
    
    city_editor=Entry(editor,width=30)
    city_editor.grid(row=6,column=1)
    
    zipcode_editor=Entry(editor,width=30)
    zipcode_editor.grid(row=7,column=1)
    
    first_name_label=Label(editor,text="First Name")
    first_name_label.grid(row=0,column=0,pady=(10,0))
    
    last_name_label=Label(editor,text="Last Name")
    last_name_label.grid(row=1,column=0)
    
    address_label=Label(editor,text="Address")
    address_label.grid(row=2,column=0)
    
    age_label=Label(editor,text="Age")
    age_label.grid(row=3,column=0)
    
    password_label=Label(editor,text="Password")
    password_label.grid(row=4,column=0)
    
    fatherName_label=Label(editor,text="Father Name")
    fatherName_label.grid(row=5,column=0)
    
    city_label=Label(editor,text="City")
    city_label.grid(row=6,column=0)
    
    zipcode_label=Label(editor,text="ZipCode")
    zipcode_label.grid(row=7,column=0)
    
    for record in records:
        first_name_editor.insert(0,record[0])
        last_name_editor.insert(0,record[1])
        address_editor.insert(0,record[2])
        age_editor.insert(0,record[3])
        password_editor.insert(0,record[4])
        father_name_editor.insert(0,record[5])
        city_editor.insert(0,record[6])
        zipcode_editor.insert(0,record[7])
        
    edit_btn= Button(editor,text="Save",command=update)
    edit_btn.grid(row=10,columnspan=2,padx=10,pady=10,ipadx=125)
    conn.commit()
    conn.close()
        

    
    
def query():
    conn=sqlite3.connect("facebook.db")
    c=conn.cursor()
    c.execute("SELECT *,oid FROM user")
    
    records=c.fetchall()
    print(records)
   
    print_records=''
    for record in records:
        print_records += str(record[0]) + ' ' + str(record[1]) + ' '+ str(record[3])+ ' ' + '\t'+str(record[8])+"\n"
    
    query_label=Label(root,text=print_records)
    query_label.grid(row=11,column=0,columnspan=2)
    
    conn.commit()
    conn.close()


def submit():
    conn=sqlite3.connect("facebook.db")
    
    c=conn.cursor()
    
    c.execute("INSERT INTO user values(:first_name, :last_name, :address ,:age, :password, :father_name,:city, :zipcode)",{
        "first_name":first_name.get(),
        "last_name":last_name.get(),
        "address":address.get(),
        "age":age.get(),
        "password":password.get(),
        "father_name":father_name.get(),
        "city":city.get(),
        "zipcode":zipcode.get()
    } )
    
    messagebox.showinfo("Data Inserted successfully")
    conn.commit()
    conn.close()

first_name= Entry(root, width=20)
first_name.grid(row=0,column=1)


last_name=Entry(root,width=20)
last_name.grid(row=1,column=1)

address=Entry(root,width=20)
address.grid(row=2,column=1)

age=Entry(root,width=20)
age.grid(row=3,column=1)

password=Entry(root,width=20)
password.grid(row=4,column=1)

father_name=Entry(root,width=20)
father_name.grid(row=5,column=1)

city=Entry(root,width=20)
city.grid(row=6,column=1)

zipcode=Entry(root,width=20)
zipcode.grid(row=7,column=1)

delete_box=Entry(root,width=20)
delete_box.grid(row=8,column=1)


first_name=Label(root,text="First Name")
first_name.grid(row=0,column=0)

last_name=Label(root,text="Last Name")
last_name.grid(row=1,column=0)

address=Label(root,text="Address")
address.grid(row=2,column=0)


age=Label(root,text="Age",fg="black",bg="white",bd=5)
age.grid(row=3,column=0)

password=Label(root,text="Password",fg="black",bg="white")
password.grid(row=4,column=0)

father_name=Label(root,text="Father Name",fg="black",bg="white")
father_name.grid(row=5,column=0)

city=Label(root,text="City",fg="black",bg="white")
city.grid(row=6,column=0)

zipcode=Label(root,text="Zip code",fg="black",bg="white")
zipcode.grid(row=7,column=0)

delete_label=Label(root,text="delete",fg="black",bg="white")
delete_label.grid(row=8,column=0)

btn=Button(root,text="Submit",command=submit)
btn.grid(row=17,column=0,columnspan=2)
   


query_btn=Button(root, text="Show Records",command=query)
query_btn.grid(row=15,column=0,columnspan=2,padx=10,pady=10,ipadx=90)

update_btn=Button(root,text="Update",command=edit)
update_btn.grid(row=14,column=0,columnspan=2,padx=10,pady=10,ipadx=107)



delete_btn=Button(root,text="Delete",command=delete)
delete_btn.grid(row=10,column=0,columnspan=2,padx=10,pady=10,ipadx=110)

conn.commit()
conn.close()



root.mainloop()