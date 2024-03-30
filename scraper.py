# import libraries
import csv
import requests
from bs4 import BeautifulSoup
from newspaper import Article

list_of_rows = []

# this is the url i would like to scrape
url = 'https://alert.umd.edu/alerts' 

response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:121.0) Gecko/20100101 Firefox/121.0'})
html = response.content

soup = BeautifulSoup(html, features= "html.parser")

# this specifies which links i want. without this, i would also end up scraping things like the about and faq page links
main = soup.find('ul', {"class": "feed"})

# scraper start but note that this isn't exactly what i want. i have to figure out how to go through the individual alert links and get the text from there

lis = main.find_all('li')
for li in lis:
    list_of_cells = []
    title = li.find('a')
    if title:
        link = 'https://alert.umd.edu/' + li.find('a')['href']
        article = Article(link)
        article.download() 
        article.parse()

        article_text = article.text
        title_text = title.text.strip()

    day = li.find('time')
    date = day.text.strip()
    subhead = li.find('p')
    text = subhead.text.strip()
    
    list_of_cells = [link, title_text, date, text, article_text]
    list_of_rows.append(list_of_cells)
    
    
 # ok i got stumped here because the content of the actual alert is in a p tag for some, in a div tag for others and i thought i could get around it by getting the text from inside the meta tag's content class but the text isn't actually in there for all of the alerts.   
    #if title:
        #alert_response = requests.get(links, headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:121.0) Gecko/20100101 Firefox/121.0'})
        #alert_soup = BeautifulSoup(alert_response.content, 'html.parser')
        #alert_content = alert_soup.find('meta', {"class": "content"})
        #if alert_content:
         #   alert_text = alert_content.text.strip()
          #  list_of_cells.append(alert_text)
        #else:
         #   list_of_cells.append("none")
    #list_of_rows.append(list_of_cells)


#s = requests.Session()
#s.get('https://alert.umd.edu/?page=1')
#r = s.get('')



# if i want to also scrape the past alerts, i have to find a way to iterate through all the pages at the bottom. but each page doesn't have a separate url which is annoying so have to deal with that
# python requests session 


# write to the umd_alerts.csv file
outfile = open("umd_alerts.csv", "w")
writer = csv.writer(outfile)
writer.writerow(["link", "title","date", "subhead", "article.text"])
writer.writerows(list_of_rows)
