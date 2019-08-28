Web scraping demo: Portal displaying latest information about Mars
Scrape data from URLs and insert into MongoDB
Web scraping function built using Jupyter Notebook, Beautiful Soup, Pandas, and Requests/Splinter. The following information is scaped from various sources:

Latest news headline
Current featured image
Current weather
General facts
URLs scraped:

https://mars.nasa.gov/news/
https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars
https://twitter.com/marswxreport?lang=en
http://space-facts.com/mars/
Separately required: Chrome Driver (Selenium)

Serve summarized data in MongoDB via Flask app
MongoDB / Flask HTML template displays the information scraped from the URLs above.
Function contains scraping code from above to return Python dictionary of variables containing all of the data.

A Flask route "/scrape" calls above scraping function, and return value is stored in MongoDB document.

Root Flask route ("/") retrieves MongoDB document and passes its data into Flask HTML template, dynamically displaying our scraped data where indicated.