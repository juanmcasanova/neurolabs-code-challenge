# Neurolabs code challenge

Challenge:

>     1. Create a web app with a dedicated front and backend (React & FastAPI).
>     2. Save data in a single table and display it on the frontend.
>
> This task should be a starting point of development. We want to see how you tackle different application development topics. If time is an issue on your end, we can also work with projects you have been working on before, however providing us with a GitHub repo before the interview will help us greatly. We expect certain topics to be addressed without us explicitly listing them for this assignment. Feel free to have open pitfalls where you might not have an answer right away. We want to know that your awareness towards application development does not only evolve around features.

## Installation

With this repository comes a provided configuration for a [Docker Compose stack](docker-compose.yml), which is the
recommended way of executing it (which also will integrate the project with VS Code Remote Containers).

It still can be executed outside of Docker, but you will have to provide the basic requirements:

- NodeJS 18
- Python 3.9
- A database

### Backend

For the backend, you will have to install the dependencies, execute the migrations and start the server:

```bash
cd backend
pipenv install
pipenv shell
alembic upgrade head
cd ..uvicorn backend.main:app --reload

```

### Frontend

For the frontend, you only have to install the dependencies and start the server:

```bash
cd frontend
npm i
npm start
```

## Tests

### Backend

To execute the test for the FastAPI application, you simple execute (inside the Python environment):

```bash
cd backend
pytest
```

### Frontend

To execute the test for the React application, you simple execute:

```bash
cd frontend
npm test
```

Note: You may have to press "a" if you already run the tests.

## Problems with the apps

Although I'm sure there are lots of additional problems, these are the ones due to time constraints:

- The management and command executions for the applications is more complex than I would like it to be (although this
is mainly because there are two different projects in the same repository).
- The frontend loads a maximum of 1000 movies instead of paginating the data.
- There are almost no test for the frontend.
- The backend tests use the same database as the actual app execution, leaving a lot of dummy rows in it.
