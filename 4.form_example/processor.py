#!/usr/bin/env python3

# make sure this file is executable by others

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
interests = form.getfirst("interests")
ok_terms = form.getfirst("ok_terms")
ok_spam = form.getfirst("ok_spam")
ok_social = form.getfirst("ok_social")

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
			<li>Ok spam: {ok_spam}</li>
			<li>Ok social: {ok_social}</li>
			<li>Ok terms: {ok_terms}</li>
		</ul>
	</body>
</html>
'''.format(name=name, email=email, password=password, interests=interests, ok_spam=ok_spam, ok_terms=ok_terms, ok_social=ok_social))


