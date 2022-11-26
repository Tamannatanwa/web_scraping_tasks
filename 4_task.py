# import requests
# import json
# from bs4 import BeautifulSoup
# link1=requests.get("https://www.imdb.com/title/tt0066763/")
# soup=BeautifulSoup(link1.text,"html.parser")
# icon=soup.find('script',type='application/ld+json').text
# a=json.loads(icon)
# dic={}
# for i in a:
#     dic['name']=a['name']
#     dic['director']=[a['director'][0]['name']]
#     dic['image']=a['image']
#     dic['description']=a['description']
#     dic["language"]=a['review']['inLanguage']
#     dic['genre']=a['genre']
#     dic['country']='india'
# with open("4_task.json","w") as f:
#     json.dump(dic,f,indent=8)





import requests
import json
from bs4 import BeautifulSoup
c=[]
rel=requests.get("https://www.imdb.com/title/tt0066763/")
soup=BeautifulSoup(rel.text,"html.parser")
con=soup.find('script',type='application/ld+json').text
e=soup.find("li",attrs={"data-testid":"title-details-languages"}).a.get_text()
c.append(e)
a=json.loads(con)
dic={}
for i in a:
    dic['name']=a['name']
    dic['director']=[a['director'][0]['name']]
    dic['image']=a['image']
    dic['description']=a['description']
    dic["language"]=c
    dic['genre']=a['genre']
    dic['country']='india'
with open("4_task.json","w") as f:
    json.dump(dic,f,indent=8)








# import requests,json
# from bs4 import BeautifulSoup
# def scrap_movie_details():
#     page=requests.get("https://www.imdb.com/title/tt0066763/")
#     soup=BeautifulSoup(page.text,"html.parser")
#     c=soup.find("div",class_="sc-80d4314-1 fbQftq").h1.get_text()
#     # print(c)
#     d=soup.find("div",class_="ipc-metadata-list-item__content-container").a.get_text()
#     # print(d)
#     e=soup.find("li",attrs={"data-testid":"title-details-languages"}).a.get_text()
#     print(e)
#     # print(d)
#     # print(e)
# scrap_movie_details()
