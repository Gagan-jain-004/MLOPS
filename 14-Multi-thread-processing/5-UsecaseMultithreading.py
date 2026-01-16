
'''
eg: Multithreading for I/O-bound tasks like web scraping

web scraping often involves making numerous network requests to fetch web pages.
These tasks are I/O-bound because the program spends a significant amount of time waiting for responses from web servers.
Multithreading can help improve the efficiency of web scraping by allowing multiple web pages to be fetched concurrently.
'''
'''

install bs4 for web scraping
'''
'''
https://docs.langchain.com/oss/python/langchain/overview

https://docs.langchain.com/oss/python/langchain/quickstart

https://docs.langchain.com/oss/python/langchain/philosophy


'''


import threading
import requests
from bs4 import BeautifulSoup

urls=[
   'https://docs.langchain.com/oss/python/langchain/overview',

'https://docs.langchain.com/oss/python/langchain/quickstart',

'https://docs.langchain.com/oss/python/langchain/philosophy'
 
]

def fetch_content(url):
    response=requests.get(url)                       # taking content from url
    soup= BeautifulSoup(response.content,'html.parser')         # parsing html content using html.parser from bs4
    print(f'Fetched {len(soup.text)} characters from {url}')      # count of characters 

threads=[]

# traversing url and giving thread to each url and then appending them then start ,, so they run parallely 
for url in urls:
    thread=threading.Thread(target=fetch_content,args=(url,))     
    threads.append(thread)
    thread.start()



for thread in threads:
    thread.join()          # join to give collective output 

print("all web pages fetched")