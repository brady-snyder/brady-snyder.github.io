import StaticMethods


class Bid:
    def __init__(self, bid_id="", title="", fund="", amount=0.0):
        self.bid_id = bid_id
        self.title = title
        self.fund = fund
        self.amount = amount


class Node:
    def __init__(self, bid=None, color='red'):
        self.bid = bid
        self.color = color
        self.left = None
        self.right = None
        self.parent = None

    def grandparent(self):
        """
        returns grandparent of node
        :return grandparent:
        """
        if self.parent is None:
            return None
        return self.parent.parent

    def sibling(self):
        """
        returns sibling of node
        :return sibling:
        """
        if self.parent is None:
            return None
        if self == self.parent.left:
            return self.parent.right
        return self.parent.left

    def uncle(self):
        """
        returns sibling of parent of node
        :return sibling of parent:
        """
        if self.parent is None:
            return None
        return self.parent.sibling()

class RedBlackTree:
    def __init__(self):
        self.root = None

    def __del__(self):
        self.delete_node(self.root)

    def delete_node(self, node):
        """
        This function recursively deletes a node
        :param node:
        :return:
        """
        if node is not None:
            self.delete_node(node.left)
            self.delete_node(node.right)
            del node

    def in_order(self, node):
        """
        This is a recursive function-call which traverses a tree in order
        :param node:
        :return:
        """
        if node is not None:
            self.in_order(node.left)
            StaticMethods.display_bid(node.bid)
            self.in_order(node.right)

    def insert(self, bid):
        """
        This function is called to insert the passed bid into a binary search tree
        :param bid:
        :return:
        """
        new_node = Node(bid)
        if self.root is None:
            new_node.color = 'black'
            self.root = new_node
        else:
            self.add_node(self.root, new_node)
            self.insert_fixup(new_node)

    def add_node(self, curr_node, new_node):
        """
        Iterative function to add the passed node with passed bid
        :param curr_node:
        :param new_node:
        :return:
        """
        parent = None
        # while node is not none, traverse down tree
        while curr_node is not None:
            parent = curr_node
            if new_node.bid.bid_id < curr_node.bid.bid_id:
                curr_node = curr_node.left
            else:
                curr_node = curr_node.right

        # if parent is None, the root is new_node
        new_node.parent = parent
        if parent is None:
            self.root = new_node

        # otherwise, place in correct spot in tree
        elif new_node.bid.bid_id < parent.bid.bid_id:
            parent.left = new_node
        else:
            parent.right = new_node

    def insert_fixup(self, node):
        """
        Fixes red-black scheme after insertion
        :param node:
        :return:
        """
        #while tree is not fixed
        while node.parent is not None and node.parent.color == 'red':
            #udpate variables
            grandparent = node.parent.parent
            if grandparent is None:
                break

            #if parent is left child of grandparent
            if node.parent == grandparent.left:
                uncle = grandparent.right

                # if uncle exists and is red, recolor
                if uncle is not None and uncle.color == 'red':
                    node.parent.color = 'black'
                    uncle.color = 'black'
                    grandparent.color = 'red'
                    node = grandparent
                else:

                    # if node is right child, left rotation
                    if node == node.parent.right:
                        node = node.parent
                        self.rotate_left(node)

                    #if node is left child, recolor and right rotation
                    node.parent.color = 'black'
                    grandparent.color = 'red'
                    self.rotate_right(grandparent)

            #otherwise, parent is right child of grandparent
            else:
                uncle = grandparent.left

                # if uncle exists and is red, recolor
                if uncle is not None and uncle.color == 'red':
                    node.parent.color = 'black'
                    uncle.color = 'black'
                    grandparent.color = 'red'
                    node = grandparent
                else:

                    # if node is left child, right rotation
                    if node == node.parent.left:
                        node = node.parent
                        self.rotate_right(node)

                    # if node is right child, recolor and left rotation
                    node.parent.color = 'black'
                    grandparent.color = 'red'
                    self.rotate_left(grandparent)

        #set root node to black
        self.root.color = 'black'

    def rotate_left(self, node):
        """
        rotates red-black tree left
        :param node:
        :return:
        """
        #Store reference and reassign right_child's left subtree to node's right
        right_child = node.right
        node.right = right_child.left

        #if it exists, update parent reference for the moved subtree
        if right_child.left is not None:
            right_child.left.parent = node

        #Connect right_child to node's parent
        right_child.parent = node.parent

        #Update root if node is root
        if node.parent is None:
            self.root = right_child

        #Update parent's child references
        elif node == node.parent.left:
            node.parent.left = right_child
        else:
            node.parent.right = right_child

        #Make node the left child of right_child
        right_child.left = node
        node.parent = right_child

    def rotate_right(self, node):
        """
        rotates red-black tree right
        :param node:
        :return:
        """

        #Store reference and reassign left_child's right subtree to node's left
        left_child = node.left
        node.left = left_child.right

        #if it exists, update parent reference for the moved subtree
        if left_child.right is not None:
            left_child.right.parent = node

        #Connect left_child to node's parent
        left_child.parent = node.parent

        #Update root if node is root
        if node.parent is None:
            self.root = left_child

        #Update parent's child references
        elif node == node.parent.right:
            node.parent.right = left_child
        else:
            node.parent.left = left_child

        #Make node the right child of left_child
        left_child.right = node
        node.parent = left_child

    def remove(self, bid_id):
        """
        This function is called to remove the passed bid_id's bid from a binary search tree
        :param bid_id:
        :return:
        """
        node = self.search_node(bid_id)
        if node is None:
            return  # Bid not found

        #If node has one or no children
        original_color = node.color
        if node.left is None:
            child = node.right
            self.transplant(node, node.right)
        elif node.right is None:
            child = node.left
            self.transplant(node, node.left)

        #otherwise, node has two children
        else:
            successor = StaticMethods.find_min(node.right)
            original_color = successor.color
            child = successor.right
            if successor.parent != node:
                self.transplant(successor, successor.right)
                successor.right = node.right
                successor.right.parent = successor
            self.transplant(node, successor)
            successor.left = node.left
            successor.left.parent = successor
            successor.color = node.color

        if original_color == 'black':
            self.remove_fixup(child if child else self.root)

    def remove_fixup(self, node):
        """
        Restore red-black scheme after deletion
        :param node:
        :return:
        """
        while node != self.root and node.color == 'black':
            sibling = node.sibling()
            if sibling is None:
                break

            if node == node.parent.left:

                #if sibling is red, convert to black sibling
                if sibling.color == 'red':
                    sibling.color = 'black'
                    node.parent.color = 'red'
                    self.rotate_left(node.parent)
                    sibling = node.sibling()

                #if both sibling's children are black, recolor
                if (sibling.left is None or sibling.left.color == 'black') and \
                    (sibling.right is None or sibling.right.color == 'black'):
                    sibling.color = 'red'
                    node = node.parent

                #if sibling's right child is black, rotate
                else:
                    if sibling.right is None or sibling.right.color == 'black':
                        sibling.left.color = 'black'
                        sibling.color = 'red'
                        self.rotate_right(sibling)
                        sibling = node.sibling()

                    # sibling's right child is red, final adjustment
                    sibling.color = node.parent.color
                    node.parent.color = 'black'
                    sibling.right.color = 'black'
                    self.rotate_left(node.parent)
                    node = self.root
            else:

                # if sibling is red, convert to black sibling
                if sibling.color == 'red':
                    sibling.color = 'black'
                    node.parent.color = 'red'
                    self.rotate_right(node.parent)
                    sibling = node.sibling()

                # if both sibling's children are black, recolor
                if (sibling.left is None or sibling.left.color == 'black') and \
                        (sibling.right is None or sibling.right.color == 'black'):
                    sibling.color = 'red'
                    node = node.parent

                # if sibling's left child is black, rotate
                else:
                    if sibling.left is None or sibling.left.color == 'black':
                        sibling.right.color = 'black'
                        sibling.color = 'red'
                        self.rotate_left(sibling)
                        sibling = node.sibling()

                    # sibling's left child is red, final adjustment
                    sibling.color = node.parent.color
                    node.parent.color = 'black'
                    sibling.left.color = 'black'
                    self.rotate_right(node.parent)
                    node = self.root
        if node:
            node.color = 'black'

    def transplant(self, old, new):
        """
        replace subtree at old node with subtree at new node
        :param old:
        :param new:
        :return:
        """
        if old.parent is None:
            self.root = new
        else:
            if old == old.parent.left:
                old.parent.left = new
            else:
                old.parent.right = new
        if new is not None:
            new.parent = old.parent

    def search(self, bid_id):
        """
        This function searches a red-black tree to find the passed bid_id.
        :param bid_id:
        :return the bid if found, else an empty bid:
        """
        node = self.search_node(bid_id)
        return node.bid if node else Bid()


    def search_node(self, bid_id):
        """
        returns node of passed bid_id
        :param bid_id:
        :return:
        """
        curr = self.root
        while curr is not None and curr.bid.bid_id != bid_id:
            if bid_id < curr.bid.bid_id:
                curr = curr.left
            else:
                curr = curr.right
        return curr

    def in_order_traversal(self):
        """
        Function called to begin traversal through entire red-black tree
        :return:
        """
        self.in_order(self.root)
