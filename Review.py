class Review:
    reviews = []
    
    def __init__(self, customer, restaurant,rating):
        self.customer = customer
        self.restaurant = restaurant
        self.rating = rating
        
    def rating(self):
        return self.rating
    
    def customer(self):
        return self.customer
    
    def restaurant(self):
        return self.restaurant
    
    @classmethod
    def all(cls):
        return cls.reviews