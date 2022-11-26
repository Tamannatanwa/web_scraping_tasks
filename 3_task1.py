import json
with open("1_task.json","r") as data:
    list=json.load(data)
def group_by_decade():
    i=0
    list21=[]
    while i<len(list):
        mode=int(list[i]["year"])%10
        debade=int(list[i]["year"])-mode
        if debade not in list21:
            list21.append(debade)
        i=i+1
    j=0
    d={}
    list1=[]
    while j<len(list21):
        mode=int(list21[j])%10
        debade=int(list21[j])-mode
        k=0
        list1=[]
        while k<len(list):
            if int(list[k]["year"])>=debade and int(list[k]["year"])<debade+10:
                list1.append(list[k])
            k=k+1
        j=j+1
        d[debade]=list1
    with open("3_task1.json","w") as file123:
        json.dump(d,file123,indent=8)   
group_by_decade()

