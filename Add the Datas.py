from tkinter import *
import sqlite3
import tkinter.messagebox
from PIL import ImageTk, Image
conn = sqlite3.connect("store.db")
ulaga = conn.cursor()
root = Tk()
can = Image.open("D:\\COLL\\wallpaper\\assassincreed.jpg")
backg = ImageTk.PhotoImage(can)
img = Label(root, image = backg)
img.image = backg
img.place(x = -2, y = -50)

result = ulaga.execute("SELECT Max(id) from project")
for r in result:
    id = r[0]
class Database:
    def __init__(self, heading, *args, **kwargs):
        self.heading = heading
        self.master = Label(heading, text = 'Add To The Database', font =('arial', 40, 'bold'),bg = 'black', fg = 'cornsilk')
        self.master.place(x = 400, y = 0)

        self.i = Label(heading, text = "ID has reaching = " +str(id), font =('arial', 18, 'bold'))
        self.i.place(x = 0, y = 40)
        
        self.name1 = Label(heading, text = 'Enter the product name', font =('arial', 18, 'bold'))
        self.name1.place(x = 0, y = 120)

        self.stock1 = Label(heading, text = 'Enter stock', font =('arial', 18, 'bold'))
        self.stock1.place(x = 0, y = 170)

        self.cp1 = Label(heading, text = 'Enter cost price', font =('arial', 18, 'bold'))
        self.cp1.place(x = 0, y = 220)

        self.sp1 = Label(heading, text = 'Enter selling price', font =('arial', 18, 'bold'))
        self.sp1.place(x = 0, y = 270)

        self.vendor1 = Label(heading, text = 'Enter vendor name', font =('arial', 18, 'bold'))
        self.vendor1.place(x = 0, y = 320)

        self.vendornum1 = Label(heading, text = 'Enter vendor phone number', font =('arial', 18, 'bold'))
        self.vendornum1.place(x = 0, y = 370)

        self.id_1 = Label(heading, text = 'Enter ID', font =('arial', 18, 'bold'))
        self.id_1.place(x = 0, y = 420)

        self.name2 = Entry(heading, width = 20, font =('arial', 18, 'bold'))
        self.name2.place(x = 380, y = 120)

        self.stock2 = Entry(heading, width = 20, font =('arial', 18, 'bold'))
        self.stock2.place(x = 380, y = 170)

        self.cp2 = Entry(heading, width = 20, font =('arial', 18, 'bold'))
        self.cp2.place(x = 380, y = 220)

        self.sp2 = Entry(heading, width = 20, font =('arial', 18, 'bold'))
        self.sp2.place(x = 380, y = 270)

        self.vendor2 = Entry(heading, width = 20, font =('arial', 18, 'bold'))
        self.vendor2.place(x = 380, y = 320)

        self.vendornum2 = Entry(heading, width = 20, font =('arial', 18, 'bold'))
        self.vendornum2.place(x = 380, y = 370)

        self.id_2 = Entry(heading, width = 20, font =('arial', 18, 'bold'))
        self.id_2.place(x = 380, y = 420)
                          
        self.btnadd = Button(heading, text = "Add To The Database", width = 20, height = 2, bg = 'dark red', fg = 'white', command = self.get_items)
        self.btnadd.place(x = 450, y = 500)

        self.btnclear = Button(heading, text = "Clear All", width = 20, height =2, bg = 'dark red',fg = 'white', command = self.clear_all)
        self.btnclear.place(x = 250, y = 500)

        self.tbox = Text(heading, width = 60, height = 18)
        self.tbox.place(x = 700, y=120)
        self.tbox.insert(END, "ID Has Reaching = " +str(id))
 
        self.heading.bind('<Return>', self.get_items)
        self.heading.bind('<Up>', self.clear_all)
    def get_items(self, *args, **kwargs):
        self.name = self.name2.get()
        self.stock = self.stock2.get()
        self.cp = self.cp2.get()
        self.sp = self.sp2.get()
        self.vendor = self.vendor2.get()
        self.vendornum = self.vendornum2.get()

        self.totalcp = float(self.cp) * float(self.stock)
        self.totalsp = float(self.sp) * float(self.stock)
        self.assumefield = float(self.totalsp - self.totalcp)

        if self.name == ' ' or self.stock == ' ' or self.cp == ' ' or self.sp == ' ':
            tkinter.messagebox.showinfo("Error", "Please fill the all entries.")
 
        else:
            sql = "INSERT INTO project (name, stock, cp, sp, totalcp, totalsp, assumefield, vendor, vendornum) VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?)"
            ulaga.execute(sql, (self.name, self.stock, self.cp, self.sp, self.totalcp, self.totalsp, self.assumefield, self.vendor, self.vendornum))
            conn.commit()
            
            self.tbox.insert(END, "\n\nInserted " + str(self.name) + " into the database with code = " +str(self.id_2.get()))
            tkinter.messagebox.showinfo("Success", "Successfully added to the database")

    def clear_all(self, *args, **kwargs):
        self.name2.delete(0, END)
        self.stock2.delete(0, END)
        self.cp2.delete(0, END)
        self.sp2.delete(0, END)
        self.vendor2.delete(0, END)
        self.vendornum2.delete(0, END)
        self.id_2.delete(0, END)
        
       
b = Database(root)
root.geometry("1360x768")
root.title("Add To The Database")
root.mainloop()

