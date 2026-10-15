import pyttsx3
engine = pyttsx3.init()

# For Mac, If you face error related to "pyobjc" when running the `init()` method :
# Install 9.0.1 version of pyobjc : "pip install pyobjc>=9.0.1"

engine.say("Hello, I am a text-to-speech engine. I can convert text into speech using Python. How can I assist you today?")
engine.runAndWait()