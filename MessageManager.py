import time
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

cred = credentials.Certificate('learningflask-8db3e-firebase-adminsdk-2qh4b-08af089550.json')
db = firestore.client()

def SendMessage(UserId, RecipientId, Text):
    db = firestore.client()
    Messagedata = {
        "Message": Text
    }
    Time = time.time()
    Time = str(round(Time,2))
    MessageFolder = db.collection(u'users').document(RecipientId).collection(UserId).document(Time).set(Messagedata)

def GetMessages(UserId, PartnerId):
    #to UserID from Partner ID
    reference = db.collection(u'users').document(UserId).collection(PartnerId)
    list =reference.get()
    idList = []
    MessageLog =[]
    for reference in list:
        idList.append(reference.id)
    idList.sort()
    for ID in idList:
        ID = str(ID)
        file=db.collection(u'users').document(UserId).collection(PartnerId).document(ID).get()
        Message =file.get(u'Message')
        Data = {
            "Timestamp": ID,
            "Message": Message
        }
        MessageLog.append(Data)
    return(MessageLog)


# SendMessage("IYKuHOyNcdjsCrKV7yDg","OUlomzNvGv3W5BKdU3WL","Hello Fynn How Are You?")

# print(GetMessages("OUlomzNvGv3W5BKdU3WL","IYKuHOyNcdjsCrKV7yDg"))

#Structure of Messages
#Each User has a folder for every user they recieved a message from
#If sending to new user, adds folder to both profile
#Checks messages on refresh 
#Recieved messages added to own profile