from os import system
system("pip3 install bs4")
import requests
from time import sleep
from bs4 import BeautifulSoup
from urllib import parse as Encode1
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

def internet_on():
    try:
        requests.get('http://ipinfo.io/ip')
        return True
    except: return False

while True:
    try:
        ip = str(requests.get("http://ipinfo.io/ip").text)

        Mn_urls = str(requests.get("https://raw.githubusercontent.com/AnkurKumarji/Machine/feat/add-feedback-section/Zagl.Links").text).splitlines()
        Selected_Link = str(requests.get("https://Armitage.ankurkumar8.repl.co/").text).split(".")
        if int(Selected_Link[1]) >= len(Mn_urls):
            requests.get("https://Armitage.ankurkumar8.repl.co/reset.php");Selected_Url = Mn_urls[0].replace("zee.gl","za.gl")
        else:
            Selected_Url = Mn_urls[int(Selected_Link[1])].replace("zee.gl","za.gl")

        req = requests.Session()
        useragent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36"

        headers = {"user-agent": useragent,"accept": "text/html", "sec-fetch-site": "none", "sec-fetch-mode": "navigate", "sec-fetch-dest": "document","accept-language": "en-GB,en;q=0.9"}
        res1 = req.get(Selected_Url, headers=headers)
        soup = BeautifulSoup(res1.text, 'html.parser')
        Token = Encode1.quote(soup.find('input', {'name': '_Token[fields]'})['value'])
        Token_unlocked = Encode1.quote(soup.find('input', {'name': '_Token[unlocked]'})['value'])
        givenX = Encode1.quote(soup.find('input', {'name': 'givenX'})['value'])
        givenY = Encode1.quote(soup.find('input', {'name': 'givenY'})['value'])
        data = str(soup.find('button',{'id': 'greendot'}).find('img')['src']).split('png;base64,')[1]
        base64data = list(str(requests.post("https://ImageCord.ankurkumar8.repl.co",data=data).text).replace('[','').replace(']','').replace(' ','').split(','))


        headers = {'Host': 'za.gl','User-Agent': useragent,'Accept': 'text/html','Accept-Language': 'en-US,en;q=0.5','Accept-Encoding': 'gzip, deflate','Content-Type': 'application/x-www-form-urlencoded','Origin': 'https://za.gl','Referer': Selected_Url}
        data = f'_method=POST&_csrfToken={res1.cookies.get_dict()["csrfToken"]}&ref=&f_n=slc&dot=1&givenX={givenX}&givenY={givenY}&X={base64data[0]}&Y={base64data[1]}&_Token%5Bfields%5D={Token}&_Token%5Bunlocked%5D={Token_unlocked}'
        res2 = req.post(Selected_Url, headers=headers,data=data)
        soup = BeautifulSoup(res2.text, 'html.parser')
        ad_form = Encode1.quote(soup.find('input', {'name': 'ad_form_data'})['value'])
        Token = Encode1.quote(soup.find('input', {'name': '_Token[fields]'})['value'])
        Token_unlocked = Encode1.quote(soup.find('input', {'name': '_Token[unlocked]'})['value'])
        Cook = res1.cookies.get_dict()
        Cook.update(res2.cookies.get_dict())
        Cook.update({'ab':'2', 'ref':'adimin', 'sls':'0'})

        sleep(3)

        headers = {"accept": "application/json, text/javascript, */*; q=0.01", "x-requested-with": "XMLHttpRequest","user-agent": useragent,"content-type": "application/x-www-form-urlencoded; charset=UTF-8", "origin": "https://za.gl","sec-fetch-site": "same-origin", "sec-fetch-mode": "cors", "sec-fetch-dest": "empty","referer": Selected_Url}
        cookies = {"AppSession": Cook['AppSession'],"zagl_publisher": Cook['zagl_publisher'],"scr": Cook['scr'],"csrfToken": Cook['csrfToken'],"visitor": Cook['visitor'],"hash": Cook['hash'],"sls": "0","ref": "admin","browserprint": "8b009e12f3bad328ce10f5803a223ca11621cb5cdb5a207dca519f2e50565610","overlay": "1","ab": "2","sb_main_29b552ac181cd0b221e0fcc9e06f6754": "1","slv": "-1","sb_count_29b552ac181cd0b221e0fcc9e06f6754": "1"}
        data = f"_method=POST&_csrfToken={Cook['csrfToken']}&ad_form_data={ad_form}&_Token%5Bfields%5D={Token}&_Token%5Bunlocked%5D={Token_unlocked}"
        mn_req = requests.post("https://za.gl/links/go", headers=headers, cookies=Cook, data=data, timeout=3)
        if "success" in mn_req.text: print('Req1 Done..',ip)

        while True:
            new_ip = str(requests.get("http://ipinfo.io/ip").text)
            if new_ip != ip:break
    except:
        while True:
            if internet_on() == True:break
            sleep(2)
