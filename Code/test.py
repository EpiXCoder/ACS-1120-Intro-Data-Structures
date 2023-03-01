# Define a sample list of tuples with overlapping elements
import re


tuples_list = [('One', 'fish,', 'two'), ('two', 'fish,', 'red'), ('red', 'fish,', 'blue'), ('blue', 'fish,', 'two'), ('two', 'fish,', 'one')]
tuple = [('One', 'fish,'), ('fish,', 'two'), ('two', 'fish,'), ('fish,', 'red'), ('red', 'fish,'), ('fish,', 'blue'), ('blue', 'fish.'), ('fish.', 'Darl')]

# Create a list of all but the last elements of the tuples
partial_sentences = [t[:-1] for t in tuples_list]

# Join the partial sentences to form the complete sentence
sentence = ' '.join([word for partial_sentence in partial_sentences for word in partial_sentence])

# Add the last element of the last tuple to the sentence
sentence += (' ' + tuples_list[-1][-1])

# Print the final sentence
# print(sentence)

def join_tuples(list):
    # Create a list of all but the last elements of the tuples
    partial_sentences = [t[:-1] for t in list]

    # Join the partial sentences to form the complete sentence
    sentence = ' '.join([word for partial_sentence in partial_sentences for word in partial_sentence])

    # Add the last element of the last tuple to the sentence
    sentence += (' ' + list[-1][-1])
    split_string = re.split(r'([.?!])', sentence)
    new_string = split_string[0] + split_string[1]
    return new_string

print(join_tuples(tuple))