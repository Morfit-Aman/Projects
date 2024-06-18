import os
import cv2
import numpy as np
#import tensorflow as tf
from object_detection.utils import label_map_util
from object_detection.utils import visualization_utils as viz_utils
from tkinter import *
from sense_emu import SenseHat



red = (255, 0, 0)
blue = (0, 0, 255)

def create_window():
    new_window=Tk()
    new_window.title("Does this work?")
    window.destroy()

def obj_det():
    # Path to the directory containing the object detection module
    PATH_TO_MODEL_DIR = '/home/pi/Desktop'
    PATH_TO_LABELS = os.path.join(PATH_TO_MODEL_DIR, 'label_map.pbtxt')
    PATH_TO_SAVED_MODEL = os.path.join(PATH_TO_MODEL_DIR, 'saved_model')
    
    # Load the label map
    category_index = label_map_util.create_category_index_from_labelmap(PATH_TO_LABELS, use_display_name=True)
    
    # Load the saved model
    detect_fn = tf.saved_model.load(PATH_TO_SAVED_MODEL)
    
    # OpenCV code for reading and processing an image
    cap = cv2.VideoCapture(0)  # Use 0 for the primary webcam
    while True:
        ret, image_np = cap.read()
        
        # Convert the image to tensor
        input_tensor = tf.convert_to_tensor(image_np)
        input_tensor = input_tensor[tf.newaxis, ...]
    
        # Perform inference
        detections = detect_fn(input_tensor)
    
        # All outputs are batches tensors.
        # Convert to numpy arrays, and take index [0] to remove the batch dimension.
        num_detections = int(detections.pop('num_detections'))
        detections = {key: value[0, :num_detections].numpy() for key, value in detections.items()}
        detections['num_detections'] = num_detections
    
        # detection_classes should be integers.
        detections['detection_classes'] = detections['detection_classes'].astype(np.int64)
    
        # Visualization of the results of a detection.
        viz_utils.visualize_boxes_and_labels_on_image_array(
        image_np,
        detections['detection_boxes'],
        detections['detection_classes'],
        detections['detection_scores'],
        category_index,
        use_normalized_coordinates=True,
        max_boxes_to_draw=200,
        min_score_thresh=0.30,
        agnostic_mode=False)
    
        cv2.imshow('object detection', cv2.resize(image_np, (800, 600)))
        if cv2.waitKey(25) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            break
    
    #comments-
    
    
a=0
name=input("Can I know Your Name? ")
names=["aman","sinha"]


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
            Button(window,text='System startup',command=obj_det).pack()
            Button(window,text='Test',command=create_window).pack()
            window.mainloop()
            
            
        elif cmd==2:
            while True:
                sense = SenseHat()
                temp = sense.temp
                pixels = [red if i < temp else blue for i in range(64)]
                sense.set_pixels(pixels)
        
        
        
        a=a+1
    else:
        print("I don't have your database Sir,",name)
        



