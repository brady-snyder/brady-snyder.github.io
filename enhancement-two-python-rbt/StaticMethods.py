import csv

import BinarySearchTree


def display_bid(bid):
    """
    prints out bid_id, title, amount, and fund of passed bid
    :param bid:
    :return:
    """
    print(f"{bid.bid_id}: {bid.title}: {bid.amount}: {bid.fund}")


def str_to_float(string):
    """
    strips any commas or dollar signs a returns float value of passed number string
    :param string:
    :return float value:
    """
    string = string.replace('$', '')
    string = string.replace(',', '')
    return float(string)


def load_bids(csv_path, bst):
    """
    parses data from csv files and puts into a binary search tree
    :param csv_path:
    :param bst:
    :return:
    """
    print(f"Loading CSV file {csv_path}")
    with open(csv_path, newline='') as csv_file:
        csv_reader = csv.reader(csv_file)
        header = next(csv_reader)
        print(" | ".join(header))
        for row in csv_reader:
            bid = BinarySearchTree.Bid(row[1], row[0], row[8], str_to_float(row[4]))
            bst.insert(bid)


def find_min(node):
    """
    returns leftmost/min node
    :param node:
    :return:
    """
    curr = node
    while curr.left is not None:
        curr = curr.left
    return curr
