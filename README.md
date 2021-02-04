# autoproxy

simple client/server script to automatically update ip in a proxy config.

host = server with dynamic ip ( ex: your server at home)

proxy = server with static ip ( ex: cheap vps ) 

You need to run proxy.py continuously and host.py in a crontab ( ex: every 30 minutes )

template.txt contain your config file for the proxy ( the one given is for nginx )

In host.py and proxy you need to change the following:

HOST = "10.0.0.1" # the static ip ( your cheap vps )

PORT = "2943" # both need to be the same

SECRET = "supersecret" # to have a bit a security 
