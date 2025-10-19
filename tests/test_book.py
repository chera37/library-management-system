import unittest
from models.ebook import EBook
from models.printed_book import PrintedBook
from datetime import date

class TestBooks(unittest.TestCase):
    def test_ebook_late_fee(self):
        ebook = EBook("Test Book", "Test Author", "123-456", date(2023, 1, 1), 2.5)
        self.assertEqual(ebook.calculate_late_fee(5), 0.50)  # 5 days * $0.10

    def test_printed_book_late_fee(self):
        printed_book = PrintedBook("Test Book", "Test Author", "123-456", date(2023, 1, 1), 200)
        self.assertEqual(printed_book.calculate_late_fee(5), 4.50)  # $2.00 + (5 days * $0.50)

    def test_book_checkout(self):
        book = EBook("Test Book", "Test Author", "123-456", date(2023, 1, 1), 2.5)
        self.assertTrue(book.check_out())  # First checkout should succeed
        self.assertFalse(book.check_out())  # Second checkout should fail

if __name__ == '__main__':
    unittest.main()