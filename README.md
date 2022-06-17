# Alar

A demo project to show basic usage of FastAPI and docker.
Only FastAPI and SQLALchemy specific libraries used.

## Usage

1. copy content of .env.example to .env
2. run `docker-compose up -d`

#### Common
Most of the configuration cam be made via environment variables.

Default app external port is 8080, but can be changed via `APP_EXTERNAL_PORT` environment variable.

With default port, you can see documentation at: http://localhost:8080/docs

Feel free to press 'Try it out' button in the documentation to see the app in action.

#### Data example

Example of pulling data from multiple remote sources. All three sources are 
launched in separate containers. After asynchronously collecting data from all sources, 
application sorts items by id return sorted list.

* Data view: http://localhost:8080/api/v1/data

Changing `.env` file you can configure:
* External ports of remote a source: `DATA_PORT1`...
* Delay for responding to incoming request: `DATA_DELAY1`.. in seconds

:godmode: Files in folder `/test_data` are the files that contains data that is used in demo.
Feel free to change them. All changes are dynamically reflected in the demo.


#### Users example

Simple app to manage users. Supports:
* User list view: http://localhost:8080/api/v1/users
* User detail view: http://localhost:8080/api/v1/users/<user_id>
* Creating, Updating and Deleting users

Sadly I didn't have time to implement authorization and login.

_Development trick: you can change code without relaunching the container. 
Source code is volumed to container._

## TODO:
Things I wish I could do if I had time:
- authorization
- tests
- CI
- front
