import requests
import pandas as pd 
from bs4 import BeautifulSoup as bs
import re
import numpy as np

b=input("Enter products name you want to scrap : ").split()
num_pages=int(input("Enter the number of pages you want to scrap"))
c=0
for m in b:
    lst=list()
    for n in range(1,num_pages+1):
        r2 = "https://www.flipkart.com/search?q="+str(m)+"&sort=popularity&page="+str(n)
        r = requests.get(r2)
        soup = bs(r.content)
        for i,j,k in zip(soup.find_all('div',class_='col col-7-12'),soup.find_all('ul',class_='vFw0gD'),soup.find_all('div',class_='_1vC4OE _2rQ-NK')):
            g=j.find_all('li',class_='tVe95H')
            p=list()
            for w in g:
                p.append(w.text)
            lst.append([(i.find_all('div',class_='_3wU53n')[0]).text,k.text]+p)
        print(str(c),"---> Complete :",str(n),"of",num_pages)
    df = pd.DataFrame(lst) #, columns = ['Name', 'Price','feature-1','feature-2','feature-3','feature-4','feature-5','feature-6','feature-7','feature-8','feature-9','feature-10']) 
    df.to_csv(b[c]+"_flip.csv")
    c+=1
    print(m)
