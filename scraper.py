# import libraries
import os
import csv
import time
import requests
from bs4 import BeautifulSoup
from newspaper import Article
from slack import WebClient
from slack.errors import SlackApiError


list_of_rows = []

# python requests session 
s = requests.Session()

# this is the url i would like to scrape

def scrape_page(url):
    response = s.get(url, headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:121.0) Gecko/20100101 Firefox/121.0'})
    html = response.content
    soup = BeautifulSoup(html, features= "html.parser")
    
    main = soup.find('ul', {"class": "feed"})
    lis = main.find_all('li')
    for li in lis:
        title = li.find('a')
        if title:
            link = 'https://alert.umd.edu/' + li.find('a')['href']
            article = Article(link)
            article.download() 
            article.parse()

            alert_text = article.text
            title_text = title.text.strip()

            day = li.find('time')
            date = day.text.strip()
            subhead = li.find('p')
            text = subhead.text.strip()
  
        list_of_cells = [link, title_text, date, text, alert_text]
        list_of_rows.append(list_of_cells)

time.sleep(1)

default_url = 'https://alert.umd.edu/alerts' 
scrape_page(default_url)

base_url = 'https://alert.umd.edu/alerts?page='
for page in range(0, 90):
    
    url = f'{base_url}{page}'
    scrape_page(url)


# write to umd_alerts.csv file
outfile = open("umd_alerts.csv", "w")
writer = csv.writer(outfile)
writer.writerow(["link", "title","date", "subhead", "alert_text"])
writer.writerows(list_of_rows)


#slack stuff
'''
slack_token = os.environ.get('SLACK_API_TOKEN')

client = WebClient(token=slack_token)

msg = "Please react to this message with a thumbs up or down if you can/can't cover this:\n Link: {row[0]} \n Date: {row[3]} \n Title: {row[2]} \n Alert: {row[5][:500]}

csv = "umd_alerts.csv"


try:
    response = client.chat_postMessage(
        channel="slack-bots",
        text=msg,
        unfurl_links=True, 
        unfurl_media=True
    )
    print("success!")
except SlackApiError as e:
    assert e.response["ok"] is False
    assert e.response["error"]
    print(f"Got an error: {e.response['error']}")
'''