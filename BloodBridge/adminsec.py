import tkinter as tk
from tkinter import ttk
import mysql.connector
from tkinter import messagebox
from viewreport import view_report,view_report1
from mail import sendmail

mydb = mysql.connector.connect(
            host='localhost',
            user='root',
            password='root',
            database='bloodbridge'
        )

class admin:
    mydb = mysql.connector.connect(
            host='localhost',
            user='root',
            password='root',
            database='bloodbridge'
        )
    def __init__(self,bid):
        self.bid=bid
        self.window = tk.Tk()
        self.window.iconbitmap("blooddrop.ico")
        self.window.geometry('1000x700')
        self.window.config(bg='#EEEEAD')
        self.window.title("BloodBridge")
        self.window.pack_propagate(0)
        
        screen_width = self.window.winfo_screenwidth()
        screen_height = self.window.winfo_screenheight()

        # Calculate the x and y positions for the program window
        x = int((screen_width - 1000) / 2)
        y = int((screen_height - 700) / 2)

        # Set the program window position and size
        self.window.geometry(f"1000x700+{x}+{y-35}")
        # Add a heading with separator line
        
        ''' FRAME 0 MAIN WINDOW STARTS HERE AS PER THE ABOVE WIDGETS [ JISHANAHMED EDITS ]'''
            
        self.frame0=tk.Frame(self.window,width=1000,height=700,bg='#FCEDDA')
        
        separator = tk.Frame(self.frame0, height=3, width=980, bg='black')
        separator.place(x=10, y=10)
        heading = tk.Label(self.frame0, text="Welcome to the Bloodbridge Admin Section", font=("Helvetica", 36), bg='#FCEDDA', fg='#EE4E34')
        heading.place(x=30, y=20)
        separator = tk.Frame(self.frame0, height=3, width=980, bg='black')
        separator.place(x=10, y=90)
        
        ''' Mera personal wala frame aayega idhar ''' 
        
        
        frameself = tk.Frame(self.frame0, bg="light yellow", width=860, height=350)
        frameself.place(x=70, y=180)
        
        self.current_units = tk.Button(self.frame0, text="Current Blood Units", command=self.current,font=("Arial", 15,"bold"),bg='#EE4E34',fg='white',width=20,height=1)
        self.current_units.place(x=90, y=220)
        self.current_units_entry=tk.Label(self.frame0,text="<-" "Click to View Current Blood Units",font=("Helvetica", 21, "bold"),width=31,relief="sunken")
        self.current_units_entry.config(state='disabled')
        self.current_units_entry.place(x=360,y=220)

        self.blood_request_button = tk.Button(self.frame0, text="Blood Requests", command=self.request,font=("Arial", 15,"bold"),bg='#EE4E34',fg='white',width=20,height=1)
        self.blood_request_button.place(x=90, y=320)
        self.blood_requests_entry=tk.Label(self.frame0,text="<-" "Click to View Blood Requests",font=("Helvetica", 21, "bold"),width=31,relief="sunken")
        self.blood_requests_entry.config(state='disabled')
        self.blood_requests_entry.place(x=360,y=320)

        self.donation_request_button = tk.Button(self.frame0, text="Donation Requests", command=self.donation,font=("Arial", 15,"bold"),bg='#EE4E34',fg='white',width=20,height=1)
        self.donation_request_button.place(x=90, y=420)        
        self.donation_requests_entry=tk.Label(self.frame0,text="<-" "Click to View Donation Requests",font=("Helvetica", 21, "bold"),width=31,relief="sunken")
        self.donation_requests_entry.config(state='disabled')
        self.donation_requests_entry.place(x=360,y=420)
        
        separatormid = tk.Frame(self.frame0, height=3, width=980, bg='black')
        separatormid.place(x=10, y=640)
        
        back_button = tk.Button(self.frame0, text="<<", command=exit, bd=2)
        back_button.config(width=2,height=1, bd=2,font=("Helvetica",12,"bold"),bg='black', fg='white')
        back_button.place(x=10,y=650)
        
        exit_button = tk.Button(self.frame0, text="Exit", command=exit, bd=2)
        exit_button.config(width=41,height=1, bd=2,font=("Helvetica",12,"bold"),bg='#EE4E34', fg='#FCEDDA')
        exit_button.place(x=70,y=650)
        
        logout_button = tk.Button(self.frame0, text="Log Out", command=exit, bd=2)
        logout_button.config(width=41,height=1, bd=2,font=("Helvetica",12,"bold"),bg='darkgreen', fg='white')
        logout_button.place(x=510,y=650)
        
        fo_button = tk.Button(self.frame0, text=">>", command=exit, bd=2)
        fo_button.config(width=2,height=1, bd=2,font=("Helvetica",12,"bold"),bg='black', fg='white')
        fo_button.place(x=960,y=650)
        
        separatorend = tk.Frame(self.frame0, height=3, width=980, bg='black')
        separatorend.place(x=10, y=690)
        
        
        ''' FRAME 0 MAIN WINDOW ENDS HERE AS PER THE ABOVE WIDGETS [ JISHANAHMED EDITS ] '''


        # Create the three frames
        #frame1 to display current blood units available
        self.frame1 = tk.Frame(self.window, width=1000, height=700,bg='#FCEDDA')
        #frame2 is to display pending blood requests
        self.frame2 = tk.Frame(self.window, width=1000, height=700,bg='#FCEDDA')
        #frame3 is to display upcoming donation requests
        self.frame3 = tk.Frame(self.window, width=1000, height=700,bg='#FCEDDA')

        self.frame0.pack()

        # Use grid geometry manager to position the frames
        #self.frame1.grid(row=1, column=0, columnspan=2, padx=5, pady=5)
        #self.frame2.grid(row=2, column=0, padx=5, pady=5)
        #self.frame3.grid(row=2, column=1, padx=5, pady=5)

        self.frame0.pack_propagate(0)
        self.frame1.pack_propagate(0)
        self.frame2.pack_propagate(0)
        self.frame3.pack_propagate(0)

    #Contents of frame1:
        separator = tk.Frame(self.frame1, height=3, width=980, bg='black')
        separator.place(x=10, y=10)
        heading = tk.Label(self.frame1, text="Current Types of Blood Samples Available", font=("Helvetica", 36), bg='#FCEDDA', fg='#EE4E34')
        heading.pack(pady=20)
        separator = tk.Frame(self.frame1, height=3, width=980, bg='black')
        separator.place(x=10, y=90)
        
        ''' JISHAN KA KHUDKA WALA FRAME TO BE INSIDE OF FRAMES'''
        
        frameself = tk.Frame(self.frame1, bg="light yellow", width=860, height=450)
        frameself.place(x=70, y=140)
        
        
        self.donation_request_button = tk.Button(frameself, text="List of Bloodtypes and their No. of Units in your Inventory: ", command=self.donation,font=("Arial", 15,"bold"),bg='#EE4E34',fg='white',width=69,height=1)
        self.donation_request_button.place(x=10, y=10) 
        
        
        cursor = mydb.cursor()
        query = f"SELECT Current_units_Aplus, Current_units_Aminus, Current_units_Bplus, Current_units_Bminus, Current_units_ABplus, Current_units_ABminus, Current_units_Oplus, Current_units_Ominus FROM blood_banks WHERE Bid = {self.bid}"
        cursor.execute(query)
        result = cursor.fetchone()
        aplus = result[0]
        aminus = result[1]
        bplus = result[2]
        bminus = result[3]
        abplus = result[4]
        abminus = result[5]
        oplus = result[6]
        ominus = result[7]
        
        # Add labels for the current blood units
        self.aplus_label = tk.Label(frameself, text="", font=("Helvetica", 15,"bold"),width=40,relief="sunken")
        self.aplus_label.place(x=10, y=80)
        self.aplus_entry=tk.Label(frameself,text=aplus,font=("Helvetica", 15, "bold"),width=25,relief="sunken")
        self.aplus_entry.config(state='disabled')
        self.aplus_entry.place(x=540, y=80)
        
        self.aminus_label = tk.Label(frameself, text="", font=("Helvetica", 15,"bold"),width=40,relief="sunken")
        self.aminus_label.place(x=10, y=120)
        self.aminus_entry=tk.Label(frameself,text=aminus,font=("Helvetica", 15, "bold"),width=25,relief="sunken")
        self.aminus_entry.config(state='disabled')
        self.aminus_entry.place(x=540, y=120)
        
        
        self.bplus_label = tk.Label(frameself, text="", font=("Helvetica", 15,"bold"),width=40,relief="sunken")
        self.bplus_label.place(x=10, y=160)
        self.bplus_entry=tk.Label(frameself,text=bplus,font=("Helvetica", 15, "bold"),width=25,relief="sunken")
        self.bplus_entry.config(state='disabled')
        self.bplus_entry.place(x=540, y=160)
        
        
        self.bminus_label = tk.Label(frameself, text="", font=("Helvetica", 15,"bold"),width=40,relief="sunken")
        self.bminus_label.place(x=10, y=200)
        self.bminus_entry=tk.Label(frameself,text=bminus,font=("Helvetica", 15, "bold"),width=25,relief="sunken")
        self.bminus_entry.config(state='disabled')
        self.bminus_entry.place(x=540, y=200)
        
        
        
        self.abplus_label = tk.Label(frameself, text="", font=("Helvetica", 15,"bold"),width=40,relief="sunken")
        self.abplus_label.place(x=10, y=240)
        self.abplus_entry=tk.Label(frameself,text=abplus,font=("Helvetica", 15, "bold"),width=25,relief="sunken")
        self.abplus_entry.config(state='disabled')
        self.abplus_entry.place(x=540, y=240)
        
        
        self.abminus_label = tk.Label(frameself, text="", font=("Helvetica", 15,"bold"),width=40,relief="sunken")
        self.abminus_label.place(x=10, y=280)
        self.abminus_entry=tk.Label(frameself,text=abminus,font=("Helvetica", 15, "bold"),width=25,relief="sunken")
        self.abminus_entry.config(state='disabled')
        self.abminus_entry.place(x=540, y=280)
        
        
        self.oplus_label = tk.Label(frameself, text="",font=("Helvetica", 15,"bold"),width=40,relief="sunken")
        self.oplus_label.place(x=10, y=320)
        self.oplus_entry=tk.Label(frameself,text=oplus,font=("Helvetica", 15, "bold"),width=25,relief="sunken")
        self.oplus_entry.config(state='disabled')
        self.oplus_entry.place(x=540, y=320)
        
        
        self.ominus_label = tk.Label(frameself, text="",font=("Helvetica", 15,"bold"),width=40,relief="sunken")
        self.ominus_label.place(x=10, y=360)
        self.ominus_entry=tk.Label(frameself,text=ominus,font=("Helvetica", 15, "bold"),width=25,relief="sunken")
        self.ominus_entry.config(state='disabled')
        self.ominus_entry.place(x=540, y=360)
        
        
        
        
        ''' JISHANAHMED EDITS AND DESIGNING '''
        separatormid = tk.Frame(self.frame1, height=3, width=980, bg='black')
        separatormid.place(x=10, y=640)
        
        back_button = tk.Button(self.frame1, text="<<", command=self.go_back, bd=2)
        back_button.config(width=2,height=1, bd=2,font=("Helvetica",12,"bold"),bg='black', fg='white')
        back_button.place(x=10,y=650)
        
        exit_button = tk.Button(self.frame1, text="Exit", command=exit, bd=2)
        exit_button.config(width=41,height=1, bd=2,font=("Helvetica",12,"bold"),bg='#EE4E34', fg='#FCEDDA')
        exit_button.place(x=70,y=650)
        
        logout_button = tk.Button(self.frame1, text="Log Out", command=exit, bd=2)
        logout_button.config(width=41,height=1, bd=2,font=("Helvetica",12,"bold"),bg='darkgreen', fg='white')
        logout_button.place(x=510,y=650)
        
        fo_button = tk.Button(self.frame1, text=">>", command=self.go_back, bd=2)
        fo_button.config(width=2,height=1, bd=2,font=("Helvetica",12,"bold"),bg='black', fg='white')
        fo_button.place(x=960,y=650)
        
        separatorend = tk.Frame(self.frame1, height=3, width=980, bg='black')
        separatorend.place(x=10, y=690)
        
        ''' JISHANAHMED EDITS AND DESIGNING '''

        self.update_blood_units() # call the function to update the labels

    #Contents of frame2:



        separator = tk.Frame(self.frame2, height=3, width=980, bg='black')
        separator.place(x=10, y=10)
        heading = tk.Label(self.frame2, text="Current Blood Requests Panel (Verification of Reports) ", font=("Helvetica", 30), bg='#FCEDDA', fg='#EE4E34')
        heading.pack(pady=25)
        separator = tk.Frame(self.frame2, height=3, width=980, bg='black')
        separator.place(x=10, y=90)
        
        
        separatormid = tk.Frame(self.frame2, height=3, width=980, bg='black')
        separatormid.place(x=10, y=640)
        
        back_button = tk.Button(self.frame2, text="<<", command=self.go_back, bd=2)
        back_button.config(width=2,height=1, bd=2,font=("Helvetica",12,"bold"),bg='black', fg='white')
        back_button.place(x=10,y=650)
        
        exit_button = tk.Button(self.frame2, text="Exit", command=exit, bd=2)
        exit_button.config(width=41,height=1, bd=2,font=("Helvetica",12,"bold"),bg='#EE4E34', fg='#FCEDDA')
        exit_button.place(x=510,y=650)
        
        logout_button = tk.Button(self.frame2, text="Log Out", command=exit, bd=2)
        logout_button.config(width=41,height=1, bd=2,font=("Helvetica",12,"bold"),bg='darkgreen', fg='white')
        logout_button.place(x=70,y=650)
        
        fo_button = tk.Button(self.frame2, text=">>", command=self.go_back, bd=2)
        fo_button.config(width=2,height=1, bd=2,font=("Helvetica",12,"bold"),bg='black', fg='white')
        fo_button.place(x=960,y=650)
        
        separatorend = tk.Frame(self.frame2, height=3, width=980, bg='black')
        separatorend.place(x=10, y=690)
        

        # Create table
        self.tree1 = ttk.Treeview(self.frame2,height=15)
        self.tree1["columns"] = ( "username", "bloodtype", "units_required", "status")
        self.tree1.heading("#0", text="Request ID")
        self.tree1.column("#0", width=170)
        self.tree1.heading("username", text="Username")
        self.tree1.column("username", width=170)
        self.tree1.heading("bloodtype", text="Blood Type")
        self.tree1.column("bloodtype", width=170)
        self.tree1.heading("units_required", text="Units Required")
        self.tree1.column("units_required", width=170)
        self.tree1.heading("status", text="Status")
        self.tree1.column("status", width=170)

        #update the treeview
        self.update_blood_request_tree_view()

        # Pack table into Tkinter window
        self.tree1.place(x=70,y=160)


        view_button1 = tk.Button(self.frame2,width=41,text="View Report",bd=2,font=("Helvetica",12,"bold"),bg='#EE4E34',fg='white',command=lambda: self.view1())
        view_button1.place(x=70,y=500)

        approve_button1 = tk.Button(self.frame2,width=20,text="Approve",bd=2,font=("Helvetica",12,"bold"),bg='darkgreen',fg='white',command=lambda: self.approve_blood_request())
        approve_button1.place(x=510,y=500)

        decline_button1 = tk.Button(self.frame2,width=18,text="Decline",bd=2,font=("Helvetica",12,"bold"),bg='red',fg='white',command=lambda: self.decline_blood_request())
        decline_button1.place(x=730,y=500)






    #Contents of frame3(donation requests frame) start here:
        heading3 = tk.Label(self.frame3, text="Upcoming Requests from Users to Donate Blood Samples",font=("Helvetica", 15,"bold"),width=70,relief="sunken",bg='#FCEDDA', fg='#EE4E34')
        heading3.place(x=70, y=130)

        # Create table
        self.tree = ttk.Treeview(self.frame3,height=12)
        self.tree["columns"] = ("Bid", "username", "appointment", "timing")
        self.tree.heading("#0", text="Request ID")
        self.tree.column("#0", width=170)
        self.tree.heading("Bid", text="Bid")
        self.tree.column("Bid", width=170)
        self.tree.heading("username", text="Username")
        self.tree.column("username", width=170)
        self.tree.heading("appointment", text="Appointment")
        self.tree.column("appointment", width=170)
        self.tree.heading("timing", text="Timing")
        self.tree.column("timing", width=170)

        # Fetch data from MySQL table
        self.update_request_tree_view()

        # Pack table into Tkinter window
        self.tree.place(x=70, y=170)
        
        separator = tk.Frame(self.frame3, height=3, width=980, bg='black')
        separator.place(x=10, y=10)
        heading = tk.Label(self.frame3, text="Blood Donation Requests Management", font=("Helvetica",32), bg='#FCEDDA', fg='#EE4E34')
        heading.place(x=120, y=20)
        separator = tk.Frame(self.frame3, height=3, width=980, bg='black')
        separator.place(x=10, y=90)


        Approval_label = tk.Label(self.frame3, text="Manage Request Status",font=("Helvetica", 18,"bold"),width=28,relief="sunken",bg='#FCEDDA', fg='#EE4E34')
        Approval_label.place(x=70,y=450)

        # Create request id field
        tk.Label(self.frame3, text="Request ID",font=("Helvetica", 17,"bold"),width=13,relief="sunken",bg='#FCEDDA', fg='#EE4E34').place(x=730,y=450)
        self.request_id_entry = tk.Entry(self.frame3,bd=2,font=("Helvetica", 18,"bold"),width=15,relief="sunken")
        self.request_id_entry.place(x=510,y=450)

        # Create drop-down menu
        '''
        tk.Label(self.frame3, text="Select Action").pack()
        actions=["Approve","Decline"]
        self.action_var = tk.StringVar(self.frame3)
        self.action_var.set
        self.action_dropdown = ttk.Combobox(self.frame3, textvariable=self.action_var, values=["Approve", "Decline"])
        self.action_dropdown.pack()
        '''
        units_label=tk.Label(self.frame3, text="Units donated if applicable:",font=("Helvetica", 18,"bold"),width=28,relief="sunken",bg='#FCEDDA', fg='#EE4E34')
        units_label.place(x=70,y=500)
        self.units_entry=tk.Entry(self.frame3,bd=2,font=("Helvetica", 18,"bold"),width=15,relief="sunken")
        self.units_entry.place(x=510,y=500)
        # define the options for the dropdown menu
        Blood_types = ["A+", "A-", "B+", "B-", "AB+", "AB-", "O+", "O-"]

        # create the dropdown menu widget
        self.selected = tk.StringVar(self.frame3)
        self.selected.set(Blood_types[0])  # default value
        self.option_menu = tk.OptionMenu(self.frame3, self.selected, *Blood_types)
        self.option_menu.config(width=21, height=1, font=('Helvetica', 10), foreground="black", background="white", borderwidth=2, relief="groove")
        self.option_menu.place(x=730,y=500)

        # Create submit button
        view_button = tk.Button(self.frame3,width=41,text="View Report",bd=2,font=("Helvetica",12,"bold"),bg='#EE4E34',fg='white',command=lambda: self.view())
        view_button.place(x=70,y=550)

        approve_button = tk.Button(self.frame3, text="Approve",width=20,bd=2,font=("Helvetica",12,"bold"),bg='darkgreen',fg='white',command=lambda: self.approve_request())
        approve_button.place(x=510,y=550)

        decline_button = tk.Button(self.frame3, text="Decline",width=19,bd=2,font=("Helvetica",12,"bold"),bg='red',fg='white',command=lambda: self.decline_request())
        decline_button.place(x=730,y=550)
        
        separatormid = tk.Frame(self.frame3, height=3, width=980, bg='black')
        separatormid.place(x=10, y=640)
        
        back_button = tk.Button(self.frame3, text="<<", command=self.go_back, bd=2)
        back_button.config(width=2,height=1, bd=2,font=("Helvetica",12,"bold"),bg='black', fg='white')
        back_button.place(x=10,y=650)
        
        exit_button = tk.Button(self.frame3, text="Exit", command=exit, bd=2)
        exit_button.config(width=41,height=1, bd=2,font=("Helvetica",12,"bold"),bg='#EE4E34', fg='#FCEDDA')
        exit_button.place(x=510,y=650)
        
        logout_button = tk.Button(self.frame3, text="Log Out", command=exit, bd=2)
        logout_button.config(width=41,height=1, bd=2,font=("Helvetica",12,"bold"),bg='darkgreen', fg='white')
        logout_button.place(x=70,y=650)
        
        fo_button = tk.Button(self.frame3, text=">>", command=self.go_back, bd=2)
        fo_button.config(width=2,height=1, bd=2,font=("Helvetica",12,"bold"),bg='black', fg='white')
        fo_button.place(x=960,y=650)
        
        separatorend = tk.Frame(self.frame3, height=3, width=980, bg='black')
        separatorend.place(x=10, y=690)

    def view1(self):
        selected_item = self.tree1.selection()
        if selected_item:
            # Get the values of the selected item
            req_id=int(self.tree1.item(selected_item)['text'])
        view_report1(req_id)

    def view(self):
        selected_item = self.tree.selection()
        if selected_item:
            # Get the values of the selected item
            req_id=int(self.tree.item(selected_item)['text'])
        view_report(req_id)


    def approve_request(self):
        blood_type = self.selected.get()
        req_id = self.request_id_entry.get()
        units=int(self.units_entry.get())
        # Update the status of the request in the database
        cursor = mydb.cursor()
        cursor.execute("UPDATE donation_requests SET status=%s,units=%s WHERE request_id=%s", (1,units, req_id))
        mydb.commit()
        # Construct the SQL query
        sql = "UPDATE blood_banks SET "
        
        if blood_type == "A+":
            sql += "Current_units_Aplus = Current_units_Aplus + %s "
        elif blood_type == "A-":
            sql += "Current_units_Aminus = Current_units_Aminus + %s "
        elif blood_type == "B+":
            sql += "Current_units_Bplus = Current_units_Bplus + %s "
        elif blood_type == "B-":
            sql += "Current_units_Bminus = Current_units_Bminus + %s "
        elif blood_type == "AB+":
            sql += "Current_units_ABplus = Current_units_ABplus + %s "
        elif blood_type == "AB-":
            sql += "Current_units_ABminus = Current_units_ABminus + %s "
        elif blood_type == "O+":
            sql += "Current_units_Oplus = Current_units_Oplus + %s "
        elif blood_type == "O-":
            sql += "Current_units_Ominus = Current_units_Ominus + %s "
        
        sql += "WHERE Bid = %s"
         # Execute the query
        cursor.execute(sql, (units, self.bid))
        mydb.commit()

        self.update_request_tree_view()
        self.update_blood_units()

        info="Request Number: "+str(req_id)+" is approved! Mail sent to user!"
        messagebox.showinfo("Request approved",info)
        query="select  d.username,u.email from users u,donation_requests d where d.request_id=%s and u.username=d.username"
        cursor.execute(query,(req_id,))
        result=cursor.fetchone()
        username=result[0]
        email=result[1]
        sendmail(username,email,"donation")

    def approve_blood_request(self):
        mydb = mysql.connector.connect(
            host='localhost',
            user='root',
            password='root',
            database='bloodbridge'
        )
        
        selected_item = self.tree1.selection()
        if selected_item:
            # Get the values of the selected item
            req_id=int(self.tree1.item(selected_item)['text'])
            item_values = self.tree1.item(selected_item)['values']
            blood_type = item_values[1]
            units=int(item_values[2])
            #print(req_id)

        else:
            print('No item selected')

        
        
        # Update the status of the request in the database
        cursor = mydb.cursor()
        cursor.execute("UPDATE blood_requests SET status=%s WHERE request_id=%s", (1, req_id))
        mydb.commit()
        # Construct the SQL query
        sql = "UPDATE blood_banks SET "
        
        if blood_type == "A+":
            sql += "Current_units_Aplus = Current_units_Aplus - %s "
        elif blood_type == "A-":
            sql += "Current_units_Aminus = Current_units_Aminus - %s "
        elif blood_type == "B+":
            sql += "Current_units_Bplus = Current_units_Bplus - %s "
        elif blood_type == "B-":
            sql += "Current_units_Bminus = Current_units_Bminus - %s "
        elif blood_type == "AB+":
            sql += "Current_units_ABplus = Current_units_ABplus - %s "
        elif blood_type == "AB-":
            sql += "Current_units_ABminus = Current_units_ABminus - %s "
        elif blood_type == "O+":
            sql += "Current_units_Oplus = Current_units_Oplus - %s "
        elif blood_type == "O-":
            sql += "Current_units_Ominus = Current_units_Ominus - %s "
        
        sql += "WHERE Bid = %s"
         # Execute the query
        cursor.execute(sql, (units, self.bid))
        mydb.commit()

        query="select  b.username,u.email from users u,blood_requests b where b.request_id=%s and u.username=b.username"
        cursor.execute(query,(req_id,))
        result=cursor.fetchone()
        username=result[0]
        email=result[1]
        query="select Name,Contact from blood_banks where Bid=%s"
        cursor.execute(query,(self.bid,))
        result=cursor.fetchone()
        bname=result[0]
        contact=result[1]
        sndmsg="Blood Bank Name: "+bname+" Conact Details: "+contact
        sendmail(username,email,sndmsg)

        self.update_blood_request_tree_view()
        self.update_blood_units()


        info="Request Number: "+str(req_id)+" is approved! Mail sent to user!"
        messagebox.showinfo("Request approved",info)


    def decline_request(self):
        req_id = self.request_id_entry.get()
        # Update the status of the request in the database
        cursor = mydb.cursor()
        cursor.execute("UPDATE donation_requests SET status=%s WHERE request_id=%s", (-1,req_id,))
        mydb.commit()
        
        self.update_request_tree_view()
        self.update_blood_units()

        info="Request Number: "+req_id+" is declined!"
        messagebox.showinfo("Request declined",info)
        query="select  d.username,u.email from users u,donation_requests d where d.request_id=%s and u.username=d.username"
        cursor.execute(query,(req_id,))
        result=cursor.fetchone()
        username=result[0]
        email=result[1]
        sendmail(username,email,"donation")

    def decline_blood_request(self):
        selected_item = self.tree1.selection()
        if selected_item:
            # Get the values of the selected item
            req_id=int(self.tree1.item(selected_item)['text'])
            item_values = self.tree1.item(selected_item)['values']
            blood_type = item_values[1]
            units=int(item_values[2])
            #print(req_id)

        else:
            print('No item selected')
        # Update the status of the request in the database
        cursor = mydb.cursor()
        cursor.execute("UPDATE blood_requests SET status=%s WHERE request_id=%s", (-1,req_id,))
        mydb.commit()
        
        self.update_blood_request_tree_view()
        self.update_blood_units()

        
        query="select  b.username,u.email from users u,blood_requests b where b.request_id=%s and u.username=b.username"
        cursor.execute(query,(req_id,))
        result=cursor.fetchone()
        username=result[0]
        email=result[1]
        sendmail(username,email,"decline")

        info="Request Number: "+str(req_id)+" is declined!"
        messagebox.showinfo("Request declined",info)

    def go_back(self):
        self.frame1.pack_forget()
        self.frame2.pack_forget()
        self.frame3.pack_forget()
        self.frame0.pack()

    def current(self):
        self.frame0.pack_forget()
        self.frame1.pack()

    def request(self):
        self.frame0.pack_forget()
        self.frame2.pack()
        self.update_blood_request_tree_view()


    def donation(self):
        self.frame0.pack_forget()
        self.frame3.pack()

    def update_blood_units(self):
        # query the database to get the current blood units for the given blood bank ID
        cursor = mydb.cursor()
        query = f"SELECT Current_units_Aplus, Current_units_Aminus, Current_units_Bplus, Current_units_Bminus, Current_units_ABplus, Current_units_ABminus, Current_units_Oplus, Current_units_Ominus FROM blood_banks WHERE Bid = {self.bid}"
        cursor.execute(query)
        result = cursor.fetchone()
        
        aplus = str(result[0])
        aminus = str(result[1])
        bplus = str(result[2])
        bminus = str(result[3])
        abplus = str(result[4])
        abminus = str(result[5])
        oplus = str(result[6])
        ominus = str(result[7])

        # update the labels in frame1 with the current blood units
        self.aplus_label.config(text="No of Units of Blood Type :                A+ ")
        self.aminus_label.config(text="No of Units of Blood Type :               A- ")
        self.bplus_label.config(text="No of Units of Blood Type :               B+ ")
        self.bminus_label.config(text="No of Units of Blood Type :               B- ")
        self.abplus_label.config(text="No of Units of Blood Type :               AB+ ")
        self.abminus_label.config(text="No of Units of Blood Type :               AB- ")
        self.oplus_label.config(text="No of Units of Blood Type :               O+ ")
        self.ominus_label.config(text="No of Units of Blood Type :               O-")

        # update the labels with new value
        self.aplus_entry.config(text=aplus)
        self.aminus_entry.config(text=aminus)
        self.bplus_entry.config(text=bplus)
        self.bminus_entry.config(text=bminus)
        self.abplus_entry.config(text=abplus)
        self.abminus_entry.config(text=abminus)
        self.oplus_entry.config(text=oplus)
        self.ominus_entry.config(text=ominus)

    def update_request_tree_view(self):
        # Clear the tree view widget
        self.tree.delete(*self.tree.get_children())

        # Retrieve the latest donation requests from the database
        # Fetch data from MySQL table
        cursor = mydb.cursor()
        cursor.execute("SELECT request_id, Bid, username,appointment, timing FROM donation_requests where status=0 and Bid=%s",(self.bid,))
        rows = cursor.fetchall()
        for row in rows:
            self.tree.insert("", tk.END, text=row[0], values=(row[1], row[2], row[3], row[4]))

    def update_blood_request_tree_view(self):
        # Clear the tree view widget
        self.tree1.delete(*self.tree1.get_children())

        # Retrieve the latest blood requests from the database
        # Fetch data from MySQL table
        cursor = mydb.cursor()
        cursor.execute("SELECT request_id, username, bloodtype, units_required, status FROM blood_requests WHERE status = 0")
        rows = cursor.fetchall()
        for row in rows:
            self.tree1.insert("", tk.END, text=row[0], values=(row[1], row[2], row[3], row[4]))


    def run(self):
        # start the GUI main loop
        self.window.mainloop()
        

temp_obj=admin(13)
temp_obj.run()
