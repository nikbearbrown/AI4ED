# Jumbled Paragraphs


Aoccdrnig to a rscheearer at Cmabrigde Uinervtisy, it deosn’t mttaer in waht oredr the ltteers in a wrod are, the olny iprmoetnt tihng is taht the frist and lsat ltteer be at the rghit pclae. The rset can be a toatl mses and you can sitll raed it wouthit porbelm. Tihs is bcuseae the huamn mnid deos not raed ervey lteter by istlef, but the wrod as a wlohe.

Let's test this.

**jumble_paragraph.py***

To create a Python script that processes a text file to generate a "Jumbled Paragraph" version as described, follow these steps:

1. **Add Spaces Around Punctuation**: Before jumbling the text, add an extra space before and after every punctuation mark. This step ensures that punctuation marks are not scrambled with the words.

2. **Jumble Words**: Scramble the middle letters of each word while keeping the first and last letters intact. This "Jumbled Paragraph" technique allows the text to remain somewhat readable because the human brain can still recognize the word based on the first and last letters and the overall shape of the word.

3. **Remove Extra Spaces Around Punctuation**: After jumbling the words, remove the extra spaces added around punctuation marks to restore the punctuation to its original form.

Below is a Python script that performs these steps. The script takes a text file from the command line, processes it to create a "Jumbled Paragraph", and then prints the result to the console.

```python
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
```

**How to Use the Script:**

- Save the script to a file, for example, `jumble_paragraph.py`.
- Make sure you have a text file ready, let's say it's named `input.txt`.
- Run the script from the command line by passing the text file as an argument:
  ```
  python jumble_paragraph.py input.txt
  ```
- The script will print the jumbled version of the paragraph to the console.
