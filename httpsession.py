#!/usr/bin/python

import httplib

conn = httplib.HTTP('fr.wikibooks.org')

conn.putrequest('GET','http://fr.wikibooks.org/w/index.php?title=Programmation_Python_Le_r%C3%A9seau&action=edit')

conn.putheader('Accept','text/html')
conn.putheader('Accept','text/plain')
conn.putheader('User-Agent','Mozilla/5.0 (X11; U; Linux i686; fr; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3')

conn.endheaders()

errcode, errmsg, headers = conn.getreply()

print(errcode)
print(errmsg)
print(headers)

f=conn.getfile()
for line in f:
	print(line)

conn.close()
