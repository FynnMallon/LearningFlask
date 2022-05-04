
# from operator import truediv
from ast import Pass
from re import A
from django.shortcuts import render
from flask import Flask, render_template, url_for, redirect
# from flask import request
# import flask
# from markupsafe import escape
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
# Use the application default credentials
#OtherFiles
from UserIdManager import get, add
from MessageManager import SendMessage, GetMessages
from FriendsManager import AddFriend, FriendList
cred = credentials.Certificate('learningflask-8db3e-firebase-adminsdk-2qh4b-08af089550.json')

UserID = None

from flask import Flask, request

appFlask = Flask(__name__)


# def Homepage():
#       UID = str(UserID)
#       query = db.collection(u'users').document(UID).collections()
#       IDs = []
#       data = []
      
#       for collection in query:
#         IDs.append(f'{collection.id}')
#       for ID in IDs:
#         print(ID)
#         for i in ChatLog(UID,ID):
#           MessageData = {}
#           MessageData['Sender'] = ID
#           MessageData['Text'] = i['Message']
#           MessageData['TimeStamp'] = i['Timestamp']
#           data.append(MessageData)
        
#         # for doc in collection.stream():
#         #   array.append(f'{doc.id} => {doc.to_dict()}')
#         #   print(array)
#       return render_template('HomePage.html',PlaceHolder = ID, data = data)


def introduction():
  return render_template("Intro.html")
@appFlask.route('/', methods=['GET','POST'])
def choice():
  if UserID != None:
    return(Homepage())
  else:
    return(introduction())

@appFlask.route('/signup', methods=['GET', 'POST'])
def Signup():
  # handle the POST request
  if request.method == 'POST':
    Email = request.form.get('Email')
    Password = request.form.get('Password')
    Password2 = request.form.get('Password2')
    if Password == Password2:
      UserId =add(Email,Password)
      if UserId != None:
        globals()['UserID'] = UserId
        return '''
        <h1>Successfull signup</h1>
        <h1>The Username is: {}</h1>'''.format(Email)
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
  # handle the POST request
  if request.method == 'POST':
    Email = request.form.get('Email')
    Password = request.form.get('Password')
    UserID = get(Email,Password)
    globals()['UserID'] = UserID
    if UserID != False:
      return redirect(url_for('Friends'))
      # return '''
      #   <h1>The Student Name is: {}</h1>
      #   <h1>The UserId is: {}</h1>'''.format(Email, UserID)
    else:
      return '''
      <h1> Incorrect UserName or Password <h1>'''
  else:
    return render_template("Login.html")

@appFlask.route('/Friends', methods=['GET', 'POST'])
def Friends():
  if request.method == 'POST':
    print(UserID)
    Email = request.form.get('Email')
    AddFriend(UserID, Email)
    return render_template("Intro.html")
  else:
    return render_template("AddFriends.html")

def ChatLog(User1, User2):
  recieved = GetMessages(User1,User2) #To User1 from User 2
  Sent = GetMessages(User2,User1) #To User2 from User 1 


if __name__ == '__main__':
  appFlask.run(debug = True)



# Todo:
# Encrypt Password
# Make LandingPage
# Make Entry Page

#Friend System 