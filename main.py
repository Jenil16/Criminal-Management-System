from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from PIL import Image
from PIL import ImageTk
import mysql.connector as connect
import _mysql_connector
from tkinter import messagebox
# import tkinter as tk
from tkcalendar import DateEntry
from datetime import date
import mysql.connector


class Criminal:
    def __init__(self, root):
        self.root = root
        self.root.geometry('1530x790+0+0')
        # used to give the title to the software in the title bar
        self.root.title('CRIMINAL MANAGEMENT SYSTEM')

        # variables
        self.var_case_id = StringVar()
        self.var_criminal_no = StringVar()
        self.var_name = StringVar()
        self.var_nickname = StringVar()
        self.var_arrest = StringVar()
        self.var_date_of_crime = StringVar()
        self.var_address = StringVar()
        self.var_age = StringVar()
        self.var_occupation = StringVar()
        self.var_birthMark = StringVar()
        self.var_crime_type = StringVar()
        self.var_father_name = StringVar()
        self.var_gender = StringVar()
        self.var_wanted = StringVar()
        self.var_photo = StringVar()


# # # anything wich we want to write into the root is done by making the label of it

        lbl_title = Label(self.root, text='CRIMINAL MANAGEMENT SYSTEM SOFTWARE', font=(
            'times new roman', 40, 'bold'), bg='black', fg='white')
        lbl_title.place(x=0, y=0, width=1530, height=70)

# #         # ncr logo                              #how to insert image into the root?????
        img_logo = Image.open('images/ncrlogo.jpg')
        img_logo = img_logo.resize((60, 60), Image.ANTIALIAS)
        self.photo_logo = ImageTk.PhotoImage(img_logo)

        self.logo = Label(self.root, image=self.photo_logo)
        self.logo.place(x=80, y=5, width=60, height=60)

#         # image_frame
        img_frame = Frame(self.root, bd=2, relief=RIDGE, bg='white')
        img_frame.place(x=0, y=70, width=1530, height=130)

# #         # main frame
        Main_frame = Frame(self.root, bd=2, relief=RIDGE, bg='#2d70ed')
        Main_frame.place(x=10, y=70, width=1500, height=560)

# #         # upper frame
        upper_frame = LabelFrame(Main_frame, bd=2, relief=RIDGE, bg='white',
                                 text='Criminal Information', font=('times new roman', 11, 'bold'), fg='red')
        upper_frame.place(x=10, y=10, width=1480, height=270)

# #         # labels entry

# #         # case id
        caseid = Label(upper_frame, text='Case ID:',
                       font=('arial', 11, 'bold'), bg='white')
        caseid.grid(row=0, column=0, padx=2, sticky=W, pady=7)
        caseentry = ttk.Entry(upper_frame, textvariable=self.var_case_id, width=22,
                              font=('arial', 11, 'bold'))
        caseentry.grid(row=0, column=1, padx=2, sticky=W, pady=7)

# #         # Criminal no
        criminalno = Label(upper_frame, text='Criminal No:',
                           font=('arial', 11, 'bold'), bg='white')
        criminalno.grid(row=0, column=2, padx=2, sticky=W, pady=7)
        criminalentry = ttk.Entry(
            upper_frame, textvariable=self.var_criminal_no, width=22, font=('arial', 11, 'bold'))
        criminalentry.grid(row=0, column=3, padx=2, sticky=W, pady=7)

# #         # Crime type
        crimetype = Label(upper_frame, text='Crime Type:',
                          font=('arial', 11, 'bold'), bg='white')
        crimetype.grid(row=0, column=4, padx=2, sticky=W, pady=7)
        crimetypeentry = ttk.Entry(
            upper_frame, textvariable=self.var_crime_type, width=22, font=('arial', 11, 'bold'))
        crimetypeentry.grid(row=0, column=5, padx=2, sticky=W, pady=7)

# #         # Criminal name
        criminalname = Label(upper_frame, text='Criminal Name:', font=(
            'arial', 11, 'bold'), bg='white')
        criminalname.grid(row=1, column=0, padx=2, sticky=W, pady=7)
        criminalnameentry = ttk.Entry(
            upper_frame, textvariable=self.var_name, width=22, font=('arial', 11, 'bold'))
        criminalnameentry.grid(row=1, column=1, padx=2, sticky=W, pady=7)

# #         # Nickname
        nickname = Label(upper_frame, text='NickName:',
                         font=('arial', 11, 'bold'), bg='white')
        nickname.grid(row=1, column=2, padx=2, sticky=W, pady=7)
        nicknameentry = ttk.Entry(
            upper_frame, textvariable=self.var_nickname, width=22, font=('arial', 11, 'bold'))
        nicknameentry.grid(row=1, column=3, padx=2, sticky=W, pady=7)

# #         # Fathername
        fathername = Label(upper_frame, text='Father Name:',
                           font=('arial', 11, 'bold'), bg='white')
        fathername.grid(row=1, column=4, padx=2, sticky=W, pady=7)
        fathernameentry = ttk.Entry(
            upper_frame, textvariable=self.var_father_name, width=22, font=('arial', 11, 'bold'))
        fathernameentry.grid(row=1, column=5, padx=2, sticky=W, pady=7)

# #         # Arrest date
        arrestdate = Label(upper_frame, text='Arrest Date:',
                           font=('arial', 11, 'bold'), bg='white')
        arrestdate.grid(row=2, column=0, padx=2, sticky=W, pady=7)
        arrestdateentry = ttk.Entry(
            upper_frame, textvariable=self.var_arrest, width=22, font=('arial', 11, 'bold'))
        arrestdateentry.grid(row=2, column=1, padx=2, sticky=W, pady=7)

        # arrestdate = DateEntry(upper_frame, selectmode='day',date_pattern='dd-MM-yyyy')
        # arrestdate.grid(row=2, column=1, padx=2, sticky=W, pady=7)
        # dt = date.today().strftime("%d/%m/%Y")  # specific date Year, month , day
        # arrestdate.set_date(dt)  # Set the selected date
        # cal.set_date('8/16/2021') # Set the local calendar format

# #         # Date of crime
        crimedate = Label(upper_frame, text='Date of Crime:',
                          font=('arial', 11, 'bold'), bg='white')
        crimedate.grid(row=2, column=2, padx=2, sticky=W, pady=7)
        crimedateentry = ttk.Entry(
            upper_frame, textvariable=self.var_date_of_crime, width=22, font=('arial', 11, 'bold'))
        crimedateentry.grid(row=2, column=3, padx=2, sticky=W, pady=7)

# #         # Gender
        gender = Label(upper_frame, text='Gender:',
                       font=('arial', 11, 'bold'), bg='white')
        gender.grid(row=2, column=4, padx=2, sticky=W, pady=7)
        radio_frame_gender = Frame(upper_frame, bd=2, relief=RIDGE, bg='white')
        radio_frame_gender.place(x=705, y=78, width=190, height=35)
        male = Radiobutton(radio_frame_gender, variable=self.var_gender, text='Male',
                           value='male', font=('arial', 11, 'bold'), bg='white')
        male.grid(row=0, column=0, padx=5, pady=2, sticky=W)
        female = Radiobutton(radio_frame_gender, variable=self.var_gender, text='Female',
                             value='female', font=('arial', 11, 'bold'), bg='white')
        female.grid(row=0, column=2, padx=5, pady=2, sticky=W)

# #         # Address
        address = Label(upper_frame, text='Address:',
                        font=('arial', 11, 'bold'), bg='white')
        address.grid(row=3, column=0, padx=2, sticky=W, pady=7)
        addressentry = ttk.Entry(
            upper_frame, textvariable=self.var_address, width=22, font=('arial', 11, 'bold'))
        addressentry.grid(row=3, column=1, padx=2, sticky=W, pady=7)

# #         # Age
        age = Label(upper_frame, text='Age:', font=(
            'arial', 11, 'bold'), bg='white')
        age.grid(row=3, column=2, padx=2, sticky=W, pady=7)
        ageentry = ttk.Entry(
            upper_frame, textvariable=self.var_age, width=22, font=('arial', 11, 'bold'))
        ageentry.grid(row=3, column=3, padx=2, sticky=W, pady=7)

# #         # most wanted
        mostwanted = Label(upper_frame, text='Most Wanted:',
                           font=('arial', 11, 'bold'), bg='white')
        mostwanted.grid(row=3, column=4, padx=2, sticky=W, pady=7)
        radio_frame_mostwanted = Frame(
            upper_frame, bd=2, relief=RIDGE, bg='white')
        radio_frame_mostwanted.place(x=705, y=120, width=190, height=35)
        yes = Radiobutton(radio_frame_mostwanted, variable=self.var_wanted, text='Yes',
                          value='yes', font=('arial', 11, 'bold'), bg='white')
        yes.grid(row=0, column=0, padx=5, pady=2, sticky=W)
        no = Radiobutton(radio_frame_mostwanted, variable=self.var_wanted, text='No',
                         value='no', font=('arial', 11, 'bold'), bg='white')
        no.grid(row=0, column=2, padx=5, pady=2, sticky=W)

# #         # occupation
        occupation = Label(upper_frame, text='Occupation:',
                           font=('arial', 11, 'bold'), bg='white')
        occupation.grid(row=4, column=0, padx=2, sticky=W, pady=7)
        occupationentry = ttk.Entry(
            upper_frame, textvariable=self.var_occupation, width=22, font=('arial', 11, 'bold'))
        occupationentry.grid(row=4, column=1, padx=2, sticky=W, pady=7)

# #         # birthmark
        birthmark = Label(upper_frame, text='Birth Mark:',
                          font=('arial', 11, 'bold'), bg='white')
        birthmark.grid(row=4, column=2, padx=2, sticky=W, pady=7)
        birthmarkentry = ttk.Entry(
            upper_frame, textvariable=self.var_birthMark, width=22, font=('arial', 11, 'bold'))
        birthmarkentry.grid(row=4, column=3, padx=2, sticky=W, pady=7)

# # # select image and showing pic

        lbl_show_pic = Label(upper_frame, bg='white',
                             textvariable=self.var_photo)
#         # lbl_show_pic.grid(row=2,column=8, columnspan=2)
        lbl_show_pic.place(x=1000, y=65)

        UploadPhoto = Label(upper_frame, text='Upload Image:',
                            font=('arial', 11, 'bold'), bg='white')
        UploadPhoto.grid(row=4, column=4, padx=2, sticky=W, pady=7)
        btn_browse = Button(upper_frame, text='Select Image',
                            bg='Grey', fg='white')
        btn_browse.grid(row=4, column=4, columnspan=2)

        def selectPic():
            global img
            filename = filedialog.askopenfilename(initialdir="/images", title="Select Image", filetypes=(
                ("png files", "*.png"), ("jpg files", "*.jpg"), ("jpeg files", "*.jpeg")))
            img = Image.open(filename)
            img = img.resize((100, 100), Image.ANTIALIAS)
            img = ImageTk.PhotoImage(img)
            lbl_show_pic['image'] = img

        btn_browse['command'] = selectPic

        # button frame
        btn_frame = Frame(upper_frame, bd=2, relief=RIDGE, bg='white')
        btn_frame.place(x=5, y=200, width=627, height=45)

        # buttons
        # save btn
        btn_save = Button(btn_frame, text='Save', command=self.add_data, font=(
            'arial', 13, 'bold'), width=14, bg='blue', fg='white')
        btn_save.grid(row=0, column=0, padx=3, pady=5)

        # update button
        btn_update = Button(btn_frame, command=self.update_data, text='Update', font=(
            'arial', 13, 'bold'), width=14, bg='blue', fg='white')
        btn_update.grid(row=0, column=1, padx=3, pady=5)

# #         # delete button
        btn_delete = Button(btn_frame, command=self.delete_data, text='Delete', font=(
            'arial', 13, 'bold'), width=14, bg='blue', fg='white')
        btn_delete.grid(row=0, column=2, padx=3, pady=5)

# #         # clear button
        btn_clear = Button(btn_frame, command=self.clear_data, text='Clear', font=(
            'arial', 13, 'bold'), width=14, bg='blue', fg='white')
        btn_clear.grid(row=0, column=3, padx=3, pady=5)

# #         # background right side image
        # img_crime = Image.open('images/background.jpg')
        # img_crime = img_crime.resize((470, 245), Image.ANTIALIAS)
        # self.photo_crime = ImageTk.PhotoImage(img_crime)

        # self.img_crime = Label(upper_frame, image=self.photo_crime)
        # self.img_crime.place(x=1000, y=0, width=470, height=245)

# #         # down frame
        down_frame = LabelFrame(Main_frame, bd=2, relief=RIDGE, bg='white',
                                text='Criminal Information Table', font=('times new roman', 11, 'bold'), fg='red')
        down_frame.place(x=10, y=280, width=1480, height=270)

# #         # search frame
        search_frame = LabelFrame(down_frame, bd=2, relief=RIDGE, bg='white',
                                  text='Search Criminal Record', font=('times new roman', 11, 'bold'), fg='red')
        search_frame.place(x=0, y=0, width=1470, height=60)

        search_by = Label(search_frame, font=('arial', 11, 'bold'),
                          text='Search By:', bg='red', fg='white')
        search_by.grid(row=0, column=0, sticky=W, padx=5)

        self.var_com_search = StringVar()
        combo_search_box = ttk.Combobox(search_frame, textvariable=self.var_com_search, font=(
            'arial', 11, 'bold'), width=18, state='readonly')
        combo_search_box['value'] = ('Select Option', 'Case_id', 'Criminal_no')
        combo_search_box.current(0)
        combo_search_box.grid(row=0, column=1, sticky=W, padx=5)

        self.var_search = StringVar()
        search_txtentry = ttk.Entry(
            search_frame, textvariable=self.var_search, width=22, font=('arial', 11, 'bold'))
        search_txtentry.grid(row=0, column=3, padx=2, sticky=W, pady=7)

        btn_search = Button(search_frame, command=self.search_data, text='Search', font=(
            'arial', 13, 'bold'), width=14, bg='blue', fg='white')
        btn_search.grid(row=0, column=4, padx=3, pady=5)
        # btn_search = Button(search_frame, text='Search', font=(
        #     'arial', 13, 'bold'), width=14, bg='blue', fg='white')
        # btn_search.grid(row=0, column=4, padx=3, pady=5)

        btn_showall = Button(search_frame, command=self.fetch_data, text='Show All', font=(
            'arial', 13, 'bold'), width=14, bg='blue', fg='white')
        btn_showall.grid(row=0, column=5, padx=3, pady=5)
        # btn_showall = Button(search_frame, text='Show All', font=(
        #     'arial', 13, 'bold'), width=14, bg='blue', fg='white')
        # btn_showall.grid(row=0, column=5, padx=3, pady=5)

        crimeagency = Label(search_frame, text='NATIONAL CRIME AGENCY', font=(
            'Arial', 30, 'bold'), bg='white', fg='crimson')
        crimeagency.grid(row=0, column=6, sticky=W, padx=50)

#         # table
        table_frame = Frame(down_frame, bd=2, relief=RIDGE)
        table_frame.place(x=0, y=60, width=1470, height=170)

#         # scroll bar
        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)

        self.criminal_table = ttk.Treeview(table_frame, column=("1", "2", "3", "4", "5", "6", "7", "8", "9",
                                           "10", "11", "12", "13", "14", "15"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.criminal_table.xview)
        scroll_y.config(command=self.criminal_table.yview)

        self.criminal_table.heading('1', text='CaseId')
        self.criminal_table.heading('2', text='CrimeNo')
        self.criminal_table.heading('3', text='Criminal Name')
        self.criminal_table.heading('4', text='NickName')
        self.criminal_table.heading('5', text='ArrestDate')
        self.criminal_table.heading('6', text='CrimeOfDate')
        self.criminal_table.heading('7', text='Address')
        self.criminal_table.heading('8', text='Age')
        self.criminal_table.heading('9', text='Occupation')
        self.criminal_table.heading('10', text='Birth Mark')
        self.criminal_table.heading('11', text='Crime Type')
        self.criminal_table.heading('12', text='Father Name')
        self.criminal_table.heading('13', text='Gender')
        self.criminal_table.heading('14', text='Wanted')
        self.criminal_table.heading('15', text='Photo')

        self.criminal_table['show'] = 'headings'

        self.criminal_table.column('1', width=100)
        self.criminal_table.column('2', width=100)
        self.criminal_table.column('3', width=100)
        self.criminal_table.column('4', width=100)
        self.criminal_table.column('5', width=100)
        self.criminal_table.column('6', width=100)
        self.criminal_table.column('7', width=100)
        self.criminal_table.column('8', width=100)
        self.criminal_table.column('9', width=100)
        self.criminal_table.column('10', width=100)
        self.criminal_table.column('11', width=100)
        self.criminal_table.column('12', width=100)
        self.criminal_table.column('13', width=100)
        self.criminal_table.column('14', width=100)
        self.criminal_table.column('15', width=100)

        self.criminal_table.pack(fill=BOTH, expand=1)

        self.criminal_table.bind("<ButtonRelease>", self.get_cursor)

        self.fetch_data()

    # Add function

    def add_data(self):
        if self.var_case_id.get() == "":
            messagebox.showerror(
                'Error', 'All Fields are required', parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(
                    host='localhost', user='root', password='root', database='management')
                my_cursor = conn.cursor()
                my_cursor.execute('insert into criminal values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)', (
                    self.var_case_id.get(),
                    self.var_criminal_no.get(),
                    self.var_name.get(),
                    self.var_nickname.get(),
                    self.var_arrest.get(),
                    self.var_date_of_crime.get(),
                    self.var_address.get(),
                    self.var_age.get(),
                    self.var_occupation.get(),
                    self.var_birthMark.get(),
                    self.var_crime_type.get(),
                    self.var_father_name.get(),
                    self.var_gender.get(),
                    self.var_wanted.get(),
                    self.var_photo.get()
                ))

                conn.commit()

                self.fetch_data()
                self.clear_data()

                conn.close()
                messagebox.showinfo(
                    'Success', 'Criminal record has been successfully added')

            except Exception as es:
                messagebox.showerror('Error', f'Due to{str(es)}')

    # Fetch data

    def fetch_data(self):
        conn = mysql.connector.connect(
            host='localhost', user='root', password='root', database='management')
        # conn = _mysql_connector.MySQL()
        # conn.connect(host='localhost', user='root', password='root', database='management')
        my_cursor = conn.cursor()
        my_cursor.execute('select * from criminal')
        data = my_cursor.fetchall()
        if len(data) != 0:
            self.criminal_table.delete(*self.criminal_table.get_children())
            for i in data:
                self.criminal_table.insert('', END, values=i)
            conn.commit()
        conn.close()

#     # get cursor

    def get_cursor(self, event=""):
        cursor_row = self.criminal_table.focus()
        content = self.criminal_table.item(cursor_row)
        data = content['values']

        self.var_case_id.set(data[0])
        self.var_criminal_no.set(data[1])
        self.var_name.set(data[2])
        self.var_nickname.set(data[3])
        self.var_arrest.set(data[4])
        self.var_date_of_crime.set(data[5])
        self.var_address.set(data[6])
        self.var_age.set(data[7])
        self.var_occupation.set(data[8])
        self.var_birthMark.set(data[9])
        self.var_crime_type.set(data[10])
        self.var_father_name.set(data[11])
        self.var_gender.set(data[12])
        self.var_wanted.set(data[13])
        self.var_photo.set(data[14])

#     # update function

    def update_data(self):
        if self.var_case_id.get() == "":
            messagebox.showerror(
                'Error', 'All Fields are required', parent=self.root)
        else:
            try:
                update = messagebox.askyesno(
                    'Update', 'Are you sure to update this record?')
                if update > 0:
                    conn = mysql.connector.connect(
                        host='localhost', username='root', password='root', database='management')
                    my_cursor = conn.cursor()
                    my_cursor.execute('update criminal set Criminal_no=%s,Criminal_name=%s,Nick_name=%s,arrest_date=%s,dateOfCrime=%s,address=%s,age=%s,occupation=%s,BirthMark=%s,crimeType=%s,fatherName=%s,gender=%s,wanted=%s,photo=%s where Case_id=%s', (
                        self.var_criminal_no.get(),
                        self.var_name.get(),
                        self.var_nickname.get(),
                        self.var_arrest.get(),
                        self.var_date_of_crime.get(),
                        self.var_address.get(),
                        self.var_age.get(),
                        self.var_occupation.get(),
                        self.var_birthMark.get(),
                        self.var_crime_type.get(),
                        self.var_father_name.get(),
                        self.var_gender.get(),
                        self.var_wanted.get(),
                        self.var_photo.get(),
                        self.var_case_id.get()
                    ))

                else:
                    if not update:
                        return

                conn.commit()
                self.fetch_data()
                self.clear_data()
                conn.close()
                messagebox.showinfo(
                    'Success', 'Criminal Record has been successfully updated')

            except Exception as es:
                messagebox.showerror('Error', f'Due to{str(es)}')

# #     # delete function

    def delete_data(self):
        if self.var_case_id.get() == "":
            messagebox.showerror(
                'Error', 'All Fields are required', parent=self.root)
        else:
            try:
                delete = messagebox.askyesno(
                    'Delete', 'Are you sure to delete this record?')
                if delete > 0:
                    conn = mysql.connector.connect(
                        host='localhost', username='root', password='root', database='management')
                    my_cursor = conn.cursor()
                    sql = 'delete from criminal where Case_id=%s'
                    value = (self.var_case_id.get(),)
                    my_cursor.execute(sql, value)
                else:
                    if not delete:
                        return
                conn.commit()
                self.fetch_data()
                self.clear_data()
                conn.close()

                messagebox.showinfo(
                    'Success', 'Criminal Record has been deleted')

            except Exception as es:
                messagebox.showerror('Error', f'Due to{str(es)}')

# #     # clear function

    def clear_data(self):
        self.var_case_id.set("")
        self.var_criminal_no.set("")
        self.var_name.set("")
        self.var_nickname.set("")
        self.var_arrest.set("")
        self.var_date_of_crime.set("")
        self.var_address.set("")
        self.var_age.set("")
        self.var_occupation.set("")
        self.var_birthMark.set("")
        self.var_crime_type.set("")
        self.var_father_name.set("")
        self.var_gender.set("")
        self.var_wanted.set("")
        self.var_photo.set("")

#     # search

    def search_data(self):
        if self.var_com_search.get() == "":
            messagebox.showerror('Error', 'All Fields are Required')
        else:
            try:
                conn = mysql.connector.connect(
                    host='localhost', username='root', password='root', database='management')
                my_cursor = conn.cursor()
                my_cursor.execute('select * from criminal where ' + str(
                    self.var_com_search.get())+" LIKE'%"+str(self.var_search.get()+"%'"))
                rows = my_cursor.fetchall()
                if len(rows) != 0:
                    self.criminal_table.delete(
                        *self.criminal_table.get_children())
                    for i in rows:
                        self.criminal_table.insert('', END, values=i)
                conn.commit()
                conn.close()
            except Exception as es:
                messagebox.showerror('Error', f'Due to{str(es)}')


if __name__ == '__main__':
    root = Tk()
    # abc = Homepage()
    obj = Criminal(root)
    root.mainloop()
