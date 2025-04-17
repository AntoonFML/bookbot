def count_words(text):
    words_tab = text.split()
    return len(words_tab)

def count_letters(text):
    text = text.lower()
    dict = {}
    for letter in text:
        if letter.isalpha():
            if letter in dict:
                dict[letter] += 1
            else:
                dict[letter] = 1
    return dict

def sort(words_tab, dict):
    return dict.sort(reverse=True)