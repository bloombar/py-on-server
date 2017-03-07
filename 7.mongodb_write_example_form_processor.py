#!/usr/local/pkg/python/3.5/bin/python

#enable debugging... any errors will be output as HTML so they show up clearly in the web browser
import cgi, cgitb
cgitb.enable()

#make sure all output from the print statement in Python is utf-8 encoded
import sys, codecs
sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())

#import mongodb 
import pymongo

# use the CGI library to get any form data sent to the server from the client
form = cgi.FieldStorage() 

# validate that data has been submitted via the form...
if "title" not in form or "author" not in form or "edition" not in form or "price" not in form:
    # if the user did not enter form data, send the browser back to the form page
    # we do this by sending a special HTTP location header to the browser
    print("Location: ./7.mongodb_write_example_form.html\n\n")
    #exit now!
    sys.exit()

#assuming the user entered form data, get the form data into simple variables
title = form.getfirst('title')
author = form.getfirst('author')
edition = form.getfirst('edition')
price = form.getfirst('price')

#connect to db server
client = pymongo.MongoClient('mongodb://your_username:your_password@your_host_name/your_database_name')

#make a new document in Python's JSON closest equivalent... a dictionary
document = {
    'title': title,
    'author': author,
    'edition': edition,
    'price': price
}

#insert a new document into the MongoDB collection
client.amos.books.insert(document)

#send the browser to view the previous example page so the user can see the new set of books
# we do this by sending a special HTTP location header to the browser
print("Location: ./6.mongodb_read_example.py\n\n")

