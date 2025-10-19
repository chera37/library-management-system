from models.book import Book
from datetime import date

class User:
    def __init__(self, user_id, name, email):
        self._user_id = user_id  # Encapsulated attribute
        self._name = name
        self._email = email
        self._checked_out_books = []  # List of (book, due_date) tuples
        self._late_fees = 0.0

    # Getter methods for encapsulated data
    def get_user_id(self):
        return self._user_id

    def get_name(self):
        return self._name

    def get_email(self):
        return self._email

    def get_checked_out_books(self):
        return self._checked_out_books

    def get_late_fees(self):
        return self._late_fees

    def check_out_book(self, book: Book):
        if book.check_out():
            due_date = date.today()  # This would be calculated based on checkout date
            self._checked_out_books.append((book, due_date))
            print(f"Book '{book.get_title()}' checked out successfully.")
            return True
        else:
            print(f"Book '{book.get_title()}' is already checked out.")
            return False

    def return_book(self, book: Book, days_late=0):
        for checked_out_book, due_date in self._checked_out_books:
            if checked_out_book == book:
                book.check_in()
                self._checked_out_books.remove((checked_out_book, due_date))
                
                if days_late > 0:
                    late_fee = book.calculate_late_fee(days_late)
                    self._late_fees += late_fee
                    print(f"Book returned {days_late} days late. Late fee: ${late_fee:.2f}")
                else:
                    print(f"Book '{book.get_title()}' returned successfully.")
                return True
        print(f"Book '{book.get_title()}' was not checked out by this user.")
        return False

    def pay_late_fees(self, payment_method, amount=None):
        if amount is None:
            amount = self._late_fees
        
        if amount > self._late_fees:
            print(f"Cannot pay more than outstanding late fees (${self._late_fees:.2f})")
            return False
        
        # This would integrate with the Payment service
        success = payment_method.process_payment(amount)
        if success:
            self._late_fees -= amount
            print(f"Payment of ${amount:.2f} successful. Remaining late fees: ${self._late_fees:.2f}")
        return success

    def __str__(self):
        return f"User(ID: {self._user_id}, Name: {self._name}, Email: {self._email}, Late Fees: ${self._late_fees:.2f})"