# FastAPI Clean Architecture Scaffolding
[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)

This is a scaffolding project for FastAPI that includes an organized directory structure, based on the hexagonal architecture rules. 
Contains code templates, database integration, unit testing framework.
A guide to make it easy to start working on the project quickly and efficiently, speeding up development
time and improving software quality.


## Project structure
```shell
alembic/                                # folder to aggregate all database migrations generated with alembic library
├── versions/                           # migrations folder
├── env.py                              # file to confige data base connection and format and structure migrations
src/                                    # root folder of the project source code. Each folder within this is a infrastructure component
├── app/                                # principal component dedicated to application configution (database, enviroment variables, ...)
    ├── application/                    # folder to add application specific logic (uses cases)adn DTOs files 
    ├── domain/                         # folder to add interfaces to access to business objects (repositories) and infrastructure entities (mappers)
    ├── infrastructure                  # folder to add adapters to connecto with differents interfaces types (database services, web services, notification services, ...)
        ├── db/                         
            ├── alembic_common.py       # common functions to add column fields in the alembic migrations
            ├── postgresql_connect.py   # postgresql database connection
        ├── routes/                     # folder to add route versions
            ├── v1/
                ├── health_checks.py    # routes to application liveness test
        translate.py                     # configuration file for environment variables and others
├── auth/                               # authentication component
    ├── application/
        ├── auth_facebook_user_dto.py       # DTO class with attributes to receive data of facebook when be authenticated
        ├── facebook_user_autheticator.py   # interactor class with logic to facebook authenticate
        ├── generate_user_token.py          # interactor class to generate token
        ├── validate_user_token.py          # interactor class to validate token
    ├── domain/
        ├── auth_provider.py                # mapper class to specificate authentication providers
        ├── auth_repository.py              # interface to add method to create and search users registrated
    ├── infrastructure/
        ├── routes/
            ├── v1/
                ├── auth_routes.py          # routes to register and authenticate with facebook
        ├── auth_depends.py                 # authentication functions to add as dependency injection in routes and can use the interactor class 
        ├── auth_token_model.py             # token models implemented with pydantic ORM library
        ├── auth_user_model.py              # user model implemented with pydantic ORM library
        ├── user_profile_entity.py      # user profile model implemented with pydantic ORM library
        ├── postgres_auth_repository.py     # repository class to create and search users registrated with postgresql
tests/
    ├──
.env.test
.gitignore                                  # a file that list files to be excluded in GitHub repository
alembic.ini                                 # Automatic database migration configuration
docker-compose.yml                          # docker-compose configuration file
Dockerfile                                  # Docker configuration file
LICENSE.md                                  # A license to use this template repository (delete this file after using this repository)
main.py                                     # Our main backend server app
Pipfile                                     # dependencies to install and run project into virtual enviroment (Pipenv)
Pipfile.lock                                # file generated automatically by Pipenv
Procfile                                    # file to define process and commands to run in Heroku platform
README.md                                   # The main documentation file for this template repository
requirements.txt                            # Packages installed
```
## Prerequisites
Before running the project, ensure that you have the following prerequisites installed:

* [Docker](https://www.docker.com/)

* [Docker Compose](https://www.docker.com/)

## Getting Started

To get started with the project, follow these steps:

1. Clone the repository. 
2. The project can be configured using environment variables. The following environment variables are available:

`APP_NAME`: Application name

`API_VERSION`: Current version of application 

`FB_CLIENT_ID`: Facebook clint Id to enable login (https://developers.facebook.com/apps)

`FB_CLIENT_SECRET`: Facebook application secret key (https://developers.facebook.com/apps)

`FB_REDIRECT_URI`: api url of the application to redirect and obtain the session data by facebook

`ACCESS_TOKEN_EXPIRE_MINS`: time in seconds for session token expiration

`ACCESS_TOKEN_SECRET_KEY`: secret key for session token generation

## Running app locally
Run docker-compose up to build and start the containers.

```shell
docker-compose up --build
```

## How to run Migrations
1. Create any table migration
```shell
docker-compose run [app service] alembic revision -m "create users table"
```
2. Exceute migration
```shell
docker-compose run [app service] alembic upgrade head
```

## License
MIT-licensed open source project.
