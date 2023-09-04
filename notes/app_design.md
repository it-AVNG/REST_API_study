# Overview
Recipe API can be the backend component and database of the 'Recipe app' which can be use to build Android and Ios or webapps
19 Api Endpoints: manage users, recipes, tags, ingredients
User authentication
Browseable API(Swagger) for testing
Browsable Admin Interface (Django Admin)

## Api Endpoints:
+  Health Check
+ Recipe ingredients (CRUD)
+ Recipes CRUD, has uploading image API
+ Tags CRUD API
+ Schema API for 
+ User API with tokens

## Technologies:
+ Django python with Rest framework
+ Database: PostgreSQL
+ Dockerized service for API and Databse
+ Swagger for documentation
+ GitHub Actions for Automation 
  + Testing and Linting

## project structure
+ `app` - Django Project
+ `app/core/` - code shared between multiple apps
+ `app/user/` - User related code
+ `app/recipe/` - recipe related code

# Create Secrets
In Dockerhub user setting, create new access token (it displays only once, so take note!)
In the project Github repos setting crete 2 variable to contains the secrets
+ DOCKERHUB_USER: username of dockerhub
+ DOCKERHUB_TOKEN: the token that we have just created

# Create Dockerfile and docker compose
## Dockerfike:
The file will help us with creating a docker imageL
+ choose a base python image
+ Install dependencies in the image
+ setup users

## Docker compose:
define how oue images should be used by define 'services':
+ Name of the service
+ port mapping
+ Volume mappings

run all commands through docker compose
```shell
docker-compose run --rm app sh -c "python manage.py collectstatic"
```
+ `--rm` tells docker composed to remove the container after it is run
+ `app` name of the service
+ `sh -c` passes in a shell command
