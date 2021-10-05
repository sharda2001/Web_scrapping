import json
file1 = open("task_1.json")
movies_data = json.load(file1)
year_list=[]
for i in movies_data:
    if i['year'] not in year_list:
        year_list.append(i['year'])
# print(year_list)
my_list=[]
dic_1={}
for i in year_list:
    modules=i%10
    # print(modules)
    dec=i-modules
    # print(dec)
    if dec not in my_list:
        my_list.append(dec)
        dic_1[dec]=[]
        # print(dic_1)
for x in dic_1:
    for i in movies_data:
        h=str(x)
        j=str(i['year'])
        if h[-2]==j[-2]:
            dic_1[x].append(i)
    # print(dic_1)
with open("tas_3.json","w") as a:
    json.dump(dic_1,a,indent=4)