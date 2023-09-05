# config
To set the db for our docker container, we use docker compose
Docker compose helps our system to have consistance connection with database
in `services:app:` we set `depends_on:` to `db` to start db first
add `services:db:` and we set our docker compose image to `postgres:`

# volumes:
persistant data
Maps directory in container to local machine
in `db` services, add `volumes` name to location of the database

add `volumes` and configure the names of our database

# postgres configure

The db environment will be set on local machine and change it to production later
```yml
version: "3.9"

services:
  app:
    build:
      context: .
      args:
        - DEV=true
    ports:
      - "8000:8000"
    volumes:
      - ./app:/app
    command: >
      sh -c "python manage.py runserver 0.0.0.0:8000"
    environment:
      - DB_HOST=db
      - DB_NAME=devbb
      - DB_USER=devuser
      - DB_PASS=changeme
    depends_on:
      - db

  db:
    image: postgres:13-alpine
    volumes:
      - dev-db-data:/var/lib/postgresql/data
    environment:
      - POSTGRES_DB=devbb
      - POSTGRES_USER=devuser
      - POSTGRES_PASSWORD=changeme


volumes:
  dev-db-data:
```

# Configure Django
+ Tell Django how to connect
+ Install database adaptor dependencies, i.e tools django uses to connect to our database
+ update requirement.

We have to provide in settings.py:
+ Engine: type of the databae
+ hostname: IP or domainname for database
+ Port : for postgres, use default
+ Database Name
+ username
+ password

## Environment variable
+ pull config values from environment variables
+ Easily passed to Docker
+ used in local dev (or Prod)

