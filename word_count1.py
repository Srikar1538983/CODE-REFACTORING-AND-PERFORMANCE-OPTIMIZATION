from collections import Counter
import sys

def read_file(file_path):
    """
    Reads the content of a file and returns it as a string.

    Args:
        file_path (str): The path to the file.

    Returns:
        str: The content of the file.
    """
    try:
        with open(file_path, 'r') as file:
            return file.read()
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        sys.exit(1)

def count_words(text):
    """
    Counts the frequency of each word in the given text.

    Args:
        text (str): The input text.

    Returns:
        Counter: A Counter object mapping words to their frequency.
    """
    words = text.lower().split()
    return Counter(words)  # Optimized word counting using Counter

def main(file_path):
    """
    Reads a file, counts the frequency of each word, and prints the results.

    Args:
        file_path (str): The path to the file.
    """
    text = read_file(file_path)
    word_counts = count_words(text)
    
    for word, count in word_counts.items():
        print(f'{word}: {count}')

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Usage: python word_count.py <file_path>')
    else:
        main(sys.argv[1])