from flask import Flask, render_template, request, jsonify
import json
import random
import datetime

app = Flask(__name__)

# HOME

@app.route('/')
def home():

    with open('products.json', 'r') as file:
        products = json.load(file)

    return render_template('index.html', products=products)

# LOGIN

@app.route('/login')
def login():
    return render_template('login.html')

# SIGNUP

@app.route('/signup')
def signup():
    return render_template('signup.html')

# CREATE ORDER

@app.route('/create-order', methods=['POST'])
def create_order():

    data = request.json

    order_id = "VC" + str(random.randint(10000, 99999))

    order = {
        "order_id": order_id,
        "customer": data['customer'],
        "items": data['items'],
        "total": data['total'],
        "time": str(datetime.datetime.now())
    }

    try:
        with open('orders.json', 'r') as file:
            orders = json.load(file)
    except:
        orders = []

    orders.append(order)

    with open('orders.json', 'w') as file:
        json.dump(orders, file, indent=4)

    return jsonify({
        "success": True,
        "order_id": order_id
    })


if __name__ == '__main__':
    app.run(debug=True)