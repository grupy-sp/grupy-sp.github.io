Process to deploy a page:

> $ pelican content -o output -s pelicanconf.py

> $ ghp-import output

> $ git push git@github.com:grupy-sp/grupy-sp.github.io.git gh-pages:master
