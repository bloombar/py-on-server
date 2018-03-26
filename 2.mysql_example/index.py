#!/usr/local/bin/python3

#enable debugging... any errors will be output as HTML so they show up clearly in the web browser
import cgi, cgitb
cgitb.enable()

#make sure all output from the print statement in Python is utf-8 encoded
import sys, codecs
sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())

#connect to database
import pymysql
cxn = pymysql.connect(
    host="your_mysql_host_name", 
    user="your_mysql_username", 
    passwd="your_mysql_password", 
    db="your_mysql_database_name", 
    charset='utf8mb4',
    cursorclass=pymysql.cursors.DictCursor) 

#get a 'cursor'... a pointer to the database
cur = cxn.cursor()

#execute a query
cur.execute("SELECT * FROM favorite_viking_metal_bands ORDER BY origin ASC")

#store the results
rows = cur.fetchall()

#send raw HTTP headers to browser
print("Content-type: text/html;charset=utf-8")
print("\n\n")

#print the top of the document
print('''
<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8" />
        <title>MySQL Example Query from Python</title>
        <link rel="stylesheet" type="text/css" href="css/main.css" />
    </head>
    <body>
        <div class="container">
            <h1>Viking Metal Bands</h1>
''')

#loop through the query results and print them out as well-formmated HTML
for row in rows:
    print('''
             <article>
                <h1>{name}</h1>
                <p>
                    {country}
                    <br />
                    ({year})
                </p>
             </article>
            '''.format(name=row['band'], country=row['origin'], year=row['formed']))

#print out the bottom of the document
print('''
            <!-- clearfix -->
            <div class="clear"></div>
        </div>
    </body>
</html>
''')

