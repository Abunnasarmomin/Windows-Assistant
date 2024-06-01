import pyttsx3
import speech_recognition as sr
import webbrowser 
import datetime
import pyjokes
import subprocess
import datetime
import time
import requests
import json
import random
import sys
import psutil
import speedtest
import os

print("--- Welcome To Techno-Bot AI ---")



# Making the Ai to Listen
def sptext():
    recognizer = sr.Recognizer() # Applying to hear in (recognizer) variable
    with sr.Microphone() as source: # Applying that AI will listen the voice in Microphone and we are giving (source) name to Microphone
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source) # Removing Background Voices for Clearaty
        audio = recognizer.listen(source) # using (audio) variable to listen (source)
    try:
        print("recognizing..")
        data = recognizer.recognize_google(audio) # using (data) to print (audio)
        print("USER:-",data) # Printing (data) means audio
        return data
    except sr.UnknownValueError:
        print("Not Understanding")

#sptext()

# Setting Ai voice and property
def speechtx(x):
    engine = pyttsx3.init()
    voices = engine.getProperty("voices") # Getting property of voices to apply voices
    engine.setProperty('voice',voices[0].id) # voices[0].id means giving male voice to AI
    rate = engine.getProperty('rate') # Getting property in rate
    engine.setProperty('rate',159) # Addjustying speed of AI Voice
    engine.say(x)
    engine.runAndWait()

def GSI():
    # Get system information using psutil
    cpu_usage = psutil.cpu_percent()
    memory_info = psutil.virtual_memory()
    disk_info = psutil.disk_usage("/")

    # Format the information
    system_info = f"CPU Usage: {cpu_usage}%\nMemory Usage: {memory_info.percent}%\nDisk Usage: {disk_info.percent}%"

    print(system_info)
    speechtx(system_info)

def GIS():
    try:
        st = speedtest.Speedtest()
        download_speed = st.download() / 1_000_000  # Convert to Mbps
        upload_speed = st.upload() / 1_000_000  # Convert to Mbps

        return download_speed, upload_speed
    except Exception as e:
        print(f"An error occurred in GIS: {e}")
        return 0, 0 
def CIS():
    download_speed, upload_speed = GIS()
    Internet_Speed = f"current internet speed is, Download: {download_speed:.2f} Mbps, Upload: {upload_speed:.2f} Mbps."
    print(Internet_Speed)
    speechtx(Internet_Speed)

# Making the function to talk with AI
if __name__ == '__main__':

    while True:    
    #if sptext().lower() == "hello technobot" and "hello techno boat" :
        d1 = sptext().lower() # .lower will translate the letters in lower from
        if "your name" in d1: # if 'your name' this word user says in d1
            n1 = "my name is Windows Assistant" # Respose of AI
            print("Windows Assistant:-",n1)
            speechtx(n1)  
        elif "hi windows assistant" in d1:
             n0 = "hi! How are you!"
             print("Windows Assistant:-",n0)
             speechtx(n0)      
        elif "your age" in d1: # so onnn
            n2 = "I don't have any age because i am machine AI"
            print("Windows Assistant:-",n2)
            speechtx(n2)
        elif "about yourself" in d1: 
             n3 = "i am Machine AI and i can help you in various Things!!"
             print("Windows Assistant:-",n3)
             speechtx(n3)
        elif "help me" in d1:
             n4 = "I can help you in your questions answers and solving"
             print("Windows Assistant:-",n4)
             speechtx(n4)
        elif "time" in d1:             
             time = datetime.datetime.now().strftime("%I:%M%p")
             print("Time:- ",time)
             speechtx(time)
        elif 'youtube' in d1:
             webbrowser.open("https://www.youtube.com/")
             n5 = "opening youtube"               
             speechtx(n5)
        elif 'instagram' in d1:
             webbrowser.open("https://www.instagram.com/?next=%2F")
             n7 = "opening instagram"               
             speechtx(n7)
        elif 'facebook' in d1:
             webbrowser.open("https://www.facebook.com/rumana.momin.315")
             n8 = "opening facebook"               
             speechtx(n8)
        elif 'google' in d1:
             webbrowser.open("https://www.Google.com")
             n9 = "opening google"               
             speechtx(n9)
        elif 'chat GPT' in d1:
             webbrowser.open("https://chat.openai.com/")
             n10 = "opening chatgpt"
             speechtx(n10)
        elif 'account' in d1:
             webbrowser.open("https://myaccount.google.com/?utm_source=chrome-profile-chooser&pli=1")
             n11 = "opening your google account"
             speechtx(n11)
        elif 'channel' in d1 :
             webbrowser.open(f"https://www.youtube.com/results?search_query={d1}")
             n12 = f"opening {d1} channle"
             speechtx(n12)
        elif 'joke' in d1:
             joke = pyjokes.get_joke(language="en",category="neutral")
             print(joke)
             speechtx(joke)
        elif 'play song' in d1:
             add = r"C:\Users\GRAVITY\Desktop\AlarmEff"
             listsong = os.listdir(add) 
             n13 = "opening"
             speechtx(n13)
             os.startfile(os.path.join(add,listsong[3]))
       # elif 'minecraft' in d1.lower():
       #      path = r"C:\Users\GRAVITY\AppData\Roaming\.minecraft\TLauncher.exe"
       #      n14 = "opening minecraft"
       #      speechtx(n14)
       #      os.startfile(path)
        elif 'blender' in d1.lower():
             path = r"C:\Program Files\Blender Foundation\Blender 2.90\blender.exe"
             os.startfile(path)
             n15 = "opening blender"
             speechtx(n15)
        elif 'github' in d1.lower():
             path = r"C:\Users\GRAVITY\AppData\Local\GitHubDesktop\GitHubDesktop.exe"
             os.startfile(path)
             n15 = "opening github"
             speechtx(n15)
        elif 'gamepix' and 'game pics' in d1:
             webbrowser.open("https://www.gamepix.com/")
             n16 = "opening gamepix"
             speechtx(n16)
        elif "bye-bye" in d1:
             end = "By By see you again!"
             print("Windows Assistant:-",end)
             speechtx(end)
             exit()
        elif "hello" in d1:
             n17 = "hy There, how are you"
             print("Windows Assistant:-",n17)
             speechtx(n17)
        elif "i am fine" in d1:
             n18 = "Great,You can ask me questions"
             print("Windows Assistant:-",n18)
             speechtx(n18)
        elif "are you doing" in d1:
             n19 = "Developing Myself"   
             print("Windows Assistant:-",n19)
             speechtx(n19)
        elif "what is my name" in d1:
             info = input("what is your name: ")
             n20 = f"HI, {info}"
             print("Windows Assistant:-",n20)
             speechtx(n20)
        elif "your favourite food" in d1:
             n20 = "my favourite food is burger"
             print("Windows Assistant:-",n20)
             speechtx(n20)
        elif "open lively wallpaper" in d1:
             getp = r"C:\Users\GRAVITY\AppData\Local\Programs\Lively Wallpaper\Lively.exe"
             os.startfile(getp)
             g1 = "opening lively wallpaper"
             speechtx(g1)
        elif "shutdown" in d1:
            os.system("shutdown /s /t 1")  # Shutdown command
            exit()
        elif "open calendar" in d1:
             getp1 = r"C:\Program Files\Microsoft Office\root\Office16\OUTLOOK.EXE"
             os.startfile(getp1)
             g2 = "opening calendar"
             speechtx(g2)
        elif "make foler" in d1:
             desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
             getp2 = input("Name of folder: ")
             folder_path = os.path.join(desktop_path, getp2)
             os.makedirs(folder_path)     
             g3 = f"succesfully made {getp2} folder"
        elif "i call you" in d1:
             g4 = "You can call me as Windows Assistant"
             print("Windows Assistant:-",g4)
             speechtx(g4)
        elif "shut up" in d1:
             g5 = "Sorry! if i had done something wrong"
             print("Windows Assistant:-",g5)
             speechtx(g5)     
        elif "i am fine" in d1:
             g5 = "Great! How can i help you"
             print("Windows Assistant:-",g5)
             speechtx(g5) 
        elif "you are awesome" in d1:
             g6 = "Thanks! I'm here to help"
             print("Windows Assistant:-",g6)
             speechtx(g6)
        elif "amazon" in d1:
             webbrowser.open("https://www.amazon.in/?&tag=googhydrabk1-21&ref=pd_sl_drjtlom86_e&adgrpid=155259811873&hvpone=&hvptwo=&hvadid=678802104365&hvpos=&hvnetw=g&hvrand=1846329315827634926&hvqmt=e&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=1007788&hvtargid=kwd-31596400&hydadcr=5623_2412638")     
             g7 = "opening amazon"
             print("Windows Assistant:-",g7)
             speechtx(g7)
        elif "flipkart" in d1:
             webbrowser.open("https://www.flipkart.com/")     
             g8 = "opening flipkart"
             print("Windows Assistant:-",g8)
             speechtx(g8)
        elif "shut down" in d1:
             st = 30
             speechtx("Shutting down in 30 seconds. Save your work.")
             time.sleep(st)
             os.system("shutdown /s /t 1")
             exit()   
        elif "system information" in d1:
            print("Fetching system information. Please wait.")
            speechtx("Fetching system information. Please wait.")
            GSI()   
        elif "internet speed" in d1:
            CIS()        
        elif "set reminder" in d1:
             Pr = int(input("Press:1 To Write your Reminder: "))

             if Pr==1:
                 os.startfile('C:\\Users\\GRAVITY\\Desktop\\AlarmEff\\Reminder.txt')

             r3,r2,r1 = input("Enter The Date:").split("/")    
             hr,min,sec = input("Enter The Time:").split(":")    
             shedule_date = datetime.date(int(r1),int(r2),int(r3))

             n = 1
             while n>0:
                 if time.localtime().tm_hour==int(hr) and time.localtime().tm_min==int(min) and time.localtime().tm_sec==int(sec) and datetime.date.today()==shedule_date:
                     os.startfile('C:\\Users\\GRAVITY\\Desktop\\AlarmEff\\Reminder.txt')
                     os.startfile('C:\\Users\\GRAVITY\\Desktop\\AlarmEff\\noti.wav')
                     break
             else:
                 n+=1       
        elif "open calculator" in d1:
             while True:
               calget = input("Enter what you want to do 1) Multiplication(m) 2) Substraction(s) 3) Addition(a) 4) Division(d) Exit(e): ")
               if calget == 'm':
                    m1 = int(input("Enter first digit: "))
                    m2 = int(input("Enter second digit:"))
                    getm = m1*m2
                    print("Answer:-",getm)
               elif calget == 's':
                    s1 = int(input("Enter first digit: "))
                    s2 = int(input("Enter second digit:"))
                    gets = s1-s2
                    print("Answer:-",gets)
               elif calget == 'a':
                    a1 = int(input("Enter first digit: "))
                    a2 = int(input("Enter second digit:"))
                    geta = a1+a2
                    print("Answer:-",geta)
               elif calget == 'd':
                    d1 = int(input("Enter first digit: "))
                    d2 = int(input("Enter second digit:"))
                    getd = d1/d2
                    print("Answer:-",getd)
               elif calget == 'e':
                    exit()
               else:
                    g4 = "invaild Sentax"
                    print(g4)
                    speechtx(g4)
                    exit()
        elif "weather" in d1:
               url = f"http://api.weatherapi.com/v1/current.json?key=21fe31d86a7f431f83e60717232611&q=Pune&aqi=no"

               r = requests.get(url)
               wdic = json.loads(r.text)          
               info1 = wdic["current"]["temp_c"]
               info2 = wdic["current"]["temp_f"]
               info3 = wdic["current"]["condition"]["text"]
               info4 = wdic["current"]["last_updated"]

               outp = f"The Temperature of Pune city is celcius:{info1} and feranite:{info2}"
               outp1 = f"It's {info3} Weather!"
               outp2 = f"Last Updated on {info4}"

               print(outp)
               speechtx(outp)
               print(outp1)
               speechtx(outp1)
               print(outp2)
               speechtx(outp2)
        elif "alarm" in d1:
             print("1) Moring Birds\n2)itel Ringtone\n3)saaho BGM\n4)Cool Ringtone\n5)Happy Day Ringtone")
             inp = int(input("Select Your Ringtone: "))

             c,b,a = input("Enter the date: ").split("/")
             hr,min,sec = input("Enter the time: ").split(":")
             shedule_date = datetime.date(int(a),int(b),int(c))

             n = 1
             while n>0:
              if time.localtime().tm_hour==int(hr) and time.localtime().tm_min==int(min) and time.localtime().tm_sec==int(sec) and datetime.date.today()==shedule_date:
                   if inp==1:
                    os.startfile('C:\\Users\\GRAVITY\\Desktop\\AlarmEff\\morning_birds.mp3')
                   elif inp==2:
                    os.startfile('C:\\Users\\GRAVITY\\Desktop\\AlarmEff\\itel.mp3')
                   elif inp==3:
                    os.startfile('C:\\Users\\GRAVITY\\Desktop\\AlarmEff\\saaho.mp3')
                   elif inp==4:
                    os.startfile('C:\\Users\\GRAVITY\\Desktop\\AlarmEff\\cool.mp3')
                   elif inp==5:
                    os.startfile('C:\\Users\\GRAVITY\\Desktop\\AlarmEff\\Happy Day.mp3')    
                   break
              else:
                   n+=1

          #except requests.exceptions.RequestException:
          #     print("An error occurred. Please check your internet connection and try again.")
          #     e1 = "An error occurred. Please check your internet connection and try again."
          #     speechtx(e1)

         #except json.JSONDecodeError:
         #      print("Try Connecting to the internet")            
          #     e3 = "Try Connecting to the internet"
          #     speechtx(e3)                              #Add error Exception
         #except KeyError:
         #      print("--INTERNET ERROR--\nPlease Try Again")     
         #      e2 = "--INTERNET ERROR-- Please Try Again"
          #     speechtx(e2)
         #except Exception:
         #      print("--Exit--")
        elif "news" in d1:
               newsapi = f"https://newsapi.org/v2/top-headlines?country=in&apiKey=7c6050b27c044eee875133eed545b47e"

               r = requests.get(newsapi)
               ndic = json.loads(r.content)

        #for i in range():
               num_articles = len(ndic["articles"])

               # Randomly select an index
               random_index = random.randint(0, num_articles - 1)

               # Access the article at the randomly selected index
               n1 = ndic["articles"][random_index]["title"]
               n2 = ndic["articles"][random_index]["url"]
               n3 = ndic["articles"][random_index]["publishedAt"]
               
               getn = f"Title:\n{n1}"
               getn1 = f"URL:{n2}"
               getn2 = f"Publised At:{n3}"
               print(getn)
               speechtx(getn)
               print(getn1)
               print(getn2)
               speechtx(getn2)
    
    #Add calculator program (Make it advance)
    #Add news update program                          
    #Add more Conversation Program
    
    
    #else:
    #    print("you can call me as technobot")    













