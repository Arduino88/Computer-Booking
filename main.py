#---------------------------------------------
#Name of Repository: Arduino_88/Computer-Booking
#Name of Programmers: Simon Siena, Peyton Freeburn, Emily Skinner, Cody Fitzgerald, Westley Lundberg
#Language Used: Python 3.11
#Date Project Started: January 12, 2023
#Date of Most Recent Commit: January 24, 2023
#ADD DESCRIPTION HERE
#
#Data Dictionary:
#   Functions:
#       assignBookingInformation() --> Pushes tkinter object variables into the global teachers dictionary
#       bookComputer() --> Book button function; calculates the "Booking#": key in the global teachers dictionary; calls saveJSON(); calls updateBookingBrowser()
#       loadJSON() --> Loads the global teachers dictionary from masterlist.json
#       reset() --> Runs reset-masterlist.py; calls loadJSON() and then calls updateBookingBrowser()
#       saveJSON() --> Dumps the global teachers dictionary to masterlist.json with an indent of 4
#       updateBookingBrowser() --> Clears all the booking browser and then runs through each teacher key in the global teachers ditionary, adding them to the corresponding tkinter stringVar objects
#   
#   Variables:
#       



from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import json
import sv_ttk
import os

#Function Definition - loadJSON() <-- Early in code because global teachers variable is initialized
def loadJSON():
    with open("masterlist.json") as fp:
        global teachers
        teachers = json.load(fp)

loadJSON() #ADD MULTIPLE PERIODS - BRO IDFK WHAT THIS MEANS

#Initiate Teacher Tuple
teacherTuple = tuple(teachers.keys())
print(teacherTuple)

#Initiate Combobox Option Tuples
computers = ("Chromebook Cart 1", "Chromebook Cart 2", "Room 33 - Computer Lab")
days = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday")

#Initiate Tkinter Root
root = Tk()
root.title("Computer Booking v1.7")

#Tkinter Variable Initialization
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

#Set Default Tkinter Object Values
teacher = StringVar(value="Mr. Barraball") #Combobox
computer = StringVar(value="Chromebook Cart 1") #Combobox
day = StringVar(value="Monday") #Combobox
period = IntVar() #Radio Button
periods = StringVar(value=1) #Spinbox

#Function Definition
def assignBookingInformation(bookingNumber):
        teachers[teacher.get()]["Period" + str(bookingNumber)] = period.get()
        teachers[teacher.get()]["Computer" + str(bookingNumber)] = computer.get()
        teachers[teacher.get()]["Day" + str(bookingNumber)] = day.get()
        teachers[teacher.get()]["Booking#"] = bookingNumber

def bookComputer():
    try:
        teacherList = teachers[teacher.get()].keys()
        stringVariable = "period" + str(period.get()) + day.get()
        if eval(stringVariable + ".get() == \"\""):
            if not "Period1" in teacherList:
                bookingNumber = 1
                assignBookingInformation(bookingNumber=bookingNumber)
            elif not "Period2" in teacherList:
                bookingNumber = 2
                assignBookingInformation(bookingNumber=bookingNumber)
            elif not "Period3" in teacherList:
                bookingNumber = 3
                assignBookingInformation(bookingNumber=bookingNumber)
            else:
                messagebox.showerror(title="Attempted Overbook", message=(teacher.get() + " already has 3 bookings this week"), icon="error", detail=("Please wait until next week to book more lockers for " + teacher.get()))
        else:
            messagebox.showerror(title="Attempted Overwrite", message=(str(eval(stringVariable + ".get()")) + " already has Period " + str(period.get()) + " booked on " + day.get()), icon="error", detail=("Please book a different period :)"))
        saveJSON()
        updateBookingBrowser()
    except KeyError:
        pass

def updateBookingBrowser():
    period1Monday.set(value="")
    period2Monday.set(value="")
    period3Monday.set(value="")
    period4Monday.set(value="")

    period1Tuesday.set(value="")
    period2Tuesday.set(value="")
    period3Tuesday.set(value="")
    period4Tuesday.set(value="")

    period1Wednesday.set(value="")
    period2Wednesday.set(value="")
    period3Wednesday.set(value="")
    period4Wednesday.set(value="")

    period1Thursday.set(value="")
    period2Thursday.set(value="")
    period3Thursday.set(value="")
    period4Thursday.set(value="")

    period1Friday.set(value="")
    period2Friday.set(value="")
    period3Friday.set(value="")
    period4Friday.set(value="")

    for item in teachers.keys():
        if "Booking#" in teachers[item]:
            tempVar = teachers[item]["Booking#"]
            while tempVar > 0:
                stringVariable = "period" + str(teachers[item]["Period" + str(tempVar)]) + teachers[item]["Day" + str(tempVar)]
                if str(teachers[item]["Computer" + str(tempVar)]) == computer.get():
                    eval(stringVariable + ".set(\"" + item + "\")")
                tempVar = tempVar - 1
    root.after(100, updateBookingBrowser)
updateBookingBrowser()

def saveJSON():
    with open("masterlist.json", "w") as fp:
        json.dump(teachers, fp, indent=4, sort_keys=True)

def reset():
    os.system("reset-masterlist.py")
    loadJSON()
    updateBookingBrowser()

#Initialize Tkinter Mainframe
mainframe = ttk.Frame(root, padding=(3,3,12,12))

#Initialize Tkinter mainframe Objects
lblTitle = ttk.Label(mainframe, textvariable=computer)
bookingBrowserLabelFrame = ttk.LabelFrame(mainframe, text="Browse Bookings")
bookComputerLabelFrame = ttk.LabelFrame(mainframe, text="Book Computer")

#Initialize Tkinter bookingBrowserLabelFrame Objects
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

#Initialize Tkinter Teacher Labels
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

#Initialize Tkinter bookComputerLabelFrame Objects
bookComboBoxFrame = ttk.Frame(bookComputerLabelFrame)
bookPeriodFrame = ttk.Frame(bookComputerLabelFrame)
lblPeriodS = ttk.Label(bookComputerLabelFrame, text="Period(s)")
spnPeriodS = ttk.Spinbox(bookComputerLabelFrame, from_=1, to_=4, increment=1, textvariable=periods) # FIX THIS TO CALCULATE REMAINING PERIODS IN DAY
btnBook = ttk.Button(bookComputerLabelFrame, text="Book", command=bookComputer)
btnReset = ttk.Button(bookComputerLabelFrame, text="Reset", command=reset)

#Initialize Tkinter bookComboBoxFrame Objects
lblStaffMember = ttk.Label(bookComboBoxFrame, text="Staff Member")
cbxStaffMember = ttk.Combobox(bookComboBoxFrame, textvariable=teacher)
cbxStaffMember["values"] = teacherTuple

lblBooking = ttk.Label(bookComboBoxFrame, text="Booking")
cbxBooking = ttk.Combobox(bookComboBoxFrame, textvariable=computer)
cbxBooking["values"] = computers

lblDay = ttk.Label(bookComboBoxFrame, text="Day")
cbxDay = ttk.Combobox(bookComboBoxFrame, textvariable=day)
cbxDay["values"] = days

#Initialize Tkinter bookPeriodFrame Objects
lblPeriod = ttk.Label(bookPeriodFrame, text="Period")
rBtnPeriod1 = ttk.Radiobutton(bookPeriodFrame, text="1", variable=period, value=1)
rBtnPeriod2 = ttk.Radiobutton(bookPeriodFrame, text="2", variable=period, value=2)
rBtnPeriod3 = ttk.Radiobutton(bookPeriodFrame, text="3", variable=period, value=3)
rBtnPeriod4 = ttk.Radiobutton(bookPeriodFrame, text="4", variable=period, value=4)

#-----GRID FORMATTING-----
#mainframe Tkinter Grid Formatting
mainframe.grid(column=0, row=0, sticky="nwes")

#mainframe Tkinter Objects Grid Formatting
lblTitle.grid(column=0, row=0, sticky="nwes")
bookingBrowserLabelFrame.grid(column=0, row=1, sticky="nwes")
bookComputerLabelFrame.grid(column=0, row=2, sticky="nwes")

#bookComputerLabelFrame Tkinter Objects Grid Formatting
bookComboBoxFrame.grid(column=0, row=0, rowspan=3, sticky="nwes")
bookPeriodFrame.grid(column=1, row=0, rowspan=3, sticky="nwes")
lblPeriodS.grid(column=2, row=0, sticky="nwes")
spnPeriodS.grid(column=3, row=0, sticky="nwes")
btnBook.grid(column=2, row=1, columnspan=2, sticky="nwes")
btnReset.grid(column=2, row=2, columnspan=2, sticky="nwes")

#bookComboBoxFrame Tkinter Objects Grid Formatting
lblStaffMember.grid(column=0, row=0, sticky="nwes")
cbxStaffMember.grid(column=0, row=1, sticky="nwes")

lblBooking.grid(column=0, row=2, sticky="nwes")
cbxBooking.grid(column=0, row=3, sticky="nwes")

lblDay.grid(column=0, row=4, sticky="nwes")
cbxDay.grid(column=0, row=5, sticky="nwes")

#bookPeriodFrame Tkinter Objects Grid Formatting
lblPeriod.grid(column=0, row=0, sticky="nwes")
rBtnPeriod1.grid(column=0, row=1, sticky="nwes")
rBtnPeriod2.grid(column=0, row=2, sticky="nwes")
rBtnPeriod3.grid(column=0, row=3, sticky="nwes")
rBtnPeriod4.grid(column=0, row=4, sticky="nwes")


#bookingBrowserLabelFrame Tkinter Objects Grid Formatting
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

#bookingBrowserLabelFrame Sub-Labelframe Tkinter Object Grid Formatting
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

#-----COLUMN & ROW CONFIGURATION-----
#root Column Configuration
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

#mainframe Column Configuration
mainframe.columnconfigure(0, weight=1)

#bookingBroweseLabelFrame Row Configuration
mainframe.rowconfigure(0, weight=1)
mainframe.rowconfigure(1, weight=1)
mainframe.rowconfigure(2, weight=1)

#bookingBroweseLabelFrame Column Configuration
bookingBrowserLabelFrame.columnconfigure(0, weight=1)
bookingBrowserLabelFrame.columnconfigure(1, weight=1)
bookingBrowserLabelFrame.columnconfigure(2, weight=1)
bookingBrowserLabelFrame.columnconfigure(3, weight=1)
bookingBrowserLabelFrame.columnconfigure(4, weight=1)

#bookingBrowserLabelFrame Row Configuration
bookingBrowserLabelFrame.rowconfigure(0, weight=1)
bookingBrowserLabelFrame.rowconfigure(1, weight=1)
bookingBrowserLabelFrame.rowconfigure(2, weight=1)
bookingBrowserLabelFrame.rowconfigure(3, weight=1)
bookingBrowserLabelFrame.rowconfigure(4, weight=1)

#bookComputerLabelFrame Column Configuration
bookComputerLabelFrame.columnconfigure(0, weight=1)
bookComputerLabelFrame.columnconfigure(1, weight=3)
bookComputerLabelFrame.columnconfigure(2, weight=1)
bookComputerLabelFrame.columnconfigure(3, weight=1)

#bookComputerLabelFrame Row Configuration
bookComputerLabelFrame.rowconfigure(0, weight=1)
bookComputerLabelFrame.rowconfigure(1, weight=1)
bookComputerLabelFrame.rowconfigure(2, weight=1)

#bookComboBoxFrame Column Configuraion
bookComboBoxFrame.columnconfigure(0, weight=1)

#bookComboBoxFrame Row Configuration
bookComboBoxFrame.rowconfigure(0, weight=1)
bookComboBoxFrame.rowconfigure(1, weight=1)
bookComboBoxFrame.rowconfigure(2, weight=1)
bookComboBoxFrame.rowconfigure(3, weight=1)
bookComboBoxFrame.rowconfigure(4, weight=1)
bookComboBoxFrame.rowconfigure(5, weight=1)

#bookPeriodFrame Column Configuration
bookPeriodFrame.columnconfigure(0, weight=1)

#bookPeriodFrame Row Configuration
bookPeriodFrame.rowconfigure(0, weight=1)
bookPeriodFrame.rowconfigure(1, weight=1)
bookPeriodFrame.rowconfigure(2, weight=1)
bookPeriodFrame.rowconfigure(3, weight=1)
bookPeriodFrame.rowconfigure(4, weight=1)

#Formatting Loops
for child in bookComputerLabelFrame.winfo_children():
    child.grid_configure(padx=5, pady=5)

for child in bookingBrowserLabelFrame.winfo_children():
    child.grid_configure(padx=5, pady=5, ipadx=5, ipady=5)

for child in mainframe.winfo_children():
    child.grid_configure(padx=5, pady=5)

#Set Tkinter TTK Theme
sv_ttk.set_theme("dark")

#Update Booking Browser Loop
root.after(100, updateBookingBrowser)

#Main Event Handler Loop
root.mainloop()