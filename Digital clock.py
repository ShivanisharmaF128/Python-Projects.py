from tkinter import Tk, Label
import time

# Initialize the main application window
root = Tk()
root.title("Clock")

# Function to update the time on the clock
def present_time():
    display_time = time.strftime("%I:%M:%S %p")  # Format the time
    digi_clock.config(text=display_time)  # Update the label
    digi_clock.after(200, present_time)  # Schedule the function to run again

# Create a label for the digital clock
digi_clock = Label(root, font=("Century Schoolbook", 150), bg="yellow", fg="black")
digi_clock.pack()

# Start updating the clock
present_time()

# Run the Tkinter event loop
root.mainloop()
