import json
with open("task_55.json","r") as file1:
    data1=json.load(file1)
    # print(data1)
def analyse_movies_language(data):
    dict={}
    list=[]
    for i in data:
        for b in i:
            if b =="director":
                list.append(i[b])
            # print(li)
    count=0
    index=0
    for index in range(0,len(list)):
        count=0
        for i in range (0,len(list)):
            if list[index]==list[i]:
                count+=1
        if list[index] not in dict:
            dict[list[index]]=count
    print(dict)
    with open("task_7.json","w") as file:
        json .dump(dict,file,indent=4) 
analyse_movies_language(data1)