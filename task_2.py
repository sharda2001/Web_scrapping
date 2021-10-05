import json
file1 = open("task_1.json")
movies = json.load(file1)
def group_by_year():
    emp_dic={}
    for i in movies:
        movie_list=[]
        year=i["year"]
        if year not in  emp_dic:
            for j in movies:
                if year==j["year"]:
                    movie_list.append(j)
            emp_dic[year]=movie_list
        # print(emp_dic)
    with open("task_2.json","w")as file:
        json.dump(emp_dic,file,indent=4)
group_by_year()