from time import sleep
from org.myrobotlab.service import Speech
from org.myrobotlab.framework import MRLListener
  
  
# this subscribe is easy shorthand method
# Name it "speech".
speech = Runtime.create("speech","Speech")
speech.startService()
  
speech.setGoogleURI("http://thehackettfamily.org/Voice_api/api2.php?voice=Laura&txt=") 
  
serial1 = Runtime.start('serial1','Serial')
serial2 = Runtime.start('serial2','Serial')
speech.speak("hello")
  
serial1.connect('COM8')
serial2.connect('COM6')
 
# python.subscribe('serial1','publishRX')
# python.subscribe('serial2','publishRX')
# this subscribe with 4 parameters has all details - subscribe to and callback info
# we subscribe to one service's topic to one method and the other to a different method
 
# this is how its done in latest mrl - nice no ?
# python.subscribe('serial1','publishRX', python.getName(), 'serial1RX')
# python.subscribe('serial2','publishRX', python.getName(), 'serial2RX')
 
# this is how its done in 119
listener1 = MRLListener('publishRX', 'python', 'serial1RX', None)
serial1.addListener(listener1)
listener2 = MRLListener('publishRX', 'python', 'serial2RX', None)
serial2.addListener(listener2)
  
#  i want this to be the data from serial1
  
def serial1RX(data):
    print(data)
    num = data
    #num = chr(data)
    #print(num)
    if (num == 1):
       speech.speak("1")
    if (num == 2):
       speech.speak("2")
    if (num == 3):
       speech.speak("3")
    if (num == 4):
       speech.speak("4")         
    if (num == 5):
       speech.speak("5")
    if (num == 6):
       speech.speak("6")
    if (num == 7):
       speech.speak("7")
    if (num == 8):
       speech.speak("8")
    if (num == 9):
       speech.speak("9")
    if (num == 10):
       speech.speak("10")
    if (num == 11):
       speech.speak("11")
    if (num == 12):
       speech.speak("12")
  
#  and this to be the data from serial2
  
def serial2RX(data):
    print(data)
    num = data
    #num = chr(data)
    #print(num)
    if (num == 1):
       speech.speak("1")
    if (num == 2):
       speech.speak("2")
    if (num == 3):
       speech.speak("3")
    if (num == 4):
       speech.speak("4")         
    if (num == 5):
       speech.speak("5")
    if (num == 6):
       speech.speak("6")
    if (num == 7):
       speech.speak("7")
    if (num == 8):
       speech.speak("8")
    if (num == 9):
       speech.speak("9")
    if (num == 10):
       speech.speak("10")
    if (num == 11):
       speech.speak("11")
    if (num == 12):
       speech.speak("12")
