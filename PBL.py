#Imports
import os
import cv2
import pywhatkit
import tkinter as tk
from tkinter import *
from sense_emu import SenseHat

#Classes
class new_win:
    def __init__(self):
        print("Hi")
        
    def create_window(self):
        #new_window=Tk()
        #new_window.title("New Window")
        
        
        #Use test=tk.tk() or test=TK() as both imported
        root = tk.Tk()
        root.title("What else would you like to know?")
        
        self.entry = tk.Entry(root, width=50)
        self.entry.pack()
        
        # Create a button to get the input value
        button = tk.Button(root, text="Search", command=win.get_input_value)
        button.pack()
        
        # Run the main event loop
        root.mainloop()
    
    def get_input_value(self):
        self.value = self.entry.get()
        self.search_input = self.value
        print("\nInput value:", self.value,"\n Searching...")
        pywhatkit.playonyt(self.search_input)
        
    
#Define Functions
        
def face_det():
    # trained Haar Cascade model for face detection
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    
    # Load the image
    image = cv2.imread('/home/pi/Desktop/crowd_test.jpg')

    # Convert the image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Detect faces in the image
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    # Draw rectangles around the faces
    for (x, y, w, h) in faces:
        cv2.rectangle(image, (x, y), (x + w, y + h), (255, 0, 0), 2)

    # Display the image with detected faces
    cv2.imshow('Face Detection', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()



#Conditions to get inside Aashi

win=new_win()
a=0
name=input("Can I know Your Name? ")
names=["aman","naveen","saumya","sinha"]


if a==0:
    if name.lower() in names:
        print("How may I be of your service today? ", name)
        print('''1. System start
2. Power ARC Reactor''')
        cmd=int(input("Please Enter your command, Sir: "))
        
        
        if cmd==1:
            print("Preparing System Startup...")
            window=Tk()
            window.title('Welcome To Aashi')
            Button(window,text='System startup',command=face_det).pack()
            Button(window,text='Search',command=win.create_window).pack()
            window.mainloop()
            
            
        elif cmd==2:
            
            sense = SenseHat()
            
            red = (255, 0, 0)
            blue = (0, 0, 255)
            
            while True:
                
                temp = sense.temp
                pixels = [red if i < temp else blue for i in range(64)]
                sense.set_pixels(pixels)
        
        
        
        a=a+1
    else:
        print("I don't have your database Sir/Ma'am, ",name)
        




