<h1 align="center">flask-blog 👋</h1>
<p align="center">
  <img alt="Version" src="https://img.shields.io/badge/version-1.0.0-blue.svg?cacheSeconds=2592000" />
  <a href="https://github.com/alphaolomi/flask-blog#readme" target="_blank">
    <img alt="Documentation" src="https://img.shields.io/badge/documentation-yes-brightgreen.svg" />
  </a>
  <a href="https://github.com/alphaolomi/flask-blog/graphs/commit-activity" target="_blank">
    <img alt="Maintenance" src="https://img.shields.io/badge/Maintained%3F-yes-green.svg" />
  </a>
  <a href="https://github.com/alphaolomi/flask-blog/blob/master/LICENSE" target="_blank">
    <img alt="License: MIT" src="https://img.shields.io/github/license/alphaolomi/flask-blog" />
  </a>
</p>

Simple application with authentication and CRUD functionality using the Python Flask micro-framework

### Links

🏠 [Homepage](https://github.com/alphaolomi/flask-blog#readme)

## Dashboard Features:

- SQLite, MySQL, SQLAlchemy ORM
- Alembic (DB schema migrations)
- Modular design with **Blueprints**
- Session-Based authentication (via **flask_login**)
- Forms validation
- Deployment scripts: Docker, Gunicorn
- UI Kit: **[Bootstrap](https://getbootstrap.com/)**
- **MIT License**


## Prerequisite


- [Python 3](https://python.org)
- [Pip Package Manager](https://pypi.python.org/pypi)


## How to use it

```bash
# Virtualenv modules installation (Unix based systems)
virtualenv --no-site-packages env
source env/bin/activate

# Virtualenv modules installation (Windows based systems)
# virtualenv --no-site-packages env
# .\env\Scripts\activate

# Install modules - SQLite Database
pip3 install -r requirements.txt

# Set the FLASK_APP environment variable
# (Unix/Mac) export FLASK_APP=run.py
# (Windows) set FLASK_APP=run.py
# (Powershell) $env:FLASK_APP = ".\run.py"
export FLASK_APP=run.py
# Set up the DEBUG environment
# (Unix/Mac) export FLASK_ENV=development
# (Windows) set FLASK_ENV=development
# (Powershell) $env:FLASK_ENV = "development"
export FLASK_ENV=development

# Start the application (development mode)
# --host=0.0.0.0 - expose the app on all network interfaces (default 127.0.0.1)
# --port=5000    - specify the app port (default 5000)
flask run --host=0.0.0.0 --port=5000

# Access the dashboard in browser: http://127.0.0.1:5000/
```

<br />

## Deployment

The app has a basic configuration to be executed in [Docker](https://www.docker.com/), [Gunicorn](https://gunicorn.org/), and [Waitress](https://docs.pylonsproject.org/projects/waitress/en/stable/).

<br />

### [Docker](https://www.docker.com/) execution

---

The application can be easily executed in a docker container. The steps:

> Get the code

```bash
git clone
cd flask-blog
```

> Start the app in Docker

```bash
sudo docker-compose pull &&\
 sudo docker-compose build &&\
  sudo docker-compose up -d
```

Visit `http://localhost:5005` in your browser. The app should be up & running.

<br />

### [Gunicorn](https://gunicorn.org/)

---

Gunicorn 'Green Unicorn' is a Python WSGI HTTP Server for UNIX.

> Install using pip

```bash
pip install gunicorn
```

> Start the app using gunicorn binary

```bash
gunicorn --bind 0.0.0.0:8001 run:app
# Serving on http://localhost:8001
```

Visit `http://localhost:8001` in your browser. The app should be up & running.


### [Waitress](https://docs.pylonsproject.org/projects/waitress/en/stable/)

---

Waitress (Gunicorn equivalent for Windows) is meant to be a production-quality pure-Python WSGI server with very acceptable performance. It has no dependencies except ones that live in the Python standard library.

> Install using pip

```bash
$ pip install waitress
```

> Start the app using [waitress-serve](https://docs.pylonsproject.org/projects/waitress/en/stable/runner.html)

```bash
waitress-serve --port=8001 run:app
# Serving on http://localhost:8001
```

Visit `http://localhost:8001` in your browser. The app should be up & running.

<br />

## Author

👤 **Alpha Olomi <alphaolomi@gmail.com>**

* Website: https://alphaolomi.me
* Github: [@alphaolomi](https://github.com/alphaolomi)

## 🤝 Contributing

Contributions, issues and feature requests are welcome!<br />Feel free to check [issues page](https://github.com/alphaolomi/flask-blog/issues). You can also take a look at the [contributing guide](https://github.com/alphaolomi/flask-blog/blob/master/CONTRIBUTING.md).

## Show your support

Give a ⭐️ if this project helped you!

## 📝 License

Copyright © 2020 [Alpha Olomi <alphaolomi@gmail.com>](https://github.com/alphaolomi).<br />
This project is [MIT](https://github.com/alphaolomi/flask-blog/blob/master/LICENSE) licensed.

<br />

## Credits & Reference Links



- [Flask](https://www.palletsprojects.com/p/flask/) is a lightweight WSGI web application framework.
- https://www.digitalocean.com/community/tutorials/how-to-structure-large-flask-applications
- https://flask.palletsprojects.com/en/1.1.x/
- https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world
