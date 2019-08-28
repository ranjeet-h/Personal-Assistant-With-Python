import pyttsx3


engine  = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[1].id)
"""Voices[0] = for mens voice and voices[1] for girl's voice"""
engine.setProperty('voices', voices[1].id)



def speak(audio):
    pass

