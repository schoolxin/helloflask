# -*- coding: utf-8 -*-
"""
    :author: Grey Li (李辉)
    :url: http://greyli.com
    :copyright: © 2018 Grey Li
    :license: MIT, see LICENSE for more details.
"""
import click
from flask import Flask

app = Flask(__name__)  # 实例化Flask 这个类就得到了程序实例app

app.config['ADMIN_NAME'] = 'Peter'


# the minimal Flask application
@app.route('/')
def index():
    return '<h1>Hello, World2222!</h1>'



# bind multiple URL for one view function
@app.route('/hi')
@app.route('/hello')
def say_hello():
    return '<h1>Hello, Flask!</h1>'


# dynamic route, URL variable default
@app.route('/greet', defaults={'name': 'Programmer'})
@app.route('/greet/<name>')
def greet(name):
    return '<h1>Hello, %s!</h1>' % name


# custom flask cli command
@app.cli.command()
def hello():
    """Just say hello."""
    click.echo('Hello, Human!')
@app.cli.command('say_hello')
def hello():
    """Just say hello."""
    click.echo('Hello, Human!')
