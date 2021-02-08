import uuid
from datetime import date


class Book:
    def __init__(self,
                 title,
                 author_name,
                 is_borrowed=False,
                 borrowed_by=None,
                 borrowed_at=None,
                 borrowed_until=None):
        self.is_borrowed = is_borrowed
        self.borrowed_until = borrowed_until
        self.borrowed_by = borrowed_by
        self.borrowed_at = borrowed_at
        self.title = title
        self.author = author_name
