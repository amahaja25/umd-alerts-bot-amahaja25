# import libraries
import os
import csv
import time
import requests
import re
from bs4 import BeautifulSoup
from newspaper import Article
from slack import WebClient
from slack.errors import SlackApiError
from datetime import datetime, timezone

with open('umd_alerts.csv', 'r') as existing_alerts:
    reader = csv.DictReader(existing_alerts)
    previous_alerts = [x['link'] for x in reader]

#open the old csv
# save the old/existing links 

list_of_rows = []
#time
current_utc_datetime = datetime.now(timezone.utc).isoformat()

# python requests session 
s = requests.Session()

# this is the url i would like to scrape

def scrape_page(url):
    response = s.get(url, headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:121.0) Gecko/20100101 Firefox/121.0'})
    html = response.content
    soup = BeautifulSoup(html, features= "html.parser")
    
    main = soup.find('ul', {"class": "feed"})
    try:
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
                
            
  
            list_of_cells = [link, title_text, date, text, alert_text, current_utc_datetime]
            list_of_rows.append(list_of_cells)
    except:
        pass


time.sleep(1)

default_url = 'https://alert.umd.edu/alerts' 
scrape_page(default_url)

base_url = 'https://alert.umd.edu/alerts?page='
for page in range(0, 100):
    
    url = f'{base_url}{page}'
    scrape_page(url)

new_alerts = [x for x in list_of_rows if x[0] not in previous_alerts]

print(len(new_alerts))

if len(new_alerts) > 0:
    with open("umd_alerts.csv", 'a') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["link", "title","date", "subhead", "alert_text"])
        writer.writerows(new_alerts)
    #if new_incidents, then send it to slack, if you don't then don't send anything 
    #slack stuff
    slack_token = os.environ.get('SLACK_API_TOKEN')
    client = WebClient(token=slack_token)
    mostrecent_alert = new_alerts[0] 

    cleaned_alert_text = re.sub(r'\s+', ' ', mostrecent_alert[3][:500]).strip()
    member_id = 'U06FUFNJ2PK'

    msg = f"<@{member_id}> Please react to this message with a thumbs up or down if you can/can't cover this: \n Link: {mostrecent_alert[0]} \n Date: {mostrecent_alert[2]} \n Title: {mostrecent_alert[1]} \n Alert: {cleaned_alert_text}"


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
    else:
        pass




