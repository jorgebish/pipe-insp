#from Motor import Motor
from GUI import GUI
import tkinter as tk
#P - Pipe
#I - Inspection
#S - Surveillance
#S - Spherical
#E - Engineering
#R - Robot

# Path: Project/main.py
# Create the motor objects
#wheels = Motor(22, 17, 27)
# Create the GUI object
root = tk.Tk()
gui = GUI(root)
root.mainloop()