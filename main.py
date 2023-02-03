#-----------------------------------------------------------------------------------------------------------------------------------------------------------
#Name of Repository: Arduino_88/Computer-Booking
#Name of Programmers: Simon Siena, Peyton Freeburn, Emily Skinner, Cody Fitzgerald, Westley Lundberg
#Language Used: Python 3.10.4
#Date Project Started: January 12, 2023
#Date of Most Recent Commit: January 26, 2023

#Description:
#   This program allows staff members to access and book computer labs and/or chromebook carts.
#   At the top of the screen it will display what is currently selected to be booked.
#   Below that is the days of the week Monday to Friday, with 4 columns in each day. 
#   The columns are what period it is, being period 1, 2, 3, and 4. 
#   The boxes that are empty are available to be booked, meanwhile those with a teacher's name
#   and are highlighted are taken. This display screen is not interactive, the way you book 
#   is with the Tkinter objects below. You first select your name which is on a list of teachers, and the computer you wish to book. 
#   (To avoid people by passing the 3 of the same period per week rule). 
#   Then, select the day, time, and period. You can then click the submit button, 
#   which will either tell you that you’ve successfully booked a slot or, 
#   this time is already taken, which can also be seen on the booking browser.

#Data Dictionary:
#   Functions:
#       assignBookingInformation() --> Pushes tkinter object variables into the global teachers dictionary
#       bookComputer() --> Book button function; calculates the "Booking#": key in the global teachers dictionary; calls saveJSON(); calls updateBookingBrowser()
#       checkWeekBookings() --> Checks the currently selected teacher's bookings in the same period to ensure they can only book a computer 3 times in one period per week
#       getBookingNumber() --> Returns the number of computer bookings in the current teacher's subdictionary of the global teachers dictionary
#       loadJSON() --> Loads the global teachers dictionary from masterlist.json
#       reset() --> Runs reset-masterlist.py; calls loadJSON() and then calls updateBookingBrowser()
#       saveJSON() --> Dumps the global teachers dictionary to masterlist.json with an indent of 4
#       updateBookingBrowser() --> Clears all the booking browser and then runs through each teacher key in the global teachers ditionary, adding them to the corresponding tkinter stringVar objects
#   
#   Variables:
#       Boolean:
#           day_is_booked --> Boolean variable to store if the current day is booked by the selected teacher
#           loop --> Boolean variable used to exit a while loop
#           skip --> Boolean variable used to exit a while loop
#
#       Dictionary:
#           teacherList --> Dictionary variable used to store current teacher's sub-dictionary from the teachers dictionary
#           teachers --> Global dictionary variable used to store all the booking data
#
#       Index:
#           child --> Temporary variable used in for loops
#           item --> Temporary for loop variable used to store dictionary keys
#
#       Integer:
#           bookingNumber --> Temporary integer variable and parameter used to store the current booking number when booking a slot
#           counter --> Temporary integer variable used when selecting multiple periods at once
#           periodInt --> Temporary integer variable and parameter used to store the current period number when booking a slot (when booking multiple periods)
#           tempVar --> Temporary local counter variable used to store the current booking number for a teacher
#
#       Object:
#           bookComboBoxFrame --> Tkinter Frame object which contains the booking comboboxes
#           bookComputerLabelFrame --> Tkinter Label Frame object which contains the bottom section of the UI
#           bookingBrowserLabelFrame --> Tkinter Label Frame object which contains the upper secion of the UI
#           bookPeriodFrame --> Tkinter Frame object which contains the radio buttons used to book the period
#           btnBook --> Tkinter Button object which books a period with the selected parameters
#           btnReset --> Tkinter Button object which clears masterlist.json
#           cbxBooking --> Tkinter Combobox object is used to select which computers are being booked
#           cbxDay --> Tkinter Combobox object which is used to select which day is being booked
#           cbxStaffMember --> Tkinter Combobox object which is used to select which staff member is booking the computers
#           computer --> Tkinter StringVar object used to store the selected computer
#           day --> Tkinter StringVar object used to store the selected day
#           lblBooking --> Tkinter Label object used as a booking combobox header
#           lblDay --> Tkinter Label object used as a day combobox header
#           lblFriday --> Tkinter Label object used as a header for the Friday column in the booking browser
#           lblMonday --> Tkinter Label object used as a header for the Monday column in the booking browser
#           lblPeriod --> Tkinter Label object used as a header for the period combobox header
#           lblPeriod1Friday --> Tkinter Label object to display if the corresponding period is booked
#           lblPeriod1Monday --> Tkinter Label object to display if the corresponding period is booked
#           lblPeriod1Thursday --> Tkinter Label object to display if the corresponding period is booked
#           lblPeriod1Tuesday --> Tkinter Label object to display if the corresponding period is booked
#           lblPeriod1Wednesday --> Tkinter Label object to display if the corresponding period is booked
#           lblPeriod2Friday --> Tkinter Label object to display if the corresponding period is booked
#           lblPeriod2Monday --> Tkinter Label object to display if the corresponding period is booked
#           lblPeriod2Thursday --> Tkinter Label object to display if the corresponding period is booked
#           lblPeriod2Tuesday --> Tkinter Label object to display if the corresponding period is booked
#           lblPeriod2Wednesday --> Tkinter Label object to display if the corresponding period is booked
#           lblPeriod3Friday --> Tkinter Label object to display if the corresponding period is booked
#           lblPeriod3Monday --> Tkinter Label object to display if the corresponding period is booked
#           lblPeriod3Thursday --> Tkinter Label object to display if the corresponding period is booked
#           lblPeriod3Tuesday --> Tkinter Label object to display if the corresponding period is booked
#           lblPeriod3Wednesday --> Tkinter Label object to display if the corresponding period is booked
#           lblPeriod4Friday --> Tkinter Label object to display if the corresponding period is booked
#           lblPeriod4Monday --> Tkinter Label object to display if the corresponding period is booked
#           lblPeriod4Thursday --> Tkinter Label object to display if the corresponding period is booked
#           lblPeriod4Tuesday --> Tkinter Label object to display if the corresponding period is booked
#           lblPeriod4Wednesday --> Tkinter Label object to display if the corresponding period is booked
#           lblPeriodS --> Tkinter Label object used as a period(s) spinbox header
#           lblStaffMember --> Tkinter Label object used as a staff member combobox header
#           lblThursday --> Tkinter Label object used as a header for the Thursday column in the booking browser
#           lblTitle --> Tkinter Label object used as the title of the program (header)
#           lblTuesday --> Tkinter Label object used as a header for the Tuesday column in the booking browser
#           lblWednesday --> Tkinter Label object used as a header for the Wednesday column in the booking browser
#           mainframe --> Tkinter Frame object used as the main panel of the program above root
#           period --> Tkinter IntVar object used to store the value of the period radiobuttons
#           period1Friday --> Tkinter StringVar object used to store the value of the corresponding period's booking
#           period1FridayLabelFrame --> Tkinter Label Frame object used as a way to emphasize the corresponding period and hold the period label
#           period1Monday --> Tkinter StringVar object used to store the value of the corresponding period's booking
#           period1MondayLabelFrame --> Tkinter Label Frame object used as a way to emphasize the corresponding period and hold the period label
#           period1Thursday --> Tkinter StringVar object used to store the value of the corresponding period's booking
#           period1ThursdayLabelFrame --> Tkinter Label Frame object used as a way to emphasize the corresponding period and hold the period label
#           period1Tuesday --> Tkinter StringVar object used to store the value of the corresponding period's booking
#           period1TuesdayLabelFrame --> Tkinter Label Frame object used as a way to emphasize the corresponding period and hold the period label
#           period1Wednesday --> Tkinter StringVar object used to store the value of the corresponding period's booking
#           period1WednesdayLabelFrame --> Tkinter Label Frame object used as a way to emphasize the corresponding period and hold the period label
#           period2Friday --> Tkinter StringVar object used to store the value of the corresponding period's booking
#           period2FridayLabelFrame --> Tkinter Label Frame object used as a way to emphasize the corresponding period and hold the period label
#           period2Monday --> Tkinter StringVar object used to store the value of the corresponding period's booking
#           period2MondayLabelFrame --> Tkinter Label Frame object used as a way to emphasize the corresponding period and hold the period label
#           period2Thursday --> Tkinter StringVar object used to store the value of the corresponding period's booking
#           period2ThursdayLabelFrame --> Tkinter Label Frame object used as a way to emphasize the corresponding period and hold the period label
#           period2Tuesday --> Tkinter StringVar object used to store the value of the corresponding period's booking
#           period2TuesdayLabelFrame --> Tkinter Label Frame object used as a way to emphasize the corresponding period and hold the period label
#           period2Wednesday --> Tkinter StringVar object used to store the value of the corresponding period's booking
#           period2WednesdayLabelFrame --> Tkinter Label Frame object used as a way to emphasize the corresponding period and hold the period label
#           period3Friday --> Tkinter StringVar object used to store the value of the corresponding period's booking
#           period3FridayLabelFrame --> Tkinter Label Frame object used as a way to emphasize the corresponding period and hold the period label
#           period3Monday --> Tkinter StringVar object used to store the value of the corresponding period's booking
#           period3MondayLabelFrame --> Tkinter Label Frame object used as a way to emphasize the corresponding period and hold the period label
#           period3Thursday --> Tkinter StringVar object used to store the value of the corresponding period's booking
#           period3ThursdayLabelFrame --> Tkinter Label Frame object used as a way to emphasize the corresponding period and hold the period label
#           period3Tuesday --> Tkinter StringVar object used to store the value of the corresponding period's booking
#           period3TuesdayLabelFrame --> Tkinter Label Frame object used as a way to emphasize the corresponding period and hold the period label
#           period3Wednesday --> Tkinter StringVar object used to store the value of the corresponding period's booking
#           period3WednesdayLabelFrame --> Tkinter Label Frame object used as a way to emphasize the corresponding period and hold the period label
#           period4Friday --> Tkinter StringVar object used to store the value of the corresponding period's booking
#           period4FridayLabelFrame --> Tkinter Label Frame object used as a way to emphasize the corresponding period and hold the period label
#           period4Monday --> Tkinter StringVar object used to store the value of the corresponding period's booking
#           period4MondayLabelFrame --> Tkinter Label Frame object used as a way to emphasize the corresponding period and hold the period label
#           period4Thursday --> Tkinter StringVar object used to store the value of the corresponding period's booking
#           period4ThursdayLabelFrame --> Tkinter Label Frame object used as a way to emphasize the corresponding period and hold the period label
#           period4Tuesday --> Tkinter StringVar object used to store the value of the corresponding period's booking
#           period4TuesdayLabelFrame --> Tkinter Label Frame object used as a way to emphasize the corresponding period and hold the period label
#           period4Wednesday --> Tkinter StringVar object used to store the value of the corresponding period's booking
#           period4WednesdayLabelFrame --> Tkinter Label Frame object used as a way to emphasize the corresponding period and hold the period label
#           periods --> Tkinter IntVar object used to store the value of the period(s) spinbox
#           rBtnPeriod1 --> Tkinter Radio Button object used to signify period 1
#           rBtnPeriod2 --> Tkinter Radio Button object used to signify period 2
#           rBtnPeriod3 --> Tkinter Radio Button object used to signify period 3
#           rBtnPeriod4 --> Tkinter Radio Button object used to signify period 4
#           root --> Tkinter Root object (the physical window itself)
#           spnPeriodS --> Tkinter Spinbox object used to select the number of periods to book
#           teacher --> Tkinter StringVar object used to store the selected teacher
#
#       Path:
#           fp --> Temporary Path variable used to store the location of masterlist.json
#
#       String:
#           color1 --> String variable to store a theme color for easy customization
#           color2 --> String variable to store a theme color for easy customization
#           color3 --> String variable to store a theme color for easy customization
#           color4 --> String variable to store a theme color for easy customization
#           periodKey --> String variable used to store the currently selected period as a dictionary key
#           stringVariable --> String variable used to store a set of code as text in order to function properely in an eval() function
#
#       Tuple:
#           computers --> Tuple variable used to store the list of all selectable computers
#           days --> Tuple variable used to store the list of all selectable days
#           teacherTuple --> Tuple variable used as options to select for the teacher combobox
#-----------------------------------------------------------------------------------------------------------------------------------------------------------

from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import json
import sv_ttk
import os

#Function Definition - loadJSON() <-- Early in code because global teachers variable is initialized
def loadJSON():
    with open("masterlist.json") as fp:
        global teachers #Initialize global teachers dictionary
        teachers = json.load(fp) #Load JSON file to ditionary

loadJSON() #Load the JSON file at start of program
teacherTuple = tuple(teachers.keys()) #Set teacherTuple to every dictionary key from teachers

#Initiate Combobox Option Tuples
computers = ("Chromebook Cart 1", "Chromebook Cart 2", "Room 33 - Computer Lab", "Room 35 - Computer Lab", "Room 37 - Computer Lab", "Room 39 - Computer Lab", "Room 280 - Computer Lab", "Upper Math Lab")
days = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday")

#Initiate Tkinter Root
root = Tk()
root.title("Computer Booking v1.7") #Set window title

#Placeholder color variables 
color1 = "#bde0fe"
color2 = "#a8dadc"
color3 = "#457b9d"
color4 = "#f1faee"

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
periods = IntVar(value=1) #Spinbox

#Function Definition
def assignBookingInformation(bookingNumber, periodInt):
        teachers[teacher.get()]["Period" + str(bookingNumber)] = periodInt #Write period to dictionary
        teachers[teacher.get()]["Computer" + str(bookingNumber)] = computer.get() #Write computer to dictionary
        teachers[teacher.get()]["Day" + str(bookingNumber)] = day.get() #Write to to dictionary
        teachers[teacher.get()]["Booking#"] = bookingNumber # Write booking number to dictionary

def checkWeekBookings(periodInt, teacherList):
    try:
        counter = 0 #Initialize counter at 0
        for item in days:
            stringVariable = "period" + str(periodInt) + str(item) #Set to name of variable of selected period and current day in loop
            day_is_booked = eval(stringVariable + ".get() == teacher.get()")
            if day_is_booked:
                counter = counter + 1 #Increment the counter by 1
        if counter >= 3: #If the teacher has 3 bookings in this period
                messagebox.showerror(title="Attempted Overbook", message=(teacher.get() + " already has 3 bookings in period " + str(period.get())), icon="error", detail=("Please choose a different period")) #Overbook error message
        else:
            assignBookingInformation(periodInt=periodInt, bookingNumber=getBookingNumber(teacherList=teacherList)) #Otherwise allow them to book
    except KeyError: #KeyErrors result from searching a dicitonary for a key that does not exist (This occurs for each empty teacher dictionary)
        pass

def getBookingNumber(teacherList):
    counter = 1
    loop = True
    while loop: #Count every key in the format "Period" followed by an integer - ex: "Period12"
        periodKey = "Period" + str(counter)
        if periodKey in teacherList: #If the current key exists in the teacherList dictionary
            counter = counter + 1 #Increment counter
        else:
            loop = False #Otherwise, exit the loop
    return counter

def bookComputer():
    #Initiate temporary variables
    periodInt = period.get()
    counter = periods.get()
    skip = False
    while counter > 0 and not skip: #Repeat for the number of periods the user is booking
        try:
            teacherList = teachers[teacher.get()].keys()
            stringVariable = "period" + str(periodInt) + day.get() #Set stringVariable to the name of the desired variable (format: "period1Monday")
            if eval(stringVariable + ".get() == \"\""): #evaluate stringVariable (format: period1Monday.get() == "")
                checkWeekBookings(periodInt=periodInt, teacherList=teacherList)
            else: #Selected period already booked
                messagebox.showerror(title="Attempted Overwrite", message=(str(eval(stringVariable + ".get()")) + " already has Period " + str(period.get()) + " booked on " + day.get()), icon="error", detail=("Please book a different period :)"))
                skip = True #Move to the next nested teacher dictionary
            saveJSON()
            updateBookingBrowser()
        except KeyError: #KeyErrors result from searching a dictionary for a key that does not exist (This occurs for each empty teacher dictionary)
            pass #Ignore these errors
        periodInt = periodInt + 1 #Increment periodInt
        counter = counter - 1 #Increment counter

def updateBookingBrowser():
    #Clear all booking labels
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

    for item in teachers.keys(): #For each teacher in the database
        if "Booking#" in teachers[item]: #If a key called "Booking#" exists
            tempVar = teachers[item]["Booking#"] #Set tempVar as the booking number
            while tempVar > 0: #Loop tempVar times
                stringVariable = "period" + str(teachers[item]["Period" + str(tempVar)]) + teachers[item]["Day" + str(tempVar)] #Set stringVariable to the variable named current period and date (format: period1Monday)
                if str(teachers[item]["Computer" + str(tempVar)]) == computer.get(): #Only display the bookings for the currently selected computer
                    eval(stringVariable + ".set(\"" + item + "\")") #Display the current booking in the booking browser
                tempVar = tempVar - 1 #Decrement tempVar (move down to next booking for the current teacher)
    root.after(100, updateBookingBrowser) #Run this function every 100ms (0.1 seconds)
updateBookingBrowser() #Run this function at the start of the program to display the saved bookings

def saveJSON():
    with open("masterlist.json", "w") as fp:
        json.dump(teachers, fp, indent=4, sort_keys=True) #Alphabetically pretty print the teachers dictionary into masterlist.json with an indent of 4

def reset():
    os.system("reset-masterlist.py") #Run reset-masterlist.py
    loadJSON() #Load the now-empty masterlist.json
    updateBookingBrowser() #Update the booking browser

#-----USER INTERFACE-----
#Initialize Tkinter Mainframe
mainframe = ttk.Frame(root, padding=(3,3,12,12))

#Initialize Tkinter mainframe Objects
lblTitle = ttk.Label(mainframe, textvariable=computer, font=("Calibri", 23), foreground=color4)
bookingBrowserLabelFrame = ttk.LabelFrame(mainframe, text="Browse Bookings")
bookComputerLabelFrame = ttk.LabelFrame(mainframe, text="Book Computer")

#Initialize Tkinter bookingBrowserLabelFrame Objects
lblMonday = ttk.Label(bookingBrowserLabelFrame, text="Monday", font=("Calibri", 14), foreground=color1)
lblTuesday = ttk.Label(bookingBrowserLabelFrame, text="Tuesday", font=("Calibri", 14), foreground=color1)
lblWednesday = ttk.Label(bookingBrowserLabelFrame, text="Wednesday", font=("Calibri", 14), foreground=color1)
lblThursday = ttk.Label(bookingBrowserLabelFrame, text="Thursday", font=("Calibri", 14), foreground=color1)
lblFriday = ttk.Label(bookingBrowserLabelFrame, text="Friday", font=("Calibri", 14), foreground=color1)

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
lblPeriod1Monday = ttk.Label(period1MondayLabelFrame, textvariable=period1Monday, font=("Calibri", 13), foreground=color2)
lblPeriod2Monday = ttk.Label(period2MondayLabelFrame, textvariable=period2Monday, font=("Calibri", 13), foreground=color2)
lblPeriod3Monday = ttk.Label(period3MondayLabelFrame, textvariable=period3Monday, font=("Calibri", 13), foreground=color2)
lblPeriod4Monday = ttk.Label(period4MondayLabelFrame, textvariable=period4Monday, font=("Calibri", 13), foreground=color2)

lblPeriod1Tuesday = ttk.Label(period1TuesdayLabelFrame, textvariable=period1Tuesday, font=("Calibri", 13), foreground=color2)
lblPeriod2Tuesday = ttk.Label(period2TuesdayLabelFrame, textvariable=period2Tuesday, font=("Calibri", 13), foreground=color2)
lblPeriod3Tuesday = ttk.Label(period3TuesdayLabelFrame, textvariable=period3Tuesday, font=("Calibri", 13), foreground=color2)
lblPeriod4Tuesday = ttk.Label(period4TuesdayLabelFrame, textvariable=period4Tuesday, font=("Calibri", 13), foreground=color2)

lblPeriod1Wednesday = ttk.Label(period1WednesdayLabelFrame, textvariable=period1Wednesday, font=("Calibri", 13), foreground=color2)
lblPeriod2Wednesday = ttk.Label(period2WednesdayLabelFrame, textvariable=period2Wednesday, font=("Calibri", 13), foreground=color2)
lblPeriod3Wednesday = ttk.Label(period3WednesdayLabelFrame, textvariable=period3Wednesday, font=("Calibri", 13), foreground=color2)
lblPeriod4Wednesday = ttk.Label(period4WednesdayLabelFrame, textvariable=period4Wednesday, font=("Calibri", 13), foreground=color2)

lblPeriod1Thursday = ttk.Label(period1ThursdayLabelFrame, textvariable=period1Thursday, font=("Calibri", 13), foreground=color2)
lblPeriod2Thursday = ttk.Label(period2ThursdayLabelFrame, textvariable=period2Thursday, font=("Calibri", 13), foreground=color2)
lblPeriod3Thursday = ttk.Label(period3ThursdayLabelFrame, textvariable=period3Thursday, font=("Calibri", 13), foreground=color2)
lblPeriod4Thursday = ttk.Label(period4ThursdayLabelFrame, textvariable=period4Thursday, font=("Calibri", 13), foreground=color2)

lblPeriod1Friday = ttk.Label(period1FridayLabelFrame, textvariable=period1Friday, font=("Calibri", 13), foreground=color2)
lblPeriod2Friday = ttk.Label(period2FridayLabelFrame, textvariable=period2Friday, font=("Calibri", 13), foreground=color2)
lblPeriod3Friday = ttk.Label(period3FridayLabelFrame, textvariable=period3Friday, font=("Calibri", 13), foreground=color2)
lblPeriod4Friday = ttk.Label(period4FridayLabelFrame, textvariable=period4Friday, font=("Calibri", 13), foreground=color2)

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
lblTitle.grid(column=0, row=0)
bookingBrowserLabelFrame.grid(column=0, row=1, sticky="nwes")
bookComputerLabelFrame.grid(column=0, row=2, sticky="nwes")

#bookComputerLabelFrame Tkinter Objects Grid Formatting
bookComboBoxFrame.grid(column=0, row=0, rowspan=3, sticky="nwes")
bookPeriodFrame.grid(column=1, row=0, rowspan=3, sticky="nwes")
lblPeriodS.grid(column=2, row=0)
spnPeriodS.grid(column=3, row=0)
btnBook.grid(column=2, row=1, columnspan=2, sticky="nwes")
btnReset.grid(column=2, row=2, columnspan=2)

#bookComboBoxFrame Tkinter Objects Grid Formatting
lblStaffMember.grid(column=0, row=0, sticky="nwes")
cbxStaffMember.grid(column=0, row=1, sticky="nwes")

lblBooking.grid(column=0, row=2, sticky="nwes")
cbxBooking.grid(column=0, row=3, sticky="nwes")

lblDay.grid(column=0, row=4, sticky="nwes")
cbxDay.grid(column=0, row=5, sticky="nwes")

#bookPeriodFrame Tkinter Objects Grid Formatting
lblPeriod.grid(column=0, row=0)
rBtnPeriod1.grid(column=0, row=1)
rBtnPeriod2.grid(column=0, row=2)
rBtnPeriod3.grid(column=0, row=3)
rBtnPeriod4.grid(column=0, row=4)


#bookingBrowserLabelFrame Tkinter Objects Grid Formatting
lblMonday.grid(column=0, row=0)
lblTuesday.grid(column=1, row=0)
lblWednesday.grid(column=2, row=0)
lblThursday.grid(column=3, row=0)
lblFriday.grid(column=4, row=0)

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
lblPeriod1Monday.grid(column=0, row=0)
lblPeriod2Monday.grid(column=0, row=0)
lblPeriod3Monday.grid(column=0, row=0)
lblPeriod4Monday.grid(column=0, row=0)

lblPeriod1Tuesday.grid(column=0, row=0)
lblPeriod2Tuesday.grid(column=0, row=0)
lblPeriod3Tuesday.grid(column=0, row=0)
lblPeriod4Tuesday.grid(column=0, row=0)

lblPeriod1Wednesday.grid(column=0, row=0)
lblPeriod2Wednesday.grid(column=0, row=0)
lblPeriod3Wednesday.grid(column=0, row=0)
lblPeriod4Wednesday.grid(column=0, row=0)

lblPeriod1Thursday.grid(column=0, row=0)
lblPeriod2Thursday.grid(column=0, row=0)
lblPeriod3Thursday.grid(column=0, row=0)
lblPeriod4Thursday.grid(column=0, row=0)

lblPeriod1Friday.grid(column=0, row=0)
lblPeriod2Friday.grid(column=0, row=0)
lblPeriod3Friday.grid(column=0, row=0)
lblPeriod4Friday.grid(column=0, row=0)

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

#bookingBrowserLabelFrame Column Configuration
period1MondayLabelFrame.columnconfigure(0, weight=1)
period1TuesdayLabelFrame.columnconfigure(0, weight=1)
period1WednesdayLabelFrame.columnconfigure(0, weight=1)
period1ThursdayLabelFrame.columnconfigure(0, weight=1)
period1FridayLabelFrame.columnconfigure(0, weight=1)

period2MondayLabelFrame.columnconfigure(0, weight=1)
period2TuesdayLabelFrame.columnconfigure(0, weight=1)
period2WednesdayLabelFrame.columnconfigure(0, weight=1)
period2ThursdayLabelFrame.columnconfigure(0, weight=1)
period2FridayLabelFrame.columnconfigure(0, weight=1)

period3MondayLabelFrame.columnconfigure(0, weight=1)
period3TuesdayLabelFrame.columnconfigure(0, weight=1)
period3WednesdayLabelFrame.columnconfigure(0, weight=1)
period3ThursdayLabelFrame.columnconfigure(0, weight=1)
period3FridayLabelFrame.columnconfigure(0, weight=1)

period4MondayLabelFrame.columnconfigure(0, weight=1)
period4TuesdayLabelFrame.columnconfigure(0, weight=1)
period4WednesdayLabelFrame.columnconfigure(0, weight=1)
period4ThursdayLabelFrame.columnconfigure(0, weight=1)
period4FridayLabelFrame.columnconfigure(0, weight=1)


#bookingBrowserLabelFrame Column Configuration
period1MondayLabelFrame.rowconfigure(0, weight=1)
period1TuesdayLabelFrame.rowconfigure(0, weight=1)
period1WednesdayLabelFrame.rowconfigure(0, weight=1)
period1ThursdayLabelFrame.rowconfigure(0, weight=1)
period1FridayLabelFrame.rowconfigure(0, weight=1)

period2MondayLabelFrame.rowconfigure(0, weight=1)
period2TuesdayLabelFrame.rowconfigure(0, weight=1)
period2WednesdayLabelFrame.rowconfigure(0, weight=1)
period2ThursdayLabelFrame.rowconfigure(0, weight=1)
period2FridayLabelFrame.rowconfigure(0, weight=1)

period3MondayLabelFrame.rowconfigure(0, weight=1)
period3TuesdayLabelFrame.rowconfigure(0, weight=1)
period3WednesdayLabelFrame.rowconfigure(0, weight=1)
period3ThursdayLabelFrame.rowconfigure(0, weight=1)
period3FridayLabelFrame.rowconfigure(0, weight=1)

period4MondayLabelFrame.rowconfigure(0, weight=1)
period4TuesdayLabelFrame.rowconfigure(0, weight=1)
period4WednesdayLabelFrame.rowconfigure(0, weight=1)
period4ThursdayLabelFrame.rowconfigure(0, weight=1)
period4FridayLabelFrame.rowconfigure(0, weight=1)

#Formatting Loops
for child in bookComputerLabelFrame.winfo_children(): #Set the padx and pady parameters of all the sub-objects in bookComputerLabelFrame
    child.grid_configure(padx=5, pady=5)

for child in bookingBrowserLabelFrame.winfo_children(): #Set the padx and pady parameters of all the sub-objects in bookingBrowserLabelFrame
    child.grid_configure(padx=5, pady=5, ipadx=5, ipady=5)
    for item in child.winfo_children(): #Set the padx and pady parameters of all the sub-objects in each sub-object in bookingBrowserLabelFrame
        item.grid_configure(padx=5, pady=5)

for child in mainframe.winfo_children(): #Set the padx and pady parameters of all the sub-objects in mainframe
    child.grid_configure(padx=5, pady=5)

#Set Tkinter TTK Theme
sv_ttk.set_theme("dark")

#Update Booking Browser Loop
root.after(100, updateBookingBrowser) #Call updateBookingBrowser() 10 times per second

#Main Event Handler Loop
root.mainloop()