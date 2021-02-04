# autoproxy

simple client/server script to automatically update ip in a proxy config.

host = server with dynamic ip ( ex: your server at home)

proxy = server with static ip ( ex: cheap vps ) 

You need to run proxy.py continuously and host.py in a crontab ( ex: every 30 minutes )

template.txt contain your config file for the proxy ( the one given is for nginx )
