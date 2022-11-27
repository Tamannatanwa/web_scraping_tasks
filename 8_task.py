# import requests
# import json
# from bs4 import BeautifulSoup
# rel=requests.get("https://www.imdb.com/title/tt0066763/")
# soup=BeautifulSoup(rel.text,"html.parser")
# con=soup.find('script',type='application/ld+json').text
# a=json.loads(con)
# dic={}
# for i in a:
#     if i=="url":
#         dic['id']=a[i]
# with open ("8_task.json","w") as file:
#     json.dump(dic,file,indent=8)







import requests
import json
from bs4 import BeautifulSoup
import os


with open('1_task.json','r') as f:
    a1=json.load(f)
n=1
url=[]
for i in a1:
    url.append(i['url'])
    print(n,i['name'])
    n=n+1
choose=int(input("enter the id:-"))-1
id=url[choose][-10:-1]
file=id+'.json'
page=requests.get(url[choose])
soup=BeautifulSoup(page.text,"html.parser")
con=soup.find('script',type='application/ld+json').text
e=soup.find("li",attrs={"data-testid":"title-details-languages"}).a.get_text()
a=json.loads(con)
dic={}
for i in a:
    dic['name']=a['name']
    dic['director']=[a['director'][0]['name']]
    dic['image']=a['image']
    dic['description']=a['description']
    dic["language"]=e
    dic['genre']=a['genre']
    dic['country']='india'
with open(file,"w") as f:
    json.dump(dic,f,indent=8)
c=[]
m=1
for k in url:
    c.append(k[-10:-1])
    print(m,k[-10:-1])
    m+=1
choice=int(input("enter id:- "))-1
filename=c[choice]+'.json'
path='/home/anisha/web_scrapping/'
if os.path.exists(path+filename):
    with open(filename,"r") as f1:
        data=json.load(f1)
    print(data)   
else:
    print("file not exist")



