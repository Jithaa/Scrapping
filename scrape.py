import requests
from bs4 import BeautifulSoup
import re
class rec():
    def cases(self,n,k):
        if k=="in":
            r=requests.get('https://www.worldometers.info/coronavirus/country/India')
            r=r.text
            soup=BeautifulSoup(r,"html.parser")
            p=soup.title
            b=soup.find_all('span')
            b=str(b)
            b=re.sub(",","",b)
            temp = re.findall(r'\d+', b)
            res= list(map(int, temp))
            self.n=n
            res1=int(res[self.n])
            return(res1)
        else:
            r=requests.get('https://www.worldometers.info/coronavirus')
            r=r.text
            soup=BeautifulSoup(r,"html.parser")
            p=soup.title
            b=soup.find_all('span')
            b=str(b)
            b=re.sub(",","",b)
            temp = re.findall(r'\d+', b)
            res= list(map(int, temp))
            self.n=n
            res1=int(res[self.n+1])
            print(res)
            return(res1)
    


