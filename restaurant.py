class Restaurant:
    restaurants = []
    customer_list = []
    
    def __init__(self, name):
        self.name = name
        self.reviews = []
    
    def name(self):
        return self.name
    
    def reviews(self):
        return self.reviews
    
    def customers(self):
        for customer in self.customers:
            pass
    
restaurant = Restaurant("Cratex")
print (restaurant.name())
    # def customers(self):
    #     return  