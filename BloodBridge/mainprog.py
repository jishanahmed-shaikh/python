import sys
import tkinter as tk
from tkinter import filedialog, messagebox, ttk

import mysql.connector
from tkcalendar import DateEntry

from fileediter import gen_report
from mail import sendmail_donation, sendmail_request

mydb = mysql.connector.connect(
            host='localhost',
            user='root',
            password='root',
            database='bloodbridge'
        )

class main:
    def __init__(self, username):
        self.username = username

        self.window = tk.Tk()
        self.window.iconbitmap("blooddrop.ico")
        self.window.geometry('640x400')
        self.window.config(bg='#FCEDDA')
        self.window.title("BloodBridge Home Page")
        # calculate the coordinates for centering the window
        x = (self.window.winfo_screenwidth() - self.window.winfo_reqwidth()) / 2
        y = (self.window.winfo_screenheight() - self.window.winfo_reqheight()) / 2

        # set the window position
        self.window.geometry("+%d+%d" % (x-220,y-118))


        frame = tk.Frame(self.window, bg="light yellow", width=500, height=200)
        frame.place(x=70, y=110)

        separator = tk.Frame(self.window, height=3, width=620, bg='black')
        separator.place(x=10, y=10)
        
        '''
        welcome_label = tk.Label(self.window, text="Welcome to Blood Bridge "+username+"!", font=("Arial", 23,"bold"),bg='#FCEDDA')
        welcome_label.place(x=10,y=20)
        '''
        
        heading_frame = tk.Frame(self.window, bg='#2F3C7E')
        heading_frame.pack(pady=20)
        heading = tk.Label(heading_frame, text="Welcome to the Bloodbridge! "+username+"! ", font=("Helvetica", 22), bg='#FCEDDA', fg='#EE4E34')
        heading.pack()
        
        subtext_label = tk.Label(self.window,text="A link between Blood Donors,Blood Banks and Receivers",font=("Arial", 16),bg='#FCEDDA')
        subtext_label.place(x=40,y=60)
        
        separatorafterwelcome = tk.Frame(self.window, height=3, width=620, bg='black')
        separatorafterwelcome.place(x=10, y=90)

        request_label = tk.Label(frame, text="To Request: ", font=("Helvetica", 16, "bold"), bg='light yellow', fg='#EE4E34')
        request_label.place(x=20, y=20)

        Request_Blood_Units = tk.Button(frame, text="Request Blood", command=self.request_blood_units,font=("Arial", 12,"bold"),bg='#EE4E34', fg='#FCEDDA',width=25)
        Request_Blood_Units.place(x=220, y=20)        

        donate_label = tk.Label(frame, text="To Donate: ", font=("Helvetica", 16, "bold"), bg='light yellow', fg='#EE4E34')
        donate_label.place(x=20, y=90)

        Request_Blood_Donation = tk.Button(frame, text="Donate Blood", command=self.requests_blood_donation,font=("Arial", 12,"bold"),bg='#EE4E34', fg='#FCEDDA',width=25) 
        Request_Blood_Donation.place(x=220,y=90)

        profile_label = tk.Label(frame, text="To Profile section: ", font=("Helvetica", 16, "bold"), bg='light yellow', fg='#EE4E34')
        profile_label.place(x=20, y=160)

        Request_Blood_Donation = tk.Button(frame, text="My Profile", command=self.call_profile,font=("Arial", 12,"bold"),bg='#EE4E34', fg='#FCEDDA',width=25) 
        Request_Blood_Donation.place(x=220,y=160)
        
        separatoraboveexit = tk.Frame(self.window, height=3, width=620, bg='black')
        separatoraboveexit.place(x=10, y=340)
        
        logoutbutton = tk.Button(self.window, text="Logout", command=exit,font=("Arial", 12,"bold"),bg='darkgreen', fg='#FCEDDA',width=24) 
        logoutbutton.place(x=70,y=350)
        
        exitbutton = tk.Button(self.window, text="Exit", command=exit,font=("Arial", 12,"bold"),bg='#EE4E34', fg='#FCEDDA',width=22) 
        exitbutton.place(x=335,y=350)
        
        back_button = tk.Button(self.window, text="<<", command=exit, bd=2)
        back_button.config(width=2,height=1, bd=2,font=("Helvetica",12,"bold"),bg='black', fg='white')
        back_button.place(x=10,y=350)
        
        separatorbelowexit = tk.Frame(self.window, height=3, width=620, bg='black')
        separatorbelowexit.place(x=10, y=390)
        
    def backbutton(self):
        self.window.destroy()
        
    mydb = mysql.connector.connect(
            host='localhost',
            user='root',
            password='root',
            database='bloodbridge'
        )

    def run(self):
        # start the GUI main loop
        self.window.mainloop()

    def call_profile(self):
        self.window.destroy()
        profile_obj=profile(self.username)
        profile_obj.run()
        

    def request_blood_units(self):
        self.window.destroy()
        # create an instance of the Blood_units class and call its run method
        blood_units_window = blood_units(self.username)
        blood_units_window.run()
        

    def requests_blood_donation(self):
        
        #hide the main page
        self.window.destroy()

        # create an instance of the blood_donation_request class and call its run method
        blood_donation_window = blood_donation(self.username) # fixed the class name
        blood_donation_window.run()

class profile:
    def __init__(self, username):
        mydb = mysql.connector.connect(
            host='localhost',
            user='root',
            password='root',
            database='bloodbridge'
        )
        self.username = username
        mycursor = mydb.cursor()

        sql = "select name,phone_number,email from users"
        mycursor.execute(sql)
        result=mycursor.fetchone()
        self.name=result[0]
        self.number=result[1]
        self.email=result[2]

        self.window = tk.Tk()
        self.window.iconbitmap("blooddrop.ico")
        self.window.geometry('640x400')
        self.window.config(bg='#FCEDDA')
        self.window.title("Your Profile")
        
        
        x = (self.window.winfo_screenwidth() - self.window.winfo_reqwidth()) / 2
        y = (self.window.winfo_screenheight() - self.window.winfo_reqheight()) / 2

        # set the window position
        self.window.geometry("+%d+%d" % (x-220,y-118))
        
        
        separator1 = tk.Frame(self.window, height=3, width=620, bg='black')
        separator1.place(x=10, y=10)

        # create a label for the upload button
        self.titleprofile_button = tk.Button(self.window, text="Welcome "+username+" to Your Discrete Profile Section:",command="", font=("Helvetica", 12, "bold"),bg='#EE4E34', fg='#FCEDDA',width=50)
        self.titleprofile_button.place(x=60,y=20)
        
        separator2 = tk.Frame(self.window, height=3, width=620, bg='black')
        separator2.place(x=10, y=60)
      

        # create a label for the dropdown menu
        data1=self.name
        data1_var = tk.StringVar(value=data1)
        
        data2=self.number
        data2_var = tk.StringVar(value=data2)
        
        data3=self.email
        data3_var = tk.StringVar(value=data3)
        
        self.name_label = tk.Label(self.window,text="Your Name: ",font=("Helvetica", 14, "bold"), bg='#FCEDDA', fg='#EE4E34')
        self.name_label.place(x=60,y=80)
        
        self.number_label = tk.Label(self.window,text="Your Number: ",font=("Helvetica", 14, "bold"), bg='#FCEDDA', fg='#EE4E34')
        self.number_label.place(x=60,y=110)
        
        self.mail_label = tk.Label(self.window,text="Your Mail: ",font=("Helvetica", 14, "bold"), bg='#FCEDDA', fg='#EE4E34')
        self.mail_label.place(x=60,y=140)
        
        self.name_entry = tk.Entry(self.window,width=33,font=("Helvetica", 14,"bold"),state='disabled',textvariable=data1_var)
        self.name_entry.place(x=210,y=80)
        
        self.number_entry = tk.Entry(self.window,width=33,text=data2,font=("Helvetica", 14,"bold"), state='disabled',textvariable=data2_var)
        self.number_entry.place(x=210,y=110)
        
        self.mail_entry = tk.Entry(self.window,width=33,text=data3,font=("Helvetica", 14,"bold"), state='disabled',textvariable=data3_var)
        self.mail_entry.place(x=210,y=140)
        


        frame = tk.Frame(self.window, bg="light yellow", width=510, height=150,bd=5)
        frame.place(x=60, y=180)

        # create a button to past history of donation and requests
        self.donation_button = tk.Button(self.window, text="Press to See Donation History", command=self.donation_hist,font=("Helvetica", 13, "bold"),bg='#EE4E34', fg='#FCEDDA',width=40)
        self.donation_button.place(x=110,y=200)
        
        self.donation_button = tk.Button(self.window, text="Press to See Donation Status", command=self.donation_stat,font=("Helvetica", 13, "bold"), bg='#EE4E34', fg='#FCEDDA',width=40)
        self.donation_button.place(x=110,y=240)
        
        self.request_button = tk.Button(self.window, text="Press to See Blood Request Status and History", command=self.req_hist,font=("Helvetica", 13, "bold"),bg='#EE4E34', fg='#FCEDDA',width=40)
        self.request_button.place(x=110,y=280)
        
        separatoraboveexit = tk.Frame(self.window, height=3, width=620, bg='black')
        separatoraboveexit.place(x=10, y=340)
        
        logoutbutton = tk.Button(self.window, text="Log Out", command=exit,font=("Arial", 12,"bold"),bg='darkgreen', fg='#FCEDDA',width=24) 
        logoutbutton.place(x=60,y=350)
        
        exitbutton = tk.Button(self.window, text="Exit", command=exit,font=("Arial", 12,"bold"),bg='#EE4E34', fg='#FCEDDA',width=24) 
        exitbutton.place(x=320,y=350)
        
        back_button = tk.Button(self.window, text="<<", command=self.gobacktoNavigator, bd=2)
        back_button.config(width=2,height=1, bd=2,font=("Helvetica",12,"bold"),bg='black', fg='white')
        back_button.place(x=10,y=350)
        
        separatorbelowexit = tk.Frame(self.window, height=3, width=620, bg='black')
        separatorbelowexit.place(x=10, y=390)
        
    def gobacktoNavigator(self):
        self.window.destroy()
        a=main(self.username)
    

    def donation_stat(self):
        mydb = mysql.connector.connect(
            host='localhost',
            user='root',
            password='root',
            database='bloodbridge'
        )
        mycursor = mydb.cursor()

        sql = "SELECT request_id, Bid, username,appointment,timing,status FROM donation_requests where status!=1 and username=%s"
        mycursor.execute(sql,(self.username,))
        result=mycursor.fetchone()
        displaymsg="Request ID: "+str(result[0])+" Blood Bank ID: "+str(result[1])+"\n Username: "+str(result[2])+" Appointment Date: "+str(result[3])+"\n Time: "+str(result[4])
        if result[5]==0:
            displaymsg+=" Status: Pending"
        else:
            displaymsg+=" Status: Declined"
        
        reqid=str(result[0])
        bid=str(result[1])
        usern=str(result[2])
        appointment=str(result[3])
        tim=str(result[4])
        
        if result[5]==0:
            status="Pending"
        else:
            status="Declined"
        
            
        self.window.iconify()
        self.popup=tk.Tk()
        self.popup.iconbitmap("blooddrop.ico")
        self.popup.title("Donation Status")
        self.popup.geometry('640x400')
        self.popup.config(bg='#FCEDDA')
        
        x = (self.popup.winfo_screenwidth() - self.popup.winfo_reqwidth()) / 2
        y = (self.popup.winfo_screenheight() - self.popup.winfo_reqheight()) / 2

        # set the window position
        self.popup.geometry("+%d+%d" % (x-220,y-118))
        
        separatortop = tk.Frame(self.popup, height=3, width=620, bg='black')
        separatortop.place(x=10, y=10)
        
        # create a label for the heading
        self.heading_label = tk.Label(self.popup, text="Donations and Requests Status:", font=("Helvetica", 18, "bold"), bg='#FCEDDA', fg='#EE4E34')
        self.heading_label.place(x=130,y=20)
        
        separatorbelowtitle = tk.Frame(self.popup, height=3, width=620, bg='black')
        separatorbelowtitle.place(x=10, y=55)
        
  
        #FRAME AND LABELS INSIDE IT
        
        frame = tk.Frame(self.popup, bg="light yellow", width=510, height=230,bd=5)
        frame.place(x=65, y=85)
        
        self.id_button = tk.Button(frame, text="The User ID is: ", command="",font=("Arial", 11,"bold"),bg='#EE4E34', fg='#FCEDDA',width=22)
        self.id_button.place(x=10,y=5)
        self.id_entry=tk.Entry(frame, font=("Helvetica", 16, "bold"))
        self.id_entry.insert(0,reqid)
        self.id_entry.config(state='disabled')
        self.id_entry.place(x=250,y=5)
        
        
        
        self.bid_button = tk.Button(frame, text="Chosen Bloodbank ID: ", command="",font=("Arial", 11,"bold"),bg='#EE4E34', fg='#FCEDDA',width=22)
        self.bid_button.place(x=10,y=40)
        self.bid_entry=tk.Entry(frame,font=("Helvetica", 16, "bold"))
        self.bid_entry.insert(0,bid)
        self.bid_entry.config(state='disabled')
        self.bid_entry.place(x=250,y=40)
        
        
        self.usern_button = tk.Button(frame, text="The Username is ", command="",font=("Arial", 11,"bold"),bg='#EE4E34', fg='#FCEDDA',width=22)
        self.usern_button.place(x=10,y=75)
        self.usern_entry=tk.Entry(frame,font=("Helvetica", 16, "bold"))
        self.usern_entry.insert(0,usern)
        self.usern_entry.config(state='disabled')
        self.usern_entry.place(x=250,y=75)
        
        
        
        self.appointment_button = tk.Button(frame, text="Appointment Scheduled at ", command="",font=("Arial", 11,"bold"),bg='#EE4E34', fg='#FCEDDA',width=22)
        self.appointment_button.place(x=10,y=110)
        self.appointment_entry=tk.Entry(frame,font=("Helvetica", 16, "bold"))
        self.appointment_entry.insert(0,appointment)
        self.appointment_entry.config(state='disabled')
        self.appointment_entry.place(x=250,y=110)
        
        
        self.time_button = tk.Button(frame, text="Time Chosen as", command="",font=("Arial", 11,"bold"),bg='#EE4E34', fg='#FCEDDA',width=22)
        self.time_button.place(x=10,y=145)
        self.time_entry=tk.Entry(frame,font=("Helvetica", 16, "bold"))
        self.time_entry.insert(0,tim)
        self.time_entry.config(state='disabled')
        self.time_entry.place(x=250,y=145)
        
        
        self.status_button = tk.Button(frame, text="The Status is Marked as ", command="",font=("Arial", 11,"bold"),bg='#EE4E34', fg='#FCEDDA',width=22)
        self.status_button.place(x=10,y=180)
        self.status_entry=tk.Entry(frame,font=("Helvetica", 16, "bold"))
        self.status_entry.insert(0,status)
        self.status_entry.config(state='disabled')
        self.status_entry.place(x=250,y=180)
        
        
        
        
        
        
        
        
        
       
        separatormid = tk.Frame(self.popup, height=3, width=620, bg='black')
        separatormid.place(x=10, y=340)

        # create a button to trigger the search
        self.exit_button = tk.Button(self.popup, text="Exit", command=exit,font=("Arial", 12,"bold"),bg='#EE4E34', fg='#FCEDDA',width=50)
        self.exit_button.place(x=65,y=350)
        
        back_button = tk.Button(self.popup, text="<<",command=self.back, bd=2)
        back_button.config(width=2,height=1, bd=2,font=("Helvetica",12,"bold"),bg='black', fg='white')
        back_button.place(x=10,y=350)
        
        fo_button = tk.Button(self.popup, text=">>",command=self.back, bd=2)
        fo_button.config(width=2,height=1, bd=2,font=("Helvetica",12,"bold"),bg='black', fg='white')
        fo_button.place(x=600,y=350)
        
        separator = tk.Frame(self.popup, height=3, width=620, bg='black')
        separator.place(x=10, y=390)

    def donation_hist(self):
        self.window.iconify()
        self.popup=tk.Tk()
        self.popup.iconbitmap("blooddrop.ico")
        self.popup.title("Donation History")
        self.popup.geometry('640x400')
        self.popup.config(bg='#FCEDDA')
        
        x = (self.popup.winfo_screenwidth() - self.popup.winfo_reqwidth()) / 2
        y = (self.popup.winfo_screenheight() - self.popup.winfo_reqheight()) / 2

        # set the window position
        self.popup.geometry("+%d+%d" % (x-220,y-118))
        
        
        separatortop = tk.Frame(self.popup, height=3, width=620, bg='black')
        separatortop.place(x=10, y=10)
        
        # create a label for the heading
        self.heading_label = tk.Label(self.popup, text="Report Generation and Donations History:", font=("Helvetica", 18, "bold"), bg='#FCEDDA', fg='#EE4E34')
        self.heading_label.place(x=80,y=20)
        
        separatorbelowtitle = tk.Frame(self.popup, height=3, width=620, bg='black')
        separatorbelowtitle.place(x=10, y=55)
        
        
        
        # Create table
        self.tree = ttk.Treeview(self.popup,height=12)
        self.tree["columns"] = ("Bid", "username", "appointment", "timing","status")
        self.tree.heading("#0", text="Request ID")
        self.tree.column("#0", width=80)
        self.tree.heading("Bid", text="Bid")
        self.tree.column("Bid", width=50)
        self.tree.heading("username", text="Username")
        self.tree.column("username", width=100)
        self.tree.heading("appointment", text="Appointment")
        self.tree.column("appointment", width=100)
        self.tree.heading("timing", text="Timing")
        self.tree.column("timing", width=80)
        self.tree.heading("status", text="Status")
        self.tree.column("status", width=80)

        # Fetch data from MySQL table
        self.update_request_tree_view()

        # Pack table into Tkinter window
        self.tree.place(x=80, y=70)

        self.download_button = tk.Button(self.popup, text="Download Report", command=self.display,font=("Helvetica", 13, "bold"), bg='darkgreen', fg='white',width=24)
        self.download_button.place(x=80,y=350)
       
        separatormid = tk.Frame(self.popup, height=3, width=620, bg='black')
        separatormid.place(x=10, y=340)

        # create a button to trigger the search
        self.exit_button = tk.Button(self.popup, text="Exit", command=exit,font=("Arial", 12,"bold"),bg='#EE4E34', fg='#FCEDDA',width=22)
        self.exit_button.place(x=340,y=350)
        
        back_button = tk.Button(self.popup, text="<<",command=self.back, bd=2)
        back_button.config(width=2,height=1, bd=2,font=("Helvetica",12,"bold"),bg='black', fg='white')
        back_button.place(x=10,y=350)
        
        separator = tk.Frame(self.popup, height=3, width=620, bg='black')
        separator.place(x=10, y=390)

    def req_hist(self):
        self.window.iconify()
        self.popup1=tk.Tk()
        self.popup1.iconbitmap("blooddrop.ico")
        self.popup1.title("Blood Request Status and History")
        self.popup1.geometry('640x400')
        self.popup1.config(bg='#FCEDDA')
        
        x = (self.popup1.winfo_screenwidth() - self.popup1.winfo_reqwidth()) / 2
        y = (self.popup1.winfo_screenheight() - self.popup1.winfo_reqheight()) / 2

        # set the window position
        self.popup1.geometry("+%d+%d" % (x-220,y-118))
    
        separatortop = tk.Frame(self.popup1, height=3, width=620, bg='black')
        separatortop.place(x=10, y=10)
        
        # create a label for the heading
        self.heading_label = tk.Label(self.popup1, text="Report Generation and Donations History:", font=("Helvetica", 18, "bold"), bg='#FCEDDA', fg='#EE4E34')
        self.heading_label.place(x=80,y=20)
        
        separatorbelowtitle = tk.Frame(self.popup1, height=3, width=620, bg='black')
        separatorbelowtitle.place(x=10, y=55)
    
        # Create table
        self.tree1 = ttk.Treeview(self.popup1)
        self.tree1["columns"] = ("username", "bloodtype", "units_required", "status")
        self.tree1.heading("#0", text="Request ID")
        self.tree1.column("#0", width=100)
        self.tree1.heading("username", text="Username")
        self.tree1.column("username", width=100)
        self.tree1.heading("bloodtype", text="Blood Type")
        self.tree1.column("bloodtype", width=100)
        self.tree1.heading("units_required", text="Units Required")
        self.tree1.column("units_required", width=100)
        self.tree1.heading("status", text="Status")
        self.tree1.column("status", width=80)

        #update the treeview
        self.update_blood_request_tree_view()

        # Pack table into Tkinter window
        self.tree1.place(x=80, y=85)
        
        
        separatormid = tk.Frame(self.popup1, height=3, width=620, bg='black')
        separatormid.place(x=10, y=340)
        
        self.Logout_button = tk.Button(self.popup1, text="Logout", command=exit,font=("Helvetica", 13, "bold"), bg='darkgreen', fg='white',width=24)
        self.Logout_button.place(x=80,y=350)

        # create a button to trigger the search
        self.exit_button = tk.Button(self.popup1, text="Exit", command=exit,font=("Arial", 12,"bold"),bg='#EE4E34', fg='#FCEDDA',width=22)
        self.exit_button.place(x=340,y=350)
        
        back_button = tk.Button(self.popup1, text="<<",command=self.back1, bd=2)
        back_button.config(width=2,height=1, bd=2,font=("Helvetica",12,"bold"),bg='black', fg='white')
        back_button.place(x=10,y=350)
        
        separator = tk.Frame(self.popup1, height=3, width=620, bg='black')
        separator.place(x=10, y=390)


    def back(self):
        self.popup.destroy()
        self.window.deiconify()

    def back1(self):
        self.popup1.destroy()
        self.window.deiconify()

    def update_blood_request_tree_view(self):
        mydb = mysql.connector.connect(
            host='localhost',
            user='root',
            password='root',
            database='bloodbridge'
        )
        # Clear the tree view widget
        self.tree1.delete(*self.tree1.get_children())

        # Retrieve the latest blood requests from the database
        # Fetch data from MySQL table
        cursor = mydb.cursor()
        cursor.execute("SELECT request_id, username, bloodtype, units_required, status FROM blood_requests WHERE username=%s",(self.username,))
        rows = cursor.fetchall()
        for row in rows:
            self.tree1.insert("", tk.END, text=row[0], values=( row[1], row[2], row[3], row[4]))


    def update_request_tree_view(self):
        mydb = mysql.connector.connect(
            host='localhost',
            user='root',
            password='root',
            database='bloodbridge'
        )
        # Clear the tree view widget
        self.tree.delete(*self.tree.get_children())

        # Retrieve the latest donation requests from the database
        # Fetch data from MySQL table
        cursor = mydb.cursor()
        cursor.execute("SELECT request_id, Bid, username,appointment, timing,status FROM donation_requests where status!=0 and username=%s",(self.username,))
        rows = cursor.fetchall()
        for row in rows:
            self.tree.insert("", tk.END, text=row[0], values=(row[1], row[2], row[3], row[4],row[5]))

    def display(self):
        # Assuming self.tree is the Treeview widget
        selected_item = self.tree.selection()
        if selected_item:
            # Get the values of the selected item
            request_id = int(self.tree.item(selected_item)['text'])
            gen_report(request_id)
            messagebox.showinfo("Downloaded","Your donation report has been successfully downloaded!")
        else:
            messagebox.showerror('No item selected',"Please Select one record")



    def run(self):
        # start the GUI main loop
        self.window.mainloop()


class blood_units:

    mydb = mysql.connector.connect(
            host='localhost',
            user='root',
            password='root',
            database='bloodbridge'
        )

    def __init__(self, username):
        self.username = username

        self.window = tk.Tk()
        self.window.iconbitmap("blooddrop.ico")
        self.window.geometry('640x400')
        self.window.config(bg='#FCEDDA')
        self.window.title("Blood Requests")
        x = (self.window.winfo_screenwidth() - self.window.winfo_reqwidth()) / 2
        y = (self.window.winfo_screenheight() - self.window.winfo_reqheight()) / 2

        # set the window position
        self.window.geometry("+%d+%d" % (x-220,y-118))
        
        
        frame = tk.Frame(self.window, bg="light yellow", width=500, height=200)
        frame.place(x=70, y=100)

        # create a label for the dropdown menu
        self.select_label = tk.Label(self.window, text="Select Blood Type:", font=("Helvetica", 18, "bold"), bg='light yellow', fg='#EE4E34')
        self.select_label.place(x=80,y=220)

        # define the options for the dropdown menu
        Blood_types = ["A+", "A-", "B+", "B-", "AB+", "AB-", "O+", "O-"]

        # create the dropdown menu widget
        self.selected = tk.StringVar(self.window)
        self.selected.set(Blood_types[0])  # default value
        self.option_menu = tk.OptionMenu(self.window, self.selected, *Blood_types)
        self.option_menu.config(width=25, height=1, font=('Helvetica', 10), foreground="black", background="white", borderwidth=2, relief="groove")
        self.option_menu.place(x=345,y=220)


        separator = tk.Frame(self.window, height=3, width=620, bg='black')
        separator.place(x=10, y=10)
        
        # create a label for the upload button
        self.upload_label = tk.Label(self.window, text="Validation and Request for Blood Units:", font=("Helvetica", 18, "bold"), bg='#FCEDDA', fg='#EE4E34')
        self.upload_label.place(x=95,y=20)
        
        separatorbelowtitle = tk.Frame(self.window, height=3, width=620, bg='black')
        separatorbelowtitle.place(x=10, y=55)
        
        self.upload_label = tk.Label(self.window, text="Upload Your Medical Blood Request File:", font=("Helvetica", 18, "bold"), bg='light yellow', fg='#EE4E34')
        self.upload_label.place(x=80,y=125)

        # create a button to trigger the file upload
        self.upload_button = tk.Button(self.window, text="Click to Upload Your File",command=self.upload_file,font=("Helvetica", 13, "bold"),bg='#EE4E34', fg='#FCEDDA',width=46)
        self.upload_button.place(x=80,y=170)

        units_label = tk.Label(self.window, text="Enter Units Required:",font=("Helvetica", 18,"bold"), bg='light yellow', fg='#EE4E34',bd=0)
        units_label.place(x=80,y=265)
        self.units_entry = tk.Entry(self.window,width=19,font=("Helvetica", 14,"bold"))
        self.units_entry.place(x=350,y=270)

        '''
        # Create email label and entry field
        units_label = tk.Label(self.window, text="Units Required:")
        units_label.place(x=140,y=100)

        self.units_entry = tk.Entry(self.window)
        self.units_entry.place(x=140,y=170)
        '''
        
        separatormid = tk.Frame(self.window, height=3, width=620, bg='black')
        separatormid.place(x=10, y=340)

        # create a button to trigger the search
        self.search_button = tk.Button(self.window, text="Request", command=self.insert_blood_request,font=("Arial", 12,"bold"),bg='#EE4E34', fg='#FCEDDA',width=22)
        self.search_button.place(x=80,y=350)

        self.exit_button = tk.Button(self.window, text="Exit", command=exit,font=("Arial", 12,"bold"),bg='#EE4E34', fg='#FCEDDA',width=22)
        self.exit_button.place(x=330,y=350)
        
        back_button = tk.Button(self.window, text="<<", command=self.gobacktoNavigator, bd=2)
        back_button.config(width=2,height=1, bd=2,font=("Helvetica",12,"bold"),bg='black', fg='white')
        back_button.place(x=10,y=350)
        
        separator = tk.Frame(self.window, height=3, width=620, bg='black')
        separator.place(x=10, y=390)

        # create a label to display the search results
        

        self.urgent_statement = tk.Label(self.window, text="If urgent, please call 123456", fg="red")
        
    def gobacktoNavigator(self):
        self.window.destroy()
        a=main(self.username)
        


    def upload_file(self):
        # open a file dialogue box to select a file to upload
        filename = filedialog.askopenfilename(initialdir="/", title="Select a File", filetypes=(("jpg", "*.jpg*"), ("png","*.png*"), ("all files", "*.*")))

        if filename:
            # read the contents of the file
            with open(filename, 'rb') as f:
                file_data = f.read()
                self.file_data = file_data  # store file_data as an instance variable
                messagebox.showinfo("File Upload","File uploaded succesfully!")

    def run(self):
        # start the GUI main loop
        self.window.mainloop()

    def close_window(self):
        # destroy the Blood Units window and bring back the main window
        self.window.destroy()
        self.main_window.deiconify()

    def insert_blood_request(self):
        mydb = mysql.connector.connect(
            host='localhost',
            user='root',
            password='root',
            database='bloodbridge'
        )
        # get the selected blood type from the dropdown menu
        Blood_type = self.selected.get()
        units_required=self.units_entry.get()
        
        mycursor = mydb.cursor()

        sql = "insert into blood_requests(username,request_report,bloodtype,units_required) values(%s, %s,%s, %s)"
        mycursor.execute(sql, (self.username,self.file_data,Blood_type,units_required))
        mydb.commit()
        sendmail_request(self.username)
        messagebox.showinfo("Blood Request","Your request has been succesfully submitted,you can see details in your profile.A confirmation mail has been sent as well")
        self.window.destroy()
        main_obj=main(self.username)
        main_obj.run()
            

class blood_donation:

    mydb = mysql.connector.connect(
            host='localhost',
            user='root',
            password='root',
            database='bloodbridge'
        )

    def __init__(self, username):
        self.username = username
        self.file_data = None        
        
        self.window = tk.Tk()
        self.window.iconbitmap("blooddrop.ico")
        self.window.geometry('640x400')
        self.window.title("Blood Donation Request")
        self.window.config(bg="#FCEDDA")
        
        x = (self.window.winfo_screenwidth() - self.window.winfo_reqwidth()) / 2
        y = (self.window.winfo_screenheight() - self.window.winfo_reqheight()) / 2

        # set the window position
        self.window.geometry("+%d+%d" % (x-220,y-118))
        
        separator1 = tk.Frame(self.window, height=3, width=620, bg='black')
        separator1.place(x=10, y=10)

        # create a label for the upload button
        self.upload_label = tk.Label(self.window, text="Donation Requests and Appointments Scheduling:", font=("Helvetica", 14, "bold"),bg='#FCEDDA', fg='#EE4E34')
        self.upload_label.place(x=90,y=20)
        
        separator2 = tk.Frame(self.window, height=3, width=620, bg='black')
        separator2.place(x=10, y=50)
        
        self.upload_label = tk.Label(self.window, text="Upload Your Medical Check-up File clicking below:", font=("Helvetica", 14, "bold"),bg='#FCEDDA', fg='#EE4E34')
        self.upload_label.place(x=80,y=150)

        # create a button to trigger the file upload
        self.upload_button = tk.Button(self.window, text="Click to Upload Your File", command=self.upload_file,font=("Helvetica", 13, "bold"),bg='#EE4E34', fg='#FCEDDA',width=46)
        self.upload_button.place(x=80,y=180)

        # create a label for the blood bank list
        self.blood_bank_label = tk.Label(self.window, text="List of Blood Banks displayed in the following list:", font=("Helvetica", 14, "bold"),bg='#FCEDDA', fg='#EE4E34')
        self.blood_bank_label.place(x=80,y=215)

        # create a listbox to display the blood bank list
        self.blood_bank_listbox = tk.Listbox(self.window, width=80,height=5)
        self.blood_bank_listbox.place(x=80,y=245)

        # Create a label for the date picker
        date_label = tk.Label(self.window, text='Select a date:',bg='#FCEDDA', fg='#EE4E34',font=("Arial", 14, "bold"))
        date_label.place(x=80,y=70)

        # Create a date picker widget
        self.date_picker = DateEntry(self.window, width=17, background='#EE4E34',
                                foreground='white', borderwidth=2)
        self.date_picker.place(x=80,y=100)

        # Create Combobox widget for Appointment selection
        self.appointment_combobox = ttk.Combobox(self.window, values=["10 AM","11 AM","12 PM","1 PM","2 PM","3 PM","4 PM"], width=44)

        # Add label for hours and time format
        self.appointment_label = ttk.Label(self.window, text="Select an Appointment Timing:",background='#FCEDDA',foreground='#EE4E34',font=("Arial", 14, "bold"))
        self.appointment_label.place(x=260,y=70)
        self.appointment_combobox.place(x=260,y=100)



        separatoraboverequest = tk.Frame(self.window, height=3, width=620, bg='black')
        separatoraboverequest.place(x=10, y=340)

        # create a button to trigger the blood donation request
        self.request_button = tk.Button(self.window, text="Request Blood Donation", command=lambda: self.request_blood_donation(username), font=("Helvetica", 13, "bold"), bg='#EE4E34', fg='#FCEDDA',width=23)
        self.request_button.place(x=80,y=350)

        self.exit_button = tk.Button(self.window, text="Exit", command=exit, font=("Helvetica", 13, "bold"),bg='#EE4E34', fg='#FCEDDA',width=22)
        self.exit_button.place(x=333,y=350)
        
        back_button = tk.Button(self.window, text="<<", command=self.gobacktoLogin, bd=2)
        back_button.config(width=2,height=1, bd=2,font=("Helvetica",12,"bold"),bg='black', fg='white')
        back_button.place(x=10,y=350)
        
        separatorend = tk.Frame(self.window, height=3, width=620, bg='black')
        separatorend.place(x=10, y=390)
        
    def gobacktoLogin(self):
        self.window.destroy()
        a=main(self.username)
        

    def run(self):
        # start the GUI main loop
        self.window.mainloop()

    def upload_file(self):
        mydb = mysql.connector.connect(
            host='localhost',
            user='root',
            password='root',
            database='bloodbridge'
        )
        
        # open a file dialogue box to select a file to upload
        filename = filedialog.askopenfilename(initialdir="/", title="Select a File", filetypes=(("jpg", "*.jpg*"), ("png","*.png*"), ("all files", "*.*")))

        if filename:
            # read the contents of the file
            with open(filename, 'rb') as f:
                file_data = f.read()
                self.file_data = file_data  # store file_data as an instance variable

            # enable the blood bank list and request button
            self.blood_bank_listbox.delete(0, tk.END)
            
            mycursor = mydb.cursor()
            mycursor.execute("SELECT Bid, Name, Landmark, Contact FROM blood_banks")
            results = mycursor.fetchall()
            
            for r in results:
                row_string = f"{r[0]} | {r[1]} | {r[2]} | {r[3]}"
                self.blood_bank_listbox.insert(tk.END, row_string)
            """
            print(self.request_button['state'])  # print the current state of the button
            self.request_button.config(state=tk.NORMAL)
            print(self.request_button['state'])  # print the state of the button after enabling it
            """

    def request_blood_donation(self,username):

        mydb = mysql.connector.connect(
            host='localhost',
            user='root',
            password='root',
            database='bloodbridge'
        )
        
        selected_indices = self.blood_bank_listbox.curselection()
        for index in selected_indices:
            selected_item = self.blood_bank_listbox.get(index)
            # do something with the selected item
            self.bid=selected_item[0:2]
            #print(bid)

        # retrieve data from the database and populate widgets
        
        appoitment_date=self.date_picker.get_date()
        appointment_time = self.appointment_combobox.get()

        mycursor = mydb.cursor()
        query = "SELECT Name, Landmark, Contact FROM blood_banks WHERE Bid=%s"
        mycursor.execute(query, (self.bid,))
        results = mycursor.fetchall()
        for r in results:
            bname=r[0]
            blandmark=r[1]
            bcontact=r[2]

        query="INSERT INTO donation_requests (Bid, username, medical_report,appointment,timing) VALUES (%s, %s, %s,%s,%s)"
        mycursor.execute(query, (self.bid,username,self.file_data,appoitment_date,appointment_time))
        mydb.commit()
        sendmail_donation(username,bname,blandmark,appoitment_date,appointment_time)

        # create a new window with a yes/no question
        self.window.destroy()
        self.confirmation_window = tk.Tk()
        self.confirmation_window.geometry('640x400')
        self.confirmation_window.title("Blood Bank Details Confirmation")
        self.confirmation_window.config(bg='#FCEDDA')
        self.confirmation_window.iconbitmap("blooddrop.ico")
         # calculate the coordinates for centering the window
        x = (self.confirmation_window.winfo_screenwidth() - self.confirmation_window.winfo_reqwidth()) / 2
        y = (self.confirmation_window.winfo_screenheight() - self.confirmation_window.winfo_reqheight()) / 2

        # set the window position
        self.confirmation_window.geometry("+%d+%d" % (x-220,y-118))
        
        separator1 = tk.Frame(self.confirmation_window, height=3, width=620, bg='black')
        separator1.place(x=10, y=10)

        # create a label for the upload button
        self.titleprofile_button = tk.Button(self.confirmation_window, text="Confirmation Panel for Blood Donation Appointment",command="", font=("Helvetica", 12, "bold"),bg='#EE4E34', fg='#FCEDDA',width=50)
        self.titleprofile_button.place(x=60,y=20)
        
        separator2 = tk.Frame(self.confirmation_window, height=3, width=620, bg='black')
        separator2.place(x=10, y=60)
        
        
        frame = tk.Frame(self.confirmation_window, bg="light yellow", width=510, height=230,bd=5)
        frame.place(x=65, y=85)
        
        
        self.confirmationlabel_button = tk.Button(frame, text="Your Donation Appointment is Scheduled at: ", command="",font=("Arial", 11,"bold"),bg='#EE4E34', fg='#FCEDDA',width=52)
        self.confirmationlabel_button.place(x=10,y=5)   

        self.bname_button = tk.Button(frame, text="Bloodbank: ", command="",font=("Arial", 11,"bold"),bg='#EE4E34', fg='#FCEDDA',width=15)
        self.bname_button.place(x=10,y=60)          
        self.bname_entry=tk.Label(frame,text=bname,font=("Helvetica", 13, "bold"),width=31,relief="sunken")
        self.bname_entry.config(state='disabled')
        self.bname_entry.place(x=160,y=63)
                                       
        self.address_button = tk.Button(frame, text="Address: ", command="",font=("Arial", 11,"bold"),bg='#EE4E34', fg='#FCEDDA',width=15)
        self.address_button.place(x=10,y=100)      
        self.address_entry=tk.Label(frame,text=blandmark,font=("Helvetica", 14, "bold"),width=26,height=3,wraplength=200,relief="sunken")
        self.address_entry.config(state='disabled')
        self.address_entry.place(x=160,y=100)
                    
        self.contact_button = tk.Button(frame, text="Contact: ", command="",font=("Arial", 11,"bold"),bg='#EE4E34', fg='#FCEDDA',width=15)
        self.contact_button.place(x=10,y=180)
        self.contact_entry=tk.Label(frame,text=bcontact,font=("Helvetica", 15, "bold"),width=26,relief="sunken")
        self.contact_entry.config(state='disabled')
        self.contact_entry.place(x=160,y=182)
       
        '''
        # create a label with the question text
        displaymsg = "Your donation appointment is booked at \n"+bname+"\n Address:"+blandmark
        self.question_label = tk.Label(self.confirmation_window, text=displaymsg)
        self.question_label.pack()
        '''
        
        # create button for confirmation
        
        separatoraboveexit = tk.Frame(self.confirmation_window, height=3, width=620, bg='black')
        separatoraboveexit.place(x=10, y=340)
        #button command not working
        confirmationbutton = tk.Button(self.confirmation_window, text="Confirmed", command=lambda: self.backhome(),font=("Arial", 12,"bold"),bg='darkgreen', fg='#FCEDDA',width=50) 
        confirmationbutton.place(x=60,y=350)
        
        separatorbelowexit = tk.Frame(self.confirmation_window, height=3, width=620, bg='black')
        separatorbelowexit.place(x=10, y=390)
        """
        self.no_button = tk.Button(self.confirmation_window, text="No", command=self.confirmation_window.destroy)
        self.no_button.pack(side=tk.RIGHT, padx=10)
        

        # make the main window inactive until the question is answered
        self.window.attributes("-disabled", True)
        """
    def backhome(self):
        self.confirmation_window.destroy()
        main_obj=main(self.username)
        main_obj.run()

    def exit_program(self):
        # enable the main window and close the program
        sys.exit()

'''
username="jishan"
main_obj=main(username)
main_obj.run()
'''

mydb.close()