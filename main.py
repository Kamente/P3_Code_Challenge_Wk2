from customer import Customer
from review import Review
from restaurant import Restaurant

customer1 = Customer("Justin", "Kamente")
restaurant1 = Restaurant("Cratex")

customer1.add_review(restaurant1, 4)
average_rating = restaurant1.average_star_rating()
print(f"Average rating for {restaurant1.name} = {average_rating}")
