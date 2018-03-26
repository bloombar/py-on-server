#!/usr/local/bin/python3

#enable debugging... any errors will be output as HTML so they show up clearly in the web browser
import cgi, cgitb
cgitb.enable()

#make sure all output from the print statement in Python is utf-8 encoded
import sys, codecs
sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())

#import the string templating library to do allow us to separate the HTML code from the Python code
from string import Template

#connect to database
import pymysql
cxn = pymysql.connect(
    host="warehouse", 
    user="amos", 
    passwd="pqvksah8", 
    db="amos_db_design_spring_2016", 
    charset='utf8mb4',
    cursorclass=pymysql.cursors.DictCursor) 

#get a 'cursor'... a pointer to the database
cur = cxn.cursor()

#execute a query
cur.execute("SELECT * FROM favorite_viking_metal_bands ORDER BY origin ASC")

#store the results
rows = cur.fetchall()

#open the article template
f = open('article_template.txt')
article_template = Template(f.read())
f.close()

#open the page template
f = open('page_template.txt')
page_template = Template(f.read())
f.close()

#generate the html for all articles

#a blank list that will be filled in with the html for all articles
articles_html = []

for row in rows:
    #put together data foe this article
    article_data = {
        "name": row['band'],
        "country": row['origin'],
        "year": row['formed']
    }
    article_html = article_template.substitute(article_data)
    articles_html.append(article_html)


#set up the variables to plug into the template
page_data = {
    'title': "Viking Meral Bands",
    'heading': "List of Viking Metal Bands",
    'css_url': 'css/main.css',
    'articles': "\n".join(articles_html)
}

#plug the variables into the template to generate the complete HTML
page_html = page_template.substitute(page_data)

#output filled-in template
print(page_html)


