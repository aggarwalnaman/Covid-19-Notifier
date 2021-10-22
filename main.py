from plyer import notification
import requests
from bs4 import BeautifulSoup
import time
def notifyMe(title, message):
    notification.notify(
        title = title,
        message = message,
        app_icon = None ,
        timeout = 25
    )

def getData(url):
    r = requests.get(url)
    return r.text

if __name__ == "__main__":
    # notifyMe("Indians","Lets Stop the spread of corona virus togethor")
#     https://github.com/utkarsh1810/To-Do_React_App
    myHtmlData = getData('https://www.mohfw.gov.in/')

    soup = BeautifulSoup(myHtmlData, 'html.parser')
    myDataStr=""
    for tr in soup.find_all('tbody')[0].find_all('tr'):
        # for td in soup.tr.find_all('td'):
        myDataStr += tr.get_text()
        myDataStr += "\n"
    # print(str(myDataStr))
    myDataStr=myDataStr[1:]
    itemList=myDataStr.split("\n\n\n")
    # print(itemList)
    states = ['Chandigarh','Uttarakhand','Uttar Pradesh','Haryana','Delhi']
    for item in itemList[0:27]:
        dataList = item.split("\n")
        print(dataList)
        if dataList[1] in states:
            nText=f"STATE => {dataList[1]} \n Total : {dataList[2]}\n cured : {dataList[3]}\n Deaths : {dataList[4]} "
            notifyMe("Cases of Covid-19",nText)
            time.sleep(2)
            # print(nText)
            # print(nText)
            
        
