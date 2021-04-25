
import requests
from requests import get
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
import mysql.connector
from mysql.connector import Error
results=requests.get("https://www.amazon.in/gp/browse.html?node=6612025031&ref_=nav_em_sbc_mobcomp_powerbank_0_2_8_6")

soup = BeautifulSoup(results.text, "html.parser")
connection = mysql.connector.connect(host='localhost',
                                         database='db1',
                                         user='root',
                                         password='')
cur=connection.cursor()
titles = []
years = []
time = []


movie_div = soup.find_all('div', class_='a-section a-spacing-none apb-browse-searchresults-product')


#cur.execute(sql)
#print(cur.rowcount)

for container in movie_div:

        
        
        #year
        year = container.find('div', class_='a-section a-spacing-none a-spacing-top-small').text.strip()
        titles.append(year)
        #print(titles)
        
        
        
        #runtime
        runtime = container.find('span', class_='a-size-small a-color-link').text if container.find('span', class_='a-size-small a-color-link').text else '-'
        time.append(runtime)
        #print(runtime)
        
       
        cur.execute("insert into power (cost,name)values(%s,%s)",(runtime,year))
        
      
#cur.execute("alter table power drop year")
connection.commit()        
print("gf",cur.rowcount)

connection.close()
#building our Pandas dataframe         
movies = pd.DataFrame({
'Name': titles,
#'reviews': years})
'reviews': time})
''''imdb': imdb_ratings,
'metascore': metascores,
'votes': votes,
'us_grossMillions': us_gross,
})'''
print(movies)
'''#cleaning data with Pandas
movies['movie'] = movies['movie'].str.extract('(\d+)').astype(int)
#movies['mov'] = movies['movie'].str.extract('(\d+)').astype(int)
movies['timeMin'] = movies['timeMin'].str.extract('(\d+)').astype(float)
#movies['metascore'] = movies['metascore'].astype(int)
movies['votes'] = movies['votes'].str.replace(',', '').astype(int)
movies['us_grossMillions'] = movies['us_grossMillions'].map(lambda x: x.lstrip('$').rstrip('M'))
movies['us_grossMillions'] = pd.to_numeric(movies['us_grossMillions'], errors='coerce')'''
movies.to_csv('power.csv')
#print(movies)
