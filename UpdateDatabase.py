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
        self.master = Label(heading, text = 'Update The Database', font =('arial', 40, 'bold'),bg = 'black', fg = 'cornsilk')
        self.master.place(x = 400, y = 0)

        self.id1 = Label(heading, text = "Enter id", font=('arial', 18, 'bold'))
        self.id1.place(x = 0, y = 120)

##        self.i = Label(heading, text = "ID has reaching = " +str(id), font =('arial', 18, 'bold'))
##        self.i.place(x = 0, y = 170)
        
        self.name1 = Label(heading, text = 'Enter the product name', font =('arial', 18, 'bold'))
        self.name1.place(x = 0, y = 170)

        self.stock1 = Label(heading, text = 'Enter stock', font =('arial', 18, 'bold'))
        self.stock1.place(x = 0, y = 220)

        self.cp1 = Label(heading, text = 'Enter cost price', font =('arial', 18, 'bold'))
        self.cp1.place(x = 0, y = 270)

        self.sp1 = Label(heading, text = 'Enter selling price', font =('arial', 18, 'bold'))
        self.sp1.place(x = 0, y = 320)

        self.vendor1 = Label(heading, text = 'Enter vendor name', font =('arial', 18, 'bold'))
        self.vendor1.place(x = 0, y = 370)

        self.vendornum1 = Label(heading, text = 'Enter vendor phone number', font =('arial', 18, 'bold'))
        self.vendornum1.place(x = 0, y = 420)

##        self.id_1 = Label(heading, text = 'Enter ID', font =('arial', 18, 'bold'))
##        self.id_1.place(x = 0, y = 470)

        self.id2 = Entry(heading, width = 10, font =('arial', 18, 'bold'))
        self.id2.place(x = 380, y = 120)

        self.name2 = Entry(heading, width = 20, font =('arial', 18, 'bold'))
        self.name2.place(x = 380, y = 170)

        self.stock2 = Entry(heading, width = 20, font =('arial', 18, 'bold'))
        self.stock2.place(x = 380, y = 220)

        self.cp2 = Entry(heading, width = 20, font =('arial', 18, 'bold'))
        self.cp2.place(x = 380, y = 270)

        self.sp2 = Entry(heading, width = 20, font =('arial', 18, 'bold'))
        self.sp2.place(x = 380, y = 320)

        self.vendor2 = Entry(heading, width = 20, font =('arial', 18, 'bold'))
        self.vendor2.place(x = 380, y = 370)

        self.vendornum2 = Entry(heading, width = 20, font =('arial', 18, 'bold'))
        self.vendornum2.place(x = 380, y = 420)

##        self.id_2 = Entry(heading, width = 20, font =('arial', 18, 'bold'))
##        self.id_2.place(x = 380, y = 420)
                          
        self.btnadd = Button(heading, text = "Update The Database", width = 20, height = 2, bg = 'dark red', fg = 'white')
        self.btnadd.place(x = 450, y = 500)

        self.btnclear = Button(heading, text = "Clear All", width = 20, height =2, bg = 'dark red',fg = 'white')
        self.btnclear.place(x = 250, y = 500)

        self.btnsearch = Button(heading, text = "Search", width = 10, height =2, bg = 'dark red',fg = 'white', command = self.search)
        self.btnsearch.place(x = 550, y = 120)        

        self.tbox = Text(heading, width = 60, height = 18)
        self.tbox.place(x = 700, y=120)
        self.tbox.insert(END, "ID Has Reaching = " +str(id))

    def search(self, *args, **kwargs):
        sql = "SELECT * FROM project WHERE id = ?"
        result = ulaga.execute(sql, (self.id2.get(),))
        for r in result:
            self.n1 = r[1]
            self.n2 = r[2]
            self.n3 = r[3]
            self.n4 = r[4]
            self.n5 = r[5]
            self.n6 = r[6]
            self.n7 = r[7]
            self.n8 = r[8]
            self.n9 = r[9]
        conn.commit()     

        self.name2.delete(0, END) 
        self.name2.insert(0, str(self.n1))
        self.stock2.delete(0, END) 
        self.stock2.insert(0, str(self.n2))
        self.cp2.delete(0, END) 
        self.cp2.insert(0, str(self.n3))
        self.sp2.delete(0, END) 
        self.sp2.insert(0, str(self.n4))
        self.vendor2.delete(0, END) 
        self.vendor2.insert(0, str(self.n8))
        self.vendornum2.delete(0, END) 
        self.vendornum2.insert(0, str(self.n9))
        
b = Database(root)
root.geometry("1360x768")
root.title("Update The Database")
root.mainloop()        
