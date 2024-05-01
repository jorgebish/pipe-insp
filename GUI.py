import tkinter as tk
import math

class GUI():
    def __init__(self, master):
        self.master = master
        master.title("Robot Control")
        
        self.canvas_width = 250
        self.canvas_height = 250
        self.joystick_width = 50
        self.joystick_height = 50
        
        self.canvas = tk.Canvas(master, width=self.canvas_width, height=self.canvas_height)
        self.canvas.pack()
        
        self.joystick = self.canvas.create_oval(self.canvas_width/2 - self.joystick_width/2, self.canvas_height/2 - self.joystick_height/2, self.canvas_width/2 + self.joystick_width/2, self.canvas_height/2 + self.joystick_height/2, fill="blue")
        
        self.canvas.bind("<B1-Motion>", self.move_joystick)
        
    def move_joystick(self, event):
        x = event.x - self.joystick_width/2
        y = event.y - self.joystick_height/2
        
        if ((x - self.canvas_width/2)**2 + (y - self.canvas_height/2)**2) > 100**2:
            angle = math.atan2(y - self.canvas_height/2, x - self.canvas_width/2)
            x = self.canvas_width/2 + 100*math.cos(angle) - self.joystick_width/2
            y = self.canvas_height/2 + 100*math.sin(angle) - self.joystick_height/2
        
        self.canvas.coords(self.joystick, x, y, x + self.joystick_width, y + self.joystick_height)

    def control_robot(joystick_position):
        #print the joystick position to the terminal
        print(joystick_position)
        #if joystick is in the center, print "Robot stopped" to the terminal, centre is a 25 by 25 square around 0, 0
        if joystick_position[0] > -40 and joystick_position[0] < 40 and joystick_position[1] > -40 and joystick_position[1] < 40:
            print("Robot stopped")
        #if joystick is not in the center, print "Robot moving" to the terminal
        else:
            if joystick_position[0] > 0 and joystick_position[1] > 0:
                if joystick_position[0] > joystick_position[1]:
                    print("Robot moving right")
                else:
                    print("Robot moving backwards")
            elif joystick_position[0] > 0 and joystick_position[1] < 0:
                if joystick_position[0] > -joystick_position[1]:
                    print("Robot moving right")
                else:
                    print("Robot moving forward")
            elif joystick_position[0] < 0 and joystick_position[1] > 0:
                if -joystick_position[0] > joystick_position[1]:
                    print("Robot moving left")
                else:
                    print("Robot moving backwards")
            elif joystick_position[0] < 0 and joystick_position[1] < 0:
                if -joystick_position[0] > -joystick_position[1]:
                    print("Robot moving left")
                else:
                    print("Robot moving forward")
