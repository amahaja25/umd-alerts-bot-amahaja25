# umd-alerts-bot-amahaja25

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

4/8 (i am incredibly sorry this is late)
* Finally have included the code for the Slack message!! Used an if else statement for both writing to the csv and to sending the Slack message only if the number of new incidents is greater than zero. Comparing the existing alerts to the new ones.
* I have started to play around with getting the date based on GitHub actions -- going to work a little bit more on this in the next few days because right now they have all of the same time. I think the thing with comparing the old and new alerts would help this since it doesn't have to write the entire csv at once
* I also don't really know how to test if the bot works or not or if the message works well/looks right until the next UMD Alert is sent.
* Going to adjust how frequently the GitHub actions runs to like every minute so the time can be as accurate as possible.