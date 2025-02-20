import string
from collections import Counter

def analyze_text(file_path):
    """Analyze the text in the specified file."""
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            text = file.read()
    except FileNotFoundError:
        print("The specified file was not found.")
        return
    except Exception as e:
        print(f"An error occurred: {e}")
        return

    # Remove punctuation and convert to lowercase
    text_cleaned = text.translate(str.maketrans('', '', string.punctuation)).lower()

    # Split the text into words
    words = text_cleaned.split()
    
    # Calculate statistics
    word_count = len(words)
    sentence_count = text.count('.') + text.count('!') + text.count('?')
    character_count = len(text)
    word_frequency = Counter(words)

    # Display the results
    print(f"Total words: {word_count}")
    print(f"Total sentences: {sentence_count}")
    print(f"Total characters (including spaces): {character_count}")
    print("\nWord Frequency:")
    for word, freq in word_frequency.most_common(10):  # Display top 10 most common words
        print(f"{word}: {freq}")

def main():
    print("Welcome to the Text Analyzer!")
    file_path = input("Enter the path of the text file to analyze: ")
    analyze_text(file_path)

if __name__ == "__main__":
    main()
