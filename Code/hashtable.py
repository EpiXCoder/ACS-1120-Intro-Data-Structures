#!python

from linkedlist import LinkedList


class HashTable(object):

    def __init__(self, init_size=8):
        """Initialize this hash table with the given initial size."""
        # Create a new list (used as fixed-size array) of empty linked lists
        self.buckets = []
        for i in range(init_size):
            self.buckets.append(LinkedList())

    def __str__(self):
        """Return a formatted string representation of this hash table."""
        items = []
        for key, val in self.items():
            items.append('{!r}: {!r}'.format(key, val))
        return '{' + ', '.join(items) + '}'

    def __repr__(self):
        """Return a string representation of this hash table."""
        return 'HashTable({!r})'.format(self.items())

    def _bucket_index(self, key):
        """Return the bucket index where the given key would be stored."""
        # Calculate the given key's hash code and transform into bucket index
        return hash(key) % len(self.buckets)
    
    def _find_bucket(self, key):
        """Return the bucket index where the given key would be stored."""
        # Calculate the given key's hash code and transform into bucket index
        index = index = self._bucket_index(key)
        return  self.buckets[index]

    def keys(self):
        """Return a list of all keys in this hash table.
        TODO: Running time: O(???) Why and under what conditions?"""
        # Collect all keys in each bucket
        all_keys = []
        for bucket in self.buckets:
            for key, value in bucket.items():
                all_keys.append(key)
        return all_keys

    def values(self):
        """Return a list of all values in this hash table.
        TODO: Running time: O(???) Why and under what conditions?"""
        # TODO: Loop through all buckets
        # TODO: Collect all values in each bucket
        all_values = []
        for bucket in self.buckets:
            for key, value in bucket.items():
                all_values.append(value)
        return all_values

    def items(self):
        """Return a list of all items (key-value pairs) in this hash table.
        TODO: Running time: O(???) Why and under what conditions?"""
        # Collect all pairs of key-value entries in each bucket
        all_items = []  # O(1) time to create empty list
        for bucket in self.buckets: # Always n iterations because no early return
            all_items.extend(bucket.items())  # O(1) time (on average) to append to list
        return all_items # O(1) time to return list

    def length(self):
        """Return the number of key-value entries by traversing its buckets.
        TODO: Running time: O(???) Why and under what conditions?"""
        # TODO: Loop through all buckets
        # TODO: Count number of key-value entries in each bucket
        length = 0 # O(1) time to create variable
        for bucket in self.buckets:  # Always n iterations because no early return
            length += bucket.length() # O(1) time (on average) to add
        return length # O(1) time to return the variable

    def contains(self, key):
        """Return True if this hash table contains the given key, or False.
        TODO: Running time: O(???) Why and under what conditions?"""
        # TODO: Find bucket where given key belongs
        # TODO: Check if key-value entry exists in bucket
        bucket = self._find_bucket(key) # O(1) time (on average) to call coupled functions to find bucket
        entry = bucket.find_using_lambda_fn(lambda entry: entry[0] == key) # O(1) time (on average) to call coupled functions to find entry
        if entry is not None: # O(1) time to evaluate conditional
            return True
        else: 
            return False
      
    def get(self, key):
        """Return the value associated with the given key, or raise KeyError.
        TODO: Running time: O(???) Why and under what conditions?"""
        # TODO: Find bucket where given key belongs
        # TODO: Check if key-value entry exists in bucket
        # TODO: If found, return value associated with given key
        # TODO: Otherwise, raise error to tell user get failed
        # Hint: raise KeyError('Key not found: {}'.format(key))
        bucket = self._find_bucket(key) # O(1) time (on average) to call coupled functions to find bucket
        entry = bucket.find_using_lambda_fn(lambda entry: entry[0] == key) # O(1) time (on average) to call coupled functions to find entry
        if entry is not None:  # O(1) time to evaluate conditional
            value = entry[1]  # O(1) time to access and assign data to value
            return value # O(1) time to return the variable
        else: 
            raise KeyError('Key not found: {}'.format(key)) # O(1) time to raise error

    def set(self, key, value):
        """Insert or update the given key with its associated value.
        TODO: Running time: O(???) Why and under what conditions?"""
        # TODO: Find bucket where given key belongs
        # TODO: Check if key-value entry exists in bucket
        # TODO: If found, update value associated with given key
        # TODO: Otherwise, insert given key-value entry into bucket
        bucket = self._find_bucket(key) # O(1) time (on average) to call coupled functions to find bucket
        node = bucket.head # O(1) time (on average) to call coupled functions to find node
        while node: # Always n iterations because no early return
            if node.data[0] == key:   # O(1) time to evaluate conditional
                node.data = (key, value)  #O(1) for assignment
                return
            node = node.next #O(1) for assignment
        bucket.append((key, value)) # O(1) time (on average) to append to list

    def delete(self, key):
        """Delete the given key from this hash table, or raise KeyError.
        TODO: Running time: O(???) Why and under what conditions?"""
        # TODO: Find bucket where given key belongs
        # TODO: Check if key-value entry exists in bucket
        # TODO: If found, delete entry associated with given key
        # TODO: Otherwise, raise error to tell user delete failed
        # Hint: raise KeyError('Key not found: {}'.format(key))
        bucket = self._find_bucket(key) # O(1) time (on average) to call coupled functions to find bucket
        entry = bucket.find_using_lambda_fn(lambda entry: entry[0] == key) # O(1) time (on average) to call coupled functions to find entry
        if entry is None:  # O(1) time to evaluate conditional
            raise KeyError('Key not found: {}'.format(key))  # O(1) time to raise error
        else: 
            bucket.delete((entry))  # O(1) time to delete entry

def test_hash_table():
    ht = HashTable()
    print('hash table: {}'.format(ht))

    print('\nTesting set:')
    for key, value in [('I', 1), ('V', 5), ('X', 10)]:
        print('set({!r}, {!r})'.format(key, value))
        ht.set(key, value)
        print('hash table: {}'.format(ht))

    print('\nTesting get:')
    for key in ['I', 'V', 'X']:
        value = ht.get(key)
        print('get({!r}): {!r}'.format(key, value))

    print('contains({!r}): {}'.format('X', ht.contains('X')))
    print('length: {}'.format(ht.length()))

    # Enable this after implementing delete method
    delete_implemented = True
    if delete_implemented:
        print('\nTesting delete:')
        for key in ['I', 'V', 'X']:
            print('delete({!r})'.format(key))
            ht.delete(key)
            print('hash table: {}'.format(ht))

        print('contains(X): {}'.format(ht.contains('X')))
        print('length: {}'.format(ht.length()))


if __name__ == '__main__':
    test_hash_table()
