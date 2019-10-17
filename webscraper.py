from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd

driver = webdriver.Chrome(executable_path='/usr/local/bin/chromedriver')
driver.get("https://www.nytimes.com/search/?date_select=full&query=Flint+Water+Crisis&type=nyt&x=0&y=0")
content = driver.page_source
soup = BeautifulSoup(content)
urls = []
titles = []
dates = []
for a in soup.findAll('li', attrs={'class':'css-1l4w6pd'}):
    url = a.find('a', href=True)
    title = a.find('h4', attrs={'class':'css-1lppelv'})
    date = a.find('time', attrs={'class':'css-13nimws'})
    
    urls.append(url.get('href'))
    titles.append(title.text)
    dates.append(date.text)

df = pd.DataFrame({'Article Name':titles,'Link':urls,'Dates':dates})
df.to_csv('articles.csv', index=False, encoding='utf-8')
