# FASTAPI PROJECT SETUP

python --version

mkdir fastapi_project

cd fastapi_project

python -m venv venv

## Windows

venv\Scripts\activate

## Linux / macOS

source venv/bin/activate

## Install fastapi and uvicorn

pip install fastapi uvicorn

## Run the Server

uvicorn main:app --reload
uvicorn app.main:app --reload

## Fatal error in launcher: Unable to create process using

First, ensure you're in the correct virtual environment
python -m pip uninstall uvicorn -y
python -m pip install uvicorn

`main` → file name

`app` → FastAPI instance

`-reload` → auto-restart on changes

## Open in Browser

API: 👉 [http://127.0.0.1:8000](http://127.0.0.1:8000/)

Swagger Docs (auto): 👉 <http://127.0.0.1:8000/docs>

ReDoc: 👉 <http://127.0.0.1:8000/redoc>

## Generate dependencies file

pip freeze > requirements.txt
