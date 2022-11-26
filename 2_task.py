import json,requests
with open("1_task.json","r") as file:
    data=json.load(file)
def group_by_year(movies):
    years=[]
    for i in movies:
        year=i["year"]
        if year not in years:
            years.append(year)
    movie_dict={i:[] for i in years}
    for i in movies:
        year=i['year']
        for x in movie_dict:
            if str(x)==str(year):
                movie_dict[x].append(i)
    with open("2_task.json","w") as new:
        json.dump(movie_dict,new,indent=8)
    return movie_dict
screap=group_by_year(data)



