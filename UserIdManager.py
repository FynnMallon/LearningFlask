# from operator import truediv
from ast import Pass
from flask import Flask, render_template
import hashlib
# from flask import request
# import flask
# from markupsafe import escape
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
# Use the application default credentials

cred = credentials.Certificate('learningflask-8db3e-firebase-adminsdk-2qh4b-08af089550.json')
firebase_admin.initialize_app(cred, {'projectId': 'learningflask-8db3e',})

def get(name,password):
    password = encrypt(password)
    name = name.lower()
    id = None
    db = firestore.client()
    UserExists = False
    query = db.collection(u'users').where(u'Email',u'==',name).stream()
    for entry in query:
        Password = entry.get(u'Password')
        if password ==Password:
            id = entry.id
        return(id)
    if id == None:
        return(UserExists)

def add(username, password):
    password = encrypt(password)
    db = firestore.client()
    username = username.lower()
    UserId = None
    query = db.collection(u'users').where(u'Email',u'==',username).stream()
    results = 0
    if results == 0:
        for a in query:
            results+=1
    if results == 0:
        doc_ref = db.collection(u'users').document()
        doc_ref.set({
            u'Email': username,
            u'Password': password,
        })
        UserId = doc_ref.id
    return(UserId)

def encrypt(password):                          #given password encrypted in sha256 
    hash_func = hashlib.sha256()            #using the sha256 algorithm from the hashlib library
    epassword=password.encode()             #encodes password
    hash_func.update(epassword)             #updates password to be sha256 encrypted
    password=hash_func.hexdigest()          #saves as hex instead of binary
    return(password)                        #returns encrypted password

