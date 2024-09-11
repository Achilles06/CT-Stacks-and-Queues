from collections import deque

class OrderQueue:
    def __init__(self):
        # Initialize an empty queue for orders
        self.queue = deque()

    def add_order(self, order):
        """Add a new order to the end of the queue."""
        self.queue.append(order)
        print(f"Order '{order}' added to the queue.")

    def complete_order(self):
        """Remove and return the first order from the queue (FIFO)."""
        if self.queue:
            completed_order = self.queue.popleft()
            print(f"Order '{completed_order}' completed.")
            return completed_order
        else:
            print("No orders to complete.")
            return None

    def view_orders(self):
        """Display current orders in the queue."""
        if self.queue:
            print("Current orders in the queue:", list(self.queue))
        else:
            print("No orders in the queue.")


# Test the OrderQueue class
if __name__ == "__main__":
    # Initialize the order queue
    kitchen_queue = OrderQueue()

    # Add orders
    kitchen_queue.add_order("Pizza")
    kitchen_queue.add_order("Burger")
    kitchen_queue.add_order("Pasta")

    # View current orders
    kitchen_queue.view_orders()

    # Complete orders
    kitchen_queue.complete_order()

    # View remaining orders
    kitchen_queue.view_orders()
