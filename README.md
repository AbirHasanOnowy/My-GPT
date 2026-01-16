# My-GPT

A backend project to manage user prompt with or without image and give AI response.

It is a private project which is currently paused. We may resume it later. If you wish to contribute, you are welcome to go ahead and do so.

# Docker Commands

docker build command:

```
docker compose up --build -d
```

remove a compose build:

```
docker compose down -v
```

start from a new build:

```
docker compose up -d --build
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
