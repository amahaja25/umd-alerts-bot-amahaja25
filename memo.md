Bot Final Submission!

When I started this project, I wanted to make a Slack bot that could be used to expedite coverage of breaking news based on alerts from UMPD. I also wanted it to have the ability to alert reporters specifically when the message goes out. Since this bot is just in the news app slack, there isn't a tag for reporters, so I had it give me a notification based on my Slack member id, which ended up working. I did store the data and I am able to get the alerts from the first 100 pages, which is useful to look at the types of alerts and which ones are more frequent going forward. 

If this bot could accept input from users, I think it could work so that users could potentially respond and ask questions about the full text of the document for their reporting, like who the point of contact from UMPD or PGPD should be if they need a statement or more information about the alert. This would require a full-text search and even cleaning the text so that it doesn't contain the extra information from UMPD. A simpler version of this could be even just having the reporter who wants to pick up the story react with a specific emoticon in Slack to the message, which can then alert the news editors to get the process started. I have found that the best schedule for updates to this bot is having it scrape every 4 or 5 minutes or so, but I do think incorporating an alternative way to keep track of time would be the most optimal.

I wanted to be able to control the types of alerts that sent messages. For example, if "police activity" or “investigation” was in the alert text, then the bot would send a message, but if "alert test" was in it, then it wouldn't, to tailor the bot more to the needs of the individual newsroom and its coverage. I was unable to get to this part of the bot, but I do think if I did, it would have been elevated since it would be more personalized. I also originally wanted to get the individual time of when the scraper picked up a new alert and add it to a column in the table, but I was not able to refine this and get it the way I wanted. If I had more time to work on this, that would be what I’d change first, since the actual time the alerts are published is different than when they originally go out, so at the minimum I want to see what the difference in time is. I also had the idea of getting the information from the email or SMS alerts instead of the website because of that gap in time, so I wish I was able to work with that to get the most accurate time the alerts are sent out to students. 
