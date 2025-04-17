from stats import count_words, count_letters, sort

def get_book_text(path):
    with open(path) as f:
        file_contents = f.read()
    return file_contents

def main():
    text = get_book_text("./books/frankenstein.txt")
    print(text)
    num_words = count_words(text)
    print(f"{num_words} words found in the document")
    num_letters = count_letters(text)
    print(num_letters)
    print(sort(num_words, num_letters))

main()
    