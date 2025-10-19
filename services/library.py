from models.book import Book
from services.payment import Payment

class Library:
    def __init__(self):
        self._books = []

    def add_book(self, book):
        self._books.append(book)

    def find_book_by_isbn(self, isbn):
        for book in self._books:
            if book._isbn == isbn:
                return book
        return None

    # DIP: This method depends on the Payment abstraction.
    def pay_late_fee(self, book, days_late, payment_method: Payment):
        fee = book.calculate_late_fee(days_late)
        print(f"Late fee to pay: ${fee}")
        success = payment_method.process_payment(fee)
        if success:
            print("Payment successful! Your account is clear.")
        return success