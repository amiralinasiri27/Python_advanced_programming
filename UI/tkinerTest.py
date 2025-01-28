from tkinter import *

# Create the main window
root = Tk()
root.title("HOPE")
root.geometry('500x300')

# Create the label
firstLabel = Label(root, text="Welcome To HOPE", font=("Helvetica", 24))
firstLabel.pack(pady=90)

# Initialize counter
counter = int(input('Enter Seconds : '))

# Function to update the label text
def update_label():
    global counter
    if counter > 0:
        firstLabel.config(text=counter)
        counter -= 1
        # Call this function again after 1000 milliseconds (1 second)
        root.after(1000, update_label)
    else:
        firstLabel.config(text="Time's up!")

# Start the countdown
update_label()

# Start the main event loop
root.mainloop()