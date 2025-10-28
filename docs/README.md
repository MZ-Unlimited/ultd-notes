# Notes API

Notes API.

# Table of Contents

## Prerequisites

  - Make sure you have Docker Desktop installed in you computer.
  - Clone ultd-notes repository out of GitHub.

## Installation

  - After cloning the repository, `cd` to `ultd-notes` folder and create a virtual environment:
    - `python3.12 -m venv .venv`
      - This command will create an python virtual environment, and you will be able to install all of the projects requirements.
    - Run `source .venv/bin/activate`
    - Run `pip install invoke`.
      - This will install the tasks manager.
    - If there is no `requiremenst.txt` file in the `requirements` folder:
      - Run `inv pip-compile` this will compile the `requirements.txt` file.
    - Run `pip install -r requirements/requirements.txt`.
    - If everything worked as expected, you will enter the virtual environment context.

## Configuration
  - I am sending the `.env` file for quick reference, but this fils shouldn't be in git. if you can't find it:   
  - Copy and rename `example.env` to `.env`.
    - Make sure you set the correct database configuration in `.env`
    - From outside the docker container you can access the database using:
      - `DATABASE_URL=localhost`
      - `DATABASE_PORT=5432`
    - From inside the docker container your application should access:
      - `DATABASE_URL=notes-api-db`
      - `DATABASE_PORT=5432`

## Building and running the service
  - Now you can run `inv -l` and you will see a list of commands available in the project.
  - Run `inv build` - this should create your docker containers.
  - Run `inv run` to start all containers.
  - After running `inv run` everything should be installed, the database and the migration.
  - If you can't see the database or if the `note` table is not showing up, issue a `Ctrl+C` in your command prompt, but make sure you restart the database container.
  - Run `inv migrate`, this should create the database structure. You can now access the database using an external IDE.
    - If any errors are raised in the command prompt, run `inv db-upgrade` this should solve it.
    - If you can`t fix the problem, please reach out to fabio@ultd.ai

## Swagger
  - You can access swagger's information in `http://localhost:19000/docs/
  - In order to use Swagger's environment you will need to get the API KEY in the `config/base.py` file.
    - Add it to the Header section with the variable name `x-api-key`.
  - Go to postman and test the endpoints.
    
## Api
  - The API is built under the folder `services`. Feel free to look around and get a sense of how it is built.
    - In order to use the endpoints that are available you will need to add `x-api-key=API_KEY` to your header call.
    - Use this API Key `52b23c0a-cf59-48ef-be2f-921c45377ac8`

## Database configuration
  - If you need to access the database, you can do so by installing a PostgreSQL client/IDE in your computer.
  - Use `host=localhost`, `port=15440`, `user=postgres`, `pwd=AS_DEFINED_IN_YOU_ENV_FILE`.
  - Please remember that you must configure is it your `.env` file.

## The API is deployed at https://notes.ultd.ai
