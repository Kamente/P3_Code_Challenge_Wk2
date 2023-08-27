class Restaurant:
    restaurants = []
    
    def __init__(self, name):
        self.name = name
        self.reviews = []
    
    def name(self):
        return self.name
    
    def reviews(self):
        return self.reviews
    
restaurant = Restaurant("Cratex")
print (restaurant.name())
    # def customers(self):
    #     return  
