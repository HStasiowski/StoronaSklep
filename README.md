
### Config
```
db: projectai
user: projectai
password: projectaipwd
```

### Start server
```
python manage.py makemigrations main
python manage.py sqlmigrate main 0001
python manage.py migrate
python manage.py runserver 0.0.0.0:8000
```