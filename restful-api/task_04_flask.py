#!/usr/bin/python3
'''
This module provides a certain number of routes defining a simple
Flask API for a basic server.
'''
from flask import Flask, jsonify, request


app = Flask(__name__)
users = {}


@app.route('/')
def home():
    return jsonify({"message": "Welcome to the Flask API!"}), 200


@app.route('/data')
def users_list():
    return jsonify(list(users.keys())), 200


@app.route('/status')
def return_status():
    return jsonify({"status": "OK"}), 200


@app.route('/users/<username>')
def get_username(username):
    user = users.get(username)
    if user:
        return jsonify(user)
    else:
        return jsonify({"error": "user not found"}), 404


@app.route('/add_user', methods=['POST'])
def add_user():
    data = request.get_json()
    if not data or not data.get('username'):
        return jsonify({"error": "username is needed"}), 400
    new_user = {
        "username": data["username"],
        "name": data["name"],
        "age": data["age"],
        "city": data["city"]
    }
    users[data["username"]] = new_user

    return jsonify({
        "message": "User added succesfully",
        "user": new_user
    }), 201


if __name__ == "__main__":
    app.run()
