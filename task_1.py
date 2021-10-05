import requests
from bs4 import BeautifulSoup
import json

link=" https://www.imdb.com/india/top-rated-indian-movies/"
a=requests.get(link)
# print(a)
soup=BeautifulSoup(a.text,'html.parser')
# print(type(soup))

def scrap_top_list():
    main_div=soup.find('div',class_='lister')
    tbody=main_div.find('tbody',class_='lister-list')
    trs=tbody.find_all("tr")
    movie_ranks=[]
    movie_name=[]
    years=[]
    movie_url=[]
    ratings=[]
    top_indain_movies=[]

    for tr in trs:
        movies_details={}
        position=tr.find('td',class_="titleColumn").get_text().strip()
        movie_rank=''
        for i in position:
            if '.' not in i:
                movie_rank=movie_rank+i
            else:
                break
        movie_ranks.append(movie_rank)
        name_of_movie=tr.find('td',class_="titleColumn").a.get_text()
        movie_name.append(name_of_movie)
        year=tr.find('td',class_="titleColumn").span.get_text()
        years.append(year)
        # print(year_of_realease)
        imdb_rating=tr.find('td',class_="ratingColumn imdbRating").strong.get_text()
        ratings.append(imdb_rating)
        # print(movie_ratings)
        link=tr.find('td',class_="titleColumn").a['href']
        movie_link="https://www.imbd.com"+link
        movie_url.append(movie_link)
        movies_details["name of movie"]=name_of_movie
        movies_details["year"]=int(year[1:5])
        movies_details["position of movie"]=int(movie_rank)
        movies_details["url"]=movie_link
        movies_details["rating"]=float(imdb_rating)



        top_indain_movies.append(movies_details)
    return top_indain_movies

    # print(top_movie)
    # with open("imdb_movies.json","w") as file1:
    #     file2=json.dump(top_movie,file1,indent=4)

movies_data=scrap_top_list()
# print(movies_data)
with open ("task_1.json","w+") as file:
    json.dump(movies_data,file,indent=4)