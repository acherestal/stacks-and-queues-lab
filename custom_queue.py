import random

class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        # Add item to the end of the queue
        self.items.append(item)

    def dequeue(self):
        # Remove and return the front item
        if self.is_empty():
            return None
        return self.items.pop(0)

    def peek(self):
        # Return front item without removing it
        if self.is_empty():
            return None
        return self.items[0]

    def is_empty(self):
        return len(self.items) == 0

    def select_and_announce_winner(self):
        """
        Randomly selects a winner from the queue.
        Dequeues all items up to and including the winner.
        Returns the name of the winning customer.
        """
        if self.is_empty():
            return None

        winner = random.choice(self.items)

        # Remove customers until winner is removed
        while True:
            removed = self.dequeue()
            if removed == winner:
                break

        return winner
