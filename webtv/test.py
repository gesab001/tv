#!/home/python
import cgi
import cgitb
cgitb.enable()

form = cgi.FieldStorage()

keyword = form.getvalue('keyword')

print 'Content-type: text/html\r\n\r'
print '<html>'
print keyword
print '</html>'