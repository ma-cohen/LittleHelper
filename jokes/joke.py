from datetime import datetime


class Joke:
    def __init__(self, author: str, joke: str, category: str, date=None):
        self._author = author
        self._joke = joke
        self._category = category
        if date is None:
            self._date = datetime.now()
        else:
            self._date = date

    @classmethod
    def from_dict(cls, doc):
        doc = doc.to_dict()
        _author = doc['author']
        _joke = doc['joke']
        _category = doc['category']
        _date = doc['date']
        return cls(_author, _joke, _category, _date)

    def to_dict(self):
        return {
            'joke': self._joke,
            'author': self._author,
            'category': self._category,
            'date': self._date
        }

    def __str__(self):
        header = f"Joke by: {self._author} at {self._date.strftime('%d/%m/%Y, %H:%M:%S')}"
        divider = '-->'
        return f'{header}\n{divider}\n{self._joke}\n{divider}'
