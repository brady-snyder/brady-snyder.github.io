import RedBlackTree
import StaticMethods
import time


def main():
    # Hard-Coded Variables
    csv_path = "eBid_Monthly_Sales.csv"
    bid_key = "98223"

    rbt = RedBlackTree.RedBlackTree()

    # Main Loop
    while True:
        print("Menu:")
        print("  1. Load Bids")
        print("  2. Display All Bids")
        print("  3. Find Bid")
        print("  4. Remove Bid")
        print("  9. Exit")
        choice = input("Enter choice: ").strip()

        # Load Bids
        if choice == '1':
            ticks = time.time()
            StaticMethods.load_bids(csv_path, rbt)
            ticks = time.time() - ticks
            print(f"time: {ticks} seconds")

        # Display All Bids
        elif choice == '2':
            rbt.in_order_traversal()

        # Find Hard-Coded Bid
        elif choice == '3':
            ticks = time.time()
            bid = rbt.search(bid_key)
            ticks = time.time() - ticks
            print(f"time: {ticks} seconds")
            if bid.bid_id:
                StaticMethods.display_bid(bid)
            else:
                print(f"Bid Id {bid_key} not found.")

        # Remove Hard-Coded Bid
        elif choice == '4':
            rbt.remove(bid_key)

        # Exit
        elif choice == '9':
            break
    print("Good bye.")


if __name__ == "__main__":
    main()
