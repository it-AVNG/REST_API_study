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

