import time
from datetime import datetime
from playsound import playsound
import os

try:
    class User:
        users = {
            }
        
        def login(objects1):
            for i in objects1:
                if i.user1==User_first and i.pass1==Pass_first:
                    return i
        
        def signup(objects1):
            User.users[User_first]=Pass_first
            a=User(User_first,Pass_first)
            objects1.append(a)
            return a
            
        def __init__(self,user1,pass1):
            self.user1=user1
            self.pass1=pass1
            self.tasks=[]
            self.websites = []
            
        def web_block(self):
            if not self.websites == []:
                print("\n Your Websites ----------> \n")
                for i in self.websites:
                    print(">>>", i)
                inp = input("\n Would you like to make a new list of websites (y / n) ---------->\n>>> ").lower()
                if inp=="y":
                    self.websites = []
                    
            if self.websites == []:
                while True:
                    
                    choi = input("\n Add site? (y/ n) ---------->\n>>> ").lower()
                    
                    if choi == "y":
                        temp = input("\n Please enter website to block ---------->\n>>> ")
                        self.websites.append(temp)
                    
                    
                    elif choi == "n":
                        break
            
            send_to = "127.0.0.1"

            host = r"C:\Windows\System32\drivers\etc\hosts"

            file = open(host, "r+")
            content = file.read()
            
            for i in self.websites:
                if i not in content:
                    file.write(send_to+" "+i+'\n')
                    
            file.close()
            
            print()
            os.system("taskkill /F /IM msedge.exe")
            print()
            
            next = input("** Blocking Started **")
                    
        def stop_web_block(self):
            
            host = r"C:\Windows\System32\drivers\etc\hosts"
            
            file = open(host, "r+")
            content = file.readlines()
            
            file.seek(0)
            for i in content:
                flag=True
                for j in self.websites:
                    if j in i:
                        flag=False
                        break
                if flag:
                    file.write(i)
            file.truncate()
            file.close()
            
        def alarm(self):
            date1 = input("\n Enter date in format YYYY-MM-DD ----------> \n>>> ")
            time1 = input("\n Enter time in 24 hour format HH:MM:SS ----------> \n>>> ")
            
            print("** sleeping... **")
            
            
            while True:
                try:
                    if date1 == str(datetime.now().date()) and time1 == str(datetime.now().time())[:8]:
                        
                        # print(str(datetime.now().date()), str(datetime.now().time()))
                        print(("_"*36).center(130))
                        print("|    █ █ █ ▄▀▄ █▄▀ █▀▀    █ █ █▀█    |".center(130)) 
                        print("|    ▀▄▀▄▀ █▀█ █ █ ██▄    █▄█ █▀▀    |".center(130)) 
                        print(("_"*36).center(130))
                        playsound(r"./audio.wav")
                        break
                except KeyboardInterrupt:
                    break
                            
            next = input("** Time To Wake Up **")

                
        def pom_time(self):
            while True:
                try:
                    long1 = int(input("\n Enter Work period in Min ---------->\n>>> "))
                    short1 = int(input("\n Enter Break period in Min ---------->\n>>> "))
                    session = int(input("\n How Many Sessions ---------->\n>>> "))
                    break
                except:
                    print("** Enter Valid Index **")
                    continue
            
            for i in range(session):
                try:
                    print(("_"*46).center(130))
                    print("|    █ █ █ █▀█ █▀█ █▄▀    ▀█▀ ▀█▀ █▄ ▄█ █▀▀    |".center(130))
                    print("|    ▀▄▀▄▀ █▄█ █▀▄ █ █     █  ▄█▄ █ ▀ █ ██▄    |".center(130))
                    print(("_"*46).center(130))
                    
                    time.sleep(long1*60)
                    playsound(r"./audio.wav")
                    
                    
                    
                    print(("_"*48).center(130))
                    print("|    █▄▄ █▀█ █▀▀ ▄▀▄ █▄▀    ▀█▀ ▀█▀ █▄ ▄█ █▀▀    |".center(130)) 
                    print("|    █▄█ █▀▄ ██▄ █▀█ █ █     █  ▄█▄ █ ▀ █ ██▄    |".center(130)) 
                    print(("_"*48).center(130))
                    
                    time.sleep(short1*60)
                    playsound(r"./audio.wav")
                except KeyboardInterrupt:
                    break
                           
            next = input("** Session Over **")
            
        # def todo(self):
            
        def add_task(self):
            a = input("\n Enter Task ---------->\n>>> ")
            self.tasks.append([a,False])
            next = input("** New task Added **")
                    
        def remove_task(self):
            if self.tasks == []:
                next = input("** List Empty **")
            else:
                while True:
                    try:
                        a = int(input("\n Select Index of Task to Remove ---------->\n>>> "))
                        if a<1:
                            print("** Enter Valid Index **")
                            continue
                        try:                
                            self.tasks.pop(a-1)
                            next = input("** Task Removed **")
                            break
                        except:
                            print("** Enter Valid Index **")
                            continue
                    except:
                        print("** Enter Valid Index **")
                        
        def comp_tasks(self):
            if self.tasks == []:
                next = input("** List Empty **")
            else:
                while True:
                    try:
                        a = int(input("\n Enter Index of Completed Task ---------->\n>>> "))
                        if a<1:
                            print("** Enter Valid Index **")
                            continue
                        try:
                            self.tasks[a-1][1] = True
                            next = input("** Task Completed **")
                            break
                        except:
                            print("** Enter Valid Index **")
                            continue
                    except:
                        print("** Enter Valid Index **")
                    
        def show(self):
            for i in range(len(self.tasks)):
                print(f"{i+1}. {self.tasks[i][0]} : {chr(9745) if self.tasks[i][1] else chr(9633)}".center(130))
            
            next = input("****")
                        
                    
    things=[]
    while True:
        
        print(" "+"_"*130)
        print("|"+"█   █ █████ █      ████  ███  █   █ █████            █████  ███ ".center(130)+"|") 
        print("|"+"█   █ █     █     █     █   █ ██ ██ █                  █   █   █".center(130)+"|") 
        print("|"+"█ █ █ ████  █     █     █   █ █ █ █ ████               █   █   █".center(130)+"|") 
        print("|"+"██ ██ █     █     █     █   █ █   █ █                  █   █   █".center(130)+"|") 
        print("|"+"█   █ █████ █████  ████  ███  █   █ █████              █    ███ ".center(130)+"|")
        print("|"+" "*130+"|")
        print("|"+" "*130+"|")
        print("|"+"█████  ███  █████ █  █  █   █  ███  █████ █████ █████ ████ ".center(130)+"|")
        print("|"+"  █   █   █ █     █ █   ██ ██ █   █ █       █   █     █   █".center(130)+"|")
        print("|"+"  █   █████ █████ ██ █  █ █ █ █████ █████   █   ████  ████ ".center(130)+"|")
        print("|"+"  █   █   █     █ █  █  █   █ █   █     █   █   █     █   █".center(130)+"|")
        print("|"+"  █   █   █ █████ █   █ █   █ █   █ █████   █   █████ █   █".center(130)+"|")
        print(" "+"_"*130)

    
        
        a=0
        while True:
            
            print(("_"*67).center(130))
            print("|    █   █▀█ █▀▀    ▀█▀ █▄ █    |    █▀▀ ▀█▀ █▀▀ █▄ █    █ █ █▀█    |".center(130))
            print("|    █▄▄ █▄█ █▄█    ▄█▄ █ ▀█    |    ▄██ ▄█▄ █▄█ █ ▀█    █▄█ █▀▀    |".center(130))
            print(("_"*67).center(130))
            
            
            choi = input("\n Type LOGIN / SIGNUP ----------> \n>>> ").lower()
            
            if choi == "login":
                User_first = input("\nEnter Username ----------> \n>>> ")
                Pass_first = input("\nEnter Password ----------> \n>>> ")
                
                if User_first in User.users and Pass_first==User.users[User_first]:
                    a = User.login(things)
                    break
                else:
                    next = input("** No Such User Exists **")
                    
            elif choi == "signup":
                
                User_first = input("\nEnter Username ----------> \n>>> ")
                Pass_first = input("\nEnter Password ----------> \n>>> ")
                
                if User_first in User.users:
                    next = input("** User Already Exists **")
                else:
                    a = User.signup(things)
                    break
                
                
        while True:
            
            print(("_"*56).center(130))
            print("|    ▄▀▄ █▀█ █▀█ █   ▀█▀ █▀▀ ▄▀▄ ▀█▀ ▀█▀ █▀█ █▄ █ █▀▀    |".center(130)) 
            print("|    █▀█ █▀▀ █▀▀ █▄▄ ▄█▄ █▄▄ █▀█  █  ▄█▄ █▄█ █ ▀█ ▄██    |".center(130)) 
            print(("_"*56).center(130))

            print()
            print("1 WEB BLOCKER".center(130))

            print()
            print("2 ALARM".center(130))

            print()
            print("3 POMODORO TIMER".center(130))

            print()
            print("4 TODO LIST".center(130))
            
            print()
            print("5 EXIT".center(130))
                
            choi = input("\n Enter Application Number ---------->\n>>> ")
            if choi == "1":
                while True:
                    
                    print(("_"*53).center(130))
                    print("|    █ █ █ █▀▀ █▄▄      █▄▄ █   █▀█ █▀▀ █▄▀ █▀▀ █▀█   |".center(130))
                    print("|    ▀▄▀▄▀ ██▄ █▄█      █▄█ █▄▄ █▄█ █▄▄ █ █ ██▄ █▀▄   |".center(130))
                    print(("_"*53).center(130))

                    print()
                    print("1 START".center(130))

                    print()
                    print("2 STOP".center(130))

                    print()
                    print("3 EXIT".center(130))
                    
                    choi = input("\n Enter Choice Number ---------->\n>>> ")
                    if choi == "1":
                        a.stop_web_block()
                        a.web_block()
                    elif choi == "2":
                        a.stop_web_block()
            
                        next = input("** Blocking Stopped **")
                    elif choi == "3":
                        a.stop_web_block()
                        break
                    
            elif choi == "2":
                while True:
                    
                    print(("_"*29).center(130))
                    print("|    ▄▀▄ █   ▄▀▄ █▀█ █▄ ▄█    |".center(130)) 
                    print("|    █▀█ █▄▄ █▀█ █▀▄ █ ▀ █    |".center(130)) 
                    print(("_"*29).center(130))

                    print()
                    print("1 SET ALARM".center(130))

                    print()
                    print("2 EXIT".center(130))
                    
                    choi = input("\n Enter Choice Number ---------->\n>>> ")
                    if choi == "1":
                        a.alarm()
                    elif choi == "2":
                        break
                    
            elif choi == "3":
                while True:
                    
                    print(("_"*67).center(130))
                    print("|    █▀█ █▀█ █▄ ▄█ █▀█ █▀▄ █▀█ █▀█ █▀█     ▀█▀ ▀█▀ █▄ ▄█ █▀▀ █▀█    |".center(130)) 
                    print("|    █▀▀ █▄█ █ ▀ █ █▄█ █▄▀ █▄█ █▀▄ █▄█      █  ▄█▄ █ ▀ █ ██▄ █▀▄    |".center(130)) 
                    print(("_"*67).center(130))

                    print()
                    print("1 SET POMODORO TIMER".center(130))

                    print()
                    print("2 EXIT".center(130))
                    
                    
                    choi = input("\n Enter Choice Number ---------->\n>>> ")
                    if choi == "1":
                        a.pom_time()
                    elif choi == "2":
                        break
            
            elif choi == "4":
                while True:
                    
                    print(("_"*39).center(130))
                    print("|    ▀█▀ █▀█ █▀▄ █▀█ █   ▀█▀ █▀▀ ▀█▀    |".center(130)) 
                    print("|     █  █▄█ █▄▀ █▄█ █▄▄ ▄█▄ ▄██  █     |".center(130)) 
                    print(("_"*39).center(130))

                    print()
                    print("1 ADD TASK".center(130))

                    print()
                    print("2 REMOVE TASK".center(130))

                    print()
                    print("3 COMPLETE TASK".center(130))

                    print()
                    print("4 SHOW TASKS".center(130))

                    print()
                    print("5 EXIT".center(130))

                    
                    choi = input("\n Enter Choice Number ---------->\n>>> ")
                    if choi == "1":
                        a.add_task()
                    elif choi == "2":
                        a.remove_task()
                    elif choi == "3":
                        a.comp_tasks()
                    elif choi == "4":
                        a.show()
                    elif choi == "5":
                        break
            elif choi == "5":
                break
        
        
        
        hm = input("\n Do You Want to Exit (y / n) --------->\n>>> ").lower()
        if hm=="y":
            break
        
except KeyboardInterrupt:
    try:
        a.stop_web_block()
        print("\n ** Ctrl + C Pressed ** \n")
        print("\n ** Exiting Program... ** \n")
    except:
        print("\n ** Ctrl + C Pressed ** \n")
        print("\n ** Exiting Program... ** \n")