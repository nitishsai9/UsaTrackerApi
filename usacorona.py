from bs4 import BeautifulSoup as bs
from urllib.request import urlopen as ur
import requests
import json

URL='https://www.worldometers.info/coronavirus/country/us/'
headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'}
page=requests.get(URL,headers=headers)
soup=bs(page.content,'html.parser')



f={
    "Main":[]
}
ss=[]
mains=soup.findAll("div", {"id": "maincounter-wrap"} )
for i in mains:
    ss.append(i.find("span").text)
cocu,dea,rec=ss
f["Main"].append({
    "CoronaCases":cocu,
    "CoroanDeaths":dea,
    "recoverd":rec
})













tables=soup.find('table')
rows = tables.find_all('tr')
d={
    "Corona":[]
    }
tot=[]
for row in rows:
    cols=row.find_all('td')
    z=['0' if v.text.strip() == "" else v.text.strip() for v in cols]
    tot.append(z)

for i in tot:
    if len(i)==7:
        st,tc,nc,totd,newd,acc,su=i
        d['Corona'].append({
            "stateName":st,
            "totalCases":tc,
            "newCases":nc,
            "totaldeaths":totd,
            "newdeaths":newd,
            "ActiveCase":acc,

        })
        
         

