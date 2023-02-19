import os

# Load the .env file(s)
# Doing it this way allows us to have a .env.local file with secrets, but keep a base
# .env with basic configuration that should make the applicacion run without changes
# TODO: Currently this has to be done before the imports because of how the database
#       initialization works, but we should try to make it so it doesn't really matter
from dotenv import load_dotenv
load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), '.env.local'))
load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), '.env'))

import uvicorn

from fastapi import FastAPI

from .database import Base, engine
from .routers import movies

# sqlalchemy initialization
Base.metadata.create_all(bind=engine)

# Create the main app instance
app = FastAPI()

app.include_router(movies.router)

@app.get("/")
async def root() -> dict:
    """Example root endpoint.

    This is only a placeholder.
    """
    return {"message": "It works!"}

if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=8000)
