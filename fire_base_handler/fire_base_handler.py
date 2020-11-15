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

    def add_doc(self, collection, doc):
        self._data_base.collection(collection).add(doc)

    def add_docs(self, collection, docs):
        for doc in docs:
            self.add_doc(collection, doc)


fire_base_handler = _FireBaseHandler()
