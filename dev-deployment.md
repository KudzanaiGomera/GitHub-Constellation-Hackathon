# Summary:
- This documentation serves as a guide to for development delpoyment for the project.

# Setting up the project:

## create virtual environment
    python -m venv ./venv
## change directory to venv\Scripts
    cd venv\Scripts
## activate your environment
    activate

ref source: https://www.geeksforgeeks.org/create-virtual-environment-using-venv-python/   

# Installing Django:

## else Installing
    py -m pip install Django

## verify if Django already exists
    py -m django --version

source: https://docs.djangoproject.com/en/5.0/topics/install/

# Installing Requirements:

## First Freeze pip

    <!--pip freeze > requirements.txt-->

    pip install -r requirements.txt

ref source: https://stackoverflow.com/questions/66899666/how-to-install-from-requirements-txt

# Running server:

## make sure you are in dir where manage.py is and run below
    py manage.py runserver
ref source: https://docs.djangoproject.com/en/5.0/intro/tutorial01/

# Testing Creds:

## Test User:
- create new user

## Test Admin:
- create new admin

## Testing Debt Card: 
    number: 4111 1111 1111 1111
    exp: 01/25
    cvv: 111
    zip:11111
ref source: https://developer.squareup.com/docs/devtools/sandbox/payments

Happy Coding
