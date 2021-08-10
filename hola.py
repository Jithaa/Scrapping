import requests
from bs4 import BeautifulSoup
import re

website=[]
img=[]
title=[]

class news():
    def main(self,com):
        self.com=com
        if self.com=="news":
            urll = "https://www.bing.com/news"
            response = requests.request("GET", urll)
            response=response.text
            soup=BeautifulSoup(response,"html.parser")
            b=soup.find_all('a')
            for link in b:
                if 'href' in link.attrs:
                    b=str(link.attrs['href'])+"\n"
                    if b.startswith('https://'):            
                        website.append(b)
                        r=requests.get(b)
                        r=r.text
                        soup=BeautifulSoup(r,"html.parser")
                        tt=soup.title
                        tt=str(tt)
                        no=len(tt)
                        title.append(tt[7:no-8])
                        k=soup.find('span',{'class':'image',})
                        k=str(k)
                        for i in range (len(k)-3):
                            if i+2<len(k):
                                if k[i]=='s' and k[i+1]=='r' and k[i+2] =='c':
                                    k=k[i+5:]
                        for j in range (len(k)):
                            if j<len(k):
                                if k[j]=='"':
                                    k=k[:j]
                        img.append("https:"+k)
        return(img,website,title)