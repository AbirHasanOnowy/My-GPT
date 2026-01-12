# My-GPT

A backend project to manage user prompt with or without image and give AI response.

docker build command:

```
docker compose up --build -d
```

check backend log:

```
docker compose logs -f backend
```

restart backend:

```
docker compose restart backend
```

run alembic inside docker:

```
docker compose exec backend alembic upgrade head
```
