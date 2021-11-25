
#         Key : Value
cars = {"brand":"Ford",
        "model":2021,
        "Colour":"blue"}

print(len(cars))
cars.update({"model":2022})

print(cars.pop("model"))

print(cars)

print(cars.popitem())

del cars["brand"]
print(cars)
