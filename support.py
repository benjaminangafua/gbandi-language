

##Understanding pdf
# importing required modules

# Rate
# rate = engine.getProperty('rate')
# print(rate)

# # Volume
# volume = engine.getProperty('volume')
# raise_volume = float(input("Determine the Volume: "))
# # print(volume)


# # Voice
# # print(voices)

# qr code
import os
import qrcode

img = qrcode.make("https://youtu.be/oHg5SJYRHA0")
img.save("qr.png", "PNG")
os.system("open qr.png")


import speech_recognition
recognizer = speech_recognition.Recognizer()

with speech_recognition.Microphone() as source:
    print("Say something: ")
    audio = recognizer.listen(source)

print("You said: ")
# print(recognizer_instance.recognize_google_cloud(audio))

word = input("say something: ")

if "hello" in word:
    print("How are you doing")
elif "how are you" in word:
    print("I am well, thanks.")
elif "goodbye" in word:
    print("Goodbye to you too!")
else:
    print("Huh?")

# Automate WhatsApp msg
import pywhatkit
pywhatkit.sendwhatmsg('+231776654128', 'Hi James K. Gaye this work', 11, 29)