from abc import ABC, abstractmethod
from datetime import date, timedelta

class Book(ABC):
    def __init__(self, title, author, isbn, publication_date):
        self._title = title
        self._author = author
        self._isbn = isbn
        self._publication_date = publication_date
        self._is_checked_out = False

    def get_title(self):
        return self._title

    def get_author(self):
        return self._author

    def get_isbn(self):
        return self._isbn

    def check_out(self):
        if not self._is_checked_out:
            self._is_checked_out = True
            return True
        return False

    def check_in(self):
        self._is_checked_out = False

    @abstractmethod
    def calculate_late_fee(self, days_late):
        pass

    def __str__(self):
        return f"'{self._title}' by {self._author}"