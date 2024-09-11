class BrowsingHistory:
    def __init__(self):
        # Initialize an empty stack for browsing history
        self.stack = []

    def add_page(self, page):
        """Add a new page to the stack (browsing history)."""
        self.stack.append(page)
        print(f"Page '{page}' added to browsing history.")

    def remove_page(self):
        """Remove and return the last visited page from the stack."""
        if self.stack:
            last_page = self.stack.pop()
            print(f"Page '{last_page}' removed from browsing history.")
            return last_page
        else:
            print("No pages to remove from browsing history.")
            return None

    def pages_viewed(self):
        """Return the number of pages viewed in this session."""
        return len(self.stack)

    def is_empty(self):
        """Check if the browsing session is empty."""
        return len(self.stack) == 0


# Test the BrowsingHistory class
if __name__ == "__main__":
    # Initialize browsing history manager
    history = BrowsingHistory()

    # Add some pages to browsing history
    history.add_page("https://example.com")
    history.add_page("https://openai.com")
    history.add_page("https://github.com")

    # Check how many pages viewed
    print(f"Pages viewed: {history.pages_viewed()}")

    # Check if the browsing session is empty
    print(f"Is browsing history empty? {history.is_empty()}")

    # Remove a page
    history.remove_page()

    # Check how many pages viewed after removal
    print(f"Pages viewed: {history.pages_viewed()}")

    # Check if browsing history is empty
    print(f"Is browsing history empty? {history.is_empty()}")
