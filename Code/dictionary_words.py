import random
import argparse

def create_sentence(words):
    sentence = ''

    with open('/usr/share/dict/words', 'r') as file:
        lines = file.readlines()
    file.close()

    for i in range(words):
        random_word = random.choice(lines).strip()
        if i != words - 1:
            sentence += random_word + ' '
        else: 
            sentence += random_word + '.'

    return sentence

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description = 'adds arguments for the sentence creator')

    parser.add_argument('number_of_words', metavar='number_of_words', type=int, help='enter number_of_words you want in the sentence')
    args = parser.parse_args()
    number_of_words = args.number_of_words

    print(create_sentence(number_of_words))


    