
# from operator import truediv
from ast import Pass
from re import A
from flask import Flask, render_template, url_for, redirect, abort
import json
# from flask import request
# import flask
# from markupsafe import escape
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
# Use the application default credentials
#OtherFiles
from UserIdManager import get, add, getName
from MessageManager import SendMessage, GetMessages
cred = credentials.Certificate('learningflask-8db3e-firebase-adminsdk-2qh4b-08af089550.json')
db = firestore.client()
from flask import Flask, request

appFlask = Flask(__name__)
UserID = None

def introduction():
      return render_template("Intro.html")



def Homepage():
      UID = str(UserID)
      query = db.collection(u'users').document(UID).collections()
      IDs = []
      data = []
      
      for collection in query:
        IDs.append(f'{collection.id}')
      for ID in IDs:
        print(ID)
        for i in ChatLog(UID,ID):
          MessageData = {}
          MessageData['Sender'] = ID
          MessageData['Text'] = i['Message']
          MessageData['TimeStamp'] = i['Timestamp']
          data.append(MessageData)
        
        # for doc in collection.stream():
        #   array.append(f'{doc.id} => {doc.to_dict()}')
        #   print(array)
      return render_template('HomePage.html',PlaceHolder = ID, data = data)


@appFlask.route('/', methods=['GET','POST'])
def choice():
  if UserID != None:
    return(Homepage())
  else:
    return(introduction())
  
@appFlask.route('/signup', methods=['GET', 'POST'])
def Signup():
  global UserID
  # handle the POST request
  if request.method == 'POST':
    Email = request.form.get('Email')
    Password = request.form.get('Password')
    Password2 = request.form.get('Password2')
    if Password == Password2:
      UserID =add(Email,Password)
      if UserID != None:
        return redirect(url_for('choice'))
      else:
        return'''
        <h1> invalid details please try again </h1>'''
    else:
      return'''
      <h1> invalid details please try again </h1>'''
  else:
    return render_template("Signup.html")

@appFlask.route('/Login', methods=['GET', 'POST'])
def Login():
  global UserID
  # handle the POST request
  if request.method == 'POST':
    Email = request.form.get('Email')
    Password = request.form.get('Password')
    UserID = get(Email,Password)
    if UserID != None:
      return redirect(url_for('choice'))
    else:
      return '''
      <h1> Incorrect UserName or Password <h1>'''
  else:
    return render_template("Login.html")

def ChatLog(User1, User2):
  recieved = GetMessages(User1,User2) #To User1 from User 2
  Sent = GetMessages(User2,User1) #To User2 from User 1 
  return(recieved)


if __name__ == '__main__':
  appFlask.run(debug = True)

# Todo:
# Encrypt Password - done
# Make LandingPage - done
# Make Entry Page 

#Friend System 