# xmlrpc-checker
Simple python implemetation of XMLRPC.php checking for SSRF / XSPA vulnerability using pingback.ping module and POST request

# Multiple targets:
+ Simple bash loop:
```
for i in $(cat rpc.txt);do python xmlrpcfinder.py $i;done
```

TODO:
1. pingback.ping exploitation with burp/hunter collaborator
