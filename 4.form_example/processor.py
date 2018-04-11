#!/usr/bin/env python3

#enable debugging... any errors will be output as HTML so they show up clearly in the web browser
import cgi, cgitb
cgitb.enable()

#make sure all output from the print statement in Python is utf-8 encoded
import sys, codecs
sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())

# use the CGI library to get any form data sent to the server from the client
form = cgi.FieldStorage() 
name = form.getfirst("name")
email = form.getfirst("email")
password = form.getfirst("password")

print('''Content-type: text/html

<!doctype html>
<html lang="en">
	<body>
		<h1>Got the following data from the browser:</h1>
		<ul>
			<li>Name: {name}</li>
			<li>Email: {email}</li>
			<li>Password: {password}</li>
			<li>Interests: {interests}</li>
		</ul>
	</body>
</html>
'''.format(name=name, email=email, password=password))
	
