class Customer:
    customers = []

    def __init__(self, given_name, family_name):
        self.given_name = given_name
        self.family_name = family_name
        self.customers.append(self)
        self.reviews = []


    def given_name(self):
        return self.given_name

    def family_name(self):
        return self.family_name

    def full_name(self):
        return f'{self.given_name} {self.family_name}'

    def add_review(self, restaurant, rating):
        new_review = Review(self, restaurant, rating)
        self.reviews.append(new_review)

    def num_reviews(self):
        return len(self.reviews)

    @classmethod
    def all(cls):
        return cls.customers

    @classmethod
    def find_by_name(cls, name):
        for customer in cls.customers:
            if customer.full_name() == name:
                return customer
        return None

    @classmethod
    def find_all_by_given_name(cls, name):
        matching_customers = []
        for customer in cls.customers:
            if customer.given_name == name:
                matching_customers.append(customer)
        return matching_customers

    def restaurants(self):
        reviewed_restaurants = []
        for review in self.reviews:
            if review.restaurant() not in reviewed_restaurants:
                reviewed_restaurants.append(review.restaurant())
        return reviewed_restaurants

from review import Review