# import libraries
import csv
import requests
from bs4 import BeautifulSoup

# this is the url that i would like to scrape
url = 'https://alert.umd.edu/alerts' 

# scraper

# write to the umd_alerts.csv file
outfile = open("umd_alerts.csv", "w")
writer = csv.writer(outfile)