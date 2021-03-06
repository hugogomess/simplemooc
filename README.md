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

3. Solve the dependencys:

  ```
  $ pip install -r requirements.txt
  ```

4. Create and config database

  ```
  $ python manage.py migrate --run-syncdb
  ```

5. Create a super user if you want get access to admin area (you need this to create a course)

  ```
  $ python manage.py createsuperuser
  ```

## Use

1. Inside the project root folder, run:

  ```
  $ python manage.py runserver
  ```

2. In your browser, open [http://localhost:8000](http://localhost:8000).

3. If you want create a course, open [http://localhost:8000/admin](http://localhost:8000/admin).

----------