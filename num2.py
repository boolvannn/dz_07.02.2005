import string

def translate(text):
    vowels = "аAeEeЁёИиОоУуЫыЭэЮюЯя"
    punctuation = string.punctuation
    translated_words = []
    words = text.split()
    for word in words:
        clean_word = ''.join(char for char in word if char not in punctuation)
        no_vowels = ''.join(char for char in clean_word if char not in vowels)
        translated_words.append(no_vowels)
    return ' '.join(translated_words)

example_text = "Удивительный факт, но текст на языке НРЗБРЧВ оказывается довольно просто читать. Достаточно небольшой тренировки - и вы сможете это делать."
result = translate(example_text)
print(result)