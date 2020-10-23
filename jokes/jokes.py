from jokes import Joke


class _Jokes:
    def __init__(self):
        self._jokes = []

    def __len__(self):
        return len(self._jokes)

    def __str__(self):
        jokes_str = ''
        number_of_jokes = len(self)
        ending = '\n\n'
        for joke_id, joke in enumerate(self._jokes):
            if joke_id == number_of_jokes - 1:
                ending = '\n'
            jokes_str += f"ID: {joke_id}\n{joke}{ending}"

        return jokes_str

    def append(self, joke: Joke) -> None:
        self._jokes.append(joke)


jokes = _Jokes()
