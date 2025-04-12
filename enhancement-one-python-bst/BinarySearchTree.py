import StaticMethods


class Bid:
    def __init__(self, bid_id="", title="", fund="", amount=0.0):
        self.bid_id = bid_id
        self.title = title
        self.fund = fund
        self.amount = amount


class Node:
    def __init__(self, bid=None):
        self.bid = bid
        self.left = None
        self.right = None


class BinarySearchTree:
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
        if self.root is None:
            self.root = Node(bid)
        else:
            self.add_node(self.root, bid)

    def remove(self, bid_id):
        """
        This function is called to remove the passed bid_id's bid from a binary search tree
        :param bid_id:
        :return:
        """
        self.root = self.remove_node(self.root, bid_id)

    def search(self, bid_id):
        """
        This function searches a binary search tree to find the passed bid_id.
        :param bid_id:
        :return the bid if found, else an empty bid:
        """
        curr = self.root
        while curr is not None and curr.bid.bid_id != bid_id:
            if bid_id < curr.bid.bid_id:
                curr = curr.left
            else:
                curr = curr.right
        return curr.bid if curr is not None else Bid()

    def add_node(self, node, bid):
        """
        Recursively called function to add the passed node with passed bid
        :param node:
        :param bid:
        :return:
        """
        if bid.bid_id < node.bid.bid_id:
            if node.left is None:
                node.left = Node(bid)
            else:
                self.add_node(node.left, bid)
        else:
            if node.right is None:
                node.right = Node(bid)
            else:
                self.add_node(node.right, bid)

    def remove_node(self, node, bid_id):
        """
        recursively called function that removes a node from a binary search tree
        :param node:
        :param bid_id:
        :return node:
        """
        if node is None:
            return node
        elif bid_id < node.bid.bid_id:
            node.left = self.remove_node(node.left, bid_id)
        elif bid_id > node.bid.bid_id:
            node.right = self.remove_node(node.right, bid_id)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            temp = StaticMethods.find_min(node.right)
            node.bid = temp.bid
            node.right = self.remove_node(node.right, temp.bid.bid_id)
        return node

    # traverse entire tree
    def in_order_traversal(self):
        """
        Function called to begin traversal through entire binary search tree
        :return:
        """
        self.in_order(self.root)
