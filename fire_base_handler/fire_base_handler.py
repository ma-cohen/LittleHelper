from typing import List

import firebase_admin
from firebase_admin import credentials, firestore


class _FireBaseHandler:
    def __init__(self):
        cred = credentials.Certificate('firebase-sdk.json')
        firebase_admin.initialize_app(cred)
        self._data_base = firestore.client()

    def get_all_docs(self, collection: str) -> List[dict]:
        docs = []
        docs_stream = self._data_base.collection(collection).stream()
        for doc in docs_stream:
            docs.append(doc)
        return docs


fire_base_handler = _FireBaseHandler()
