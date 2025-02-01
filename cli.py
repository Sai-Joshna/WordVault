from my_dictionary import Dictionary  # Importing from my_dictionary.py
from storage import Storage
from word_of_the_day import WordOfTheDay

def main():
    print("\n📚 Welcome to CLI Dictionary! 📚")
    while True:
        print("\nAvailable commands:")
        print("1. Search for a word")
        print("2. View search history")
        print("3. Word of the Day")
        print("4. Exit")

        choice = input("\nEnter your choice: ").strip()

        if choice == '1':
            word = input("\nEnter a word: ").strip()
            if word.lower() == 'exit':
                break
            data = Dictionary.get_word_details(word)  # Using Dictionary class
            print(Dictionary.parse_word_data(data))  # Using parse_word_data method
            Storage.save_word(word)

        elif choice == '2':
            history = Storage.get_history()
            if history:
                print("\n🔍 Search History:")
                for idx, word in enumerate(history, 1):
                    print(f"{idx}. {word}")
            else:
                print("No search history found.")

        elif choice == '3':
            print(Dictionary.get_word_of_the_day())  # Fetch and display Word of the Day

        elif choice == '4':
            print("Goodbye! 👋")
            break

        else:
            print("Invalid choice! Please select again.")
