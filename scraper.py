# import libraries
import csv
import requests
from bs4 import BeautifulSoup

list_of_rows = []

# this is the url i would like to scrape
url = 'https://alert.umd.edu/alerts' 

# scraper
response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:121.0) Gecko/20100101 Firefox/121.0'})
html = response.content

soup = BeautifulSoup(html, features="html.parser")
lis = soup.find('li')

for li in lis:
    list_of_cells = []
    anchor = li.find('a')
    if anchor:
        link = "https://alert.umd.edu/alerts/" + li.find('a')['href']
        list_of_cells.append(link)
    paragraph = li.find('p')
    if paragraph:
        text = paragraph.text.strip()
        list_of_cells.append(text)
    list_of_rows.append(list_of_cells)

# write to the umd_alerts.csv file
outfile = open("umd_alerts.csv", "w")
writer = csv.writer(outfile)
writer.writerow(["url", "text"])
writer.writerows(list_of_rows)
