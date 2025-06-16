# ElevateDB Setup Instructions


```bash
docker run --name pgdev -e POSTGRES_DB=elevate_db -e POSTGRES_USER=eval_user -e POSTGRES_PASSWORD=eval_password -p 5432:5432 -d postgres
```

then
```bash
docker exec -it pgdev psql -U eval_user -d elevate_db
```

# Django Project
```bash
python manage.py makemigrations
```

then,
```bash
python manage.py migrate
```


collectstatic will collect all static files from your Django apps and place them in the directory specified by the `STATIC_ROOT` setting in your Django settings file. This is necessary for serving static files in production.

```bash
python manage.py collectstatic
```