import random
import sys

def create_sentence(words):
    word_list = []

    with open('/usr/share/dict/words', 'r') as file:
        lines = file.readlines()

    for i in range(words):
        random_word = random.choice(lines).strip()
        word_list.append(random_word)

    sentence = f'{" ".join(word_list)}.'
        # if i != words - 1:
        #     sentence += random_word + ' '
        # else: 
        #     sentence += random_word + '.'

    return sentence

if __name__ == '__main__':
    print(create_sentence(int(sys.argv[1])))


    