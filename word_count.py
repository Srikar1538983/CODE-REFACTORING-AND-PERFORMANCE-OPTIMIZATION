def read_file(file_path):
    with open(file_path, 'r') as file:
        return file.read()

def count_words(text):
    word_counts = {}
    words = text.split()
    for word in words:
        word = word.lower()
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1
    return word_counts

def main(file_path):
    text = read_file(file_path)
    word_counts = count_words(text)
    for word, count in word_counts.items():
        print(f'{word}: {count}')

if __name__ == '__main__':
    import sys
    if len(sys.argv) != 2:
        print('Usage: python word_count.py <file_path>')
    else:
        main(sys.argv[1])