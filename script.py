import requests
from time import sleep
from urllib import parse as Encode1
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)


url = "https://za.gl/links/go"
#___________Url-Selector__________________
Mn_urls = str(requests.get("https://raw.githubusercontent.com/AnkurKumarji/Machine/feat/add-feedback-section/Zagl.Links").text).splitlines()
Selected_Link = str(requests.get("https://Armitage.ankurkumar8.repl.co/").text).split(".")

if int(Selected_Link[1]) >= len(Mn_urls):
    requests.get("https://Armitage.ankurkumar8.repl.co/reset.php");Selected_Url = Mn_urls[0]
else:
    Selected_Url = Mn_urls[int(Selected_Link[1])];print(len(Mn_urls), Selected_Link, Selected_Url)
#__________Url-Selector__________Finished


#__________Req1___________________________
headers = {"user-agent": "Mozilla/5.0 (Linux; Android 10; Redmi Note 8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.101 Mobile Safari/537.36","accept": "text/html", "sec-fetch-site": "none", "sec-fetch-mode": "navigate", "sec-fetch-dest": "document","accept-language": "en-GB,en;q=0.9"}
req1 = requests.get(Selected_Url, headers=headers)
Cook = req1.cookies.get_dict()
#__________Req1__________________Finished


#__________Var-Extract___________________
#_______Using_BS4__________
# from bs4 import BeautifulSoup
# soup = BeautifulSoup(req1.content, 'lxml')
# ad_form = Encode1.quote(soup.find('input', {'name': 'ad_form_data'})['value'])
# Token = Encode1.quote(soup.find('input', {'name': '_Token[fields]'})['value'])
# Token_unlocked = Encode1.quote(soup.find('input', {'name': '_Token[unlocked]'})['value'])

#_____Using_String Method___
ad_form = Encode1.quote(str(req1.text[str(req1.text).find('ad_form_data" value="')+21:str(req1.text).find('ad_form_data" value=')+450]).split('" />')[0])
Token = Encode1.quote(str(req1.text[str(req1.text).find('_Token[fields]" autocomplete="off" value="')+42:str(req1.text).find('_Token[fields]" autocomplete="off" value="')+200]).split('" />')[0])
Token_unlocked = Encode1.quote(str(req1.text[str(req1.text).find('_Token[unlocked]" autocomplete="off" value="')+44:str(req1.text).find('_Token[unlocked]" autocomplete="off" value="')+200]).split('" />')[0])
#__________Var-Extract___________Finished


sleep(3)


#__________Main-Request___________________
headers = {"accept": "application/json, text/javascript, */*; q=0.01", "x-requested-with": "XMLHttpRequest","user-agent": "Mozilla/5.0 (Linux; Android 10; Redmi Note 8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.101 Mobile Safari/537.36","content-type": "application/x-www-form-urlencoded; charset=UTF-8", "origin": "https://za.gl","sec-fetch-site": "same-origin", "sec-fetch-mode": "cors", "sec-fetch-dest": "empty","referer": Selected_Url, "accept-language": "en-GB,en;q=0.9"}
cookies = {"AppSession": Cook['AppSession'],"zagl_publisher": Cook['zagl_publisher'],"scr": Cook['scr'],"csrfToken": Cook['csrfToken'],"visitor": Cook['visitor'],"hash": Cook['hash'],"sls": "0","ref": "admin","browserprint": "8b009e12f3bad328ce10f5803a223ca11621cb5cdb5a207dca519f2e50565610","overlay": "1","ab": "2","sb_main_29b552ac181cd0b221e0fcc9e06f6754": "1","slv": "-1","sb_count_29b552ac181cd0b221e0fcc9e06f6754": "1","pbpr0tpuw4isk85t8yg3jb2lj5vqf": "wilfulpessimistic.com","_ga": "GA1.2.1726704085.1610002127","_gid": "GA1.2.394003706.1610002127","_gat_gtag_UA_120643151_1": "1"}
data = f"_method=POST&_csrfToken={Cook['csrfToken']}&ad_form_data={ad_form}&_Token%5Bfields%5D={Token}&_Token%5Bunlocked%5D={Token_unlocked}"
mn_req = requests.post(url, headers=headers, cookies=cookies, data=data)
#__________Main-Request__________Finished

print(mn_req.text)
