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
from fastapi.responses import RedirectResponse
from fastapi.middleware.cors import CORSMiddleware

from .database import Base, engine
from .routers import movies

# sqlalchemy initialization
Base.metadata.create_all(bind=engine)

# Create the main app instance
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_methods=["*"],
    allow_headers=["*"]
)
app.include_router(movies.router)


@app.get("/")
async def root() -> dict:
    """Main endpoint.

    Redirects the user to the OpenAPI documentation.
    """
    return RedirectResponse("/docs")


if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=8000)
