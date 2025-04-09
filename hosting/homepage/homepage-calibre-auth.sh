#!/bin/bash

# place file in homepage config folder

curl -Lvso /dev/null 'http://<address>:<port>/calibre/ajax/search' --digest -u <username>:<password> 2> .tenv 
sed '/Authorization/!d' .tenv | cut -c 3- > .env
