class Car:
    def __init__(self,model,color,year):
        self.model = model
        self.color = color
        self.year = year

    def __str__(self):
        return f"Model: {self.model}\n color: {self.color}\n year: {self.year}"
    
car = Car("Honda Civic","Silver",2014)
print()
print(car)

class Restaurant:
    name = ''
    category = ''
    active = False
    stars = 0
    value = ""

    def __init__(self,name,category,active,stars,value):
        self.name = name
        self.category = category
        self.active = False
        self.stars = stars
        self.value = value

    def __str__(self):
        return f"Name: {self.name}\n Category: {self.category}"
        


restaurant = Restaurant("Wild Food","Street",True,5,"Expensive")

print()
print(restaurant)



class Client:
    def __init__(self, name, color, country, age):
        self.name = name
        self.color = color
        self.country = country
        self.age = age

    def __str__(self):
        return f"Client:\n Name: {self.name}\n color: {self.color}\n country: {self.country}\n age: {self.age}"
    


client = Client("Miranda","brown","Brazil",20)

print()
print(client)