class Restaurant:
    restaurants = []

    def __init__(self, name):
        self.name = name
        self.reviews = []

    def name(self):
        return self.name

    def reviews(self):
        return self.reviews

    def customers(self):
        customer_list = []
        for review in self.reviews:
            if review.customer() not in customer_list:
                customer_list.append(review.customer())
        return customer_list

    def average_star_rating(self):
        if not self.reviews:
            return 0
        total_rating = sum(review.rating() for review in self.reviews)
        return total_rating / len(self.reviews)

