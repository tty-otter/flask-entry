from flask import Flask
app = Flask(__name__)
import flask_entry.main

from flask_entry import db
db.create_books_table()
