import conf
import firebase_admin
from firebase_admin import credentials,firestore
from little_helper import bot
from logger import initialize_logger



def main():
    # initialize_logger()
    # bot.run(conf.token)
    cred = credentials.Certificate('firebase-sdk.json')
    firebase_admin.initialize_app(cred)
    db = firestore.client()
    emp_ref = db.collection('jokes')
    docs = emp_ref.stream()
    for doc in docs:
        print(doc.to_dict())


if __name__ == '__main__':
    main()
