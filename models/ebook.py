from models.book import Book

class EBook(Book):
    def __init__(self, title, author, isbn, publication_date, file_size):
        super().__init__(title, author, isbn, publication_date)
        self.file_size = file_size # In MB

    # Polymorphism: Overriding the abstract method
    def calculate_late_fee(self, days_late):
        # EBooks might have a small, fixed late fee or none at all
        return days_late * 0.10  # 10 cents per day