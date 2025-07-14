#!/usr/bin/python
from flask import Flask, render_template, request
import json
import csv


# Helper functions to read CSV or JSON
def load_from_json(filename="products.json"):
    try:
        with open(filename) as f:
            return json.load(f)
    except Exception:
        return []

def load_from_csv(filename="products.csv"):
    products = []
    try:
        with open(filename) as f:
            reader = csv.DictReader(f)
            for row in reader:
                row["id"] = int(row["id"])
                row["price"] = float(row["price"])
                products.append(row)
    except Exception:
        pass
    return products

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/items')
def items():
    try:
        with open("items.json") as f:
            data = json.load(f)
            items = data.get("items", [])
    except Exception as e:
        items = []
    return render_template('items.html', items=items)

@app.route('/products')
def products():
    source = request.args.get("source")
    id = request.args.get("id")
    error = None
    products = []

    if source == "json":
        products = load_from_json()
    elif source == "csv":
        products = load_from_csv()
    else:
        error = "Wrong source"
        return render_template("product_display.html", error=error, products=[])
    
    # ID filter if given
    if id:
        try:
            product_id = int(id)
            filtered = [p for p in products if int(p["id"]) == product_id]
            if not filtered:
                error = "Product not found"
            products = filtered
        except ValueError:
            error = "Invalid ID format"

    return render_template("product_display.html", products=products, error=error)

if __name__ == '__main__':
    app.run(debug=True, port=5001)
