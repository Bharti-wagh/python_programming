#TASK: Intall an external module and use it to perform an operation of your interest.

# pyttsx3 is a text-to-speech conversion library in Python.
import pyttsx3

# Initialize the speech engine
engine = pyttsx3.init()

# Set the text you want to convert to speech
text = "You look Beautiful always"

# Speak the text
engine.say(text)

# Wait for the speech to finish
engine.runAndWait()
