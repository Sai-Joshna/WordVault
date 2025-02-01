import requests

class WordOfTheDay:
    WORDS_API = "https://random-word-api.herokuapp.com/word"
    
    @staticmethod
    def get_random_word():
        """Fetch a random word."""
        response = requests.get(WordOfTheDay.WORDS_API)
        if response.status_code == 200:
            return response.json()[0]
        return None

