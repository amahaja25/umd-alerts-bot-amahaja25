# umd-alerts-bot-amahaja25

3/14 
* I created the python file for the scraper as well as the csv that i want to store the alerts in.
* Created some sort of start to the scraper, but there is more I need to work on. Starting out, I was able to get the links to the alerts and attach them to the base UMD Alerts link, get the date of the alert, as well as the title, and write this all out to the csv. 
* I need to now find a way to scrape the individual alert pages so I can get the text, and further split this up into things like location and time of incident.
* Need to split up alerts by type -- Gas Line, Robbery, Indecent Exposure, On- vs Off-Campus.
* Have to implement GitHub Actions to automate running this every minute or two so I can be most up to date on the alerts.
* I need to develop a more thought-out criteria for the alerts I want and if I should include "community alerts" which are off-campus. the purpose of my bot is to alert when a breaking news story could come from an alert, and off-campus incidents might not be the most relevant, but i also think it could be interesting to look at the trends over time in the off-campus incidents as I gather more data.
* The ideal version of this bot would run every minute, and when a new update is posted, it would record the time and send a message with the time, location (maybe a link to a map of the block or address of the incident?), and type of incident.
