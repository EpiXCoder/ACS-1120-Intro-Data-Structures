
import re

# text = 'one-fish two,_!fish red "fish" blue fish.'
text = open("Kiyosaki.txt","r").read()

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
    
def unique_words(histogram):
    return len(histogram)

def frequency(word, histogram):
    return histogram.get(word, "not found")


def writing_to_txt(histogram):
    df=open('histogram.txt','w')
    for key in histogram:
        df.write(key)
        df.write(' ')
        df.write(str(histogram[key]))
        df.write('\n')
    df.close()

if __name__ == '__main__':
    histogram = histogram(text)
    print(histogram)
    print(unique_words(histogram))
    print(frequency('rat', histogram))
    writing_to_txt(histogram)
