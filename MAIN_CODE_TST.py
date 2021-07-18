import tensorflow as tf, sys
import cv2
import time
from tkinter import filedialog
from tkinter import messagebox
import tkinter.messagebox
import numpy as np


image_path= filedialog.askopenfilename(filetypes = (("BROWSE BANANA IMAGE", "*.jpg"), ("All files", "*")))
I=cv2.imread(image_path)
cv2.imshow('INPUT IMAGE',I);
# Read in the image_data
image_data = tf.gfile.FastGFile(image_path, 'rb').read()
# Open label file
label_lines = [line.rstrip() for line
    in tf.gfile.GFile("retrained_labels.txt")]
# CNN trained file
with tf.gfile.FastGFile("retrained_graph.pb", 'rb') as f:
    graph_def = tf.GraphDef()
    graph_def.ParseFromString(f.read())
    _ = tf.import_graph_def(graph_def, name='')



# TEST given input image
with tf.Session() as sess:
     softmax_tensor = sess.graph.get_tensor_by_name('final_result:0')
     print(softmax_tensor)
     predictions = sess.run(softmax_tensor, 
     {'DecodeJpeg/contents:0': image_data})
     # Confidenece
     top_k = predictions[0].argsort()[-len(predictions[0]):][::-1]
     human_string = label_lines[0]
     score1 = predictions[0][0]
     print('PREDICTION----:\n',predictions)
     #print('SCORES--:\n',score1)
     CurID=np.argmax(predictions)
     print('PREDICTED CLASS INDEX\n',CurID)

#print('-----------------------------------------------------\n')
#print('----------------------RESULT-------------------------\n')
if np.max(predictions)>=0.92:
    if CurID==0:
        messagebox.showinfo('RESULT', 'BANANA IS NORMAL AND DOES NOT CONTAIN CARBIDE')
        #print('BANANA IS NORMAL--:\n')
    if CurID==1:
        messagebox.showinfo('RESULT', 'BANANA IS INFECTED AND CONTAINS CARBIDE')
        #print('BANANA IS INFECTED--:\n')
else:
    messagebox.showinfo('RESULT', 'UNABLE TO PREDICT. PLEASE CHECK INPUT IMAGE')
    #print('UNABLE TO PREDICT--:\n')


