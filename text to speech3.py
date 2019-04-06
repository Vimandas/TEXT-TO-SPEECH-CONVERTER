# -*- coding: utf-8 -*-
"""
Created on Sat Apr  6 22:33:05 2019

@author: viman
"""

# Python program to convert 
# text to speech 
  
# import the required module from text to speech conversion 
import win32com.client 
  
# Calling the Disptach method of the module which  
# interact with Microsoft Speech SDK to speak 
# the given input from the keyboard 
  
speaker = win32com.client.Dispatch("SAPI.SpVoice") 
  s = 'my name is viman,studying in iit bhubaneswar and my dream is to open my own institute this is my small projects love u allll'
 
#while 1: 
   # print("Enter the word you want to speak it out by computer") 
    s = input() 
    speaker.Speak(s) 
  
# To stop the program press 
# CTRL + Z 