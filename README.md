CSB 2020 project

```
python3 manage.py migrate
python3 manage.py createsuperuser --username=bob --email=bob@squared.com
*enter password for the test user* (for example squarepants)
python3 manage.py createsuperuser --username=alice --email=alice@redman.com
*enter password for the second test user* (for example redqueen)
python3 manage.py runserver
```

The web app is now running at localhost:8000