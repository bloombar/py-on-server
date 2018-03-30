#!/usr/bin/env python3

#enable debugging... any errors will be output as HTML so they show up clearly in the web browser
import cgi, cgitb
cgitb.enable()

#make sure all output from the print statement in Python is utf-8 encoded
import sys, codecs
sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())

#import the string templating library to do allow us to separate the HTML code from the Python code
from string import Template

#determine the current version of python on this server
python_version = str(sys.version[0]) + "." + str(sys.version[2])

#open the template file and extract the contents
f = open('page_template.txt')
template = Template(f.read())

#set up the variables to plug into the template
data = {
 'title': "It's snowing",
 'heading': "Python works!",
 'python_version': python_version,
 'css_url': 'css/main.css',
 'link_url': "https://wiki.python.org/moin/Templating"
}

#plug the variables into the template to generate the complete HTML
html = template.substitute(data)

#output filled-in template
print(html)



