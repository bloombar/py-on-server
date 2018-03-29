#!/usr/local/bin/python3

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
    #print("Location: ./index.html\n\n")
    #exit now!
    sys.exit()

#assuming the user entered form data, get the form data into simple variables
title = form.getfirst('title')
author = form.getfirst('author')
edition = form.getfirst('edition')
price = form.getfirst('price')

#connect to db server
try:
	client = pymongo.MongoClient('mongodb://amos:TcW8xE9J@class-mongodb.cims.nyu.edu/amos')
except pymongo.errors.ConnectionFailure as e:
	#show connection error details
    print(e.details)

#make a new document in Python's JSON closest equivalent... a dictionary
document = {
    'title': title,
    'author': author,
    'edition': edition,
    'price': price
}

try:
	client.amos.books.insert(document)
except pymongo.errors.OperationFailure as e:
	#show operation error details
    print(e.details)

#send the browser to view the previous example page so the user can see the new set of books
# we do this by sending a special HTTP location header to the browser
print("Location: ../6.mongo_db_read_example/index.py\n\n")

