import json
from flask import Flask, jsonify, request
from auth_service import AuthService
from dotenv import load_dotenv
import os
from flask_cors import CORS

load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('JWT_SECRET_KEY')

CORS(app)

@app.route('/api/login', methods=['POST'])
def authenticate_user():
    data = request.json
    response = AuthService.login(data['username'], data['password'])
    return response

@app.route('/api/createUser', methods=['POST'])
def create_user():
    data = request.json
    response = AuthService.createUser(data['name'],data['username'], data['password'])
    return response

@app.route('/api/listUsers', methods=['GET'])
def list_users():
    return AuthService.listUsers()

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0', port=5001)
