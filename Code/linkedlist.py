#!python


class Node(object):

    def __init__(self, data):
        """Initialize this node with the given data."""
        self.data = data
        self.next = None

    def __repr__(self):
        """Return a string representation of this node."""
        return f'Node({self.data})'


class LinkedList:

    def __init__(self, items=None):
        """Initialize this linked list and append the given items, if any."""
        self.head = None  # First node
        self.tail = None  # Last node
        # Append given items
        if items is not None:
            for item in items:
                self.append(item)

    def __repr__(self):
        """Return a string representation of this linked list."""
        ll_str = ""
        for item in self.items():
            ll_str += f'({item}) -> '
        return ll_str

    def items(self):
        """Return a list (dynamic array) of all items in this linked list.
        Best and worst case running time: O(n) for n items in the list (length)
        because we always need to loop through all n nodes to get each item."""
        items = []  # O(1) time to create empty list
        # Start at head node
        node = self.head  # O(1) time to assign new variable
        # Loop until node is None, which is one node too far past tail
        while node is not None:  # Always n iterations because no early return
            items.append(node.data)  # O(1) time (on average) to append to list
            # Skip to next node to advance forward in linked list
            node = node.next  # O(1) time to reassign variable
        # Now list contains items from all nodes
        return items  # O(1) time to return list

    def is_empty(self):
        """Return a boolean indicating whether this linked list is empty."""
        return self.head is None

    def length(self):
        """Return the length of this linked list by traversing its nodes.
        TODO: Running time: O(n) Why and under what conditions?"""
        # TODO: Loop through all nodes and count one for each
        count = 0 # O(1) time to create new variable
        node = self.head # O(1) time to assign new variable
        while node is not None: # Always n iterations because we have to crawl along the whole list
            node = node.next # O(1) time to reassign variable
            count += 1 # Not sure about this - but assuming O(1) time to do the addition
        return count # O(1) time to return variable


    def append(self, item):
        """Insert the given item at the tail of this linked list.
        TODO: Running time: O(???) Why and under what conditions?"""
        # TODO: Create new node to hold given item
        # TODO: If self.is_empty() == True set the head and the tail to the new node
        # TODO: Else append node after tail
        new_node = Node(item) # O(1) time to assign new variable
        if self.is_empty(): # O(1) time to check if array is empty
            self.head = new_node # O(1) time for variable assignment
            self.tail = new_node # O(1) time for variable assignment
        else: 
            self.tail.next = new_node # O(1) time for variable assignment
            self.tail = new_node # O(1) time for variable assignment

    def prepend(self, item):
        """Insert the given item at the head of this linked list.
        TODO: Running time: O(???) Why and under what conditions?"""
        # TODO: Create new node to hold given item
        # TODO: Prepend node before head, if it exists
        new_node = Node(item) # O(1) time to assign new variable
        if self.head is not None: # O(1) time to check if node is empty
            new_node.next = self.head # O(1) time for variable assignment
            self.head = new_node # O(1) time for variable assignment
        else: 
            self.head = new_node # O(1) time for variable assignment
            self.tail = new_node # O(1) time for variable assignment

    def find(self, match):
        """Return an item from this linked list if it is present.
        TODO: Best case running time: O(???) Why and under what conditions?
        TODO: Worst case running time: O(???) Why and under what conditions?"""
        # TODO: Loop through all nodes to find item, if present return True otherwise False
        
        #input is an item
        node = self.head # O(1) time for variable assignment
        while node is not None: # Always n iterations because we have to crawl along the whole list
            if node.data == match: # O(1) time to check match
                return True # O(1) time to return boolean
            else: 
                node = node.next # O(1) time for variable assignment
        return False # O(1) time to return boolean    
    
    def find_using_lambda_fn(self, matcher):
        node = self.head
        while node: 
            if matcher(node.data):
                return node.data
            node = node.next
        return None

    def delete(self, item):
        """Delete the given item from this linked list, or raise ValueError.
        TODO: Best case running time: O(???) Why and under what conditions?
        TODO: Worst case running time: O(???) Why and under what conditions?"""
        # TODO: Loop through all nodes to find one whose data matches given item
        # TODO: Update previous node to skip around node with matching data
        # TODO: Otherwise raise error to tell user that delete has failed
        # Hint: raise ValueError('Item not found: {}'.format(item))

        #check if list is empty and raise error if it is
        if self.head is None: # O(1) time to check if node is empty
            raise ValueError('List Empty.') # O(1) time to raise error

        #check if item is the first item - delete execution differs for first item
            #here we will address one item list as well
        node = self.head # O(1) time for variable assignment
        if node.data == item: # O(1) time to check if node.data == item
            if node.next is not None: # O(1) time to check 
                self.head = node.next # O(1) time for variable assignment
            else: 
                self.head = None # O(1) time for variable assignment
                self.tail = None # O(1) time for variable assignment
            return # O(1) time to terminate process flow

        #here we will crawl along rest of list
        while node is not None: # m+1 iterations (m being the position of the item being deleted) because we have to crawl along until item is found then also find the next item
            next_node = node.next # O(1) time for variable assignment
            if next_node is not None: # O(1) time to check
                if next_node.data == item: # O(1) time to check
                    new_next_node = next_node.next # O(1) time for variable assignment
                    if new_next_node is not None:  # O(1) time to check
                        node.next = new_next_node # O(1) time for variable assignment
                    else: 
                        self.tail = node # O(1) time for variable assignment
                        node.next = None # O(1) time for variable assignment
                    return # O(1) time to terminate process flow
            node = node.next # O(1) time for variable assignment

        raise ValueError('Item not found: {}'.format(item)) # O(1) time to raise error

    def replace(self, matcher, replacer):
        node = self.head  # O(1) time to assign new variable
        # Loop until matcher is found
        while node is not None:  # m iterations (m being the position of the item being replaced) because we have to crawl along until item is found
            if node.data == matcher: # O(1) time to check
                node.data = replacer  # O(1) time (on average) to append to list
            node = node.next  # O(1) time to reassign variable
        # Now list contains items from all nodes

def test_linked_list():
    ll = LinkedList()
    print('list: {}'.format(ll))
    print('\nTesting append:')
    for item in ['A', 'B', 'C']:
        print('append({!r})'.format(item))
        ll.append(item)
        print('list: {}'.format(ll))

    print('head: {}'.format(ll.head))
    print('tail: {}'.format(ll.tail))
    print('length: {}'.format(ll.length()))

    # Enable this after implementing delete method
    delete_implemented = False
    if delete_implemented:
        print('\nTesting delete:')
        for item in ['B', 'C', 'A']:
            print('delete({!r})'.format(item))
            ll.delete(item)
            print('list: {}'.format(ll))

        print('head: {}'.format(ll.head))
        print('tail: {}'.format(ll.tail))
        print('length: {}'.format(ll.length()))


if __name__ == '__main__':
    test_linked_list()
