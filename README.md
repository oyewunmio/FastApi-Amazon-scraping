
## Setting up your development environment

### Installing the libraries
At the same directory as this file, run:
  - `pip install pipenv`
  - `pipenv install`

### Running the API for development
Initialize your app using `pipenv`:

- `pipenv shell`

Then run the following commands:

- `uvicorn app.main:app --reload`

And your app will be running on http://localhost:8000/

Tip:

Access http://localhost:8000/docs to use the built-in interface.


The app is available through a rest API.
  API
    - Allow the user to get a list of all products from the e-commerce platform, and present them in a structured way.
    - Allows user to list only the best-selling products from the e-commerce sites.
    - Allows user to list only the products with a rating higher than a given value.

