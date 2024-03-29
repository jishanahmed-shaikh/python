import tkinter as tk
from tkinter import filedialog, messagebox
import mysql.connector
from mainprog import main
from adminsec import admin

# Establish MySQL connection
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="bloodbridge"
)
# Create cursor object
cursor = db.cursor()

class LoginWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("BloodBridge")
        self.iconbitmap("blooddrop.ico")
        self.geometry("640x400")
        self.config(bg='#FCEDDA')
         # calculate the coordinates for centering the window
        x = (self.winfo_screenwidth() - self.winfo_reqwidth()) / 2
        y = (self.winfo_screenheight() - self.winfo_reqheight()) / 2

        # set the window position
        self.geometry("+%d+%d" % (x-220,y-118))

        #FCEDDA light yellow
        #EE4E34 orange

        # Add a heading with separator line
        separator = tk.Frame(self, height=3, width=620, bg='black')
        separator.place(x=10, y=10)
        
        heading_frame = tk.Frame(self, bg='#2F3C7E')
        heading_frame.pack(pady=20)
        heading = tk.Label(heading_frame, text="Welcome to the Bloodbridge!", font=("Helvetica", 36), bg='#FCEDDA', fg='#EE4E34')
        heading.pack()
        separator = tk.Frame(self, height=3, width=620, bg='black')
        separator.place(x=10, y=90)

        # create a sign up button
        signup_label = tk.Label(self, text="To Register: ",font=("Helvetica", 18, "bold"), bg='#FCEDDA', fg='#EE4E34')
        signup_label.place(x=80, y=130)
        signup_btn = tk.Button(self, text="Sign Up", font=("Helvetica", 15,"bold"), width=20, bg='#EE4E34', fg='#FCEDDA', command=self.signup)
        signup_btn.place(x=300, y=130)

        # create a log in button
        login_label = tk.Label(self, text="To Login: ", font=("Helvetica", 18, "bold"), bg='#FCEDDA', fg='#EE4E34')
        login_label.place(x=80, y=190)
        login_btn = tk.Button(self, text="Log In", font=("Helvetica", 15, "bold"), width=20, bg='#EE4E34', fg='#FCEDDA', command=self.login)
        login_btn.place(x=300, y=190)

        # create an exit button
        admin_label = tk.Label(self, text="Admin Portal: ", font=("Helvetica", 18, "bold"), bg='#FCEDDA', fg='#EE4E34')
        admin_label.place(x=80, y=250)
        admin_button = tk.Button(self, text="Admin Login", font=("Helvetica", 15, "bold"), bg='#EE4E34', fg='#FCEDDA', width=20, command=self.admin)
        admin_button.place(x=300, y=250)
        
        exit_label = tk.Label(self, text="To Exit: ", font=("Helvetica", 18, "bold"), bg='#FCEDDA', fg='#EE4E34')
        exit_label.place(x=80, y=310)
        exit_button = tk.Button(self, text="Exit", font=("Helvetica", 15, "bold"), bg='#EE4E34', fg='#FCEDDA', width=20, command=exit)
        exit_button.place(x=300, y=310)
        
        separator2 = tk.Frame(self, height=3, width=620, bg='black')
        separator2.place(x=10, y=380)

    def login(self):
        self.iconify()
        login_window = Login(self)

    def admin(self):
        self.iconify()
        admin_login_window = AdminLogin(self)

    def signup(self):
        # code to call signup class
        self.iconify()
        signup_window = Signup(self)

class AdminLogin(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Admin Login")
        self.iconbitmap("blooddrop.ico")
        self.geometry("640x400")
        self.config(bg='#FCEDDA')
        # calculate the coordinates for centering the window
        x = (self.winfo_screenwidth() - self.winfo_reqwidth()) / 2
        y = (self.winfo_screenheight() - self.winfo_reqheight()) / 2

        # set the window position
        self.geometry("+%d+%d" % (x-220,y-118))
        
        separator = tk.Frame(self, height=3, width=620, bg='black')
        separator.place(x=10, y=10)
        
        heading_frame = tk.Frame(self, bg='#2F3C7E')
        heading_frame.pack(pady=20)
        heading = tk.Label(heading_frame, text="Welcome to the Bloodbridge!", font=("Helvetica", 36), bg='#FCEDDA', fg='#EE4E34')
        heading.pack()
        separator = tk.Frame(self, height=3, width=620, bg='black')
        separator.place(x=10, y=90)
        
        
        description_btn = tk.Button(self, text="Enter Your Login Details in the Below Fields:", font=("Helvetica", 15,"bold"), width=39, bg='#FF745C', fg='#FCEDDA', command="",bd=2)
        description_btn.place(x=70, y=130)
        
        bid_label = tk.Label(self, text="Enter Blood Bank ID:",font=("Helvetica", 18,"bold"), bg='#FCEDDA', fg='#EE4E34')
        bid_label.place(x=70, y=182)
        self.bid_entry = tk.Entry(self,width=21,font=("Helvetica", 14,"bold"))
        self.bid_entry.place(x=320,y=190)

        # Create password label and entry field
        password_label = tk.Label(self, text="Enter Password:",font=("Helvetica", 18,"bold"), bg='#FCEDDA', fg='#EE4E34')
        password_label.place(x=70,y=228)
        self.password_entry = tk.Entry(self, show="*",width=21,font=("Helvetica", 14,"bold"))
        self.password_entry.place(x=320,y=236)
        
        separatormid = tk.Frame(self, height=3, width=620, bg='black')
        separatormid.place(x=10, y=340)
        
        back_button = tk.Button(self, text="<<", command=self.back, bd=2)
        back_button.config(width=2,height=1, bd=2,font=("Helvetica",12,"bold"),bg='black', fg='white')
        back_button.place(x=10,y=350)
        
        exit_button = tk.Button(self, text="Exit", command=exit, bd=2)
        exit_button.config(width=22,height=1, bd=2,font=("Helvetica",12,"bold"),bg='#EE4E34', fg='#FCEDDA')
        exit_button.place(x=70,y=350)
        
        login_button = tk.Button(self, text="Login", command=self.login, bd=2)
        login_button.config(width=23,height=1, bd=2,font=("Helvetica",12,"bold"),bg='darkgreen', fg='white')
        login_button.place(x=310,y=350)
        
        separator3 = tk.Frame(self, height=3, width=620, bg='black')
        separator3.place(x=10, y=390)
        
    def back(self):
        AdminLogin.destroy(self)
        app.deiconify()

    def login(self):
        # Replace this with your login code
        bid = self.bid_entry.get()
        password = self.password_entry.get()
        #print(f"Login with username {username} and password {password}")
        
        # Create a MySQL cursor object
        cursor = db.cursor()

        # Execute the SQL query to verify the user's credentials
        query = "SELECT * FROM blood_banks WHERE Bid=%s AND password=%s"
        cursor.execute(query, (bid, password))

        # Fetch the result of the query
        result = cursor.fetchone()
        
         # If the query returns a row, the login is successful
        if result:
            messagebox.showinfo("Login", "Login successful!")
            self.destroy()
            temp_obj=admin(bid)
            temp_obj.run()

        else:
            messagebox.showerror("Login", "Invalid bid or password.")

class Login(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Login")
        self.iconbitmap("blooddrop.ico")
        self.geometry("640x400")
        self.config(bg='#FCEDDA')
        # calculate the coordinates for centering the window
        x = (self.winfo_screenwidth() - self.winfo_reqwidth()) / 2
        y = (self.winfo_screenheight() - self.winfo_reqheight()) / 2

        # set the window position
        self.geometry("+%d+%d" % (x-220,y-118))
        
        separator = tk.Frame(self, height=3, width=620, bg='black')
        separator.place(x=10, y=10)
        
        heading_frame = tk.Frame(self, bg='#2F3C7E')
        heading_frame.pack(pady=20)
        heading = tk.Label(heading_frame, text="Welcome to the Bloodbridge!", font=("Helvetica", 36), bg='#FCEDDA', fg='#EE4E34')
        heading.pack()
        separator = tk.Frame(self, height=3, width=620, bg='black')
        separator.place(x=10, y=90)
        
        
        description_btn = tk.Button(self, text="Enter Your Login Details in the Below Fields:", font=("Helvetica", 15,"bold"), width=39, bg='#FF745C', fg='#FCEDDA', command="",bd=2)
        description_btn.place(x=70, y=130)
        
        username_label = tk.Label(self, text="Enter Username:",font=("Helvetica", 18,"bold"), bg='#FCEDDA', fg='#EE4E34')
        username_label.place(x=70, y=182)
        self.username_entry = tk.Entry(self,width=22,font=("Helvetica", 14,"bold"))
        self.username_entry.place(x=300,y=190)

        # Create password label and entry field
        password_label = tk.Label(self, text="Enter Password:",font=("Helvetica", 18,"bold"), bg='#FCEDDA', fg='#EE4E34')
        password_label.place(x=70,y=228)
        self.password_entry = tk.Entry(self, show="*",width=22,font=("Helvetica", 14,"bold"))
        self.password_entry.place(x=300,y=236)
        
        separatormid = tk.Frame(self, height=3, width=620, bg='black')
        separatormid.place(x=10, y=340)
        
        back_button = tk.Button(self, text="<<", command=self.back, bd=2)
        back_button.config(width=2,height=1, bd=2,font=("Helvetica",12,"bold"),bg='black', fg='white')
        back_button.place(x=10,y=350)
        
        exit_button = tk.Button(self, text="Exit", command=exit, bd=2)
        exit_button.config(width=22,height=1, bd=2,font=("Helvetica",12,"bold"),bg='#EE4E34', fg='#FCEDDA')
        exit_button.place(x=70,y=350)
        
        login_button = tk.Button(self, text="Login", command=self.login, bd=2)
        login_button.config(width=23,height=1, bd=2,font=("Helvetica",12,"bold"),bg='darkgreen', fg='white')
        login_button.place(x=310,y=350)
        
        separator3 = tk.Frame(self, height=3, width=620, bg='black')
        separator3.place(x=10, y=390)
        
    def back(self):
        Login.destroy(self)
        app.deiconify()

    def login(self):
        # Replace this with your login code
        username = self.username_entry.get()
        password = self.password_entry.get()
        #print(f"Login with username {username} and password {password}")
        
        # Create a MySQL cursor object
        cursor = db.cursor()

        # Execute the SQL query to verify the user's credentials
        query = "SELECT * FROM users WHERE username=%s AND password=%s"
        cursor.execute(query, (username, password))

        # Fetch the result of the query
        result = cursor.fetchone()
        
         # If the query returns a row, the login is successful
        if result:
            messagebox.showinfo("Login", "Login successful!")
            self.destroy()
            app.destroy()
            main_obj=main(username)
            main_obj.run()

        else:
            messagebox.showerror("Login", "Invalid username or password.")





class Signup(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Signup")
        self.iconbitmap("blooddrop.ico")
        self.geometry("640x400")
        self.config(bg='#FCEDDA')
        # calculate the coordinates for centering the window
        x = (self.winfo_screenwidth() - self.winfo_reqwidth()) / 2
        y = (self.winfo_screenheight() - self.winfo_reqheight()) / 2

        # set the window position
        self.geometry("+%d+%d" % (x-220,y-118))
        
        
        separator1 = tk.Frame(self, height=3, width=620, bg='black')
        separator1.place(x=10, y=10)

        # Create username label and entry field
        username_label = tk.Label(self, text="Enter Your Username:",font=("Helvetica", 11, "bold"), bg='#FCEDDA', fg='#EE4E34')
        username_label.place(x=70, y=30)
        self.username_entry = tk.Entry(self,width=40)
        self.username_entry.place(x=300,y=30)



        # Create password label and entry field
        password_label = tk.Label(self, text="Enter Your Password:",font=("Helvetica", 11, "bold"), bg='#FCEDDA', fg='#EE4E34')
        password_label.place(x=70,y=60)
        self.password_entry = tk.Entry(self, show="*",width=40)
        self.password_entry.place(x=300,y=60)



        # Create confirm password label and entry field
        confirm_password_label = tk.Label(self, text="Please Confirm Password:",font=("Helvetica", 11, "bold"), bg='#FCEDDA', fg='#EE4E34')
        confirm_password_label.place(x=70,y=90)
        self.confirm_password_entry = tk.Entry(self, show="*",width=40)
        self.confirm_password_entry.place(x=300,y=90)


        # Create email label and entry field
        email_label = tk.Label(self, text="Enter Your Email:",font=("Helvetica", 11, "bold"), bg='#FCEDDA', fg='#EE4E34')
        email_label.place(x=70,y=120)
        self.email_entry = tk.Entry(self,width=40)
        self.email_entry.place(x=300,y=120)


        # Create name label and entry field
        name_label = tk.Label(self, text="Enter Your Full Name:",font=("Helvetica", 11, "bold"), bg='#FCEDDA', fg='#EE4E34')
        name_label.place(x=70,y=150)
        self.name_entry = tk.Entry(self,width=40)
        self.name_entry.place(x=300,y=150)


        # Create phone number label and entry field
        phone_label = tk.Label(self, text="Enter Your Phone Number:",font=("Helvetica", 11, "bold"), bg='#FCEDDA', fg='#EE4E34')
        phone_label.place(x=70,y=180)
        self.phone_entry = tk.Entry(self,width=40)
        self.phone_entry.place(x=300,y=180)



        # Create Aadhar card upload button
        aadhar_label = tk.Label(self, text="Please Upload Aadhar Card:",font=("Helvetica", 11, "bold"), bg='#FCEDDA', fg='#EE4E34')
        aadhar_label.place(x=70,y=210)
        self.aadhar_filename = tk.StringVar()
        self.aadhar_filename.set("No file chosen.")
        self.aadhar_label = tk.Label(self, textvariable=self.aadhar_filename,font=("Helvetica", 11, "bold"), bg='#FCEDDA', fg='#EE4E34',width=11)
        self.aadhar_label.place(x=300,y=210)
        self.aadhar_button = tk.Button(self, text="Choose File", command=self.choose_file)
        self.aadhar_button.config(width=16,height=1,bg="white",fg="black")
        self.aadhar_button.place(x=420,y=210)


        # create blood type field
        blood_type_label = tk.Label(self, text="Select your Blood Type:",font=("Helvetica", 11, "bold"), bg='#FCEDDA', fg='#EE4E34')
        blood_type_label.place(x=70,y=270)
        self.blood_type_var = tk.StringVar()
        self.blood_type_var.set("A+")  # default value
        blood_type_options = ["A+", "A-", "B+", "B-", "AB+", "AB-", "O+", "O-"]
        self.blood_type_dropdown = tk.OptionMenu(self, self.blood_type_var, *blood_type_options)
        self.blood_type_dropdown.config(width=34,bg="white",fg="black")
        self.blood_type_dropdown.place(x=300,y=270)



        # create location label and dropdown menu
        location_label = tk.Label(self, text="Select Your Location:",font=("Helvetica", 11, "bold"), bg='#FCEDDA', fg='#EE4E34')
        location_label.place(x=70,y=300)
        self.location_var = tk.StringVar()
        self.location_var.set("Kasarvadavli")  # default value
        location_options = ["Kasarvadavli", "Ovala", "Kavesar", "Waghbil", "Hiranandani Estate", "Manpada", "Pokharan Road", "Majiwada", "Naupada", "Dr. Ambedkar Road", "Vasant Vihar", "Louis Wadi", "Gokhale Road", "Ram Maruti Road", "Jambhli Naka","Tembhi Naka","Kalwa","Thane East","Teen Hath Naka"]
        self.location_dropdown = tk.OptionMenu(self, self.location_var, *location_options)
        self.location_dropdown.config(width=34,bg="white",fg="black")
        self.location_dropdown.place(x=300,y=300)


        separatormid = tk.Frame(self, height=3, width=620, bg='black')
        separatormid.place(x=10, y=340)   


        # Create back , signup and exit buttons
        back_button = tk.Button(self, text="<<", command=self.back, bd=2)
        back_button.config(width=2,height=1, bd=2,font=("Helvetica",12,"bold"),bg='black', fg='white')
        back_button.place(x=10,y=350)
        
        exit_button = tk.Button(self, text="Exit", command=exit, bd=2)
        exit_button.config(width=22,height=1, bd=2,font=("Helvetica",12,"bold"),bg='#EE4E34', fg='#FCEDDA')
        exit_button.place(x=70,y=350)
        
        signup_button = tk.Button(self, text="Signup", command=self.signup, bd=2)
        signup_button.config(width=23,height=1, bd=2,font=("Helvetica",12,"bold"),bg='darkgreen', fg='white')
        signup_button.place(x=310,y=350)
        
        
        separator2 = tk.Frame(self, height=3, width=620, bg='black')
        separator2.place(x=10, y=390)
        
    def back(self):
        Signup.destroy(self)
        app.deiconify()
        

    def choose_file(self):
        file_path = tk.filedialog.askopenfilename()
        if file_path:
            # read the contents of the file
            with open(file_path, 'rb') as f:
                file_data = f.read()
                self.file_data = file_data  # store file_data as an instance variable

            self.aadhar_filename.set(file_path)
            self.aadhar_label.config(textvariable=self.aadhar_filename)
            self.aadhar_button.config(state=tk.DISABLED)


    def signup(self):
        # Replace this with your signup code
        username = self.username_entry.get()
        name = self.name_entry.get()
        phone_number = self.phone_entry.get()

        password = self.password_entry.get()
        confirm_password = self.confirm_password_entry.get()
        email = self.email_entry.get()
        location = self.location_var.get()



        if password != confirm_password:
            tk.messagebox.showerror("Error", "Passwords do not match.")
            return

        #print(f"Signup with username {username}, password {password}, email {email}")
        

        # Prepare SQL query to insert a record into the users table
        query = "INSERT INTO users (username, name, phone_number, aadhar_card, email, password, location) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        values = (username, name, phone_number, self.file_data, email, password, location)

        # Execute the query and commit the changes to the database
        cursor.execute(query, values)
        db.commit()

        messagebox.showinfo("Sign up", "User sign up successful!")
        self.destroy()
        app.deiconify()

        # Close the database connection
        #db.close()


if __name__ == "__main__":
    app = LoginWindow()
    app.mainloop()
    """
    root=tk.Tk()
    temp = Signup(root)
    temp.mainloop()
"""























