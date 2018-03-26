#!/usr/local/bin/python3

#enable debugging... any errors will be output as HTML so they show up clearly in the web browser
import cgi, cgitb
cgitb.enable()

#make sure all output from the print statement in Python is utf-8 encoded
import sys, codecs
sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())

#determine the current version of python on this server using the sys library
python_version = str(sys.version[0]) + "." + str(sys.version[2])

#send raw HTTP headers to browser
#NOTE: this must be the first thing sent to the web browser
print("Content-type: text/html;charset=utf-8")
print("\n\n")  #two line breaks indicates the end of the headers

#send body content to browser
#NOTE: this must follow two line breaks separating it from the headers
print('''
<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8" />
        <title>It's snowing</title>
        <link rel="stylesheet" type="text/css" href="css/main.css" />
    </head>
    <body>
        <div class="container">
            <h1>Python works</h1>
            <p>This script was executed by the Python {version} interpreter on the web server.  The output was sent to the web browser.</p>
            <p>
                Running Python from the web is what's called a CGI script.  See <a href="https://docs.python.org/3.5/library/cgi.html">for info on Python's support for CGI</a>.
            </p>
            <p>
                A popular framework for simplifying server-side Python for web applications is <a href="http://flask.pocoo.org/">Flask</a>.  We are not using that here.
            </p>
        </div>
    </body>
</html>
'''.format(version=python_version))


