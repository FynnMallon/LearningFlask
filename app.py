
# from operator import truediv
from ast import Pass
from re import A
from flask import Flask, render_template, url_for
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
cred = credentials.Certificate('learningflask-8db3e-firebase-adminsdk-2qh4b-08af089550.json')



from flask import Flask, request

appFlask = Flask(__name__)

@appFlask.route('/', methods=['GET','POST'])
def introduction():
  return render_template("Intro.html")

@appFlask.route('/signup', methods=['GET', 'POST'])
def Signup():
  UserID = None
  # handle the POST request
  if request.method == 'POST':
    Email = request.form.get('Email')
    Password = request.form.get('Password')
    Password2 = request.form.get('Password2')
    if Password == Password2:
      UserID =add(Email,Password)
      if UserID != None:
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
  UserID = None
  # handle the POST request
  if request.method == 'POST':
    Email = request.form.get('Email')
    Password = request.form.get('Password')
    UserID = get(Email,Password)
    if UserID != False:
      return '''
        <h1>The Student Name is: {}</h1>
        <h1>The UserId is: {}</h1>'''.format(Email, UserID)
    else:
      return '''
      <h1> Incorrect UserName or Password <h1>'''
  else:
    return render_template("Login.html")

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