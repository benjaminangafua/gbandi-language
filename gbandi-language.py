#--------------------------------------------------------------------
# Import text to speech, pdf & speech recognizer
import pyttsx3
import speech_recognition as sr
import PyPDF2 

# #--------------------------------------------------------------------
# # configure pyttsx3
engine = pyttsx3.init('espeak')
engine.setProperty('rate', 130)
engine.setProperty('volume', 1)
gender = engine.setProperty('gender', "male")

# print(gender)
# engine.setProperty('gender', "")
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[4].id)

# #----------------------------------------------------------------------
# #Reading the pdf file
# pdfFileObj = open('automate2e_SampleCh7.pdf', 'rb')
# pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
# pdfReader.numPages
# pageObj = pdfReader.getPage(0)

# Execute
def execute(response):
    engine.say(f"{response}")
# pdfFileObj.close()
    engine.runAndWait()

# #----------------------------------------------------------------------
# # Printing the document {pageObj.extractText()}
n = 0
while n < 4:
    
    greeting = input("Hello: ")
    if greeting == "Hi":
        execute("di ha lur  isu")
    elif greeting == "I am fine and you":
        execute("nga seh geh gu la nga la ma")
        
    elif greeting == "You're welcome":
        execute("e va ngor wan neh ngor lay")
    n+=1





# what = input("What do you want: \n")

# ----------------------------------------------------------------------
# Audio Recognition 
# r = sr.Recognizer()
# with sr.Microphone() as source:
#     print("Say something: ")
#     r.adjust_for_ambient_noise(source)
#     audio = r.listen(source)
    # try:
    #     text = r.recognize_google(audio)
    #     print(text)
    #     engine.say("You said")
    #     engine.runAndWait()
    # except:
    #     print("Couldn't get you.")


#--------------------------------------------------------------------
# Printing the extracted file

