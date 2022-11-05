import feedparser
import json
import time
import win32api
import os
from datetime import datetime

checkLoop = True
os.system("cls")

dt = datetime.now()
current_time = dt.strftime("%H:%M:%S")

hours = 0

# Create a new .json file if not exist
onePiece = feedparser.parse('https://www.japscan.me/rss/one-piece/')
    
titleLast = onePiece.entries[0].title
linkLast = onePiece.entries[0].link
dateLast = onePiece.entries[0].published

onePieceLast = {
    "title": titleLast,
    "link": linkLast,
    "date": dateLast,
}

file = open("save.json", "w+") 
json.dump(onePieceLast, file, indent = 4)
file.close()

# loop
while checkLoop:
    onePiece = feedparser.parse('https://www.japscan.me/rss/one-piece/')
      
    # Lecture des infos dans save.json

    with open('save.json', 'r') as f:
        onePieceCheck = json.load(f)

    
    # Verif si les infos du json sont identique au infos du RSS 
    if onePieceCheck['title'] == titleLast:
        if onePieceCheck['link'] == linkLast:
            print("\nNothing new appear !")
            print("Spent time : ", hours, "H")
            print("Since : ", current_time)
    else:
        print("\nNEW SCAN !\n")
        print("Last release : " + titleLast + "\nLink : " + linkLast + "\nDate : " + dateLast)
        win32api.MessageBox(0, 'LAST SCAN : ' + titleLast, 'ONE PIECE SCAN ALERT')
        checkLoop = False
        

    # Dump des infos du last scan dans save.json

    file = open("save.json", "w") 
    json.dump(onePieceLast, file, indent = 4)
    file.close()
     
    # 1h delay = 3600
    time.sleep(3600)
    hours += 1
    
