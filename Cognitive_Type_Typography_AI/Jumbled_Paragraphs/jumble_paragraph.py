import sys
import random
import re

def scramble_word(word):
    if len(word) > 3:
        middle = list(word[1:-1])
        random.shuffle(middle)
        return word[0] + ''.join(middle) + word[-1]
    else:
        return word

def add_spaces_around_punctuation(text):
    return re.sub(r'([,.!?;:])', r' \1 ', text)

def remove_extra_spaces_around_punctuation(text):
    return re.sub(r'\s+([,.!?;:])\s+', r'\1', text)

def jumble_paragraph(text):
    text_with_spaces = add_spaces_around_punctuation(text)
    words = text_with_spaces.split()
    jumbled_words = [scramble_word(word) for word in words]
    jumbled_text = ' '.join(jumbled_words)
    return remove_extra_spaces_around_punctuation(jumbled_text)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <filename>")
        sys.exit(1)

    filename = sys.argv[1]
    try:
        with open(filename, 'r') as file:
            text = file.read()
            jumbled_text = jumble_paragraph(text)
            print(jumbled_text)
    except FileNotFoundError:
        print(f"File {filename} not found.")


'''

The Project Gutenberg eBook of Grimms Fairy Tales

'''