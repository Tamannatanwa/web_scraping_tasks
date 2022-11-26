import json,requests
with open("5_task.json","r") as file:
    data=json.load(file)
def analyse_language_and_directors(data):
    director_dic={}
    for movie in data:
        if 'director' in movie:
            director_dic[movie['director']]={}
    for i in data:
        for director in director_dic:
            if director in i['director']:
                if 'language' in i:
                    director_dic[director][i['language']]=0
    for i in data:
        for director in director_dic:
            if director in i['director']:
                if 'language' in i:
                    director_dic[director][i['language']]+=1
    with open("10_task.json","w") as f:
        json.dump(director_dic,f,indent=8)      
analyse_language_and_directors(data)

        
        
        