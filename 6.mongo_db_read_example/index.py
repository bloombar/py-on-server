#!/usr/local/bin/python3

#enable debugging... any errors will be output as HTML so they show up clearly in the web browser
import cgi, cgitb
cgitb.enable()

#make sure all output from the print statement in Python is utf-8 encoded
import sys, codecs
sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())

#import mongodb 
import pymongo

#connect to db server
client = pymongo.MongoClient('mongodb://amos:TXG2Mju3@class-mongodb.cims.nyu.edu/amos')

#send raw HTTP response headers to web browser
#NOTE: this must be the first thing sent to the web browser
print("Content-type: text/html;charset=utf-8")
print("\n\n")  #two line breaks indicates the end of the headers

#output the top of the HTML document
print('''
<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8" />
        <title>MongoDB Read From Python</title>
        <link rel="stylesheet" type="text/css" href="css/main.css" />
    </head>
    <body>
        <div class="container">
        	<h1>View the books in the library</h1>
            <p>
                <a href="../7.mongodb_write_example/">Or add a new book to the collection</a>
            </p>
''')

#loop through all the books in the collection in the 'amos' database
for book in client.amos.books.find():

    #get the data about this book from the dictionary... MongoDB is schemaless, so replace any missing fields are replaced by default values
    title = book.get('title', 'Untitled')
    author = book.get('author', 'Unknown Author')
    edition = book.get('edition', 'Unknown Edition')
    price = book.get('price', 'Unknown price')

    print('''

            <article>
                <h2>{title}</h2>
                <p>
                    by {author} 
                    <br />
                    ({edition})
                </p>
                <div class='price'>
                    ${price}
                </div>
            </article>      

    '''.format(title=title, author=author, edition=edition, price=price))


#output the bottom of the HTML document
print('''
    
            <!-- clearfix -->
            <div class="clear"></div>
        </div>
    </body>
</html>
''')

