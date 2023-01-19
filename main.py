from tkinter import *
from tkinter import ttk
from tkinter import messagebox

root = Tk()
root.title("Computer Booking v1.0")

titleText = StringVar()

period1Monday = StringVar()
period2Monday = StringVar()
period3Monday = StringVar()
period4Monday = StringVar()

period1Monday = "cock"

period1Tuesday = StringVar()
period2Tuesday = StringVar()
period3Tuesday = StringVar()
period4Tuesday = StringVar()

period1Wednesday = StringVar()
period2Wednesday = StringVar()
period3Wednesday = StringVar()
period4Wednesday = StringVar()

period1Thursday = StringVar()
period2Thursday = StringVar()
period3Thursday = StringVar()
period4Thursday = StringVar()

period1Friday = StringVar()
period2Friday = StringVar()
period3Friday = StringVar()
period4Friday = StringVar()


mainframe = ttk.Frame(root, padding=(3,3,12,12))

lblTitle = ttk.Label(mainframe, textvariable=titleText)
bookingBrowserLabelFrame = ttk.LabelFrame(mainframe, text="Browse Bookings")
bookComputerLabelFrame = ttk.LabelFrame(mainframe, text="Book Computer")

#Computer Browser
lblMonday = ttk.Label(bookingBrowserLabelFrame, text="Monday")
lblTuesday = ttk.Label(bookingBrowserLabelFrame, text="Tuesday")
lblWednesday = ttk.Label(bookingBrowserLabelFrame, text="Wednesday")
lblThursday = ttk.Label(bookingBrowserLabelFrame, text="Thursday")
lblFriday = ttk.Label(bookingBrowserLabelFrame, text="Friday")

period1MondayLabelFrame = ttk.LabelFrame(bookingBrowserLabelFrame, text="Period 1")
period2MondayLabelFrame = ttk.LabelFrame(bookingBrowserLabelFrame, text="Period 2")
period3MondayLabelFrame = ttk.LabelFrame(bookingBrowserLabelFrame, text="Period 3")
period4MondayLabelFrame = ttk.LabelFrame(bookingBrowserLabelFrame, text="Period 4")

period1TuesdayLabelFrame = ttk.LabelFrame(bookingBrowserLabelFrame, text="Period 1")
period2TuesdayLabelFrame = ttk.LabelFrame(bookingBrowserLabelFrame, text="Period 2")
period3TuesdayLabelFrame = ttk.LabelFrame(bookingBrowserLabelFrame, text="Period 3")
period4TuesdayLabelFrame = ttk.LabelFrame(bookingBrowserLabelFrame, text="Period 4")

period1WednesdayLabelFrame = ttk.LabelFrame(bookingBrowserLabelFrame, text="Period 1")
period2WednesdayLabelFrame = ttk.LabelFrame(bookingBrowserLabelFrame, text="Period 2")
period3WednesdayLabelFrame = ttk.LabelFrame(bookingBrowserLabelFrame, text="Period 3")
period4WednesdayLabelFrame = ttk.LabelFrame(bookingBrowserLabelFrame, text="Period 4")

period1ThursdayLabelFrame = ttk.LabelFrame(bookingBrowserLabelFrame, text="Period 1")
period2ThursdayLabelFrame = ttk.LabelFrame(bookingBrowserLabelFrame, text="Period 2")
period3ThursdayLabelFrame = ttk.LabelFrame(bookingBrowserLabelFrame, text="Period 3")
period4ThursdayLabelFrame = ttk.LabelFrame(bookingBrowserLabelFrame, text="Period 4")

period1FridayLabelFrame = ttk.LabelFrame(bookingBrowserLabelFrame, text="Period 1")
period2FridayLabelFrame = ttk.LabelFrame(bookingBrowserLabelFrame, text="Period 2")
period3FridayLabelFrame = ttk.LabelFrame(bookingBrowserLabelFrame, text="Period 3")
period4FridayLabelFrame = ttk.LabelFrame(bookingBrowserLabelFrame, text="Period 4")

lblPeriod1Monday = ttk.Label(period1MondayLabelFrame, textvariable=period1Monday)
lblPeriod2Monday = ttk.Label(period2MondayLabelFrame, textvariable=period2Monday)
lblPeriod3Monday = ttk.Label(period3MondayLabelFrame, textvariable=period3Monday)
lblPeriod4Monday = ttk.Label(period4MondayLabelFrame, textvariable=period4Monday)

lblPeriod1Tuesday = ttk.Label(period1TuesdayLabelFrame, textvariable=period1Tuesday)
lblPeriod2Tuesday = ttk.Label(period2TuesdayLabelFrame, textvariable=period2Tuesday)
lblPeriod3Tuesday = ttk.Label(period3TuesdayLabelFrame, textvariable=period3Tuesday)
lblPeriod4Tuesday = ttk.Label(period4TuesdayLabelFrame, textvariable=period4Tuesday)

lblPeriod1Wednesday = ttk.Label(period1WednesdayLabelFrame, textvariable=period1Wednesday)
lblPeriod2Wednesday = ttk.Label(period2WednesdayLabelFrame, textvariable=period2Wednesday)
lblPeriod3Wednesday = ttk.Label(period3WednesdayLabelFrame, textvariable=period3Wednesday)
lblPeriod4Wednesday = ttk.Label(period4WednesdayLabelFrame, textvariable=period4Wednesday)

lblPeriod1Thursday = ttk.Label(period1ThursdayLabelFrame, textvariable=period1Thursday)
lblPeriod2Thursday = ttk.Label(period2ThursdayLabelFrame, textvariable=period2Thursday)
lblPeriod3Thursday = ttk.Label(period3ThursdayLabelFrame, textvariable=period3Thursday)
lblPeriod4Thursday = ttk.Label(period4ThursdayLabelFrame, textvariable=period4Thursday)

lblPeriod1Friday = ttk.Label(period1FridayLabelFrame, textvariable=period1Friday)
lblPeriod2Friday = ttk.Label(period2FridayLabelFrame, textvariable=period2Friday)
lblPeriod3Friday = ttk.Label(period3FridayLabelFrame, textvariable=period3Friday)
lblPeriod4Friday = ttk.Label(period4FridayLabelFrame, textvariable=period4Friday)

bookComboBoxFrame = ttk.Frame(bookComputerLabelFrame)
bookPeriodFrame = ttk.Frame(bookComputerLabelFrame)
lblPeriodS = ttk.Label(bookComputerLabelFrame)
spnPeriodS = ttk.Spinbox(bookComputerLabelFrame)
btnBack = ttk.Button(bookComputerLabelFrame)
btnReset = ttk.Button(bookComputerLabelFrame)

lblStaffMember = ttk.Label(bookComboBoxFrame)
cbxStaffMember = ttk.Combobox(bookComboBoxFrame)

lblBooking = ttk.Label(bookComboBoxFrame)
cbxBooking = ttk.Combobox(bookComboBoxFrame)

lblDay = ttk.Label(bookComboBoxFrame)
cbxDay = ttk.Combobox(bookComboBoxFrame)

lblPeriod = ttk.Label(bookPeriodFrame)
rBtnPeriod1 = ttk.Radiobutton(bookPeriodFrame, text="1")
rBtnPeriod2 = ttk.Radiobutton(bookPeriodFrame, text="1")
rBtnPeriod3 = ttk.Radiobutton(bookPeriodFrame, text="1")
rBtnPeriod4 = ttk.Radiobutton(bookPeriodFrame, text="1")

mainframe.grid(column=0, row=0, sticky=(N, W, E, S))

#PERIOD LABELFRAME GRID FORMATTING
lblMonday.grid(column=0, row=0, sticky=(N, E, S, W))
lblTuesday.grid(column=1, row=0, sticky=(N, E, S, W))
lblWednesday.grid(column=2, row=0, sticky=(N, E, S, W))
lblThursday.grid(column=3, row=0, sticky=(N, E, S, W))
lblFriday.grid(column=4, row=0, sticky=(N, E, S, W))

period1MondayLabelFrame.grid(column=0, row=1)
period1TuesdayLabelFrame.grid(column=1, row=1)
period1WednesdayLabelFrame.grid(column=2, row=1)
period1ThursdayLabelFrame.grid(column=3, row=1)
period1FridayLabelFrame.grid(column=4, row=1)

period2MondayLabelFrame.grid(column=0, row=2)
period2TuesdayLabelFrame.grid(column=1, row=2)
period2WednesdayLabelFrame.grid(column=2, row=2)
period2ThursdayLabelFrame.grid(column=3, row=2)
period2FridayLabelFrame.grid(column=4, row=2)

period3MondayLabelFrame.grid(column=0, row=3)
period3TuesdayLabelFrame.grid(column=1, row=3)
period3WednesdayLabelFrame.grid(column=2, row=3)
period3ThursdayLabelFrame.grid(column=3, row=3)
period3FridayLabelFrame.grid(column=4, row=3)

period4MondayLabelFrame.grid(column=0, row=4)
period4TuesdayLabelFrame.grid(column=1, row=4)
period4WednesdayLabelFrame.grid(column=2, row=4)
period4ThursdayLabelFrame.grid(column=3, row=4)
period4FridayLabelFrame.grid(column=4, row=4)

#PERIOD LABELFRAME LABEL GRID FORMATTING
lblPeriod1Monday.grid(column=0, row=0, sticky=(N, E, S, W))
lblPeriod2Monday.grid(column=0, row=0, sticky=(N, E, S, W))
lblPeriod3Monday.grid(column=0, row=0, sticky=(N, E, S, W))
lblPeriod4Monday.grid(column=0, row=0, sticky=(N, E, S, W))

lblPeriod1Tuesday.grid(column=0, row=0, sticky=(N, E, S, W))
lblPeriod2Tuesday.grid(column=0, row=0, sticky=(N, E, S, W))
lblPeriod3Tuesday.grid(column=0, row=0, sticky=(N, E, S, W))
lblPeriod4Tuesday.grid(column=0, row=0, sticky=(N, E, S, W))

lblPeriod1Wednesday.grid(column=0, row=0, sticky=(N, E, S, W))
lblPeriod2Wednesday.grid(column=0, row=0, sticky=(N, E, S, W))
lblPeriod3Wednesday.grid(column=0, row=0, sticky=(N, E, S, W))
lblPeriod4Wednesday.grid(column=0, row=0, sticky=(N, E, S, W))

lblPeriod1Thursday.grid(column=0, row=0, sticky=(N, E, S, W))
lblPeriod2Thursday.grid(column=0, row=0, sticky=(N, E, S, W))
lblPeriod3Thursday.grid(column=0, row=0, sticky=(N, E, S, W))
lblPeriod4Thursday.grid(column=0, row=0, sticky=(N, E, S, W))

lblPeriod1Friday.grid(column=0, row=0, sticky=(N, E, S, W))
lblPeriod2Friday.grid(column=0, row=0, sticky=(N, E, S, W))
lblPeriod3Friday.grid(column=0, row=0, sticky=(N, E, S, W))
lblPeriod4Friday.grid(column=0, row=0, sticky=(N, E, S, W))

for child in mainframe.winfo_children():
    child.grid_configure(padx=5, pady=5)

root.mainloop()