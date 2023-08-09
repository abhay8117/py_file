import sqlite3
from flask import Flask, request, jsonify

"""
import os
import psycopg2
"""

app = Flask(__name__)

"""
# Get database credentials from environment variables (set these in your AWS environment)
db_host = os.environ.get('DB_HOST')
db_name = os.environ.get('DB_NAME')
db_user = os.environ.get('DB_USER')
db_password = os.environ.get('DB_PASSWORD')

# Function to connect to the PostgreSQL database
def get_db():
    conn = psycopg2.connect(host=db_host, dbname=db_name, user=db_user, password=db_password)
    return conn

# Rest of the API endpoints and code similar to the code
"""

DATABASE = 'customer.db'

def get_db():
    db = getattr(app, '_database', None)
    if db is None:
        db = app._database = sqlite3.connect(DATABASE)
    return db

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(app, '_database', None)
    if db is not None:
        db.close()

@app.route('/customers', methods=['GET'])
def get_customers():
    db = get_db()
    cursor = db.cursor()
    cursor.execute('SELECT * FROM customers')
    customers = cursor.fetchall()
    cursor.close()
    return jsonify(customers)

@app.route('/customers/<int:id>', methods=['GET'])
def get_customer(id):
    db = get_db()
    cursor = db.cursor()
    cursor.execute('SELECT * FROM customers WHERE id=?', (id,))
    customer = cursor.fetchone()
    cursor.close()
    if customer:
        return jsonify(customer)
    else:
        return jsonify({'message': 'Customer not found'}), 404

@app.route('/customers', methods=['POST'])
def add_customer():
    data = request.get_json()
    name = data.get('name')
    email = data.get('email')
    phone = data.get('phone')

    db = get_db()
    cursor = db.cursor()
    cursor.execute('INSERT INTO customers (name, email, phone) VALUES (?, ?, ?)', (name, email, phone))
    db.commit()
    cursor.close()
    return jsonify({'message': 'Customer added successfully'}), 201

@app.route('/customers/<int:id>', methods=['PUT'])
def update_customer(id):
    data = request.get_json()
    name = data.get('name')
    email = data.get('email')
    phone = data.get('phone')

    db = get_db()
    cursor = db.cursor()
    cursor.execute('UPDATE customers SET name=?, email=?, phone=? WHERE id=?', (name, email, phone, id))
    db.commit()
    cursor.close()
    return jsonify({'message': 'Customer updated successfully'})

@app.route('/customers/<int:id>', methods=['DELETE'])
def delete_customer(id):
    db = get_db()
    cursor = db.cursor()
    cursor.execute('DELETE FROM customers WHERE id=?', (id,))
    db.commit()
    cursor.close()
    return jsonify({'message': 'Customer deleted successfully'})

if __name__ == '__main__':
    app.run(debug=True)