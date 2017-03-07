#!/usr/local/pkg/python/3.5/bin/python

#enable debugging... any errors will be output as HTML so they show up clearly in the web browser
import cgi, cgitb
cgitb.enable()

#make sure all output from the print statement in Python is utf-8 encoded
import sys, codecs
sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())

#import the string templating library to do allow us to separate the HTML code from the Python code
from string import Template

# use the CGI library to get any form data sent to the server from the client
form = cgi.FieldStorage() 

# validate that data has been submitted via the form...
if "your_name" not in form or "your_rating" not in form:
    # if the user did not enter form data, send the browser back to the form page
    # we do this by sending a special HTTP location header to the browser
    print("Location: ./4.form_example.html\n\n")
    #exit now!
    sys.exit()

#assuming the user entered form data, get the form data into simple variables
your_name = form.getfirst('your_name')
your_rating = form.getfirst('your_rating')

#load up the template
#open the template file and extract the contents
f = open('4.form_example_page_template.txt')
template = Template(f.read())

#set up the variables to plug into the template
data = {
    'name': your_name,
    'rating': your_rating
}

#plug the variables into the template to generate the complete HTML
html = template.substitute(data)

#output filled-in template
print(html)

