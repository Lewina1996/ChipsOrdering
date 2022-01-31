from tkinter import*
root = Tk()

root.geometry("500x300")

def getvals():
    if Address == Address:
        print("Accepted")
        
    else:
        print("Address not blanks")

#Heading

Label(root,text="CHIPS ORDERING SYSTEM", font="arial 15 bold").grid(row=0, column=3)

#Field Name
name = Label(root, text="please enter your fulll name")
phone = Label(root, text="please enter your phone number")
gender= Label(root, text="please enter your Gender")
Address= Label(root, text="please enter your Address")
paymentmood= Label(root, text="please enter your Payment Mood")

# Packing Fields
name.grid(row=1, column=2)
phone.grid(row=2, column=2)
gender.grid(row=3, column=2)
Address.grid(row=4, column=2)
paymentmood.grid(row=5, column=2)

#Variable for storing data

namevalue = StringVar
phonevalue = StringVar
gendervalue = StringVar
Addressvalue = StringVar
paymentmoodvalue = StringVar

checkvalue = IntVar

#Creating entry fields
nameentry = Entry(root, textvariable =namevalue)
phoneentry = Entry(root, textvariable =phonevalue)
genderentry = Entry(root, textvariable =gendervalue)
paymentmoodentry = Entry(root, textvariable =paymentmoodvalue)
Addressentry = Entry(root, textvariable =Addressvalue)

#Packing entry fields
nameentry.grid(row=1, column=3)
phoneentry.grid(row=2, column=3)
genderentry.grid(row=3, column=3)
Addressentry.grid(row=4, column=3)
paymentmoodentry.grid(row=5, column=3)

#Creating Checkbox
checkbtn = Checkbutton(text="remember me?", variable = checkvalue)
checkbtn.grid(row=6, column=3)

#Submitt Button 
Button(text="Submit", command=getvals).grid(row=7, column=3)


root.mainloop()