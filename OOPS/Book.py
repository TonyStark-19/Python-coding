# This program creates a system for book management.

class Book:
    # total number of reviews added
    count = 0

    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.reviews = []

    def book_info(self):
        print("Book details:")
        print(f"The Book '{self.title}', written by {self.author}")

        if not self.reviews:
            print("No reviews yet.")
        else:
            for el in self.reviews:
                print(el, end=" ")
        print()

    def add_review(self, review):
        self.reviews.append(review)
        print(f"Review for Book {self.title} added!")
        Book.count += 1

    @classmethod
    def count_reviews(cls):
        print(f"Total reviews = {cls.count}")

    def print_all_reviews(self):
        for el in self.reviews:
            print(el)

# book 1
b1 = Book("Brief History of Time", "Stephen Hawking")

b1.add_review("Excellent")
b1.add_review("Fascinating")

b1.book_info()
b1.count_reviews()
b1.print_all_reviews()

# book 2
b2 = Book("Astrophyiscs for people in a hurry!", "Neil DeGrasse Tyson")

b2.add_review("Outstanding")
b2.add_review("Fascinating")

b2.book_info()
b2.count_reviews()
b2.print_all_reviews()