# ElevateDB Setup Instructions


```bash
docker run --name admin-DB -e POSTGRES_DB=elevate_db -e POSTGRES_USER=eval_user -e POSTGRES_PASSWORD=eval_password -p 5436:5432 -d postgres
```

then
```bash
docker exec -it admin-DB psql -U eval_user -d elevate_db
```

check if the user is created
```sql
\du
```




# Django Project
```bash
python manage.py makemigrations
```

then,
```bash
python manage.py migrate
```


then
```bash
python manage.py createsuperuser
```


```bash
python manage.py runserver
```

run the following command to clear the cache
```
python manage.py clear_cache --all
```

run the following command to pre-commit
```
pre-commit run --all-files
```
