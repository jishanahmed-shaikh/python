import mysql.connector
import pandas as pd

# create a connection to the MySQL server
cnx = mysql.connector.connect(user='root', password='root',
                              host='localhost', database='')

# create a cursor object to execute queries
cursor = cnx.cursor()

#Drop database
query="drop database if exists bloodbridge"
cursor.execute(query)
query="create database bloodbridge"
cursor.execute(query)
query="use bloodbridge"
cursor.execute(query)

# create the users table
cursor.execute("""
    CREATE TABLE users (
        id INT PRIMARY KEY AUTO_INCREMENT,
        username VARCHAR(255) NOT NULL,
        name VARCHAR(255) NOT NULL,
        phone_number VARCHAR(20) NOT NULL,
        aadhar_card LONGBLOB NOT NULL,
        email VARCHAR(255) NOT NULL,
        password VARCHAR(255) NOT NULL,
        location VARCHAR(255) NOT NULL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
""")

#create blood_banks table
cursor.execute("""
    CREATE TABLE blood_banks (
        Bid INT PRIMARY KEY,
        Name VARCHAR(150) NOT NULL,
        Landmark VARCHAR(80) NOT NULL,
        Contact VARCHAR(255) NOT NULL,
        CURRENT_BLOOD_TYPES VARCHAR(50) NOT NULL,
        Current_units_Aplus INT NOT NULL,
        Current_units_Aminus INT NOT NULL,
        Current_units_Bplus INT NOT NULL,
        Current_units_Bminus INT NOT NULL,
        Current_units_ABplus INT NOT NULL,
        Current_units_ABminus INT NOT NULL,
        Current_units_Oplus INT NOT NULL,
        Current_units_Ominus INT NOT NULL,
        password varchar(255)
    )        
""")

#create blood_requests table
#in status 0 means pending 1 means approved
cursor.execute("""
    CREATE TABLE blood_requests(
        request_id int primary key AUTO_INCREMENT,
        username VARCHAR(80),
        request_report LONGBLOB,
        bloodtype VARCHAR(10),
        units_required INT,
        status int default 0
    )
""")

#create donation_requests table
cursor.execute("""
    CREATE TABLE donation_requests(
        request_id int primary key AUTO_INCREMENT,
        Bid INT,
        username VARCHAR(80),
        medical_report LONGBLOB NOT NULL,
        appointment DATE,
        timing varchar(10),
        status int default 0,
        units int null
    )
""")

#Insert blood bank data in the table
df = pd.read_excel('blood_banks.xlsx', usecols=['B-ID', 'NAME', 'LANDMARK', 'CONTACT', 'CURRENT BLOOD TYPES', 'Current_units_Aplus', 'Current_units_Aminus', 'Current_units_Bplus', 'Current_units_Bminus', 'Current_units_ABplus', 'Current_units_ABminus', 'Current_units_Oplus', 'Current_units_Ominus','Password'])
sql = "INSERT INTO blood_banks (Bid,  Name,  Landmark,  Contact,  CURRENT_BLOOD_TYPES, Current_units_Aplus, Current_units_Aminus, Current_units_Bplus, Current_units_Bminus, Current_units_ABplus, Current_units_ABminus, Current_units_Oplus, Current_units_Ominus,password) VALUES (%s,%s,  %s,  %s, %s,  %s,  %s, %s, %s, %s, %s, %s, %s, %s)"
for i, row in df.iterrows():
    val = (row['B-ID'], row['NAME'], row['LANDMARK'], row['CONTACT'], row['CURRENT BLOOD TYPES'], row['Current_units_Aplus'],row['Current_units_Aminus'],row['Current_units_Bplus'],row['Current_units_Bminus'],row['Current_units_ABplus'],row['Current_units_ABminus'],row['Current_units_Oplus'],row['Current_units_Ominus'],row['Password'],)
    cursor.execute(sql, val)

# commit the changes to the database and close the cursor and connection
cnx.commit()
cursor.close()
cnx.close()

"""

"""
'''
# create the donors table
cursor.execute("""
    CREATE TABLE donors (
        id INT PRIMARY KEY ,
        user_id INT NOT NULL,
        name VARCHAR(255) NOT NULL,
        phone_number VARCHAR(20) NOT NULL,
        email VARCHAR(255) NOT NULL,
        blood_group VARCHAR(5) NOT NULL,
        aadhar_card VARCHAR(15) NOT NULL,
        image LONGBLOB NOT NULL,
        location VARCHAR(255) NOT NULL,
        last_donated_at TIMESTAMP,
        is_available BOOLEAN NOT NULL,
        FOREIGN KEY (user_id) REFERENCES users (id)
    )
""")

# create the receivers table
cursor.execute("""
    CREATE TABLE receivers (
        id INT PRIMARY KEY AUTO_INCREMENT,
        user_id INT NOT NULL,
        name VARCHAR(255) NOT NULL,
        phone_number VARCHAR(20) NOT NULL,
        email VARCHAR(255) NOT NULL,
        blood_group VARCHAR(5) NOT NULL,
        aadhar_card VARCHAR(15) NOT NULL,
        image LONGBLOB NOT NULL,
        location VARCHAR(255) NOT NULL,
        required_units INT NOT NULL,
        is_urgent BOOLEAN NOT NULL,
        status VARCHAR(20) NOT NULL,
        requested_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (user_id) REFERENCES users (id)
    )
""")

# create the donations table
cursor.execute("""
    CREATE TABLE donations (
        id INT PRIMARY KEY AUTO_INCREMENT,
        donor_name VARCHAR(255) NOT NULL,
        receiver_name VARCHAR(255) NOT NULL,
        units_donated INT NOT NULL,
        donated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (donor_name) REFERENCES users (username),
        FOREIGN KEY (receiver_name) REFERENCES users (username)
    )
""")

# create the admin_users table
cursor.execute("""
    CREATE TABLE admin_users (
        id INT PRIMARY KEY AUTO_INCREMENT,
        username VARCHAR(255) NOT NULL,
        email VARCHAR(255) NOT NULL,
        password VARCHAR(255) NOT NULL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
""")

'''