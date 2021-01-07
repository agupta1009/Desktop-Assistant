def speak(audio):
    engine.say(audio)
    engine.runAndWait()

name="Ankush"
age="21"
email_id="testsample1298@gmail.com"
email_id_password="testsample50@"
gender="Sir"
city="Ludhiana"
friend="ankushsood50@gmail.com"

def twilio_send_msg(query):
    
    account_sid = 'AC204227098e9aa29d2ea6fa618f80ca2'
    auth_token = '4c71aba7fee49a49f90287807c58fb52'


    client = Client(account_sid,auth_token)

    contact=query
    try:
        if "ankush" in contact:
            to="+918872688104"

        elif "hiten" in contact:
            to ="+919023414886"

        else:
            to='+918872688104'
    
    except: 
        pyttsx3.speak(f"No contact named in my database")

    try:
        pyttsx3.speak("please say me the content")
        body = get_audio()

        client.messages.create(body=body,
                        from_='+12513252356',
                        to=to
                    )    
        pyttsx3.speak("Message sent")

    except:
        pyttsx3.speak("Faliure in sending message")

def twilio_call(query):

    account_sid = 'AC204227098e9aa29d2ea6fa618f80ca2'
    auth_token = '4c71aba7fee49a49f90287807c58fb52'


    client = Client(account_sid,auth_token)

    contact=query
    try:
        if "ankush" in contact:
            to="+918872688104"

        elif "hiten" in contact:
            to ="+919023414886"

        else:
            to='+918872688104'
    
    except: 
        pyttsx3.speak("Hmmm seems like you have not registered the contact in my data base so I cant call")
    
    try:
        pyttsx3.speak(f"Trying to call")
        call = client.calls.create(url='http://demo.twilio.com/docs/voice.xml',
                            to=to,
                            from_='+12513252356'
                        )
    except:
        pyttsx3.speak("Eror")


def news():
    from bs4 import BeautifulSoup
    from urllib.request import urlopen
    import time 
    
    url = 'https://news.google.com/news/rss'
    
    client = urlopen(url)
    xml_data = client.read()
    client.close()
    
    soup = BeautifulSoup(xml_data,'xml')
    news_list = soup.find_all('item')
    news_list = news_list[0:3]
    msg=''
    for news in news_list:
        msg=msg+news.title.text+'\n'
    return ['News',msg]

def weather(city):
    from bs4 import BeautifulSoup
    import requests
    search = 'Weather in '+str(city)
    URL = f'https://www.google.com/search?&q={search}'
    r = requests.get(URL)
    soup = BeautifulSoup(r.text,'html.parser')
    temp = soup.find("div",class_='BNeawe')
    return ['Temperature of'+str(city),temp.text]

def battery_info():
    import psutil
    battery = psutil.sensors_battery()
    return ['battery information','charge = '+str(battery.percent),'battery plugged in: '+str(battery.power_plugged)]

def movie_info(movie_name):
    import imdb
    moviesDB = imdb.IMDb()
    movies = moviesDB.search_movie(movie_name)
    if(movies):
        id = movies[0].getID()
        movie = moviesDB.get_movie(id)
        # fetch details ...
        title = movie['title']
        year= movie['year']
        casting = movie['cast']
        actors = ", ".join(map(str,casting[0:5]))
        return ['Movie information of '+str(movie_name),'movie name: '+str(title),'movie make year: '+str(year),'movie actors: '+str(actors)]
    return ['Movie information of '+str(movie_name),'API not available']

def read():
    pg.hotkey("ctrl",'c')
    tobespoken=pyperclip.paste()
    pyttsx3.speak(tobespoken)
# 336RGV-TPYPWXQH6K
 
# def authenticate_google():
#     """Shows basic usage of the Google Calendar API.
#     Prints the start and name of the next 10 events on the user's calendar.
#     """
#     creds = None
#     if os.path.exists('calendar.pickle'):
#         with open('calendar.pickle', 'rb') as token:
#             creds = pickle.load(token)
#     if not creds or not creds.valid:
#         if creds and creds.expired and creds.refresh_token:
#             creds.refresh(Request())
#         else:
#             flow = InstalledAppFlow.from_client_secrets_file(
#                 'calendar.json', calendarscope)
#             creds = flow.run_local_server(port=0)
#         with open('calendar.pickle', 'wb') as token:
#             pickle.dump(creds, token)

#     service = build('calendar', 'v3', credentials=creds)

#     return service 


