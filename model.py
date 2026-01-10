# models.py

class Expense:
    def __init__(self, title, amount, category):
        self.title = title
        self.amount = amount
        self.category = category

    def is_large(self):
        return self.amount >= 1000

    def to_dict(self):
        return {
            "title": self.title,
            "amount": self.amount,
            "category": self.category
        }
