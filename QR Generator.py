import qrcode
from tkinter import *
from tkinter import messagebox

# Creating the window
wn = Tk()
wn.title('PACE ITS QRCode generatorS')
wn.geometry('700x700')
wn.config(bg='green')

# Function to generate the QR code and save it
def generateCode():
    # Get the size input from the user
    size_input = size.get()

    # Check if the size input is empty
    if not size_input:
        # If empty, set a default version
        version = 1
    else:
        try:
            # Convert the size input to an integer
            version = int(size_input)
        except ValueError:
            # Handle invalid input by setting a default version
            version = 1

    # Creating a QRCode object with the integer version
    qr = qrcode.QRCode(version=version, box_size=10, border=5)
    qr.add_data(text.get())  # Adding the data to be encoded to the QRCode object
    qr.make(fit=True)  # Making the entire QR Code space utilized
    img = qr.make_image()  # Generating the QR Code
    fileDirec = loc.get() + '\\' + name.get()  # Getting the directory where the file has to be saved
    img.save(f'{fileDirec}.png')  # Saving the QR Code
    # Showing the pop-up message on saving the file
    messagebox.showinfo("PACE ITS QR Code Generator", "QR Code is saved successfully!")

# Label for the window
headingFrame = Frame(wn, bg="azure", bd=5)
headingFrame.place(relx=0.15, rely=0.05, relwidth=0.7, relheight=0.1)
headingLabel = Label(headingFrame, text="Generate QRCode with PACE ITS", bg='azure', font=('Times', 20, 'bold'))
headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)

# Taking the input of the text or URL to get QR code
Frame1 = Frame(wn, bg="green")
Frame1.place(relx=0.1, rely=0.15, relwidth=0.7, relheight=0.3)

lable1 = Label(Frame1, text="Enter the text/URL: ", bg="green", fg='azure', font=('Cursive', 13, 'bold'))
lable1.place(relx=0.05, rely=0.2, relheight=0.08)

text = Entry(Frame1, font=('Century 12'))
text.place(relx=0.05, rely=0.4, relwidth=1, relheight=0.2)

# Getting input of the location to save QR Code
Frame2 = Frame(wn, bg="green")
Frame2.place(relx=0.1, rely=0.35, relwidth=0.7, relheight=0.3)

lable2 = Label(Frame2, text="Enter the location to save the QR Code: ", bg="green", fg='azure',
               font=('Cursive', 13, 'bold'))
lable2.place(relx=0.05, rely=0.2, relheight=0.08)

loc = Entry(Frame2, font=('Century 12'))
loc.place(relx=0.05, rely=0.4, relwidth=1, relheight=0.2)

# Getting input of the QR Code image name
Frame3 = Frame(wn, bg="green")
Frame3.place(relx=0.1, rely=0.55, relwidth=0.7, relheight=0.3)

lable3 = Label(Frame3, text="Enter the name of the QR Code: ", bg="green", fg='azure', font=('Cursive', 13, 'bold'))
lable3.place(relx=0.05, rely=0.2, relheight=0.08)

name = Entry(Frame3, font=('Century 12'))
name.place(relx=0.05, rely=0.4, relwidth=1, relheight=0.2)

# Getting the input of the size of the QR Code
Frame4 = Frame(wn, bg="green")
Frame4.place(relx=0.1, rely=0.75, relwidth=0.7, relheight=0.2)

lable4 = Label(Frame4, text="Enter the size from 1 to 40 to give same height and width of QR: ", bg="green", fg='azure',
               font=('Cursive', 13, 'bold'))
lable4.place(relx=0.05, rely=0.2, relheight=0.08)

size = Entry(Frame4, font=('Century 12'))
size.place(relx=0.05, rely=0.4, relwidth=0.5, relheight=0.2)

# Button to generate and save the QR Code
button = Button(wn, text='Generate Code', font=('Cursive', 15, 'normal'), command=generateCode)
button.place(relx=0.35, rely=0.9, relwidth=0.25, relheight=0.05)

# Runs the window until it is closed manually
wn.mainloop()
