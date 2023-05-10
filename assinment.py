# step 0

# pip install requests
# pip instalz bs4
# pip install html5lib

import requests
from bs4 import BeautifulSoup
url='https://theverge.com'

# step 1 
# get the HTML

r =requests.get(url)
htmlcontent=r.content  #r=content
# print(htmlcontent)

#step2
#parse the HTML

soup=BeautifulSoup(htmlcontent,'html.parser')
# print(soup)    # all code show
# print(soup.prettify)       # arrange code


#strp 3
# HTML tree traversal

title=soup.title
# print(type(title))             # give type
print(type(title.string))      # give  NavigableString


#get the title of the html page
title=soup.title
#############################################################
#get all the paragraphs from the page
paras=soup.find_all('p')
# print(paras)





#print(soup.find('p'))     # find the first paragraph in html
# print(soup.find('p')['class'])  #find the class


# print(soup.find('p')['id'])    # find the id


#find all the element with class lead

# print(soup.find_all('p',class_='lead'))


# get the text from the tags/soup
# print(soup.find('p').get_text())


# print(soup.get_text())     #for all text


#get  all the anchor tags from the page
anchor=soup.find_all('a')
print(anchor)






#######################################################################
#get all the link 
all_links=set()
for link in anchor:
    if (link.get('href')!='#'):
        linktext='https://theverge.com'+link.get('href')
        all_links.add(link)
        print(linktext)

