from bs4 import BeautifulSoup
import requests 
import pandas as pd 


movieList = []
    #source.raise_for_status()
def getMovies(tag, page):
    url = f'https://www.imdb.com/search/keyword/?keywords={tag}&ref_=kw_vw_smp&sort=moviemeter,asc&mode=simple&page={page}'
    source = requests.get(url, timeout=(3.05, 27))
    soup = BeautifulSoup(source.text, 'html.parser')
    movies = soup.find_all('div', class_= "lister-item mode-simple")#.find_all('div', class_="lister-item mode-advanced")
    for movie in movies:
        try:
            title = movie.find('div', class_= "lister-item-content").a.text
            movieYear = movie.find('span', class_= "lister-item-year text-muted unbold").text.strip('()')
            ratings = movie.find('div', class_= "col-imdb-rating").strong.text.strip()
            movieList.append([title, movieYear, ratings])
        except:
            ratings = movie.find('span', class_= "ghost")
            pass
    return 
    #movieList.append([title, movieYear, ratings])         
    #genre =   
for x in range(1, 3):    
    getMovies('nigeria', x)

df = pd.DataFrame(movieList)
df.to_excel('NaijainForeignMedia.xlsx')
print('The End')