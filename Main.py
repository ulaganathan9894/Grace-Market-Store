from tkinter import *
from tkinter import messagebox
import tkinter.messagebox
import tkinter as tk
from PIL import ImageTk, Image
from tkinter import ttk
import random
import datetime
import MySQLdb
import sqlite3
import mysql.connector
import datetime
import math

conn = sqlite3.connect("D:\\Python\\New folder\\store.db") 
c = conn.cursor()

date = datetime.datetime.now().date()

#temp lists
product_id = []
products_list = []
product_price = []
product_quantity = []
def main():
    root = Tk()
    app = Part1(root)
    #c = Canvas(self.heading, height = 1000, width = 700)
    #image = ImageTk.PhotoImage(Image.open("D\\pics\\PHOTOS\\ulaga.jpg"))
    #c.create_image(0, 0, anchor = NW, image = image)
    #c.pack()
    #root.mainloop()

class Part1(object):
    def __init__(self, heading):
        self.heading = heading
        #self.heading.title("CYBERWARRIOR")
        self.heading.geometry('1380x720')
        #self.can = Canvas(self.heading, height = 1000, width = 1000)
        can = Image.open("D:\\COLL\\wallpaper\\bridge.jpg")
        backg = ImageTk.PhotoImage(can)
        img = Label(self.heading, image = backg)
        img.image = backg
        img.place(x = -300, y = -300)
        #self.can.create_image(0, 0, anchor = CENTER, image = self.image)
        #self.heading.config(background = "D:\\pics\\PHOTOS\\ulaga.jpg")
        #self.frame = Frame(self.heading, bg = 'dark red')
        #self.can.pack(expand = YES)
        #self.can.bind('<Configure>', self.image)
        #self.heading.config.pack()
        #self.heading.can.pack()
        
        self.Username = StringVar()
        self.Password = StringVar()

        self.lblTitle = Label(self.heading, text = 'Grace Market Store', font = ('Matura MT Script Captials', 40, 'underline'), bg = 'black', fg = 'red')
        self.lblTitle.pack()#(row = 0, column = 2, columnspan = 1, pady = 0)

        #XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX#

        self.Loginframe1 = LabelFrame(self.heading, width = 100, height = 600, font =('arial', 10, 'bold'), relief = 'groove',
                                 bg = 'black', bd = 10)
        self.Loginframe1.pack()#(row = 1, column = 0)

        self.Loginframe2 = LabelFrame(self.heading, width = 100, height = 600, font =('arial', 10, 'bold'), relief = 'raised',bg = 'black', bd = 10)
        self.Loginframe2.pack()#(row = 10, column = 0)

        #XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXLABEL & ENTRY XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX        

        self.lblUsername = Label(self.Loginframe1, text = 'Username', font =('arial', 20, 'bold'), bd = 30, bg = 'black', fg = 'cornsilk')
        self.lblUsername.grid(row = 0, column = 0)
        #self.lblUsername.pack()
        
        self.txtUsername = Entry(self.Loginframe1, font = ('arial', 20, 'bold'), textvariable = self.Username, width =30)
        self.txtUsername.grid(row = 0, column = 1, columnspan = 3, padx = 10)

        self.lblPassword = Label(self.Loginframe1, text = 'Password', font =('arial', 20, 'bold'), bd = 30, bg = 'black', fg = 'cornsilk')
        self.lblPassword.grid(row = 1, column = 0)
        
        self.txtPassword = Entry(self.Loginframe1,font = ('arial', 20, 'bold'), show = "*", textvariable = self.Password, width = 30)        
        self.txtPassword.grid(row = 1, column = 1, columnspan = 3, pady = 10)

        #XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXBUTTONSXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX        

        self.btnLogin = Button(self.Loginframe2, text = 'LOGIN', width = 17, font = ('arial', 10, 'bold'), command = self.regbut2)
        self.btnLogin.grid(row = 3, column = 0, padx = 6, pady = 8)
        
        self.btnReset = Button(self.Loginframe2, text = 'RESET', width = 17, font = ('arial', 10, 'bold'), command = self.reset1)
        self.btnReset.grid(row = 3, column = 1, padx = 6, pady = 8)


        self.btnExit = Button(self.Loginframe2, text = 'EXIT', width = 17, font = ('arial', 10, 'bold'), command = self.Exit1)
        self.btnExit.grid(row = 3, column = 2, padx = 6, pady = 8)

        self.btnREG = Button(self.Loginframe2, text = 'REGISTER', width = 20, font =('arial', 10, 'bold'), command = self.new_window)
        self.btnREG.grid(row = 4, column = 1, padx = 6, pady = 8)
    

        #XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXBUTTONSXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX        

##    def Login_page(self):
##        u = (self.Username.get())
##        p = (self.Password.get())
##
##        if(u == str(123456789) and p == str(123456789)):
##            self.newWindow = Toplevel(self.heading)
##            self.app = Part2(self.newWindow)            
##
##        else:
##            tkinter.messagebox.askyesno("LOGIN SYSTEMS", "YOU ARE A FRAUD, INVALID LOGIN DETAILS")
##            self.Username.set("")
##            self.Password.set("")
##            self.txtUsername.focus() 
            
            
    def reset1(self):
        self.Username.set("")
        self.Password.set("")
        self.txtUsername.focus()

    def Exit1(self):
        self.Exit1 = tkinter.messagebox.askyesno("LOGIN SYSTEMS", "CONFIRM IF YOU WANT TO EXIT ")
        if self.Exit1 > 0:
            self.heading.destroy()
        else:
            command = self.new_part
            return
        
    def regbut2(self):
        db = MySQLdb.connect(
            host = "localhost",
            user = "root",
            passwd = "",
            database = "tkinterregister1")

        ulaga = db.cursor()
        loop = "true"
        while(loop == "true"):
            #self.regbut1()
            Username = self.Username.get()
            Password = self.Password.get()
            if(Username=="" and Password == ""):
               tkinter.messagebox.showinfo("Please enter your correct username & password")
               break
            elif(ulaga.execute("SELECT * FROM tkinterregister1 WHERE username = '"+ Username + "' AND password = '" + Password +"'")):
                self.newWindow = Toplevel(self.heading)
                self.app = Part2(self.newWindow)
                db.commit()
                break
            else:
                self.Username.set("")
                self.Password.set("")
                tkinter.messagebox.showinfo("LOGIN SYSTEMS", "YOU ARE A FRAUD, INVALID LOGIN DETAILS")
                self.txtUsername.focus()
                break
    def new_part(self):
        self.newWindow = Toplevel(self.heading)
        self.app = Part2(self.newWindow)


    def new_window(self):
        self.newWindow = Toplevel(self.heading)
        self.app = Part3(self.newWindow)

        
class Part2():
    def __init__(self, master, *args, **kwargs):
        self.master = master
        self.master.geometry('1380x720+0+0')
        can = Image.open("D:\\COLL\\wallpaper\\bluedragon.jpg")
        backg = ImageTk.PhotoImage(can)
        img = Label(self.master, image = backg)
        img.image = backg
        img.place(x = -300, y = -250)
##        self.heading.title("CYBERWARRIOR WELCOME")
##        self.heading.geometry('1280x720+0+0')
##        self.heading.config(bg = 'dark violet')
##        self.frame = Frame(self.heading, bg = 'cadet blue')
##        self.frame.pack()

        self.lblTitle = Label(self.master, text = 'WELCOME ', font = ('Elephant', 30, 'underline'), bg = 'black', fg = 'dark red')
        self.lblTitle.place(x = 50, y = 0)

        self.right = Frame(self.master, width = 600, height = 900, bg = 'cadet blue')
        self.right.pack(side = RIGHT)

        self.date1 = Label(self.right, text = 'today date:  '+str(date), font = ('courier new', 15, 'bold'), bg = 'yellow', fg = 'black')
        self.date1.place(x = 0, y = 0)

        self.rproduct = Label(self.right, text = 'Products', font = ('courier new', 15, 'bold'), bg = 'yellow', fg = 'black')
        self.rproduct.place(x = 0, y = 60)

        self.rquantity = Label(self.right, text = 'Quantity', font = ('courier new', 15, 'bold'), bg = 'yellow', fg = 'black')
        self.rquantity.place(x = 250, y = 60)

        self.ramount = Label(self.right, text = 'Amount', font = ('courier new', 15, 'bold'), bg = 'yellow', fg = 'black')
        self.ramount.place(x = 500, y = 60)
     
        self.lproduct = Label(self.master, text = 'ENTER PRODUCT ID', font = ('courier new', 20, 'bold'), bg = 'dark blue', fg = 'red')
        self.lproduct.place(x = 0, y = 100)

        self.lproducte = Entry(self.master, width = 20, font = ('arial 18 bold'), bg = 'red')
        self.lproducte.place(x = 300, y = 100)
        self.lproducte.focus()

        self.search1 = Button(self.master, text = 'Search', width = 20, height = 2, bg = 'orange', command  = self.ajax)
        self.search1.place(x = 300, y = 150)

        self.lproductname = Label(self.master, text = "", font = ('courier new', 20, 'bold'), bg = 'yellow', fg = 'black')
        self.lproductname.place(x = 0, y = 200)

        self.lprice = Label(self.master, text = "", font = ('courier new', 20, 'bold'), bg = 'yellow', fg = 'black')
        self.lprice.place(x = 0, y = 250)

        #self.lbill = Button(self.heading, text = 'Generate Bill', width = 20, height = 2, bg = 'dark red', fg = 'black')
        #self.lbill.place(x = 300, y = 350)

        self.total1 = Label(self.right, text = "", font = ("arial 30 bold"), bg = "cadetblue", fg = 'dark red')
        self.total1.place(x = 0, y = 500)
    def ajax(self, *args, **kwargs):
        self.get_id = self.lproducte.get() 
        query = "SELECT * FROM project WHERE id = ?"
        result = c.execute(query, (self.get_id,))
        for self.r in result:
            self.get_id = self.r[0]
            self.get_name = self.r[1]
            self.get_price = self.r[4]
            self.get_stock = self.r[2]
        self.lproductname.configure(text = "product Name: " + str(self.get_name  ))
        self.lprice.configure(text = "Price: Rs." + str(self.get_price))

        self.lquantity = Label(self.master, text = "Enter Quantity", font = ('courier new', 20, 'bold'), bg = 'dark blue', fg = 'red')
        self.lquantity.place(x = 20, y = 350)

        self.quantitye = Entry(self.master, width = 20, font = ('courier new',18, 'bold'), bg = 'red')
        self.quantitye.place(x = 300, y = 350)
        self.quantitye.focus()

        self.ldiscount = Label(self.master, text = "Enter Discount", font = ('courier new', 20, 'bold'), bg = 'darkblue', fg = 'red')
        self.ldiscount.place(x = 20, y = 400)

        self.discounte = Entry(self.master, width = 20, font = ('courier new',18, 'bold'), bg = 'red')
        self.discounte.place(x = 300, y = 400)
        self.discounte.insert(END, 0)

        self.laddcart = Button(self.master, text = "Add To Cart", width = 20, height = 2, bg = 'orange', command  = self.cart)
        self.laddcart.place(x = 300, y = 450)

        self.lgivenamount = Label(self.master, text = "Given Amount", font = ("courier new", 20, "bold"), bg = 'dark blue', fg = 'red')
        self.lgivenamount.place(x = 20, y = 500)

        self.givenamounte = Entry(self.master, width = 20, font = ('courier new',18, 'bold'), bg = 'red')
        self.givenamounte.place(x = 300, y = 500)

        self.ltotalprice = Button(self.master, text = "Total Price", width = 20, height = 2, bg = 'orange', command  = self.remain)
        self.ltotalprice.place(x = 300, y = 550)        

        self.lbill = Button(self.master, text = "Generate Bill", width = 108, height = 2, bg = 'Dark orange')
        self.lbill.place(x = 0, y = 660)

    def cart(self, *args, **kwargs):
        self.quantity_value = int(self.quantitye.get())
        if self.quantity_value > int(self.get_stock):
            tkinter.messagebox.showinfo("Error", "Not that many products in our project.")
        else:
            self.final_price = float(self.quantity_value) * float(self.get_price)
            products_list.append(self.get_name)
            product_price.append(self.final_price)
            product_quantity.append(self.quantity_value)
            product_id.append(self.get_id)

            self.xindex = 0
            self.yindex = 100
            self.counter = 0
            for self.p in products_list:
                self.rightname = Label(self.right, text = str(products_list[self.counter]), font = ('arial', 18, 'bold'), bg = 'cadet blue', fg = 'dark red')
                self.rightname.place(x = 0, y = self.yindex)
                self.rightquantity = Label(self.right, text = str(product_quantity[self.counter]), font = ('arial', 18, 'bold'), bg = 'cadet blue', fg = 'dark red')
                self.rightquantity.place(x = 300, y = self.yindex)
                self.rightprice = Label(self.right, text = str(product_price[self.counter]), font = ('arial', 18, 'bold'), bg = 'cadet blue', fg = 'dark red')
                self.rightprice.place(x = 500, y = self.yindex)
                self.yindex +=40
                self.counter += 1

                self.total1.configure(text = "Total: Rs. " + str(sum(product_price)))

                self.lquantity.place_forget()
                self.quantitye.place_forget()
                self.ldiscount.place_forget()
                self.discounte.place_forget()
                self.ldiscount.place_forget()
                self.discounte.place_forget()
                self.lproductname.configure(text = "")
                self.lprice.configure(text = "")
                self.laddcart.destroy()
                self.ltotalprice.destroy()
                self.lgivenamount.place_forget()
                self.givenamounte.place_forget()

    def remain(self, *args, **kwargs):
        self.amountgiven = float(self.givenamounte.get())
        self.total = float(sum(product_price))
        self.toremain = self.amountgiven - self.total
        self.camount = Label(self.right, text = "Change: Rs. "+ str(self.toremain), font = ('arial', 20, 'bold'), bg = 'cadet blue', fg = 'red')
        self.camount.place(x = 0, y = 600)
                

            
 
        #self.txtUsername = Entry(self.heading, font = ('arial', 20, 'bold'), textvariable = , width =30)
        #self.txtUsername.grid(row = 0, column = 1, columnspan = 3, padx = 10)
        
class Part3(Part1):
    def __init__(self, heading):
        self.heading = heading
        self.heading.title("REGISTER")
        self.heading.geometry('1280x720+0+0')
        self.heading.config(bg = 'dark violet')
        self.frame1 = Frame(self.heading, bg = 'dark violet')
        self.frame1.pack()

        self.USERNAME = StringVar()
        self.NICKNAME = StringVar()
        self.Password = StringVar()


        self.lblTitle = Label(self.frame1, text = 'WELCOME TO THE REGISTRATION', font = ('Agency FB', 30, 'underline'), bg = 'dark violet', fg = 'dark red')
        self.lblTitle.grid(row = 0, column = 0, columnspan = 3, pady = 40)

        self.lb1 = Label(self.frame1, text = 'Username', font =('arial', 20, 'bold'), bd = 30, bg = 'dark violet', fg = 'dark red')
        self.lb1.grid(row = 1, column = 0)
        
        self.txt1 = Entry(self.frame1,font = ('arial', 20, 'bold'), textvariable = self.USERNAME, width =20)
        self.txt1.grid(row = 1, column = 1, columnspan = 3, padx = 20)

        self.lb2 = Label(self.frame1, text = 'Nickname', font =('arial', 20, 'bold'), bd = 30, bg = 'dark violet', fg = 'dark red')
        self.lb2.grid(row = 2, column = 0)
        
        self.txt2 = Entry(self.frame1,font = ('arial', 20, 'bold'), textvariable = self.NICKNAME, width = 20)        
        self.txt2.grid(row = 2, column = 1, columnspan = 3, pady = 20)

        self.lb3 = Label(self.frame1, text = 'Password', font = ('arial', 20, 'bold'), bd = 30, bg = 'dark violet', fg = 'dark red')
        self.lb3.grid(row = 3, column = 0)

        self.txt3 = Entry(self.frame1, font = ('arial', 20, 'bold'), show = '$', textvariable = self.Password, width = 20)
        self.txt3.grid(row = 3, column = 1, columnspan = 3, padx = 20)

        self.btnreg = Button(self.frame1, text = 'REGISTER', width = 10, font = ('arial', 15, 'bold'), command = self.regbut1)
        self.btnreg.grid(row = 10, column = 0, columnspan = 3)
        

        self.Loginframe2 = LabelFrame(self.frame1, width = 700, height = 100, font =('arial', 10, 'bold'), relief = 'raised',bg = 'black', bd = 10)
        self.Loginframe2.grid(row = 4, column = 0, columnspan = 3)

        self.lblUsername = Label(self.Loginframe2, text = 'AGREE TERMS & CONDITIONS', font =('arial', 20, 'bold'), bd = 30, bg = 'dark violet', fg = 'white')
        self.lblUsername.grid(row = 0, column = 0)


        #self.txt1 = StringVar()
        #self.txt3 = StringVar()


    def regbut1(self):
        mydb = mysql.connector.connect(
            host = "localhost",
            user = "root",
            passwd = "",
            database = "tkinterregister1")

        mycursor = mydb.cursor()

        sql="INSERT INTO tkinterregister1(Username,Password) VALUES (%s,%s)"
        val=(self.txt1.get(),self.txt3.get())

        mycursor.execute(sql,val)
        mydb.commit()

        print(mycursor.rowcount,"record inserted")

        
        #self.regbut1 = tkinter.messagebox.askyesno("LOGIN SYSTEMS", "CONFIRM IF YOU WANT TO EXIT ")

        self.msg1=messagebox.showinfo("Username and Password saved")
        self.heading.destroy()
        b = Part3()
        b.regbut2()
        
        #if self.regbut1 > 0:
        #    self.frame1.destroy()
        #else:
        #    pass
                
   
if __name__ == '__main__':
    main()
    
