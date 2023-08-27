class Customer:
    customers = []
    
    def __init__(self, given_name, family_name):
        self.given_name = given_name
        self.family_name = family_name
        self.customer.append(self) # to change after the customer is created
        self.reviews= []
    
    def given_name(self): # instance method to return the given_name
        return self.given_name
    
    def family_name(self):  # instance method to return the family_name
        return self.family_name
    
    def full_name(self):  # instance method to return the full_name. i.e given_name and family_name
        return f'{self.given_name} {self.family_name}'
    
    def add_review(self, restaurant, rating): # customer making new review
        new_review = Review(self, restaurant, rating)
        self.reviews.append(new_review)
        
    def num_reviews(self):
        return len(self.reviews_list)
    
    @classmethod # decorator method(return all the customer instances)
    def all(cls):
        return cls.customers