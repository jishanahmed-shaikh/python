import mysql.connector
from tkinter import *
from PIL import Image, ImageTk
import io

# declare tk_image as a global variable
tk_image = None

def view_report(req_id):
    # create a MySQL connection
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="bloodbridge"
    )
    # create a Tkinter window and a canvas to display the image
    top = Toplevel()
    canvas = Canvas(top)
    canvas.pack(fill=BOTH, expand=YES)

    # define the maximum allowable size of the image
    MAX_WIDTH = 800
    MAX_HEIGHT = 1000

    # fetch the medical report data from the MySQL database
    mycursor = mydb.cursor()
    mycursor.execute("SELECT medical_report FROM donation_requests WHERE request_id = %s", (req_id,))
    result = mycursor.fetchone()

    # convert the binary data to an image using PIL
    if result:
        image_data = result[0]
        image = Image.open(io.BytesIO(image_data))

        # resize the image if it exceeds the maximum allowable size
        if image.width > MAX_WIDTH or image.height > MAX_HEIGHT:
            # calculate the new width and height while maintaining the aspect ratio
            aspect_ratio = image.width / image.height
            new_width = min(image.width, MAX_WIDTH)
            new_height = round(new_width / aspect_ratio)
            if new_height > MAX_HEIGHT:
                new_height = MAX_HEIGHT
                new_width = round(new_height * aspect_ratio)
            image = image.resize((new_width, new_height))

        tk_image = ImageTk.PhotoImage(image)

        # display the image on the canvas
        canvas.create_image(0, 0, anchor=NW, image=tk_image)
        canvas.config(width=image.width, height=image.height)
    else:
        print("No medical report found for request ID", req_id)

    top.iconify()
    top.deiconify()
    top.lift()

    # start the Tkinter event loop
    top.mainloop()

    # close the MySQL connection
    mydb.close()

def view_report1(req_id):
    # create a MySQL connection
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="bloodbridge"
    )
    # create a Tkinter window and a canvas to display the image
    top = Toplevel()
    canvas = Canvas(top)
    canvas.pack(fill=BOTH, expand=YES)

    # define the maximum allowable size of the image
    MAX_WIDTH = 800
    MAX_HEIGHT = 1000

    # fetch the medical report data from the MySQL database
    mycursor = mydb.cursor()
    mycursor.execute("SELECT request_report FROM blood_requests WHERE request_id = %s", (req_id,))
    result = mycursor.fetchone()

    # convert the binary data to an image using PIL
    if result:
        image_data = result[0]
        image = Image.open(io.BytesIO(image_data))

        # resize the image if it exceeds the maximum allowable size
        if image.width > MAX_WIDTH or image.height > MAX_HEIGHT:
            # calculate the new width and height while maintaining the aspect ratio
            aspect_ratio = image.width / image.height
            new_width = min(image.width, MAX_WIDTH)
            new_height = round(new_width / aspect_ratio)
            if new_height > MAX_HEIGHT:
                new_height = MAX_HEIGHT
                new_width = round(new_height * aspect_ratio)
            image = image.resize((new_width, new_height))

        tk_image = ImageTk.PhotoImage(image)

        # display the image on the canvas
        canvas.create_image(0, 0, anchor=NW, image=tk_image)
        canvas.config(width=image.width, height=image.height)
    else:
        print("No medical report found for request ID", req_id)

    top.iconify()
    top.deiconify()
    top.lift()

    # start the Tkinter event loop
    top.mainloop()

    # close the MySQL connection
    mydb.close()

view_report1(3)