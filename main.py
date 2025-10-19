# from models.book import Book
from models.ebook import EBook
from models.printed_book import PrintedBook
from models.user import User
from services.payment import CreditCardPayment, PayPalPayment
from services.library import Library
from datetime import date

def main():
    # Initialize library
    library = Library()
    
    # Create some books
    ebook1 = EBook("Python Programming", "John Doe", "978-0-123456-47-2", date(2023, 1, 15), 5.2)
    printed_book1 = PrintedBook("Clean Code", "Robert Martin", "978-0-13-235088-4", date(2008, 8, 1), 464)
    ebook2 = EBook("Design Patterns", "Erich Gamma", "978-0-201-63361-0", date(1994, 10, 21), 3.8)
    printed_book2 = PrintedBook("The Pragmatic Programmer", "Andrew Hunt", "978-0-13-595705-9", date(2019, 9, 13), 352)
    
    # Add books to library
    library.add_book(ebook1)
    library.add_book(printed_book1)
    library.add_book(ebook2)
    library.add_book(printed_book2)
    
    # Create users
    user1 = User("U001", "Alice Smith", "alice@email.com")
    user2 = User("U002", "Bob Johnson", "bob@email.com")
    
    print("=== LIBRARY MANAGEMENT SYSTEM ===")
    print("\n--- Demo: Book Checkout ---")
    
    # User checks out books
    user1.check_out_book(ebook1)
    user1.check_out_book(printed_book1)
    user2.check_out_book(ebook2)
    
    print("\n--- Demo: Polymorphism in Action ---")
    # Demonstrate polymorphism - same method, different implementations
    books_for_calculation = [ebook1, printed_book1, ebook2, printed_book2]
    
    print("Late fee calculation for 5 days late:")
    for book in books_for_calculation:
        late_fee = book.calculate_late_fee(5)
        print(f"  - {book.get_title()}: ${late_fee:.2f}")
    
    print("\n--- Demo: Book Return with Late Fees ---")
    # Simulate returning books with late fees
    user1.return_book(ebook1, 3)  # 3 days late
    user1.return_book(printed_book1, 7)  # 7 days late
    
    print(f"\nUser1 late fees balance: ${user1.get_late_fees():.2f}")
    
    print("\n--- Demo: SOLID Principles - Payment Processing ---")
    # Demonstrate Dependency Inversion and Interface Segregation
    credit_card_payment = CreditCardPayment()
    paypal_payment = PayPalPayment()
    
    print("Paying late fees with different payment methods:")
    
    # User pays with credit card
    library.pay_late_fee(printed_book1, 7, credit_card_payment)
    
    # User pays with PayPal (even though the book is already returned, we can still calculate)
    print("\nProcessing payment for user's late fees:")
    user1.pay_late_fees(credit_card_payment, 5.0)  # Pay $5 of the late fees
    
    print("\n--- Demo: Encapsulation ---")
    # Demonstrate encapsulation - we can't access private attributes directly
    print(f"Book title (via getter): {ebook1.get_title()}")
    print(f"User name (via getter): {user1.get_name()}")
    
    # This would cause an error if uncommented (attribute is private):
    # print(ebook1._title)  # This works but is against encapsulation principles
    # print(ebook1.__title) # This would cause AttributeError
    
    print("\n--- Demo: User Information ---")
    print(user1)
    print(user2)
    
    print("\n--- Books checked out by users ---")
    for user in [user1, user2]:
        checked_out = user.get_checked_out_books()
        if checked_out:
            print(f"{user.get_name()} has checked out:")
            for book, due_date in checked_out:
                print(f"  - {book.get_title()} (Due: {due_date})")
        else:
            print(f"{user.get_name()} has no books checked out.")

if __name__ == "__main__":
    main()