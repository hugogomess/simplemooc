# Simplemooc

An online course platform!

## Dependencies

First of all, you need to have installed [Python 3.7.3](https://www.python.org/downloads/) and [Pip](https://pip.pypa.io/en/stable/installing/) on your machine, you must also have the [git](https://git-scm.com/downloads) installed to get this code.

To check the dependencies, use the commands `$ python --version`, `$ pip --version` and `$ git --version` on terminal.

## Installation

1. First clone this repository:

  ```
  $ git clone git@github.com:hugogomess/simplemooc.git
  ```

2. Go to the project directory:

  ```
  $ cd simplemooc
  ```

3. Solve the dependency of the modules with:

  ```
  $ python manage.py migrate
  ```

## Use

1. Inside the project root folder, run:

  ```
  $ python manage.py runserver
  ```

2. In your browser, open [http://localhost:8000](http://localhost:8000).

----------