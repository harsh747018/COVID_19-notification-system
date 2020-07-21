from plyer import notification
import requests
from bs4 import BeautifulSoup
import time

def notifyMe(title, message):
    notification.notify(
        title= title,
        message =message,
        app_icon =None,
        timeout = 10
    )

def getdata(url):
    r= requests.get(url)
    return r.text


if __name__== "__main__":
    
    while True:
        #notifyMe("Harsh","Lets stop the spread of this virus")
        myHtmlData = getdata('https://www.mohfw.gov.in/')
    

        soup = BeautifulSoup(myHtmlData, 'html.parser')

        #print(soup.prettify())

        myDatastr=""

        for tr in soup.find_all('tbody')[0].find_all('tr'):
            myDatastr += tr.get_text()
    
        myDatastr=myDatastr[1:]
        itemlist=myDatastr.split("\n\n")

        states=['Delhi','Uttar Pradesh','Karnataka']
        for item in itemlist[0:34]:
            datalist=item.split('\n')
            if datalist[1] in states: 
                nTitle = 'Cases of Covid-19'
                nText =f"State:{datalist[1]} \n Indian: {datalist[2]} Foriegn: {datalist[3]} \n Deaths: {datalist[4]}\n Cured: {datalist[5]}"
                notifyMe(nTitle,nText)

    time.sleep(3600)
            


    



