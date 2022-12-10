
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


### Git basics
```bash
# Jakieś zmiany zrobiliśmy. Git status wyświetla zmiany
git status
# Żeby dodać pliki (plusik w VS Code), a w terminalu
git add sciezka/do/pliku.txt jeszcze/jedna/sciezka.html
# lub 
git add -u
# zeby dodac wszystkie znane przez gita (tracked) pliki
# Co się stało? 
git status
# Zeby zrobic commit: 
git commit -S -m "Wiadomosc"
```