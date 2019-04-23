from flask import Flask
app=Flask(__name__)

import sqlite3

from flask import render_template

from flask import jsonify

import random

random_list=[1]

@app.route('/douban_movie')
def show_douban_movie():
    connect = sqlite3.connect('douban_move.db')
    cursor = connect.cursor()
    cursor.execute('select cover from douban_move limit 50')
    urls = cursor.fetchall()
    urls = [url[0] for url in urls]
    connect.close()
    return render_template('douban_movie.html',urls=urls)

@app.route('/random_choice',methods={'GET'})
def get_random_choice():
    return jsonify(random_result=random.choice(random_list))

@app.route('/random_choice/<input>',methods={'POST'})
def add_random_choice(input):
    random_list.append(input)
    return jsonify(result=1)

for i in range(10):
    print(i)
