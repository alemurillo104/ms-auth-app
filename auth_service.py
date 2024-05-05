import jwt
import datetime
import os
from flask import jsonify
import mysql.connector

class AuthService:
    def login(username, password):
        db=mysql.connector.connect(host=os.getenv('DB_HOST'), 
                            user=os.getenv('DB_USER'), 
                            passwd=os.getenv('DB_PASSWD'), 
                            database=os.getenv('DB_DATABASE'))

        dbCursor = db.cursor()
        query = 'SELECT * FROM user WHERE username = %s AND password = %s'
        dbCursor.execute(query, (username, password))
        dato = dbCursor.fetchall()
        db.close() 
        return jsonify({'ok': True, 'dato': dato})

        # if username == 'admin' and password == 'password':
        #     # Crea un token JWT
        #     token = jwt.encode(
        #         {
        #             'user': username,
        #             'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=1)
        #         },
        #         os.getenv('JWT_SECRET_KEY'),
        #         algorithm='HS256'
        #     )

        #     # Devuelve el token al cliente
        #     return jsonify({'ok': True, 'token': token, 'dato': dato})
            
        # # Si la autenticación falla, devuelve un error
        # return jsonify({'ok': False, 'message': 'Credenciales erroneas'}), 401

    def createUser(name, username, password):
        db=mysql.connector.connect(host=os.getenv('DB_HOST'), 
                            user=os.getenv('DB_USER'), 
                            passwd=os.getenv('DB_PASSWD'), 
                            database=os.getenv('DB_DATABASE'))

        dbCursor = db.cursor()
        query = 'INSERT INTO User (username, name, password) VALUES (%s, %s, %s)'
        dbCursor.execute(query, (username, name, password))
        db.commit()
        db.close()  
        return jsonify({'ok': True})


    def listUsers():
        db=mysql.connector.connect(host=os.getenv('DB_HOST'), 
                            user=os.getenv('DB_USER'), 
                            passwd=os.getenv('DB_PASSWD'), 
                            database=os.getenv('DB_DATABASE'))

        dbCursor = db.cursor()
        dbCursor.execute('SELECT * FROM user')
        dato = dbCursor.fetchall()
        db.close() 
        return jsonify({'ok': True, 'dato': dato})
            