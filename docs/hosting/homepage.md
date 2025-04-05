---
title: homepage
---

# homepage

This is a very aesthetic yet simple homepage.

## Service Widgets

I used customapi for two widgets (soon to be three):

* Trilium
* tt-rss
* calibre (under works)

### Trilium

Trilium was the easiest to set up. It had a well-defined api and uses an app token.

### tt-rss

This one took me ages to figure out the error. I thought I was setting up my reverse proxy wrong, and I did technically. The tt-rss api endpoint requires a trailing slash, while homepage sanitises the trailing slash away. I couldn't find out a better way to handle this, so my nginx config looks like this:

```
server{
    <server config>

    location /tt-rss/ {
        proxy_pass http://127.0.0.1:<port>$request_uri;
    }
    location /tt-rss/api {
        proxy_pass http://127.0.0.1:<port>/tt-rss/api/;
    }
```

### calibre

Homepage has a built-in widget for calibre-web, but not one for the calibre content server. The difficulty with this is that I'm using digest authentication (because I'm not using https), which means that the authentication header requires constant update because the nonce becomes stale. The timeout for the nonce is an hour according to calibre's source code [\[x\]](https://github.com/kovidgoyal/calibre/blob/206307993ca9f88e422d12a218bf6390643743a9/src/calibre/srv/auth.py).

```
# line 22 src/calibre/srv/auth.py
MAX_AGE_SECONDS = 3600
```