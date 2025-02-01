import json

class Storage:
    FILE_PATH = "history.json"
    MAX_HISTORY_SIZE = 50  # Limit history to 50 words

    @staticmethod
    def save_word(word):
        """Save a word to history."""
        try:
            with open(Storage.FILE_PATH, "r") as file:
                history = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            history = []
        
        # If word is not in history, add it and keep history size limited
        if word not in history:
            history.append(word)
            if len(history) > Storage.MAX_HISTORY_SIZE:
                history.pop(0)  # Remove the oldest word if history exceeds limit

            with open(Storage.FILE_PATH, "w") as file:
                json.dump(history, file, indent=4)

    @staticmethod
    def get_history():
        """Retrieve search history."""
        try:
            with open(Storage.FILE_PATH, "r") as file:
                return json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    @staticmethod
    def remove_word(word):
        """Remove a word from search history."""
        history = Storage.get_history()
        if word in history:
            history.remove(word)
            with open(Storage.FILE_PATH, "w") as file:
                json.dump(history, file, indent=4)
