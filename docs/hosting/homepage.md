---
title: homepage
layout: w-nav
---

# homepage

I'm using [gethomepage/homepage](https://github.com/gethomepage/homepage). This is a very aesthetic yet simple homepage.

## Service Widgets

I used customapi for two widgets (soon to be three):

* Trilium
* tt-rss
* calibre (under works)

### Trilium

Trilium was the easiest to set up. It had a well-documented api ([official](https://github.com/zadam/trilium/blob/master/src/etapi/etapi.openapi.yaml), [Trilium Rocks](https://trilium.rocks/etapi)) and uses an app token.

```
        widget:
          type: customapi
          url: http://<address>:<port>/trilium/etapi/app-info
          refreshInterval: 9000000000   # random big number to avoid refreshing too often
          method: GET                   # not necessary
          headers:
            Authorization: <etapi_token>
          mappings:
            - field: appVersion
              label: Version
```

This simply displays the app version.

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

tt-rss uses a session id (sid) to authenticate.

You can 'login' and get a sid using curl. Below is from tt-rss official [api docs](https://tt-rss.org/ApiReference/#testing-api-calls-using-curl).

```
curl -d '{"op":"login","user":"you","password":"xxx"}' http://example.com/tt-rss/api/
```

This widget config shows the number of unread articles.

```
        widget:
          type: customapi
          url: http://<address>:<port>/tt-rss/api
          refreshInterval: 900000 			# 15 min, tt-rss' refresh interval
          method: POST
          requestBody: 
            sid: <sid>						# obtained using curl 
            op: getUnread
          mappings:
            - field: content.unread
              label: Unread
              format: number
```

### calibre

Homepage has a built-in widget for calibre-web, but not one for the calibre content server. The difficulty with this is that I'm using digest authentication (because I'm not using https), which means that the authentication header requires constant update because the nonce becomes stale. The timeout for the nonce is an hour according to calibre's source code [\[x\]](https://github.com/kovidgoyal/calibre/blob/206307993ca9f88e422d12a218bf6390643743a9/src/calibre/srv/auth.py).

```
# line 22 src/calibre/srv/auth.py
MAX_AGE_SECONDS = 3600
```

The API uses AJAX, defined in [src/calibre/srv/ajax.py](https://github.com/kovidgoyal/calibre/blob/master/src/calibre/srv/ajax.py).

This shows the numbers of books in the default Calibre library.

```
        widget:
          type: customapi
          url: http://<address>:<port>/calibre/ajax/search
          refreshInterval: 2629746000		# one month
          method: GET
          headers:
            Authorization: Digest username="<...> # obtained by putting the api url in the browser and copying the authorisation header
          mappings:
            - field: num_books_without_search
              label: '# of books'
```