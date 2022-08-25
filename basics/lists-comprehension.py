cars = ["Mazda 3", "Toyota Prius", "Honda Civic", "Jetta"]

#Creating list comprehension

print("List Comprehension with variable")

lst_cpr = [car for car in cars if "Jetta" not in car]

print(lst_cpr)

print("List Comprehension")

[print (element) for element in cars if "Jetta" not in element]
[print (type(element)) for element in cars if "Jetta" not in element]

#Comparison with a loop

newCars = []
for e in cars:
    if "Jetta" not in e:
        newCars.append(e)

print(newCars)