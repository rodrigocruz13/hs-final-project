#!/usr/bin/python3

import requests
from parsel import Selector

import time
start = time.time()

# Crawling to the website

# GET request to recurship site
response = requests.get('http://www.eltiempo.com/')

# Setup for scrapping tool

# "response.txt" contain all web page content
selector = Selector(response.text)

# Extracting href attribute from anchor tag <a href="*">
href_links = selector.xpath('//a/@href').getall()
href_links.sort()
end = time.time()
# Extracting src attribute from img tag <img src="*">
#image_links = selector.xpath('//img/@src').getall()

print('*****************************href_links************************************')
print(len(href_links))
i = 0
for link in href_links:
    print (i, link)
    i+=1

print('*****************************/href_links************************************')

#print('*****************************image_links************************************')
#print(len(image_links))
#i = 0
#for link in image_links:
#    print (i, link)
#    i+=1
#print('*****************************/image_links************************************')



with open("www.eltiempo.com.txt", "w") as f:
    for s in href_links:
        f.write(str(s) +"\n")

print("Time taken in seconds : ", (end-start))
