# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import requests
from bs4 import BeautifulSoup
import re
sum=0
r=requests.get('https://book.douban.com/subject/27006303/comments/')
soup=BeautifulSoup(r.text,'lxml')
pattern=soup.find_all('p', 'comment-content')
for item in pattern:
    print(item.string)
p=re.findall('<span class="user-stars allstar(.*?)rating"',r.text)
#print(p)
for star in p:
#    print(star)
    sum += int(star)
print(sum)


#print(r.url)