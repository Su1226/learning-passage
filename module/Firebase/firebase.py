import firebase_admin
from firebase_admin import credentials, auth, db

class FirebaseManager:
    """
    firebase 연결 매니저
    """

    def __init__(self):
        # Firebase database init
        self.cred = credentials.Certificate('C:\\Users\\DSLab\\learning-passage\\firebase_SDK.json')
        self.firebase_app = firebase_admin.initialize_app(self.cred, {
            'databaseURL' : 'https://carbon-friendly-default-rtdb.firebaseio.com/'
        })
        self.auth = auth
        self.dir = db.reference()

        