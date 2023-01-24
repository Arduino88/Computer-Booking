from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from pathlib import Path
import json
import os

teachers = {
    "Mr. Jensen": {},
    "Mr. Beekers": {},
    "Mr. Kivari": {},
    "Ms. Wraight": {},
    "Ms. Best": {},
    "Mr. White": {},
    "Mr. Barraball": {},
}


teacherTuple = tuple(teachers.keys())
print(teacherTuple)
computers = ("Chromebook Cart 1", "Chromebook Cart 2", "Room 33 - Computer Lab")
days = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday")


#def initializeTeachers(): #FIX THIS LATER

def verifyMasterLists():
    folderPath = Path("Teachers\\")
    if not folderPath.exists():
        os.mkdir(folderPath)
    for staff in teacherTuple:
        pathString = "Teachers\\" + staff + ".txt"
        filePath = Path(pathString)
        if not filePath.exists():
            file = open(pathString, "w+")
            file.close()

verifyMasterLists()

root = Tk()
root.title("Computer Booking v1.0")

titleText = StringVar()

period1Monday = StringVar()
period2Monday = StringVar()
period3Monday = StringVar()
period4Monday = StringVar()

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

teacher = StringVar()
computer = StringVar()
day = StringVar()
period = StringVar()
periods = StringVar()
periods = 1 # THIS SHIT BrOKE

def bookComputer():
    try:
        teacherList = teachers[teacher.get()].keys()
        if not "Period1" in teacherList:
            bookingNumber = 1
        elif not "Period2" in teacherList:
            bookingNumber = 2
        else:
            bookingNumber = 3 #ERROR CHECK FOR MORE THAN 3 BOOKINGS

        teachers[teacher.get()]["Period" + str(bookingNumber)] = period.get()
        teachers[teacher.get()]["Computer" + str(bookingNumber)] = computer.get()
        teachers[teacher.get()]["Day" + str(bookingNumber)] = day.get()

        saveJSON()
    except KeyError:
        pass

def saveJSON():
    with open("masterlist.json", "w") as fp:
        json.dump(teachers, fp, indent=4, sort_keys=True)

def reset():
    print(teachers)



mainframe = ttk.Frame(root, padding=(3,3,12,12))

lblTitle = ttk.Label(mainframe, textvariable=computer)
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
lblPeriodS = ttk.Label(bookComputerLabelFrame, text="Period(s)")
spnPeriodS = ttk.Spinbox(bookComputerLabelFrame, from_=1, to_=4, increment=1, textvariable=periods) # FIX THIS TO CALCULATE REMAINING PERIODS IN DAY
btnBook = ttk.Button(bookComputerLabelFrame, text="Book", command=bookComputer)
btnReset = ttk.Button(bookComputerLabelFrame, text="Reset", command=reset)

lblStaffMember = ttk.Label(bookComboBoxFrame, text="Staff Member")
cbxStaffMember = ttk.Combobox(bookComboBoxFrame, textvariable=teacher)
cbxStaffMember["values"] = teacherTuple

lblBooking = ttk.Label(bookComboBoxFrame, text="Booking")
cbxBooking = ttk.Combobox(bookComboBoxFrame, textvariable=computer)
cbxBooking["values"] = computers

lblDay = ttk.Label(bookComboBoxFrame, text="Day")
cbxDay = ttk.Combobox(bookComboBoxFrame, textvariable=day)
cbxDay["values"] = days

lblPeriod = ttk.Label(bookPeriodFrame, text="Period")
rBtnPeriod1 = ttk.Radiobutton(bookPeriodFrame, text="1", variable=period, value=1)
rBtnPeriod2 = ttk.Radiobutton(bookPeriodFrame, text="2", variable=period, value=2)
rBtnPeriod3 = ttk.Radiobutton(bookPeriodFrame, text="3", variable=period, value=3)
rBtnPeriod4 = ttk.Radiobutton(bookPeriodFrame, text="4", variable=period, value=4)

mainframe.grid(column=0, row=0, sticky="nwes")

lblTitle.grid(column=0, row=0, sticky="nwes")
bookingBrowserLabelFrame.grid(column=0, row=1, sticky="nwes")
bookComputerLabelFrame.grid(column=0, row=2, sticky="nwes")

bookComboBoxFrame.grid(column=0, row=0, rowspan=3, sticky="nwes")
bookPeriodFrame.grid(column=1, row=0, rowspan=3, sticky="nwes")
lblPeriodS.grid(column=2, row=0, sticky="nwes")
spnPeriodS.grid(column=3, row=0, sticky="nwes")
btnBook.grid(column=2, row=1, columnspan=2, sticky="nwes")
btnReset.grid(column=2, row=2, columnspan=2, sticky="nwes")

lblStaffMember.grid(column=0, row=0, sticky="nwes")
cbxStaffMember.grid(column=0, row=1, sticky="nwes")

lblBooking.grid(column=0, row=2, sticky="nwes")
cbxBooking.grid(column=0, row=3, sticky="nwes")
lblDay.grid(column=0, row=4, sticky="nwes")
cbxDay.grid(column=0, row=5, sticky="nwes")

lblPeriod.grid(column=0, row=0, sticky="nwes")
rBtnPeriod1.grid(column=0, row=1, sticky="nwes")
rBtnPeriod2.grid(column=0, row=2, sticky="nwes")
rBtnPeriod3.grid(column=0, row=3, sticky="nwes")
rBtnPeriod4.grid(column=0, row=4, sticky="nwes")


#PERIOD LABELFRAME GRID FORMATTING
lblMonday.grid(column=0, row=0, sticky="nwes")
lblTuesday.grid(column=1, row=0, sticky="nwes")
lblWednesday.grid(column=2, row=0, sticky="nwes")
lblThursday.grid(column=3, row=0, sticky="nwes")
lblFriday.grid(column=4, row=0, sticky="nwes")

period1MondayLabelFrame.grid(column=0, row=1, sticky="nwes")
period1TuesdayLabelFrame.grid(column=1, row=1, sticky="nwes")
period1WednesdayLabelFrame.grid(column=2, row=1, sticky="nwes")
period1ThursdayLabelFrame.grid(column=3, row=1, sticky="nwes")
period1FridayLabelFrame.grid(column=4, row=1, sticky="nwes")

period2MondayLabelFrame.grid(column=0, row=2, sticky="nwes")
period2TuesdayLabelFrame.grid(column=1, row=2, sticky="nwes")
period2WednesdayLabelFrame.grid(column=2, row=2, sticky="nwes")
period2ThursdayLabelFrame.grid(column=3, row=2, sticky="nwes")
period2FridayLabelFrame.grid(column=4, row=2, sticky="nwes")

period3MondayLabelFrame.grid(column=0, row=3, sticky="nwes")
period3TuesdayLabelFrame.grid(column=1, row=3, sticky="nwes")
period3WednesdayLabelFrame.grid(column=2, row=3, sticky="nwes")
period3ThursdayLabelFrame.grid(column=3, row=3, sticky="nwes")
period3FridayLabelFrame.grid(column=4, row=3, sticky="nwes")

period4MondayLabelFrame.grid(column=0, row=4, sticky="nwes")
period4TuesdayLabelFrame.grid(column=1, row=4, sticky="nwes")
period4WednesdayLabelFrame.grid(column=2, row=4, sticky="nwes")
period4ThursdayLabelFrame.grid(column=3, row=4, sticky="nwes")
period4FridayLabelFrame.grid(column=4, row=4, sticky="nwes")

#PERIOD LABELFRAME LABEL GRID FORMATTING
lblPeriod1Monday.grid(column=0, row=0, sticky="nwes")
lblPeriod2Monday.grid(column=0, row=0, sticky="nwes")
lblPeriod3Monday.grid(column=0, row=0, sticky="nwes")
lblPeriod4Monday.grid(column=0, row=0, sticky="nwes")

lblPeriod1Tuesday.grid(column=0, row=0, sticky="nwes")
lblPeriod2Tuesday.grid(column=0, row=0, sticky="nwes")
lblPeriod3Tuesday.grid(column=0, row=0, sticky="nwes")
lblPeriod4Tuesday.grid(column=0, row=0, sticky="nwes")

lblPeriod1Wednesday.grid(column=0, row=0, sticky="nwes")
lblPeriod2Wednesday.grid(column=0, row=0, sticky="nwes")
lblPeriod3Wednesday.grid(column=0, row=0, sticky="nwes")
lblPeriod4Wednesday.grid(column=0, row=0, sticky="nwes")

lblPeriod1Thursday.grid(column=0, row=0, sticky="nwes")
lblPeriod2Thursday.grid(column=0, row=0, sticky="nwes")
lblPeriod3Thursday.grid(column=0, row=0, sticky="nwes")
lblPeriod4Thursday.grid(column=0, row=0, sticky="nwes")

lblPeriod1Friday.grid(column=0, row=0, sticky="nwes")
lblPeriod2Friday.grid(column=0, row=0, sticky="nwes")
lblPeriod3Friday.grid(column=0, row=0, sticky="nwes")
lblPeriod4Friday.grid(column=0, row=0, sticky="nwes")

root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)
mainframe.rowconfigure(1, weight=1)
mainframe.rowconfigure(2, weight=1)

bookingBrowserLabelFrame.columnconfigure(0, weight=1)
bookingBrowserLabelFrame.columnconfigure(1, weight=1)
bookingBrowserLabelFrame.columnconfigure(2, weight=1)
bookingBrowserLabelFrame.columnconfigure(3, weight=1)
bookingBrowserLabelFrame.columnconfigure(4, weight=1)

bookingBrowserLabelFrame.rowconfigure(0, weight=1)
bookingBrowserLabelFrame.rowconfigure(1, weight=1)
bookingBrowserLabelFrame.rowconfigure(2, weight=1)
bookingBrowserLabelFrame.rowconfigure(3, weight=1)
bookingBrowserLabelFrame.rowconfigure(4, weight=1)

bookComputerLabelFrame.columnconfigure(0, weight=1)
bookComputerLabelFrame.columnconfigure(1, weight=3)
bookComputerLabelFrame.columnconfigure(2, weight=1)
bookComputerLabelFrame.columnconfigure(3, weight=1)

bookComputerLabelFrame.rowconfigure(0, weight=1)
bookComputerLabelFrame.rowconfigure(1, weight=1)
bookComputerLabelFrame.rowconfigure(2, weight=1)

bookComboBoxFrame.columnconfigure(0, weight=1)

bookComboBoxFrame.rowconfigure(0, weight=1)
bookComboBoxFrame.rowconfigure(1, weight=1)
bookComboBoxFrame.rowconfigure(2, weight=1)
bookComboBoxFrame.rowconfigure(3, weight=1)
bookComboBoxFrame.rowconfigure(4, weight=1)
bookComboBoxFrame.rowconfigure(5, weight=1)

bookPeriodFrame.columnconfigure(0, weight=1)


bookPeriodFrame.rowconfigure(0, weight=1)
bookPeriodFrame.rowconfigure(1, weight=1)
bookPeriodFrame.rowconfigure(2, weight=1)
bookPeriodFrame.rowconfigure(3, weight=1)
bookPeriodFrame.rowconfigure(4, weight=1)



for child in mainframe.winfo_children():
    child.grid_configure(padx=5, pady=5)

root.mainloop()