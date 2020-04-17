from flask import Flask, render_template, flash, redirect, url_for, session, request, logging
from flask_mysqldb import MySQL

app = Flask(__name__)

# Config MySQL
app.config.from_object('app.configuration.Config')

# init MYSQL
mysql = MySQL(app)

# Import routing, models and Start the App
from app import views