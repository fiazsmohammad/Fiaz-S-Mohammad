import pyttsx3 
import speech_recognition as sr 
import datetime
import wikipedia
import webbrowser
import os
import calendar
import pywhatkit as kit
import requests
import json
import pyautogui
from time import sleep
import time 
import operator
import speedtest
import openai


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices[2].id)
engine.setProperty('voice', voices[2].id)
webbrowser.register('chrome', None, webbrowser.BackgroundBrowser("C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"))

openai.api_key = "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"




def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def get_news():

    with open('newsapikey.txt', 'r') as file:
        api_key = file.readline().strip()
    
    
    url = f'https://newsapi.org/v2/top-headlines?country=us&apiKey={api_key}'
    response = requests.get(url)
    data = json.loads(response.text)
    headlines = data['articles']
    return headlines
def speak_news():
    headlines = get_news()
    if headlines:
        for i, article in enumerate(headlines[:5], start=1):
            title = article['title']
            speak(f"News {i}: {title}")
    
    else:
        engine.say("Sorry, I couldn't fetch the news.")

def get_weather(city):
    with open('weatherapikey.txt', 'r') as file:
        api_key = file.readline().strip()
 
    url = f'http://api.weatherapi.com/v1/current.json?key={api_key}&q={city}'
    response = requests.get(url)
    weather_data = json.loads(response.text)

    if 'error' in weather_data:
            speak("Sorry, I couldn't find the weather for that city.")
    else:
        current_condition = weather_data['current']['condition']['text']
        temperature_celsius = weather_data['current']['temp_c']
        humidity = weather_data['current']['humidity']
        speak(f"The weather in {city} is {current_condition}. The temperature is {temperature_celsius} degrees Celsius. The humidity is {humidity}%.")

def chat_with_gpt(prompt):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=50,
        temperature=0.7,
        n=1,
        stop=None,
    )
    return response.choices[0].text.strip()


def today_date():
    now = datetime.datetime.now()
    date_now = datetime.datetime.today()
    week_now = calendar.day_name[date_now.weekday()]
    month_now = now.month
    day_now = now.day

    months = ["January","February","March","April","May","June","July","August","September","October","November","December"]

    ordinals = ["1st","2nd","3rd","4th","5th","6th","7th","8th","9th","10th","11th","12th","13th","14th","15th","16th","17th","18th","19th","20th","21st",
        "22nd","23rd","24th","25th","26th","27th","28th","29th","30th","31st"]

    return "Today is " + week_now + ", " + months[month_now - 1] + "," + ordinals[day_now - 1] + "."


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  

    speak("I am Eva. Your virtual assistant. How may I help you ?")       

def takeCommand():
    

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
        return query

    except Exception as e:
        print(e)    
        speak("Say that again please...")  
        return "None"
   
    
    return query

wishMe()
if __name__=="__main__" :

    while True:
    
        query = takeCommand().lower()

        
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            #print(results)
            speak(results)
        elif 'date' in query:
            get_today = today_date()
            speak(get_today)

        elif 'open youtube' in query:
            speak("Opening youtube")
            webbrowser.get("chrome").open("youtube.com")

        elif 'open google' in query:
            speak("Opening google")
            webbrowser.get("chrome").open("google.com")

        elif 'open stackoverflow' in query:
            speak("Opening stackoverflow")
            webbrowser.get("chrome").open("stackoverflow.com")   
        
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"The time is {strTime}")

        elif 'open facebook' in query:
            speak("opening facebook.com")
            webbrowser.get("chrome").open("facebook.com")
        elif 'open instagram' in query:
            speak("opening instagram.com")
            webbrowser.get("chrome").open("instagram.com")
        elif 'open twitter' in query:
            speak("opening twitter.com")
            webbrowser.get("chrome").open("twitter.com")
        elif 'open microsoft' in query:
            speak("opening microsoft.com")
            webbrowser.get("chrome").open("microsoft.com")
        elif 'open amazon' in query:
            speak("opening amazon.in")
            webbrowser.get("chrome").open("amazon.in")
        
        elif "open notepad" in query:
            speak("opening notepad")
            os.system("notepad.exe")
        elif "open edge" in query:
            speak("opening microsoft edge")
            edge_path="C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe"
            os.startfile(edge_path)
        elif "open chrome" in query:
            speak("opening google chrome")
            chrome_path="C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"
            os.startfile(chrome_path)
        elif "open brave" in query:
            speak("opening brave browser")
            brave_path="C:\\Program Files\\BraveSoftware\\Brave-Browser\\Application\\brave.exe"
            os.startfile(brave_path)
        
        elif "open driver booster" in query:
            speak("opening driver booster")
            driver_path="C:\\Program Files (x86)\\IObit\Driver Booster\\10.3.0\\DriverBooster.exe"
            os.startfile(driver_path)
            
            
        elif "open visual studio code" in query:
            speak("opening visual studio code")
            code_path=("E:\\Microsoft VS Code\\Code.exe")
            os.startfile(code_path)
        elif "open pc manager" in query:
            speak("opening pc manager")
            pc_path=("C:\\Program Files\\Microsoft PC Manager\\MSPCManager.exe")
            os.startfile(pc_path)
        elif "open samsung dex" in query:
            speak("opening samsung dex")
            dex_path="C:\\Program Files (x86)\\Samsung\\Samsung DeX\\SamsungDeX.exe"
            os.startfile(dex_path)
        elif "open epic games" in query:
            speak("opening epic games launcher")
            epic_path="A:\\Epic Games\\Launcher\\Portal\\Binaries\\Win32\\EpicGamesLauncher.exe"
            os.startfile(epic_path)
        elif "open excel" in query:
            speak("opening microsoft excel")
            excel_path="C:\\Program Files (x86)\\Microsoft Office\\root\\Office16\\EXCEL.EXE"
            os.startfile(excel_path)
        elif "open powerpoint" in query:
            speak("opening microsoft powerpoint")
            ppt_path="C:\\Program Files (x86)\\Microsoft Office\\root\\Office16\\POWERPNT.EXE"
            os.startfile(ppt_path)
        elif "open word" in query:
            speak("opening microsoft word")

            word_path="C:\\Program Files (x86)\\Microsoft Office\\root\\Office16\\WINWORD.EXE"
            os.startfile(word_path)

        elif "search on google" in query.lower():
            query = query.lower().replace("search on google ", "")
            kit.search(query)
            speak("Searching on Google for: " + query)
        elif "search on youtube" in query.lower():
            query = query.lower().replace("search on youtube ", "")
            kit.playonyt(query)
            speak("Searching on YouTube for: " + query)

        elif "read news" in query.lower() or "news" in query.lower():
            speak("Latest news headlines are")
            speak_news()

        elif 'exit' in query.lower() or 'quit' in query.lower():
            speak('Sure, goodbye!, Have a nice day!')
            exit()
        elif 'weather' in query.lower():
            city = query.split('weather in ')[1]
            get_weather(city)

        elif 'play' in query or 'can you play' in query or 'please play' in query:
            speak("OK! here you go!!")
            query = query.replace("play", "")
            query = query.replace("can you play", "")
            query = query.replace("please play", "")
            webbrowser.open(f'https://open.spotify.com/search/{query}')
            sleep(3)
            pyautogui.click(x=519, y=448)
        elif 'who created you' in query.lower():
            speak(" I was created by a team of developers consisting of Gokul, Dona, Benita and Fiaz.")
        elif "shutdown the system" in query:
        
            os.system("shutdown /s /t 5")
        elif "restart the system" in query:
            os.system("shutdown /r /t 5")
        elif "lock the system" in query:
            os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")
        elif "open command prompt" in query:
            os.system("start cmd")
        elif "take screenshot" in query:
            speak('tell me a name for the file')
            name = takeCommand().lower()
            time.sleep(3)
            img = pyautogui.screenshot() 
            img.save(f"{name}.png") 
            speak("screenshot saved")
        elif "calculate" in query:
            r = sr.Recognizer()
            with sr.Microphone() as source:
                speak("Ready")
                print("Listening...")
                r.adjust_for_ambient_noise(source)
                audio = r.listen(source)
            my_string=r.recognize_google(audio)
            print(my_string)
            def get_operator_fn(op):
                return {
                    '+' : operator.add,
                    '-' : operator.sub,
                    'x' : operator.mul,
                    'divided' : operator.truediv,
                }[op]
            def eval_bianary_expr(op1,oper, op2):
                op1,op2 = int(op1), int(op2)
                return get_operator_fn(oper)(op1, op2)
            speak("your result is")
            speak(eval_bianary_expr(*(my_string.split())))
        elif "volume up" in query:
            pyautogui.press("volumeup")
            pyautogui.press("volumeup")
            pyautogui.press("volumeup")
            pyautogui.press("volumeup")
            pyautogui.press("volumeup")
            pyautogui.press("volumeup")
            pyautogui.press("volumeup")
            pyautogui.press("volumeup")
            pyautogui.press("volumeup")
            pyautogui.press("volumeup")
            pyautogui.press("volumeup")
            pyautogui.press("volumeup")
 
        elif "volume down" in query:
            pyautogui.press("volumedown")
            pyautogui.press("volumedown")
            pyautogui.press("volumedown")
            pyautogui.press("volumedown")
            pyautogui.press("volumedown")
            pyautogui.press("volumedown")
            pyautogui.press("volumedown")
            pyautogui.press("volumedown")
            pyautogui.press("volumedown")
            pyautogui.press("volumedown")
            pyautogui.press("volumedown")
            pyautogui.press("volumedown")
            pyautogui.press("volumedown")
            pyautogui.press("volumedown")
            pyautogui.press("volumedown")
        elif "mute" in query:
            pyautogui.press("volumemute")
        elif "internet speed" in query:
                wifi  = speedtest.Speedtest()
                upload_net = wifi.upload()/1048576         #Megabyte = 1024*1024 Bytes
                download_net = wifi.download()/1048576
                    
                speak(f"Wifi download speed  in mbps is {download_net}")
                speak(f"Wifi Upload speed  in mbps is {upload_net}")
        elif "click my photo" in query:
                pyautogui.press('win')
                pyautogui.typewrite('camera')
                pyautogui.press('enter')

    
                time.sleep(5)

    
                speak("Say cheese!")

    
                pyautogui.press('enter')

    
                time.sleep(4)

    
                pyautogui.press('enter')
        elif "chat" in query.lower():
            print("Assistant: Sure! Please provide the chat prompt.")
            speak("Sure! Please provide the chat prompt.")
            

            try:
                prompt = takeCommand()
                response = chat_with_gpt(prompt)
                print("Assistant:", response)
                speak(response)
            except Exception as e:
                print("Sorry, there was an error during the chat. Please try again.")
                speak("Sorry, there was an error during the chat. Please try again.")
        elif "who are you" in query or "what is your name?" in query:
            speak("I am Eva, your virtual assistant. I can do various tasks like playing videos on youtube, google search, opening apps, shutting down the system etc. How may i assist you ?")

        


        else :

            speak("I didnt get you")






   




        

        

        

        

