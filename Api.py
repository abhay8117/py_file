# -*- coding: utf-8 -*-
"""
Create an api
    fetch data from csv
    id,title,price,year
@app.route('/all')
@app.route('/books/+year')
input json format start_year end_year
@app.route('/books/<int:id>')# bokk id
@app.route('/books/<int:year>') #year
@app.route('/books/<str:part of the title>')
@app.route('/books/')
    
#request.args
"""

import flask
from flask import request, jsonify

app= flask.Flask(__name__)
books=[
      {'id':1,
       'title': 'Emotion of Molecules',
       'Price': 310,
       'year':1990
        },
       {'id':2,
       'title': 'Biology of belief',
       'Price': 309,
       'year':2010
       }
       ]

@app.route('/',methods=['GET'])
def home():
    return'''Hello World'''

@app.route('/books/all',methods=['GET'])
def display_books():
    return jsonify(books)

@app.route('/books/<int:id_>')
def fetch_book(id_):
    book=books[id_]
    return jsonify(book)

@app.route('/books/post',methods=['POST'])
def add_book():
    title=request.json.get('title','')
    year=request.json.get('year','')
    price=request.json.get('price','')
    id_=len(books)+1
    book={'id':id_,
          'title':title,
          'year':year,
          'price':price
          }
    books.append(book)
    return jsonify(book)


if __name__== '__main__':
    app.run(debug=True)
 #   app.run(host='192.168.43.174',debug=True)