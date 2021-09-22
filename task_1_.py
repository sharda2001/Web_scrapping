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
    # return tbody
# print(scrap_list())
    trs=tbody.find_all('tr')
#     return trs
# print(scrap_list())
    movie_ranks=[]
    movie_name=[]
    year_of_realease=[]
    movie_urls=[]
    movie_ratings=[]

    for tr in trs:
        position=tr.find('td',class_="titleColumn").get_text().strip()
        rank=''
        for i in position:
            if '.' not in i:
                rank=rank+i
            else:
                break
        # return (position)
        movie_ranks.append(rank)
        # print(movie_ranks)
        title=tr.find('td',class_="titleColumn").a.get_text()
        movie_name.append(title)
        year=tr.find('td',class_="titleColumn").span.get_text()
        year_of_realease.append(year)
        # print(year_of_realease)
        imdb_rating=tr.find('td',class_="ratingColumn imdbRating").strong.get_text()
        movie_ratings.append(imdb_rating)
        # print(movie_ratings)
        link=tr.find('td',class_="titleColumn").a['href']
        movie_link="https://www.imbd.com"+link
        movie_urls.append(movie_link)
        # print(movie_urls)
    top_movie=[]
    # for i in range(0,len(movie_ranks)):
    i=0
    while i<len(movie_ranks):
        details={}
        details['position']=int(movie_ranks[i])
        # print(details)
        details['name']=str(movie_name[i])
        # print(details)
        year_of_realease[i]=year_of_realease[i][1:5]
        details['year']=int(year_of_realease[i])
        details['rating']=float(movie_ratings[i])
        # print(details)
        details['url']=movie_urls[i]
        # print(details)

        top_movie.append(details)
        i=i+1
    # print(top_movie)
    with open("task1.json","w") as file1:
        file2=json.dump(top_movie,file1,indent=4)

scrap_top_list()


    