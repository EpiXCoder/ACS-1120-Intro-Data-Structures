
import re

# text = 'one-fish two,_!fish red "fish" blue fish.'
text = open("Kiyosaki.txt","r").read()

def histogram(source_text):
    clean_text = re.sub(r"[^\w\d\s]", "", source_text)
    word_count = []
    check_list = []
    words = clean_text.lower().split()

    for word in words:
        if word not in check_list:
            word_count.append([word, words.count(word)])
            check_list.append(word)
    
    
    # sort by word
    # wordKeys = list(word_count.keys())
    # wordKeys.sort()
    # sorted_by_word = {i: word_count[i] for i in wordKeys}

    # sort by count
    # sorted_words_by_count = sorted(word_count.items(), key=lambda x:x[1], reverse=True)
    # sorted_by_count_desc = dict(sorted_words_by_count)
    sorted_by_count_desc = sorted(word_count, key=lambda x: x[1], reverse=True)

    # Convert to list 
    # listogram = [[key, value] for key, value in sorted_by_count_desc.items()]


    # Return the needed dictionary
    # return sorted_by_word
    return sorted_by_count_desc
    # return listogram
    
def unique_words(listogram):
    return len(listogram)

def frequency(word, histogram):
    # return histogram.get(word, "not found")
    for x in range(len(histogram)):
        if word in histogram[x]:
            return histogram[x][1]


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
    print(frequency('red', histogram))
    # writing_to_txt(histogram)
