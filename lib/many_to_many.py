class Book:
    members = []

    def __init__(self, title):
        self.title = title
        Book.members.append(self)

    @classmethod
    def all_books(cls):
        return cls.members


class Author:
    members = []

    def __init__(self, name):
        self.name = name
        self._contracts = []
        Author.members.append(self)

    def contracts(self):
        return self._contracts

    def books(self):
        return [contract.book for contract in self._contracts]

    def sign_contract(self, book, date, royalties):
        contract = Contract(self, book, date, royalties)
        self._contracts.append(contract)
        return contract

    def total_royalties(self):
        total = 0
        for contract in self._contracts:
            total += contract.royalties
        return total


class Contract:
    members = []

    def __init__(self, author, book, date, royalties):
        if not isinstance(author, Author):
            raise Exception("Author must be an instance of Author class")
        if not isinstance(book, Book):
            raise Exception("Book must be an instance of Book class")
        if not isinstance(date, str):
            raise Exception("Date must be a string")
        if not isinstance(royalties, int):
            raise Exception("Royalties must be an integer")
        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties
        Contract.members.append(self)

    @classmethod
    def contracts_by_date(cls, date):
        return [contract for contract in cls.members if contract.date == date]


# Example usage:
if __name__ == "__main__":
    # Create authors
    author1 = Author("Author 1")
    author2 = Author("Author 2")

    # Create books
    book1 = Book("Book 1")
    book2 = Book("Book 2")

    # Sign contracts
    author1.sign_contract(book1, "2024-04-25", 10)
    author1.sign_contract(book2, "2024-04-26", 15)
    author2.sign_contract(book1, "2024-04-27", 20)

    # Accessing contracts by date
    contracts_on_25th = Contract.contracts_by_date("2024-04-25")
    for contract in contracts_on_25th:
        print(contract.author.name, "signed contract for", contract.book.title, "on", contract.date)

    # Total royalties earned by author1
    print("Total royalties earned by Author 1:", author1.total_royalties())

    # Accessing books by author1
    print("Books by Author 1:", [book.title for book in author1.books()])
