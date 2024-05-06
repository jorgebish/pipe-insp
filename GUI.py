import tkinter as tk
import math

class GUI():
    def __init__(self, master):
        self.master = master
        master.title("Robot Control")
        
        self.canvas_width = 500
        self.canvas_height = 500
        self.canvas_radius = self.canvas_width/2
        self.joystick_width = 50
        self.joystick_height = 50
        self.origin = (self.canvas_width/2, self.canvas_height/2)
        
        self.canvas = tk.Canvas(master, width=self.canvas_width, height=self.canvas_height, bg='black')
        self.canvas.pack()

        #create a cirlce in the center of the canvas that fills up the whole canvas
        self.canvas.create_oval(0, 0, self.canvas_width, self.canvas_height, fill='white')

        self.joystick = self.canvas.create_oval(self.canvas_width/2 - self.joystick_width/2, self.canvas_height/2 - self.joystick_height/2, self.canvas_width/2 + self.joystick_width/2, self.canvas_height/2 + self.joystick_height/2, fill="grey")
        
        self.canvas.bind("<B1-Motion>", self.move_joystick)

        self.photo_button = tk.Button(master, text="Take Photo", command=self.take_photo)
        self.photo_button.pack(side=tk.BOTTOM)
        
    def move_joystick(self, event):
        x = event.x - self.joystick_width/2
        y = event.y - self.joystick_height/2
        
        angle = math.degrees(math.atan2(y-self.origin[1], x-self.origin[0]))
        #check if the joystick is with a circle of radius equal to canvas_radius taking the joystick width into account
        if math.sqrt((x - self.canvas_width/2)**2 + (y - self.canvas_height/2)**2) > self.canvas_radius - self.joystick_width/2:
            #keep the joystick within the circle of radius equal to canvas_radius taking the joystick width into account
            x = self.origin[0] + self.canvas_radius * math.cos(angle*math.pi/180) - 25
            y = self.origin[1] + self.canvas_radius * math.sin(angle*math.pi/180) - 25

        self.canvas.coords(self.joystick, x, y, x + self.joystick_width, y + self.joystick_height)

        #when the joystick is moved, the function control_robot is called
        self.control_robot((x - self.canvas_width/2, y - self.canvas_height/2))

        #when the joystick is released, the joystick is reset to the center of the canvas
        self.canvas.bind("<ButtonRelease-1>", lambda event: self.canvas.coords(self.joystick, self.canvas_width/2 - self.joystick_width/2, self.canvas_height/2 - self.joystick_height/2, self.canvas_width/2 + self.joystick_width/2, self.canvas_height/2 + self.joystick_height/2))

        #when the mouse is clicked, the joystick is moved to the position of the mouse
        self.canvas.bind("<Button-1>", lambda event: self.move_joystick(event))

        #when the mouse is clicked, the joystick is moved to the position of the mouse
        self.canvas.bind("<B1-Motion>", lambda event: self.move_joystick(event))

    def control_robot(self, joystick_position):
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

    def take_photo(self):
        #when button clicked, print "Photo Taken" to the terminal
        print("Photo Taken")
        #when button clicked, create a new window with the title "Photo"
        photo_window = tk.Toplevel(self.master)
        photo_window.title("Photo")
        #when button clicked, create a label that says "Photo Taken" in the new window
        photo_label = tk.Label(photo_window, text="Photo Taken")
        photo_label.pack()

