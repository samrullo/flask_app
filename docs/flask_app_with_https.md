# How it works
I followed mainly 3 resources below
- https://mindsers.blog/post/https-using-nginx-certbot-docker/
- https://rlagowski.medium.com/create-flask-app-with-uwsgi-nginx-certbot-for-ssl-and-all-this-with-docker-a9f23516618d
- https://pentacent.medium.com/nginx-and-lets-encrypt-with-docker-in-less-than-5-minutes-b4b8a60d3a71

As we know nginx looks up configurations in ```/etc/nginx/conf.d``` folder.
There the default file it loads first is ```nginx.conf```.
```nginx.conf``` defines ```server``` block, where it routes the client to a named location ```@app```.
Named locations like ```@app``` preserver $uri before entering that location.
Flask app leverages uwsgi.ini to serve flask application routes.

Anyways, it seems like nginx reads app.conf as well if it exists.
And that's where all the stuff related to ```letsencrypt``` is configured.
In ```app.conf``` we define two server blocks.
The first one re-routes http requests to https, except requests to ```/.well-known/acme-challenge/```.
This is the endpoint from where ```certbot``` validates the domain.


The second server block processes https requests.
It defines named location @app again and serves flask application based on uwsgi.ini config.
It also defines ```ssl_certificate``` and ```ssl_certificate_key``` which probably certbot uses for validating the domain.
