import random

class Queue:
    """
    A simple FIFO (First-In, First-Out) queue implementation.
    """
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        """
        Add an item to the end of the queue.
        """
        self.items.append(item)

    def dequeue(self):
        """
        Remove and return the item at the front of the queue.
        """
        if self.is_empty():
            return None
        return self.items.pop(0)

    def peek(self):
        """
        Return the item at the front of the queue without removing it.
        """
        if self.is_empty():
            return None
        return self.items[0]

    def is_empty(self):
        """
        Return True if the queue is empty.
        """
        return len(self.items) == 0

    def select_and_announce_winner(self):
        """
        Randomly selects a winner from the queue.
        Dequeues all customers up to and including the winner.
        Returns the name of the winning customer.
        """
        if self.is_empty():
            return None

        # Randomly select a winner
        winner = random.choice(self.items)

        # Dequeue customers until the winner is removed
        while True:
            removed = self.dequeue()
            if removed == winner:
                break

        return winner


# -----------------------------
# Demonstration / Output
# -----------------------------
if __name__ == "__main__":
    print("QUEUE DEMONSTRATION: Customer Raffle System\n")

    queue = Queue()

    # Enqueue 20 customers
    for i in range(1, 21):
        queue.enqueue(f"Customer #{i}")

    print("Initial queue:")
    print(queue.items)

    # Peek at the first customer
    print("\nFirst customer in line:")
    print(queue.peek())

    # Select and announce winner
    winner = queue.select_and_announce_winner()
    print(f"\n🎉 Winner selected: {winner}")

    # Show remaining queue
    print("\nRemaining customers after winner removal:")
    print(queue.items)
