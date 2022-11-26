import json,requests
with open("1_task.json","r") as data:
    list=json.load(data)
def group_by_decade():
    dic={}
    list1=[]
    list2=[]
    list3=[]
    list4=[]
    list5=[]
    list6=[]
    list7=[]
    i=0
    while i<len(list):
        if str(list[i]["year"])>="1950" and str(list[i]["year"])<="1959":
            list1.append(list[i])
            dic["1950"]=list1
        if str(list[i]["year"])>="1960" and str(list[i]["year"])<="1969":
            list2.append(list[i])
            dic["1960"]=list2
        if str(list[i]["year"])>="1970" and str(list[i]["year"])<="1979":
            list3.append(list[i])
            dic["1970"]=list3
        
        if str(list[i]["year"])>="1980" and str(list[i]["year"])<="1989":
            list4.append(list[i])
            dic["1980"]=list4
        if str(list[i]["year"])>="1990" and str(list[i]["year"])<="1999":
            list5.append(list[i])
            dic["1990"]=list5
        
        if str(list[i]["year"])>="2000" and str(list[i]["year"])<="2009":
            list6.append(list[i])
            dic["2000"]=list6 
        if str(list[i]["year"])>="2010" and str(list[i]["year"])<="2019":
            list7.append(list[i])
            dic["2010"]=list7     
        i=i+1
    with open("3_task.json","w") as file123:
        json.dump(dic,file123,indent=8)   
group_by_decade()
    
    
    
    
    
    
















