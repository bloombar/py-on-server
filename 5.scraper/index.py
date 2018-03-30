#!/usr/bin/env python3

#enable debugging... any errors will be output as HTML so they show up clearly in the web browser
import cgi, cgitb
cgitb.enable()

#make sure all output from the print statement in Python is utf-8 encoded
import sys, codecs
sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())

#import urllib.request and beautiful soup to make web requests and parse them
import urllib.request
from bs4 import BeautifulSoup

#get the HTML code of the web page
url = "http://lyrics.wikia.com/LyricWiki:Lists/Rolling_Stone:_The_500_Greatest_Songs_of_All_Time"
html = urllib.request.urlopen(url)

#parse this page
soup = BeautifulSoup(html)

#now find and parse just the div.WikiaArticle element
div = soup.find_all('div', {"class": "WikiaArticle"})
soup = BeautifulSoup(str(div))

#now find and parse just the ol tag element in here
ol = soup.find_all('ol')
soup = BeautifulSoup(str(ol))

#now find just the a elements in here
links = soup.find_all("b")

# output the top of the document
print('''Content-type: text/html

<!doctype html>
<html lang='en'>
    <head>
        <title>The 500 Greatest Songs of All Time, According to Rolling Stone</title>
        <meta charset="utf-8" />
        <link rel="stylesheet" type="text/css" href="css/main.css" />
    </head>
    <body>
        <div class="container">

            <h1>The 500 Greatest Songs of All Time</h1>
            <h2>
                According to 
                <a href='{url}'>Rolling Stone</a>
            </h2>

'''.format(url=url))

# output each of the songs
for link in links:
    #get the text inside each link in the original html
    print('''

            <article>
                <h2>{song_title}</h2>
            </article>

        '''.format(song_title=link.string))

# output the bottom of the document
print('''

            <!-- clearfix -->
            <div class="clear"></div>

        </div><!-- //.container -->
    </body>
</html>

''')
