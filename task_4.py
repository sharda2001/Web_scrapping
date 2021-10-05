from bs4 import BeautifulSoup   
import requests
import json
def scrape_movie_details():
    details_dict = {}
    url="https://www.imdb.com/title/tt8108198/"
    page= requests.get(url)
    # print(responce)
    soup=BeautifulSoup(page.text,"html.parser")
    # print(soup)
    movie_name=soup.find("div",class_="TitleBlock__Container-sc-1nlhx7j-0 hglRHk").h1.text
    # print(movie_name)
    details_dict["Movie_name"]=movie_name
    # print(details_dict)
    data= soup.findAll("ul",class_="ipc-metadata-list ipc-metadata-list--dividers-all ipc-metadata-list--base") 
    # print(data)
    for i in data:
        f=i.findAll('li',class_="ipc-metadata-list__item")
        # print(f)
        for fi in f:
            if "Country" in fi.text:
                country=fi.find('div',class_="ipc-metadata-list-item__content-container").text
                # print(country)
            elif "Language" in fi.text:
                language=fi.findAll('a')
                # print(language)

                for l in language:
                    # print(l.text) 
                    details_dict["language"]=l.text
                    details_dict["country"]=country
                # print(details_dict)

    Genres=soup.find("div",class_="ipc-chip-list GenresAndPlot__GenresChipList-cum89p-4 gtBDBL").text
    # print(Genres)
    details_dict["Genres"]=Genres
    # print(details_dict)

    director=soup.find("li",class_="ipc-metadata-list__item").a.text
    # print(director)
    details_dict["director"]=director
    # print(details_dict)

    with open("task_4.json","w")as file:

        json.dump(details_dict,file,indent=4) 

scrape_movie_details()