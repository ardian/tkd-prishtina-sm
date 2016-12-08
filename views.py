import sqlite3
from functools import wraps

from flask import Flask, flash, redirect, render_template, \
    request, session, url_for, g


def connect_db():
    return sqlite3.connect(app.config['DATABASE_PATH'])
