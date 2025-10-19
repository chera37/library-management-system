from models.book import Book

class PrintedBook(Book):
    def __init__(self, title, author, isbn, publication_date, page_count):
        super().__init__(title, author, isbn, publication_date)
        self.page_count = page_count

    # Polymorphism: Overriding the abstract method with a different implementation
    def calculate_late_fee(self, days_late):
        # Printed books have a higher late fee
        base_fee = 2.00  # $2 base fee
        daily_fee = 0.50 # plus 50 cents per day
        return base_fee + (days_late * daily_fee)