
import re

# text = 'one-fish two,_!fish red "fish" blue fish.'
text = open("Kiyosaki.txt","r").read()

def histogram(source_text):
    clean_text = re.sub(r"[^\w\d\s-]", "", source_text)
    word_count = dict()
    words = clean_text.lower().split()

    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

    wordKeys = list(word_count.keys())
    wordKeys.sort()
    sorted_word_count = {i: word_count[i] for i in wordKeys}
    return sorted_word_count
    



def unique_words(histogram):
    unique_words = len(histogram)
    return unique_words

def frequency(word, histogram):
    return histogram.get(word, "not found")

print(histogram(text))
print(unique_words(histogram(text)))
histogram = histogram(text)
print(frequency('rat', histogram))


# def count_words(string):
#     words = string.split()
#     word_count = {}
#     for word in words:
#         if word in word_count:
#             word_count[word] += 1
#         else:
#             word_count[word] = 1
#     return [[word, word_count[word]] for word in word_count]