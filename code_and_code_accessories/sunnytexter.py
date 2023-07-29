import smtplib, requests, json, smtplib, datetime, yagmail
from bs4 import BeautifulSoup

############################################
#user info import from jsons
############################################

f = open("emailuser.json") #open user file
uinfo = json.load(f)       #load as dict
user = uinfo["user"]       #get user contact
device = uinfo["device"]   #device type
loc = uinfo["city"]        #location

############################################
#scrape weather off internet using user info
############################################
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
city=loc+" weather"
city=city.replace(" ","+")
res = requests.get(f'https://www.google.com/search?q={city}&oq={city}&aqs=chrome.0.35i39l2j0l4j46j69i60.6128j1j7&sourceid=chrome&ie=UTF-8',headers=headers) 
soup = BeautifulSoup(res.text,'html.parser')   
info = soup.select('#wob_dc')[0].getText().strip()
    
############################################
#use info to write message to send #########
############################################
if info == "Sunny":
    content = "It's sunny right now in "+loc+"!"
else:
    content = "It's still cloudy outside in "+loc+". Keep your chin up!"
    
subject = str(datetime.date.today())+": Sunny Update!"


############################################
#use info to write message to send #########
############################################

#login for email that sends out message
f = open("gmail.json")
ginfo = json.load(f)
email = ginfo["user"]
pas = ginfo["password"]

#send message accordingly if email or text
if device == "phone":
    sms_gateway = user
    smtp = "smtp.gmail.com" 
    port = 587
    # This will start our email server
    server = smtplib.SMTP(smtp,port)
    # Starting the server
    server.starttls()
    # Now we need to login
    server.login(email,pas)
    body = content
    server.sendmail(email,sms_gateway,body)
# lastly quit the server
    server.quit()
elif device == "email":
    with yagmail.SMTP(email, pas) as yag:
        yag.send(user, subject, content)
    
print('done')