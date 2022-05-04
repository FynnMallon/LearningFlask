import time
from typing import List
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from UserIdManager import getID
cred = credentials.Certificate('learningflask-8db3e-firebase-adminsdk-2qh4b-08af089550.json')
db = firestore.client()

def AddFriend(UserID, FriendEmail):
    FriendID = getID(FriendEmail.lower())
    if FriendID != False and FriendID != UserID:
        print(FriendID)
    
    #Add Friend To Friend Folder
        FileData = {
            "Email" : FriendEmail
        }
        db.collection(u'users').document(UserID).collection(u"friends").document(FriendID).set(FileData)
        
def FriendList(UserID):
    reference = db.collection(u'users').document(UserID).collection(u"friends")
    list = reference.get()
    Friends = {} 
    for Friend in list:
        ID = Friend.id
        Email =  Friend.get(u'Email')
        Friends[Email] = ID
    return(Friends)
    
#AddFriend('OUlomzNvGv3W5BKdU3WL', "jonotuite1@gmail.com")
# print(FriendList('OUlomzNvGv3W5BKdU3WL'))