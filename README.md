# FastAPI Clean Architecture Scaffolding
[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)

This is a scaffolding project for FastAPI that includes an organized directory structure, based on the hexagonal architecture rules. 
Contains code templates, database integration, unit testing framework.
A guide to make it easy to start working on the project quickly and efficiently, speeding up development
time and improving software quality.


## TODO:

## 1. Project structure
Breve descripción de la estructura del proyecto, incluyendo los directorios y archivos principales.

## 2. Prerequisites
Lista de los requisitos necesarios para correr la aplicación, incluyendo las dependencias y las versiones de Python necesarias.

## 3. Setup
Pasos necesarios para instalar y configurar el entorno de desarrollo.
Pasos necesarios para configurar la aplicación, incluyendo la configuración de variables de entorno y la conexión a una base de datos.
```shell
pipenv install
```


## 4. Running app locally
Breve descripción de cómo utilizar la aplicación y ejemplos de cómo interactuar con ella.
```shell
uvicorn main:app --reload
```

## 5. Tests
Instrucciones para correr las pruebas automatizadas incluidas en el proyecto.

## Migrations
Create any table migration
```shell
docker-compose run app alembic revision -m "create users table"
```
Exceute migration
```shell
docker-compose run app alembic upgrade head
```



## 6. License
MIT-licensed open source project.

