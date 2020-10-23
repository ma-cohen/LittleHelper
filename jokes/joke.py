from datetime import datetime


class Joke:
    def __init__(self, author: str, joke: str, category: str, date=None):
        self._author = author
        self._joke = joke
        self._category = category
        if date is None:
            self._date = datetime.now()

    def __str__(self):
        header = f"Joke by: {self._author} at {self._date.strftime('%d/%m/%Y, %H:%M:%S')}"
        divider = '-->'
        return f'{header}\n{divider}\n{self._joke}\n{divider}'
