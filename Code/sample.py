
import re
import random


def histogram(source_text):
    clean_text = re.sub(r"[^\w\d\s]", "", source_text)
    word_count = dict()
    words = clean_text.lower().split()

    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    # sort by word
    wordKeys = list(word_count.keys())
    wordKeys.sort()
    sorted_by_word = {i: word_count[i] for i in wordKeys}

    # sort by count
    sorted_words_by_count = sorted(word_count.items(), key=lambda x:x[1], reverse=True)
    sorted_by_count_desc = dict(sorted_words_by_count)

    # Return the needed dictionary
    # return sorted_by_word
    return sorted_by_count_desc
    
def weighted_selection(histogram):
    words_and_counts = list(histogram.items())
    words, weights = zip(*words_and_counts)
    selected_word = random.choices(words, weights=weights)[0]
    return selected_word
    

def simulation(histogram, iterations):
    num_iterations = iterations
    word_frequencies = {word: 0 for word in histogram.keys()}

    for _ in range(num_iterations):
        selected_word = weighted_selection(histogram)
        word_frequencies[selected_word] += 1
    for word, frequency in word_frequencies.items():
        print(f'{word}: {frequency}')




if __name__ == '__main__':
    text = 'one- fish two, !fish red "fish" blue fish.'
    # text = open("Kiyosaki.txt","r").read()
    histogram = histogram(text)
    print(histogram)
    # print(weighted_selection(histogram))
    simulation(histogram, 1000)
