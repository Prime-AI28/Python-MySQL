# -*- coding: utf-8 -*-
"""
Created on Thu Dec 10 22:03:53 2020

@author: prabh
"""

from tkinter import *
import time
import datetime
from tkinter import messagebox
import mysql.connector as mysql
from PIL import ImageTk, Image


home = Tk()
home.title("Database Management")
# home.iconbitmap('c:/pics/appimg.ico')
home.configure(bg="#FFCCBC")
# home.geometry('300x300')


def Admin():

    login_a = Toplevel()
    login_a.title("Admin Login")
    login_a.configure(bg='#FFEB3B')

    p = "admin"

    def login():
        pas = passwd.get()
        db_pass = db_passwd.get()
        # db_pass= Prime&2811

        if pas == p:
            print(db_pass)

            login_a.destroy()

            root = Toplevel()
            root.title('Databases')
            # root.iconbitmap('c:/pics/appimg.ico')
            root.configure(bg='#03A9F4')
            # root.geometry("400x400")

            def Attendance_record_delete():
                ID = Edit_ID.get()

                db = mysql.connect(host="localhost", user="root",
                                   passwd=db_pass, database="emp_info")
                # Create cursor
                c = db.cursor()

                # Insert into tabel
                query = "DROP TABLE `emp_info`.`emp_%s`;" % (ID)

                c.execute(query)

                db.commit()
                db.close()

            def Attendance_record():
                ID = Emp_ID.get()

                db = mysql.connect(host="localhost", user="root",
                                   passwd=db_pass, database="emp_info")
                # Create cursor
                c = db.cursor()

                # Insert into tabel
                query = "CREATE TABLE `emp_info`.`emp_%s` ( `Date` DATE NOT NULL, `In_time` TIME NOT NULL, `Out_time` TIME NULL, PRIMARY KEY (`Date`))" % (
                    ID)

                c.execute(query)

                db.commit()
                db.close()

           # create Submit Function
            def submit():
                # connect to datbase
                db = mysql.connect(host="localhost", user="root",
                                   passwd=db_pass, database="emp_info")
                # Create cursor
                c = db.cursor()

                # Insert into tabel
                query = "insert into emp_data(Emp_ID, Emp_Name, Emp_Address, Emp_Status, Emp_DOB, Emp_Salary, Emp_Passwd, Emp_Remark) values (%s,%s,%s,%s,%s,%s,%s,%s)"

                value = [Emp_ID.get(),
                         Emp_Name.get(),
                         Emp_Address.get(),
                         Emp_Status.get(),
                         Emp_DOB.get(),
                         Emp_Salary.get(),
                         Emp_Passwd.get(),
                         Emp_Remark.get()
                         ]
                c.execute(query, value)

                db.commit()
                db.close()

                Attendance_record()

                # clear the box
                Emp_ID.delete(0, END)
                Emp_Name.delete(0, END)
                Emp_Address.delete(0, END)
                Emp_Status.delete(0, END)
                Emp_DOB.delete(0, END)
                Emp_Salary.delete(0, END)
                Emp_Passwd.delete(0, END)
                Emp_Remark.delete(0, END)

                print("Employee Information Successfully added to records")

            def query():

                # connect to datbase
                db = mysql.connect(host="localhost", user="root",
                                   passwd=db_pass, database="emp_info")
                # Create cursor
                c = db.cursor()

                c.execute("SELECT * from emp_data")
                d = c.fetchall()

                data = ''
                global root2

                root2 = Toplevel()
                root2.title('Databases')
                # root2.iconbitmap('c:/pics/appimg.ico')
                root2.configure(bg='#03A9F4')

                rec = LabelFrame(root2, text="Employee Information",
                                 padx=70, pady=50, bg='#A9DFBF',  relief=RIDGE, bd=6)
                rec.grid(row=2, column=0)

                for i in d:
                    for j in range(0, 9):
                        data_1 = str(i[0:3])
                        Dob = str(i[3])
                        data_2 = str(Dob)
                        data_3 = str(i[4:])

                        data = (data_1+','+data_2+','+data_3)

                    print(data, end="\n")
                    query_lbl = Label(rec, text=data, bg='#A9DFBF')
                    query_lbl.pack()
                    # query_lbl.(row=0, column=0)
                    # data += str(i)+"\n"+"\n"
                    # print ()

                db.commit()
                db.close()

            def delete():

                root2.destroy()

                db = mysql.connect(host="localhost", user="root",
                                   passwd=db_pass, database="emp_info")

                # Create cursor
                c = db.cursor()

                ID = Edit_ID.get()
                print(ID, "Record deleted")

                query = "DELETE FROM `emp_info`.`emp_data` WHERE (`Emp_ID` = %s); " % (
                    ID)

                c.execute(query)

                db.commit()
                db.close()

                Attendance_record_delete()

            def update_screen():

                global Updt

                Updt = Toplevel()
                Updt.title('UPDATE')
                # Updt.iconbitmap('c:/pics/appimg.ico')
                Updt.configure(bg="#F6DDCC")

                global ID

                ID = [Edit_ID.get()]

                db = mysql.connect(host="localhost", user="root",
                                   passwd=db_pass, database="emp_info")
                c = db.cursor()

                query = "Select * from `emp_info`.`emp_data` WHERE (`Emp_ID` = %s);"
                c.execute(query, ID)

                d = c.fetchall()
                for i in d:
                    print(i, end="\n")

                f_au = LabelFrame(Updt, padx=10, pady=10,
                                  bg='#FFFFCC',  relief=RIDGE, bd=6)
                f_au.grid(row=0, column=0)

                global Emp_ID_ed, Emp_Name_ed, Emp_Address_ed, Emp_Status_ed, Emp_DOB_ed, Emp_Salary_ed, Emp_Attend_ed, Emp_Passwd_ed, Emp_Remark_ed

                # Create text boxes

                Emp_ID_ed = Entry(f_au, width=30, font=(
                    'Courier New', 16, 'bold', 'italic'), bd=5, justify='left')
                Emp_ID_ed.grid(row=0, column=1, padx=20)
                Emp_ID_ed.insert(0,  d[0][0])
                Emp_Name_ed = Entry(f_au, width=30, font=(
                    'Courier New', 16, 'bold', 'italic'), bd=5, justify='left')
                Emp_Name_ed.grid(row=1, column=1, padx=20)
                Emp_Name_ed.insert(0,  d[0][1])
                Emp_Address_ed = Entry(f_au, width=30, font=(
                    'Courier New', 16, 'bold', 'italic'), bd=5, justify='left')
                Emp_Address_ed.grid(row=2, column=1, padx=20)
                Emp_Address_ed.insert(0,  d[0][2])
                Emp_DOB_ed = Entry(f_au, width=30, font=(
                    'Courier New', 16, 'bold', 'italic'), bd=5, justify='left')
                Emp_DOB_ed.grid(row=3, column=1, padx=20)
                Emp_DOB_ed.insert(0, str(d[0][3]))
                Emp_Status_ed = Entry(f_au, width=30, font=(
                    'Courier New', 16, 'bold', 'italic'), bd=5, justify='left')
                Emp_Status_ed.grid(row=4, column=1, padx=20)
                Emp_Status_ed.insert(0,  d[0][4])
                Emp_Salary_ed = Entry(f_au, width=30, font=(
                    'Courier New', 16, 'bold', 'italic'), bd=5, justify='left')
                Emp_Salary_ed.grid(row=5, column=1, padx=20)
                Emp_Salary_ed.insert(0,  d[0][5])
                Emp_Passwd_ed = Entry(f_au, width=30, font=(
                    'Courier New', 16, 'bold', 'italic'), bd=5, justify='left')
                Emp_Passwd_ed.grid(row=7, column=1, padx=20)
                Emp_Passwd_ed.insert(0,  d[0][6])
                Emp_Remark_ed = Entry(f_au, width=30, font=(
                    'Courier New', 16, 'bold', 'italic'), bd=5, justify='left')
                Emp_Remark_ed.grid(row=8, column=1, padx=20)
                Emp_Remark_ed.insert(0,  d[0][7])

                # Create Text Box Labels

                Emp_ID_lbl = Label(f_au, text="ID No.", bg='#FFFFCC')
                Emp_ID_lbl.grid(row=0, column=0)
                Emp_Name_lbl = Label(f_au, text="Name", bg='#FFFFCC')
                Emp_Name_lbl.grid(row=1, column=0)
                Emp_Address_lbl = Label(f_au, text="Address", bg='#FFFFCC')
                Emp_Address_lbl.grid(row=2, column=0)
                Emp_DOB_lbl = Label(f_au, text="Date of Birth", bg='#FFFFCC')
                Emp_DOB_lbl.grid(row=3, column=0)
                Emp_Status_lbl = Label(f_au, text="Position", bg='#FFFFCC')
                Emp_Status_lbl.grid(row=4, column=0)
                Emp_Salary_lbl = Label(f_au, text="Salary", bg='#FFFFCC')
                Emp_Salary_lbl.grid(row=5, column=0)
                Emp_Passwd_lbl = Label(f_au, text="Password", bg='#FFFFCC')
                Emp_Passwd_lbl.grid(row=7, column=0)
                Emp_Remark_lbl = Label(f_au, text="Remarks", bg='#FFFFCC')
                Emp_Remark_lbl.grid(row=8, column=0)

                save_btn = Button(f_au, text="Save Record",
                                  command=update, padx=5, pady=5, bd=8)
                save_btn.grid(row=10, column=1, columnspan=2,
                              padx=10, pady=10, ipadx=98)

                db.commit()
                db.close()

            def update():
                # connect to datbase
                db = mysql.connect(host="localhost", user="root",
                                   passwd=db_pass, database="emp_info")
                # Create cursor
                c = db.cursor()

                value = [Emp_Name_ed.get(),
                         Emp_Address_ed.get(),
                         Emp_Status_ed.get(),
                         Emp_DOB_ed.get(),
                         Emp_Salary_ed.get(),
                         Emp_Passwd_ed.get(),
                         Emp_Remark_ed.get(),
                         Edit_ID.get()]

                # Insert into tabel
                print(value)

                query = "UPDATE `emp_info`.`emp_data` SET  `Emp_Name`= '%s',  `Emp_Address`= '%s',  `Emp_Status`= '%s',  `Emp_DOB`= '%s',  `Emp_Salary`= '%s', `Emp_Passwd`= '%s',  `Emp_Remark`= '%s' WHERE (`Emp_ID` = '%s')" % (
                    Emp_Name_ed.get(), Emp_Address_ed.get(), Emp_Status_ed.get(), str(Emp_DOB_ed.get()), Emp_Salary_ed.get(), Emp_Passwd_ed.get(), Emp_Remark_ed.get(), Edit_ID.get())

                c.execute(query)

                Updt.destroy()

                db.commit()
                db.close()

            def exit2():
                exit2 = messagebox.askyesno(
                    "Employee system", "Do you want to exit the system")
                if exit2 > 0:
                    root.destroy()
                    return

            f_a = LabelFrame(root, padx=10, pady=10,
                             bg='#FFFFCC',  relief=RIDGE, bd=6)
            f_a.grid(row=0, column=0)

            # Create text boxes

            Emp_ID = Entry(f_a, width=30, font=(
                'Courier New', 16, 'bold', 'italic',), bd=5, justify='left')
            Emp_ID.grid(row=0, column=1, padx=20)
            Emp_Name = Entry(f_a, width=30, font=(
                'Courier New', 16, 'bold', 'italic'), bd=5, justify='left')
            Emp_Name.grid(row=1, column=1, padx=20)
            Emp_Address = Entry(f_a, width=30, font=(
                'Courier New', 16, 'bold', 'italic'), bd=5, justify='left')
            Emp_Address.grid(row=2, column=1, padx=20)
            Emp_DOB = Entry(f_a, width=30, font=(
                'Courier New', 16, 'bold', 'italic'), bd=5, justify='left')
            Emp_DOB.grid(row=3, column=1, padx=20)
            Emp_DOB.insert(0, "yyyy-mm-dd")
            Emp_Status = Entry(f_a, width=30, font=(
                'Courier New', 16, 'bold', 'italic'), bd=5, justify='left')
            Emp_Status.grid(row=4, column=1, padx=20)
            Emp_Salary = Entry(f_a, width=30, font=(
                'Courier New', 16, 'bold', 'italic'), bd=5, justify='left')
            Emp_Salary.grid(row=5, column=1, padx=20)
            Emp_Passwd = Entry(f_a, width=30, font=(
                'Courier New', 16, 'bold', 'italic'), bd=5, justify='left')
            Emp_Passwd.grid(row=7, column=1, padx=20)
            Emp_Remark = Entry(f_a, width=30, font=(
                'Courier New', 16, 'bold', 'italic'), bd=5, justify='left')
            Emp_Remark.grid(row=8, column=1, padx=20)

            # Create Text Box Labels

            Emp_ID_lbl = Label(f_a, text="ID No.", bg='#FFFFCC')
            Emp_ID_lbl.grid(row=0, column=0)
            Emp_Name_lbl = Label(f_a, text="Name", bg='#FFFFCC')
            Emp_Name_lbl.grid(row=1, column=0)
            Emp_Address_lbl = Label(f_a, text="Address", bg='#FFFFCC')
            Emp_Address_lbl.grid(row=2, column=0)
            Emp_DOB_lbl = Label(f_a, text="Date of Birth", bg='#FFFFCC')
            Emp_DOB_lbl.grid(row=3, column=0)
            Emp_Status_lbl = Label(f_a, text="Position", bg='#FFFFCC')
            Emp_Status_lbl.grid(row=4, column=0)
            Emp_Salary_lbl = Label(f_a, text="Salary", bg='#FFFFCC')
            Emp_Salary_lbl.grid(row=5, column=0)
            Emp_Passwd_lbl = Label(f_a, text="Password", bg='#FFFFCC')
            Emp_Passwd_lbl.grid(row=7, column=0)
            Emp_Remark_lbl = Label(f_a, text="Remarks", bg='#FFFFCC')
            Emp_Remark_lbl.grid(row=8, column=0)

            f_ab = LabelFrame(root, padx=70, pady=10,
                              bg='#212121',  relief=GROOVE, bd=6)
            f_ab.grid(row=1, column=0)

            # Create Submit Button
            add_btn = Button(f_ab, text="Add Record",
                             command=submit, padx=5, pady=5, bd=8)
            add_btn.grid(row=1, column=1, columnspan=2,
                         padx=10, pady=10, ipadx=88)
            # Create query Button
            query_btn = Button(f_ab, text="Show Records",
                               command=query, padx=5, pady=5, bd=8)
            query_btn.grid(row=2, column=1, columnspan=2,
                           padx=10, pady=10, ipadx=82)

            Edit_ID = Entry(f_ab, width=17, font=(
                'Courier New', 18, 'bold', 'italic',), bd=5, justify='left')
            Edit_ID.grid(row=3, column=1, padx=20, columnspan=2)

            Edit_ID_lbl = Label(
                f_ab, text="Select ID", bg='#D5D8DC', fg='#455A64', font=('Book Antiqua', 18))
            Edit_ID_lbl.grid(row=3, column=0)

            # Create Delete Button
            delete_btn = Button(f_ab, text="Delete Records",
                                command=delete, padx=5, pady=5, bd=8)
            delete_btn.grid(row=4, column=1, columnspan=2,
                            padx=10, pady=10, ipadx=80)
            # Create Update Button
            update_btn = Button(f_ab, text="Edit Record",
                                command=update_screen, padx=5, pady=5, bd=8)
            update_btn.grid(row=5, column=1, columnspan=2,
                            padx=10, pady=10, ipadx=90)

            # Create Exit button
            exit_btn = Button(f_ab, text="Exit",
                              command=exit2, padx=5, pady=5, bd=8)
            exit_btn.grid(row=6, column=1, columnspan=2,
                          padx=10, pady=10, ipadx=109)

            root.mainloop()

        else:
            messagebox.showwarning("Login Error", "Credentials are Incorrect")

    user_lbl = Label(login_a, text="User Name", bg='#FFEB3B')
    user_lbl.grid(row=0, column=0)
    passwd_lbl = Label(login_a, text="Password", bg='#FFEB3B')
    passwd_lbl.grid(row=1, column=0)
    db_passwd_lbl = Label(login_a, text="Database Passwd", bg='#FFEB3B')
    db_passwd_lbl.grid(row=2, column=0)

    user = Entry(login_a, width=20, font=('Courier New', 16,
                 'bold', 'italic',), bd=5, justify='left')
    user.grid(row=0, column=1, padx=20)
    user.insert(0, "ADMIN")

    passwd = Entry(login_a, show="*",  width=20, font=('Courier New',
                   16, 'bold', 'italic',), bd=5, justify='left')
    passwd.grid(row=1, column=1, padx=20)

    db_passwd = Entry(login_a, show="*",  width=20, font=('Courier New',
                      16, 'bold', 'italic',), bd=5, justify='left')
    db_passwd.grid(row=2, column=1, padx=20)

    submit_btn = Button(login_a, text="Login",
                        command=login, padx=5, pady=5, bd=8)
    submit_btn.grid(row=3, column=0, columnspan=2, padx=10, pady=10, ipadx=104)

    login_a.mainloop()


def Emp():

    conn = mysql.connect(host="localhost", user="root",
                         passwd="Prime&2811", database="emp_info")
    c = conn.cursor()

    root = Toplevel()
    root.title("EMPLOYEE")
    # root.geometry("300x300")
    root.configure(bg="#F38F3C", bd=5)
    # root.iconbitmap("c:/pics/appimg.ico")

    def popup():
        m = messagebox.askyesno(
            "confirmation", "Are You Sure You Want To Exit")
        if (m == True):
            root.destroy()

    def update1():
        def check():
            k = 0
            import mysql.connector as mysql
            conn = mysql.connect(host="localhost", user="root",
                                 passwd="Prime&2811", database="emp_info")
            c = conn.cursor()
            c.execute("SELECT Emp_ID,Emp_Passwd from emp_data")
            m = c.fetchall()
            # h.delete(0,END)
            f = h.get()
            g = p.get()
            x = (f, g)

            def update():
                conn = mysql.connect(
                    host="localhost", user="root", passwd="Prime&2811", database="emp_info")
                c = conn.cursor()
                global hm
                hm = Toplevel()
                hm.title("Update")
                hm.geometry("390x200")
                hm.configure(bg="#AACFD1")
                # hm.iconbitmap("c:/pics/appimg.ico")

                # creating entry widgets
                addup = Entry(hm, width=30, font=('Courier New', 10, 'bold'))
                # a=str(addup.get())

                def save():
                    conn = mysql.connect(
                        host="localhost", user="root", passwd="Prime&2811", database="emp_data")
                    c = conn.cursor()

                    ID = int(h.get())

                    query = " UPDATE emp_data SET Emp_Address = %s  WHERE (Emp_ID= %s) "
                    value = (addup.get(), ID)
                    c.execute(query, value)
                    messagebox.showinfo(
                        "Success", "Your address was successfully updated")

                    print(c.rowcount, "record(s) affected")
                    addup.delete(0, END)
                    conn.commit()
                    conn.close()
                    # creating labels
                l1 = Label(hm, text="New Address*", bg="#AACFD1")
                save_bttn = Button(hm, text="Save", command=save)

                # placing labels/entry widget
                addup.grid(row=0, column=1, padx=10)
                l1.grid(row=0, column=0, padx=5)
                save_bttn.grid(row=1, column=1, padx=10)

            for i in m:
                if (int(f) == i[0] and g == i[1]):
                    update()

                else:
                    k = k+1
                    continue

            if (k == len(m)):
                m = messagebox.showinfo(
                    "ERROR", "The entered ID/ Password is wrong", icon="warning")

        global hm1
        hm1 = Toplevel()
        # hm1.iconbitmap("c:/pics/appimg.ico")
        hm1.title("Authorisation")
        hm1.configure(bg="#E3E23C")
        hm1.geometry("330x100")
        h = Entry(hm1, width=30, font=('Courier New', 10, 'bold'))
        p = Entry(hm1, width=30, font=('Courier New', 10, 'bold'), show="*")
        h.grid(row=0, column=1)
        p.grid(row=1, column=1)
        l = Label(hm1, text="Employee ID:", bg="#E3E23C")
        n = Label(hm1, text="Password:", bg="#E3E23C")
        l.grid(row=0, column=0)
        n.grid(row=1, column=0)
        # x=h.get()
        ch = Button(hm1, text="Verify", command=check)
        ch.grid(row=2, column=1, columnspan=2)

    def bill():
        from tkinter import ttk
        import tkinter.messagebox as tmsg
        import os
        import time

        # ===================Python Variables===================
        catalog_category = ["Sedan", "Coupe", "Sports Car",
                            "Station Wagon", "Hatchback", "Convertible", "SUV"]

        catalog_category_dict = {"Sedan": "1 Sedan.txt", "Coupe": "2 Coupe.txt",
                                 "Sports Car": "3 Sports Car.txt", "Station Wagon": "4 Station Wagon.txt",
                                 "Hatchback": "5 Hatchback.txt", "Convertible": "6 Convertible.txt",
                                 "SUV": "7 SUV.txt"}

        order_dict = {}
        for i in catalog_category:
            order_dict[i] = {}

        os.chdir(os.path.dirname(os.path.abspath(__file__)))
        # ====================Backend Functions====================

        def load_catalog():
            catalogCategory.set("")
            catalog_tabel.delete(*catalog_tabel.get_children())
            catalog_file_list = os.listdir("catalog")
            for file in catalog_file_list:
                f = open("catalog\\" + file, "r")
                category = ""
                while True:
                    line = f.readline()
                    if (line == ""):
                        catalog_tabel.insert('', END, values=["", "", ""])
                        break
                    elif (line == "\n"):
                        continue
                    elif (line[0] == '#'):
                        category = line[1:-1]
                        name = "\t\t"+line[:-1]
                        price = ""
                    elif (line[0] == '*'):
                        name = line[:-1]
                        price = ""
                    else:
                        name = line[:line.rfind(" ")]
                        price = line[line.rfind(" ")+1:-3]

                    catalog_tabel.insert(
                        '', END, values=[name, price, category])

        def load_order():
            order_tabel.delete(*order_tabel.get_children())
            for category in order_dict.keys():
                if order_dict[category]:
                    for lis in order_dict[category].values():
                        order_tabel.insert('', END, values=lis)
            update_total_price()

        def add_button_operation():
            name = itemName.get()
            rate = itemRate.get()
            category = itemCategory.get()
            quantity = itemQuantity.get()

            if name in order_dict[category].keys():
                tmsg.showinfo("Error", "Item already exist in your order")
                return
            if not quantity.isdigit():
                tmsg.showinfo("Error", "Please Enter Valid Quantity")
                return
            lis = [name, rate, quantity, str(
                int(rate)*int(quantity)), category]
            order_dict[category][name] = lis
            load_order()

        def load_item_from_catalog(event):
            cursor_row = catalog_tabel.focus()
            contents = catalog_tabel.item(cursor_row)
            row = contents["values"]

            itemName.set(row[0])
            itemRate.set(row[1])
            itemCategory.set(row[2])
            itemQuantity.set("1")

        def load_item_from_order(event):
            cursor_row = order_tabel.focus()
            contents = order_tabel.item(cursor_row)
            row = contents["values"]

            itemName.set(row[0])
            itemRate.set(row[1])
            itemQuantity.set(row[2])
            itemCategory.set(row[4])

        def show_button_operation():
            category = catalogCategory.get()
            if category not in catalog_category:
                tmsg.showinfo("Error", "Please select valid Choice")
            else:
                catalog_tabel.delete(*catalog_tabel.get_children())
                f = open("catalog\\" + catalog_category_dict[category], "r")
                while True:
                    line = f.readline()
                    if (line == ""):
                        break
                    if (line[0] == '#' or line == "\n"):
                        continue
                    if (line[0] == '*'):
                        name = "\t"+line[:-1]
                        catalog_tabel.insert('', END, values=[name, "", ""])
                    else:
                        name = line[:line.rfind(" ")]
                        price = line[line.rfind(" ")+1:-3]
                        catalog_tabel.insert(
                            '', END, values=[name, price, category])

        def clear_button_operation():
            itemName.set("")
            itemRate.set("")
            itemQuantity.set("")
            itemCategory.set("")

        def cancel_button_operation():
            names = []
            for i in catalog_category:
                names.extend(list(order_dict[i].keys()))
            if len(names) == 0:
                tmsg.showinfo("Error", "Your order list is Empty")
                return
            ans = tmsg.askquestion(
                "Cancel Order", "Are You Sure to Cancel Order?")
            if ans == "no":
                return
            order_tabel.delete(*order_tabel.get_children())
            for i in catalog_category:
                order_dict[i] = {}
            clear_button_operation()
            update_total_price()

        def update_button_operation():
            name = itemName.get()
            rate = itemRate.get()
            category = itemCategory.get()
            quantity = itemQuantity.get()

            if category == "":
                return
            if name not in order_dict[category].keys():
                tmsg.showinfo("Error", "Item is not in your order list")
                return
            if order_dict[category][name][2] == quantity:
                tmsg.showinfo("Error", "No changes in Quantity")
                return
            order_dict[category][name][2] = quantity
            order_dict[category][name][3] = str(int(rate)*int(quantity))
            load_order()

        def remove_button_operation():
            name = itemName.get()
            category = itemCategory.get()

            if category == "":
                return
            if name not in order_dict[category].keys():
                tmsg.showinfo("Error", "Item is not in your order list")
                return
            del order_dict[category][name]
            load_order()

        def update_total_price():
            price = 0
            for i in catalog_category:
                for j in order_dict[i].keys():
                    price += int(order_dict[i][j][3])
            if price == 0:
                totalPrice.set("")
            else:
                totalPrice.set("Rs. "+str(price)+"  /-")

        def bill_button_operation():
            customer_name = customerName.get()
            customer_contact = customerContact.get()
            names = []
            for i in catalog_category:
                names.extend(list(order_dict[i].keys()))
            if len(names) == 0:
                tmsg.showinfo("Error", "Your order list is Empty")
                return
            if customer_name == "" or customer_contact == "":
                tmsg.showinfo("Error", "Customer Details Required")
                return
            if not customerContact.get().isdigit():
                tmsg.showinfo("Error", "Invalid Customer Contact")
                return
            ans = tmsg.askquestion(
                "Generate Bill", "Are You Sure to Generate Bill?")
            ans = "yes"
            if ans == "yes":
                bill = Toplevel()
                bill.title("Bill")
                bill.geometry("670x500+300+100")
                bill_text_area = Text(bill, font=("arial", 12))
                st = "\t\t\t\tLucoe Showroom\n\t\t\tmillenium tower, sanpada-400701\n"
                st += "\t\t\tGST.NO:- 27AHDGHJJIFNHIZH\n"
                st += "-"*61 + "BILL" + "-"*61 + "\nDate:- "

                # Date and time
                t = time.localtime(time.time())
                week_day_dict = {0: "Monday", 1: "Tuesday", 2: "Wednesday", 3: "Thursday", 4: "Friday", 5: "Saturday",
                                    6: "Sunday"}
                st += f"{t.tm_mday} / {t.tm_mon} / {t.tm_year} ({week_day_dict[t.tm_wday]})"
                st += " "*10 + \
                    f"\t\t\t\t\t\tTime:- {t.tm_hour} : {t.tm_min} : {t.tm_sec}"

                # Customer Name & Contact
                st += f"\nCustomer Name:- {customer_name}\nCustomer Contact:- {customer_contact}\n"
                st += "-"*130 + "\n" + " "*4 + "DESCRIPTION\t\t\t\t\tRATE\tQUANTITY\t\tAMOUNT\n"
                st += "-"*130 + "\n"

                # List of Items
                for i in catalog_category:
                    for j in order_dict[i].keys():
                        lis = order_dict[i][j]
                        name = lis[0]
                        rate = lis[1]
                        quantity = lis[2]
                        price = lis[3]
                        st += name + "\t\t\t\t\t" + rate + "\t      " + \
                            quantity + "\t\t  " + price + "\n\n"
                st += "-"*130

                # Total Price
                st += f"\n\t\t\tTotal price (in lakhs) : {totalPrice.get()}\n"
                st += "-"*130

                # display bill in new window
                bill_text_area.insert(1.0, st)

                # write into file
                folder = f"{t.tm_mday},{t.tm_mon},{t.tm_year}"
                if not os.path.exists(f"Bill Records\\{folder}"):
                    os.makedirs(f"Bill Records\\{folder}")
                file = open(
                    f"Bill Records\\{folder}\\{customer_name+customer_contact}.txt", "w")
                file.write(st)
                file.close()

                # Clear operaitons
                order_tabel.delete(*order_tabel.get_children())
                for i in catalog_category:
                    order_dict[i] = {}
                clear_button_operation()
                update_total_price()
                customerName.set("")
                customerContact.set("")

                bill_text_area.pack(expand=True, fill=BOTH)
                bill.focus_set()
                # bill.protocol("WM_DELETE_WINDOW", close_window)

        def close_window():
            tmsg.showinfo("Thanks", "Thanks for using our service")
            root.destroy()
        # [name,rate,quantity,str(int(rate)*int(quantity)),category]
        # ==================Backend Code Ends===============

        # ================Frontend Code Start==============
        root_s = Toplevel()
        w, h = root_s.winfo_screenwidth(), root_s.winfo_screenheight()
        root_s.geometry("%dx%d+0+0" % (w, h))
        root_s.title("Welcome to Lucoe Showroom")
        # root_s.attributes('-fullscreen', True)
        # root_s.resizable(0, 0)

        # ================Title==============
        style_button = ttk.Style()
        style_button.configure("TButton", font=("arial", 10, "bold"),
                               background="darkgrey")

        title_frame = Frame(root_s, bd=8, bg="black", relief=GROOVE)
        title_frame.pack(side=TOP, fill="x")

        title_label = Label(title_frame, text="Lucoe Showroom",
                            font=("algerian", 20, "bold"), bg="black", fg="grey", pady=5)
        title_label.pack()

        # ==============Customer=============
        customer_frame = LabelFrame(root_s, text="Customer Details", font=("times new roman", 15, "bold"),
                                    bd=8, bg="grey", relief=GROOVE)
        customer_frame.pack(side=TOP, fill="x")

        customer_name_label = Label(customer_frame, text="Name",
                                    font=("arial", 15, "bold"), bg="grey", fg="darkblue")
        customer_name_label.grid(row=0, column=0)

        customerName = StringVar()
        customerName.set("")
        customer_name_entry = Entry(customer_frame, width=20, font="arial 15", bd=5,
                                    textvariable=customerName)
        customer_name_entry.grid(row=0, column=1, padx=50)

        customer_contact_label = Label(customer_frame, text="Contact",
                                       font=("arial", 15, "bold"), bg="grey", fg="darkblue")
        customer_contact_label.grid(row=0, column=2)

        customerContact = StringVar()
        customerContact.set("")
        customer_contact_entry = Entry(customer_frame, width=20, font="arial 15", bd=5,
                                       textvariable=customerContact)
        customer_contact_entry.grid(row=0, column=3, padx=50)

        # ===============Catalog===============
        catalog_frame = Frame(root_s, bd=8, bg="darkgrey", relief=GROOVE)
        catalog_frame.place(x=0, y=125, height=585, width=680)

        catalog_label = Label(catalog_frame, text="catalog",
                              font=("times new roman", 20, "bold"), bg="darkblue", fg="darkgrey", pady=0)
        catalog_label.pack(side=TOP, fill="x")

        catalog_category_frame = Frame(catalog_frame, bg="darkgrey", pady=10)
        catalog_category_frame.pack(fill="x")

        combo_lable = Label(catalog_category_frame, text="Select Type",
                            font=("arial", 12, "bold"), bg="darkgrey", fg="darkblue")
        combo_lable.grid(row=0, column=0, padx=10)

        catalogCategory = StringVar()
        combo_catalog = ttk.Combobox(catalog_category_frame, values=catalog_category,
                                     textvariable=catalogCategory)
        combo_catalog.grid(row=0, column=1, padx=30)

        show_button = ttk.Button(catalog_category_frame, text="Show", width=10,
                                 command=show_button_operation)
        show_button.grid(row=0, column=2, padx=60)

        show_all_button = ttk.Button(catalog_category_frame, text="Show All",
                                     width=10, command=load_catalog)
        show_all_button.grid(row=0, column=3)

        ####################### Catalog Tabel #######################
        catalog_tabel_frame = Frame(catalog_frame)
        catalog_tabel_frame.pack(fill=BOTH, expand=1)

        scrollbar_catalog_x = Scrollbar(catalog_tabel_frame, orient=HORIZONTAL)
        scrollbar_catalog_y = Scrollbar(catalog_tabel_frame, orient=VERTICAL)

        style = ttk.Style()
        style.configure("Treeview.Heading", font=("arial", 13, "bold"))
        style.configure("Treeview", font=("arial", 12), rowheight=25)

        catalog_tabel = ttk.Treeview(catalog_tabel_frame, style="Treeview",
                                     columns=("name", "price", "category"), xscrollcommand=scrollbar_catalog_x.set,
                                     yscrollcommand=scrollbar_catalog_y.set)

        catalog_tabel.heading("name", text="Name")
        catalog_tabel.heading("price", text="Price")
        catalog_tabel["displaycolumns"] = ("name", "price")
        catalog_tabel["show"] = "headings"
        catalog_tabel.column("price", width=50, anchor='center')

        scrollbar_catalog_x.pack(side=BOTTOM, fill=X)
        scrollbar_catalog_y.pack(side=RIGHT, fill=Y)

        scrollbar_catalog_x.configure(command=catalog_tabel.xview)
        scrollbar_catalog_y.configure(command=catalog_tabel.yview)

        catalog_tabel.pack(fill=BOTH, expand=1)

        load_catalog()
        catalog_tabel.bind("<ButtonRelease-1>", load_item_from_catalog)

        ########################################################################

        # ===============Item Frame=============
        item_frame = Frame(root_s, bd=8, bg="darkgrey", relief=GROOVE)
        item_frame.place(x=680, y=125, height=230, width=680)

        item_title_label = Label(item_frame, text="Item",
                                 font=("times new roman", 20, "bold"), bg="darkblue", fg="darkgrey")
        item_title_label.pack(side=TOP, fill="x")

        item_frame2 = Frame(item_frame, bg="darkgrey")
        item_frame2.pack(fill=X)

        item_name_label = Label(item_frame2, text="Name",
                                font=("arial", 12, "bold"), bg="darkgrey", fg="darkblue")
        item_name_label.grid(row=0, column=0)

        itemCategory = StringVar()
        itemCategory.set("")

        itemName = StringVar()
        itemName.set("")
        item_name = Entry(item_frame2, font="arial 12",
                          textvariable=itemName, state=DISABLED, width=25)
        item_name.grid(row=0, column=1, padx=10)

        item_rate_label = Label(item_frame2, text="Rate (in lakhs)",
                                font=("arial", 12, "bold"), bg="darkgrey", fg="darkblue")
        item_rate_label.grid(row=0, column=2, padx=40)

        itemRate = StringVar()
        itemRate.set("")
        item_rate = Entry(item_frame2, font="arial 12",
                          textvariable=itemRate, state=DISABLED, width=10)
        item_rate.grid(row=0, column=3, padx=10)

        item_quantity_label = Label(item_frame2, text="Quantity",
                                    font=("arial", 12, "bold"), bg="darkgrey", fg="darkblue")
        item_quantity_label.grid(row=1, column=0, padx=30, pady=15)

        itemQuantity = StringVar()
        itemQuantity.set("")
        item_quantity = Entry(item_frame2, font="arial 12",
                              textvariable=itemQuantity, width=10)
        item_quantity.grid(row=1, column=1)

        item_frame3 = Frame(item_frame, bg="darkgrey")
        item_frame3.pack(fill=X)

        add_button = ttk.Button(
            item_frame3, text="Add Item", command=add_button_operation)
        add_button.grid(row=0, column=0, padx=40, pady=30)

        remove_button = ttk.Button(
            item_frame3, text="Remove Item", command=remove_button_operation)
        remove_button.grid(row=0, column=1, padx=40, pady=30)

        update_button = ttk.Button(
            item_frame3, text="Update Quantity", command=update_button_operation)
        update_button.grid(row=0, column=2, padx=40, pady=30)

        clear_button = ttk.Button(item_frame3, text="Clear",
                                  width=8, command=clear_button_operation)
        clear_button.grid(row=0, column=3, padx=40, pady=30)

        # ==================Order Frame==================
        order_frame = Frame(root_s, bd=8, bg="darkgrey", relief=GROOVE)
        order_frame.place(x=680, y=335, height=370, width=680)

        order_title_label = Label(order_frame, text="Your Order",
                                  font=("times new roman", 20, "bold"), bg="darkblue", fg="darkgrey")
        order_title_label.pack(side=TOP, fill="x")

        ##################### Order Tabel #####################
        order_tabel_frame = Frame(order_frame)
        order_tabel_frame.place(x=0, y=40, height=260, width=680)

        scrollbar_order_x = Scrollbar(order_tabel_frame, orient=HORIZONTAL)
        scrollbar_order_y = Scrollbar(order_tabel_frame, orient=VERTICAL)

        order_tabel = ttk.Treeview(order_tabel_frame,
                                   columns=("name", "rate", "quantity", "price", "category"), xscrollcommand=scrollbar_order_x.set,
                                   yscrollcommand=scrollbar_order_y.set)

        order_tabel.heading("name", text="Name")
        order_tabel.heading("rate", text="Rate (in lakhs)")
        order_tabel.heading("quantity", text="Quantity")
        order_tabel.heading("price", text="Price")
        order_tabel["displaycolumns"] = ("name", "rate", "quantity", "price")
        order_tabel["show"] = "headings"
        order_tabel.column("rate", width=100, anchor='center', stretch=NO)
        order_tabel.column("quantity", width=100, anchor='center', stretch=NO)
        order_tabel.column("price", width=100, anchor='center', stretch=NO)

        order_tabel.bind("<ButtonRelease-1>", load_item_from_order)

        scrollbar_order_x.pack(side=BOTTOM, fill=X)
        scrollbar_order_y.pack(side=RIGHT, fill=Y)

        scrollbar_order_x.configure(command=order_tabel.xview)
        scrollbar_order_y.configure(command=order_tabel.yview)

        order_tabel.pack(fill=BOTH, expand=1)

        ########################################################################

        total_price_label = Label(order_frame, text="Total Price (in lakhs)",
                                  font=("arial", 12, "bold"), bg="darkgrey", fg="darkblue")
        total_price_label.pack(side=LEFT, anchor=SW, padx=20, pady=10)

        totalPrice = StringVar()
        totalPrice.set("")
        total_price_entry = Entry(order_frame, font="arial 12", textvariable=totalPrice, state=DISABLED,
                                  width=10)
        total_price_entry.pack(side=LEFT, anchor=SW, padx=0, pady=10)

        bill_button = ttk.Button(order_frame, text="Bill", width=8,
                                 command=bill_button_operation)
        bill_button.pack(side=LEFT, anchor=SW, padx=80, pady=10)

        cancel_button = ttk.Button(
            order_frame, text="Cancel Order", command=cancel_button_operation)
        cancel_button.pack(side=LEFT, anchor=SW, padx=20, pady=10)

        root_s.mainloop()
        # ====================Frontend code ends=====================

    def tax():
        global hm1

        def check():
            k = 0
            import mysql.connector as mysql
            conn = mysql.connect(host="localhost", user="root",
                                 passwd="Prime&2811", database="emp_info")
            c = conn.cursor()
            c.execute("SELECT Emp_ID,Emp_Passwd from emp_data")
            m = c.fetchall()
            # h.delete(0,END)
            f = h.get()
            g = p.get()
            x = (f, g)

            def calc():
                conn = mysql.connect(
                    host="localhost", user="root", passwd="Prime&2811", database="emp_info")
                c = conn.cursor()
                query = "SELECT Emp_Salary from emp_data WHERE (Emp_ID=%s)"
                a = (h.get(),)
                c.execute(query, a)
                m = c.fetchall()
                z = m[0][0]
                # y=0.123*z
                if (z <= 200000):
                    messagebox.showinfo(
                        "TAX BILL", "Sorry, you dont pay any tax")
                    hm1.destroy()
                if (z > 200000 and z <= 500000):
                    y = 0.123*z
                    messagebox.showinfo(
                        "TAX BILL", "The amount of tax you pay is: Rs."+str(y))
                    hm1.destroy()
                if (z > 500000 and z <= 1000000):
                    y = 0.15*z
                    messagebox.showinfo(
                        "TAX BILL", "The amount of tax you pay is: Rs."+str(y))
                    hm1.destroy()
                if (z > 1000000 and z <= 2000000):
                    y = 0.20*z
                    messagebox.showinfo(
                        "TAX BILL", "The amount of tax you pay is: Rs."+str(y))
                    hm1.destroy()
                if (z > 2000000):
                    y = 0.30*z
                    messagebox.showinfo(
                        "TAX BILL", "The amount of tax you pay is: Rs."+str(y))
                    hm1.destroy()

            for i in m:
                if (int(f) == i[0] and g == i[1]):
                    calc()

                else:
                    k = k+1
                    continue
            if (k == len(m)):
                m = messagebox.showinfo(
                    "ERROR", "The entered ID/ Password is wrong", icon="warning")

        hm1 = Toplevel()
        # hm1.iconbitmap("c:/pics/appimg.ico")
        hm1.title("Authorisation")
        hm1.configure(bg="#B4EFAE")
        hm1.geometry("330x100")
        h = Entry(hm1, width=30, font=('Courier New', 10, 'bold'))
        p = Entry(hm1, width=30, font=('Courier New', 10, 'bold'), show="*")
        h.grid(row=0, column=1)
        p.grid(row=1, column=1)
        l = Label(hm1, text="Employee ID:", bg="#B4EFAE")
        n = Label(hm1, text="Password:", bg="#B4EFAE")
        l.grid(row=0, column=0)
        n.grid(row=1, column=0)
        # x=h.get()
        ch = Button(hm1, text="Verify", command=check)
        ch.grid(row=2, column=1, columnspan=2)

    def att():
        from datetime import datetime
        import mysql.connector as mysql
        now = datetime.now()
        # b = now.strftime("%H:%M:%S")
        # print(current_time)
        import datetime
        a = datetime.date.today()
        # print(datetime.date.today())
        conn = mysql.connect(host="localhost", user="root",
                             passwd="Prime&2811", database="emp_info")
        c = conn.cursor()

        def check():
            k = 0
            import mysql.connector as mysql
            conn = mysql.connect(host="localhost", user="root",
                                 passwd="Prime&2811", database="emp_info")
            c = conn.cursor()
            c.execute("SELECT Emp_ID,Emp_Passwd from emp_data")
            m = c.fetchall()
            # h.delete(0,END)

            def attmark():

                def intime():
                    b = now.strftime("%H:%M:%S")
                    conn = mysql.connect(
                        host="localhost", user="root", passwd="Prime&2811", database="emp_info")
                    c = conn.cursor()
                    query = "INSERT INTO `emp_info`.`emp_%s` (`date`, `in_time`) VALUES (%s,%s);"
                    value = (int(h.get()), a, b)
                    c.execute(query, value)
                    messagebox.showinfo(
                        "Attendence", "In-time marked successfully")
                    conn.commit()
                    conn.close()

                def outtime():
                    z = now.strftime("%H:%M:%S")
                    conn = mysql.connect(
                        host="localhost", user="root", passwd="Prime&2811", database="emp_info")
                    d = conn.cursor()
                    query2 = "UPDATE `emp_info`.`emp_%s` SET `out_time` = '%s' WHERE (`date` = '%s')" % (
                        int(h.get()), z, a)

                    d.execute(query2)
                    messagebox.showinfo(
                        "Attendence", "Out-time marked successfully")
                    conn.commit()
                    conn.close()

                hm2 = Toplevel()
                # hm2.iconbitmap("c:/pics/appimg.ico")
                hm2.title("Attendence")
                hm2.configure(bg="#9CE8F5")
                hm2.geometry("400x300")
                frame1 = LabelFrame(hm2, text="", padx=50,
                                    pady=30, bd=6, bg="#F7F1DE")
                # frame2=LabelFrame(hm2,text="",padx=50,pady=30,bd=6,bg="#F7F1DE")

                frame1.pack()
                frame2.pack()
                b1 = Button(frame1, text="IN-TIME", command=intime, bd=8).grid(row=0,
                                                                               column=0, columnspan=2, ipadx=50, pady=10, padx=50)
                b2 = Button(frame1, text="OUT-TIME", command=outtime, bd=8).grid(
                    row=1, column=0, columnspan=2, ipadx=50, pady=10, padx=50)

                conn.commit()
                conn.close()

            f = h.get()
            g = p.get()
            x = (f, g)
            for i in m:
                if (int(f) == i[0] and g == i[1]):
                    attmark()
                else:
                    k = k+1
                    continue

            if (k == len(m)):
                messagebox.showinfo(
                    "ERROR", "The entered ID/ Password is wrong", icon="warning")

        # creating a top level
        hm1 = Toplevel()
        # hm1.iconbitmap("c:/pics/appimg.ico")
        hm1.title("Authorisation")
        hm1.configure(bg="#9CE8F5")
        hm1.geometry("330x100")
        h = Entry(hm1, width=30, font=('Courier New', 10, 'bold'))
        p = Entry(hm1, width=30, font=('Courier New', 10, 'bold'), show="*")
        h.grid(row=0, column=1)
        p.grid(row=1, column=1)
        l = Label(hm1, text="Employee ID:", bg="#9CE8F5")
        n = Label(hm1, text="Password:", bg="#9CE8F5")
        l.grid(row=0, column=0)
        n.grid(row=1, column=0)
        # x=h.get()
        ch = Button(hm1, text="Verify", command=check)
        ch.grid(row=2, column=1, columnspan=2)

    # creating frames:
    frame1 = LabelFrame(root, text="", padx=50, pady=30, bd=6, bg="#F7F1DE")
    frame2 = LabelFrame(root, text="", padx=50, pady=30, bd=6, bg="#F7F1DE")

    frame1.pack()
    frame2.pack()

    # creating button
    bill_bttn = Button(frame1, text="Create A Bill",
                       padx=28, pady=10, command=bill, bd=8)
    upd_bttn = Button(frame1, text="Update Address", padx=28,
                      pady=10, command=update1, bd=8)
    att_bttn = Button(frame1, text="Attendence", padx=50,
                      pady=10, command=att, bd=8)
    tax_bttn = Button(frame1, text="Tax Info",
                      command=tax, padx=50, pady=10, bd=8)
    exit_bttn = Button(frame2, text="EXIT", command=popup)

    # placing button
    bill_bttn.grid(row=0, column=0, columnspan=2, ipadx=68, pady=10)
    upd_bttn.grid(row=2, column=0, columnspan=2, ipadx=60, pady=10)
    att_bttn.grid(row=1, column=0, columnspan=2, ipadx=49, pady=10)
    tax_bttn.grid(row=4, column=0, columnspan=2, ipadx=55, pady=10)
    exit_bttn.grid(row=0, column=5, ipadx=10)
    # end committment
    conn.commit()
    conn.close()


def exit():
    m = messagebox.askyesno(
        "Employee system", "Do you want to exit the system")
    if m == True:
        home.destroy()
        return


f_m = LabelFrame(home, padx=50, pady=50, bg='#BBDEFB', bd=6)
f_m.pack(padx=10, pady=10)


admin_btn = Button(f_m, text="ADMIN", command=Admin, padx=10, pady=10, bd=8)
# admin_btn.pack(padx=10, pady=10, ipadx=110)
admin_btn.grid(row=1, column=1, columnspan=2, padx=10, pady=10, ipadx=110)

emp_btn = Button(f_m, text="EMPLOYEE", command=Emp, padx=10, pady=10, bd=8)
# emp_btn.pack(padx=10, pady=10, ipadx=105)
emp_btn.grid(row=2, column=1, columnspan=2, padx=10, pady=10, ipadx=105)

Date = StringVar()
Date.set(time.strftime("%d/%m/%Y"))
date = Label(f_m, textvariable=Date, font=('Castellar', 12, 'italic'),
             fg="#546E7A", bg="#BBDEFB").grid(row=0, column=2)

exit_btn = Button(home, text="EXIT", command=exit, padx=10, pady=10, bd=8)
exit_btn.pack(side='top', padx=10, pady=10, ipadx=120)
# exit_btn.grid(row=8, column=0, columnspan=2, padx=10, pady=10, ipadx=125)

home.mainloop()
