#get requests: useful if we want to read an info from the website
#making a simple GET resquest
import requests
url = "https://fantasy.premierleague.com"
response = requests.get(url)
#showing results
print(response) #response is 200 ==> success
#to get the status code attribute of the response object
print(response.status_code)
#Request content
#to show response content we use "content"
import requests
response = requests.get("https://fantasy.premierleague.com")
print(response.content)
#Post Request: useful if we want to send data to website(exp;create a post or submit a log)
data = {"name": "Salah", "message": "Hello!"}
url = "https://httpbin.org/post" #https://httpbin.org is a website that gives a bunch of endpoints that we can use for testing HTTP requests.
response = requests.post(url, json=data)
#to view the JSON response data, we use json() method
response_data = response.json()
# Shows the data as a dictionary
print(response_data)
#Handling errors
#to check error in code using the status code
import requests
# here we use an endpoint that always gives a 404 status error
response = requests.get("https://httpbin.org/status/404")
# if status code is not 200 (successful response), then show error message
if response.status_code != 200:
    print(f"HTTP Error: {response.status_code}")
#setting a timeout
#by passing timeout parameter to the request method
url = "https://httpbin.org/delay/10"
try:
    response = requests.get(url, timeout=5)#note:If you change the delay to 2 seconds, it will succeed. Most of the time, it is better to just fail explicitly rather than wait and see and not know what’s going on with the request.
except requests.exceptions.Timeout as err:
    print(err)
#http request headers
#to set headers we create a dict with headers values that we want to use
auth_token = "XXXXXXXX"
# here we set the authorization header with the 'bearer token' for authentication purposes.
headers = {
    "Authorization": f"Bearer {auth_token}"
}
url = "https://httpbin.org/headers"
response = requests.get(url, headers=headers)
print(response.json())
#web scrapping with beautifulsoup
#Web Scraping is the process of extracting data directly from websites.
# You can use this to scrape anything from financial data, job posts, ecommerce listings, and so on.
#to scrape a website : by using the get request method to receive the raw HTML content of the page:
import requests
url = "https://fantasy.premierleague.com"
# this will get all the HTML, javascript, css code
response = requests.get(url)
#the problem is that its hard to read from the html format
#we call module called BeautifulSoup
#install it first
#example of getting html content
import requests
from bs4 import BeautifulSoup
url = "https://fantasy.premierleague.com"
response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")
#example on how to get a title, the content on the page ad the links available on the page
title = soup.title.text
content = soup.find("p").text
links = [a["href"] for a in soup.find_all("a")]
print(title, content, links)
#requests vs urllib: difference between them is: he level of abstraction they offer to you as a user, which impacts how easy they are to use.
import urllib.request
import urllib.parse
data = urllib.parse.urlencode({"key"; "value"}).encode("utf-8")
req = urllib.request.Request( "https://fantasy.premierleague.com", data=data, method="post")
with urllib.request.urlopen(req) as response:
    html = response.read().decode("utf-8")
print(html)
