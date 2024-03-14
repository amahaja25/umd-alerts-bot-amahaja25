# import libraries
import csv
import requests
from bs4 import BeautifulSoup

list_of_rows = []

# this is the url i would like to scrape
url = 'https://alert.umd.edu/alerts' 

response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:121.0) Gecko/20100101 Firefox/121.0'})
html = response.content

soup = BeautifulSoup(html, features= "html.parser")

# this specifies which specific links i want. without this, i would also end up scraping things like the about and faq page links.
main = soup.find('ul', {"class": "feed"})

lis = main.find_all('li')
for li in lis:
    list_of_cells = []
    if li.find('a'):
        link = 'https://alert.umd.edu/alerts' + li.find('a')['href']
        list_of_cells.append(link)
    day = li.find('time')
    if day:
        date = day.text.strip()
        list_of_cells.append(date)
    paragraph = li.find('p')
    # note that this isn't exactly what i want. i have to figure out how to go to the individual alert link and get the text from there.
    if paragraph:
        text = paragraph.text.strip()
        list_of_cells.append(text)
    list_of_rows.append(list_of_cells)

# if i want to also scrape the past alerts, i have to find a way to iterate through all the pages at the bottom. but each page doesn't have a separate url which is annoying so have to deal with that.

# write to the umd_alerts.csv file
outfile = open("umd_alerts.csv", "w")
writer = csv.writer(outfile)
writer.writerow(["link", "date", "text"])
writer.writerows(list_of_rows)
