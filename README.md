# UMD Alerts scraper

I wrote this web scraper to grab all of the UMD Alerts posted on the <a href="alert.umd.edu">alert.umd.edu</a> website and put them into one csv. This originally started as a project for my news applications class in Spring 2024, but I continued to work on it after the semester ended in my free time. 

The scraper uses the Python library BeautifulSoup and iterates through all the page numbers on the site to get the text of each alert using the newspaper3k Python library. I also added a function that categorizes certain alerts based on if key words are present, such as gas line, robbery, indecent exposure and weather as well as test alerts, which happen the first Wednesday of each month. 

Another function uses key words for a category in the csv that says if the alert detailed an on-campus or off-campus incident, or if there was not enough information to determine the type. I originally just had "on-campus" and "off-campus" as key words, but expanded the categories to include words such as "hall," "parking garage," and "parking lot" as well as certain on-campus roads like Stadium Drive, which indicate if an incident was on campus even if the alert didn't explicitly state it was using those words.

More than 750 alerts, from the earliest UMD Alert on the site in August 2012 to the most recent one, are in the csv. I implemented GitHub Actions to automate the scraper to run every three minutes so I get the newest alert as soon as it's uploaded to the site.

My initial project for class was a Slack bot that sent a Slack message in a channel that directly sent me a notification whenever a new alert was added to the csv that wasn't previously there. Since my scraper is no longer connected to a Slack channel and I'm not using that functionality anymore, that part is commented out.

I'm pretty happy with where the scraper is at right now, but I'm interested in looking into eventually setting up something that grabs email or text alerts, which have a time aspect to them. On the website and its source code, there's no indication as to when an alert went out or was uploaded to the site beyond the time it was scraped, which doesn't give me much when I scraped most of the alerts at once. I might also add more categories/keywords to be more in depth.

# Previous updates log!

3/14 
* I created the python file for the scraper as well as the csv that i want to store the alerts in.
* Created some sort of start to the scraper, but there is more I need to work on. Starting out, I was able to get the links to the alerts and attach them to the base UMD Alerts link, get the date of the alert, as well as the title, and write this all out to the csv. 
* I need to now find a way to scrape the individual alert pages so I can get the text, and further split this up into things like location and time of incident.
* Need to split up alerts by type -- Gas Line, Robbery, Indecent Exposure, On- vs Off-Campus.
* Have to implement GitHub Actions to automate running this every minute or two so I can be most up to date on the alerts.
* I need to develop a more thought-out criteria for the alerts I want and if I should include "community alerts" which are off-campus. the purpose of my bot is to alert when a breaking news story could come from an alert, and off-campus incidents might not be the most relevant, but i also think it could be interesting to look at the trends over time in the off-campus incidents as I gather more data.
* The ideal version of this bot would run every minute, and when a new update is posted, it would record the time and send a message with the time, location (maybe a link to a map of the block or address of the incident?), and type of incident.

3/30
* I got the text from the individual pages using the newspaper library!!!!
* I tried using sessions to get the other pages. This did work when the site was working, but I was not getting all of the alerts, and my csv had way less rows than it should have. 
* It seems to me that the website sometimes  goes blank, with nothing on the page except for the word 'Alerts.' This is now the second time this has happened to me and I don't know how I can get around this, because now I can't really figure out what went wrong with certain alerts not getting rows in the csv since my scraper just can't run without the elements it needs on the page.
* I added a start to the Slack message. I want to incorporate something that counts the rows on the csv and sends a message when a new row is added. (but i need all of the alerts in this csv for it to work!)
* added the same github actions from bad docs, adjusted it to run every 5 minutes. (obv can't run if website is weird)

4/1
* I was playing around with github actions to try to get the automation to work, and it wasn't working when the alerts website went blank
* I tried to account for error when the website goes blank as it does.
* but i learned that the umd alerts website is updated much later than when the actual alerts go out. but the scrape every 5 min got the latest one! next i just need to have the slack message trigger once the csv is updated.

4/8 
* Finally have included the code for the Slack message!! Used an if else statement for both writing to the csv and to sending the Slack message only if the number of new incidents is greater than zero. Comparing the existing alerts to the new ones.
* I have started to play around with getting the date based on GitHub actions -- going to work a little bit more on this in the next few days because right now they have all of the same time. I think the thing with comparing the old and new alerts would help this since it doesn't have to write the entire csv at once
* Going to adjust how frequently the GitHub actions runs to like every minute so the time can be as accurate as possible.
* For the final submission, I think I just have to make sure somehow that the message sends? And that I fix what is wrong with the time. The Slack message is the main thing I was the most stumped on before.
