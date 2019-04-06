# -*- coding: utf-8 -*-
"""
Created on Fri Apr  5 19:01:41 2019

@author: viman
"""
# Import the required module for text  
# to speech conversion 
from gtts import gTTS 
  
# This module is imported so that we can  
# play the converted audio 
import os 
  #k=1
# The text that you want to convert to audio 
mytext = 'my name is viman,studying in iit bhubaneswar and my dream is to open my own institute this is my small projects love u allll'
#  while k==1:
 #     mytext=input("what do you want to change")
  #    k=2
# Language in which you want to convert 
language = 'fr'
  
# Passing the text and language to the engine,  
# here we have marked slow=False. Which tells  
# the module that the converted audio should  
# have a high speed 
myobj = gTTS(text=mytext, lang=language, slow=False) 
  
# Saving the converted audio in a mp3 file named 
# welcome  
myobj.save("text_to_speech.mp3") 
  
# Playing the converted file 
os.system("mpg321 welcome.mp3") 
