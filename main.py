from tkinter import *
from tkinter import ttk
from tkinter import messagebox

root = Tk()
root.title("Computer Booking v1.0")

titleText = StringVar()

mainframe = ttk.Frame(root, padding=(3,3,12,12))

lblTitle = ttk.Label(mainframe, textvariable=titleText)
bookingBrowserLabelFrame = ttk.LabelFrame(mainframe, text="Browse Bookings")
bookComputerLabelFrame = ttk.LabelFrame(mainframe, text="Book Computer")

