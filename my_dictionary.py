import requests
import json
from word_of_the_day import WordOfTheDay  # Import WordOfTheDay

class Dictionary:
    API_URL = "https://api.dictionaryapi.dev/api/v2/entries/en/{}"
    CACHE_FILE = 'word_cache.json'

    @staticmethod
    def _load_cache():
        """Load cached word data."""
        try:
            with open(Dictionary.CACHE_FILE, 'r') as cache_file:
                return json.load(cache_file)
        except (FileNotFoundError, json.JSONDecodeError):
            return {}

    @staticmethod
    def _save_cache(cache_data):
        """Save the word data to cache."""
        with open(Dictionary.CACHE_FILE, 'w') as cache_file:
            json.dump(cache_data, cache_file, indent=4)

    @staticmethod
    def get_word_details(word):
        """Fetch word details from an online dictionary API."""
        cached_data = Dictionary._load_cache()
        if word in cached_data:
            return cached_data[word]
        
        response = requests.get(Dictionary.API_URL.format(word))
        if response.status_code == 200:
            data = response.json()
            cached_data[word] = data
            Dictionary._save_cache(cached_data)
            return data
        return None

    @staticmethod
    def parse_word_data(data):
        """Extract and format word details."""
        if not data:
            return "Word not found. Please try again."
        
        word_info = data[0]
        word = word_info.get('word', 'N/A')
        phonetics = word_info.get('phonetics', [])
        meanings = word_info.get('meanings', [])
        
        # Start with the word and pronunciation
        word_details = f"\n📖 **Word of the Day:** {word}\n"
        
        if phonetics:
            phonetic_text = phonetics[0].get('text', 'N/A')
            word_details += f"🔊 **Pronunciation:** {phonetic_text}\n"
        else:
            word_details += "🔊 **Pronunciation:** Not available\n"

        # Loop through meanings and add definitions (no synonyms or antonyms)
        if meanings:
            for meaning in meanings:
                part_of_speech = meaning.get('partOfSpeech', 'N/A')
                word_details += f"\n👉 **Part of Speech:** {part_of_speech}\n"
                
                for definition in meaning.get('definitions', []):
                    definition_text = definition.get('definition', 'N/A')
                    word_details += f" - **Definition:** {definition_text}\n"

        # Add source URL if available
        source_urls = word_info.get('sourceUrls', [])
        if source_urls:
            word_details += f"\n🌐 **Source:** {', '.join(source_urls)}\n"

        # Add license information
        license_info = word_info.get('license', {})
        license_name = license_info.get('name', 'N/A')
        license_url = license_info.get('url', 'N/A')
        word_details += f"🔖 **License:** {license_name} | {license_url}\n"
    
        return word_details

    @staticmethod
    def get_word_of_the_day():
        """Fetch and display word of the day."""
        word = WordOfTheDay.get_random_word()
        if word:
            return Dictionary.get_word_details(word)
        return "Sorry, couldn't fetch the word of the day."
