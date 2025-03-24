cities = ("lahore", "faislabad","karachi","bahawalnagar")

city = list((cities))
cityupper = []
for x in city:
    y = x[0:1].upper() + x[1:].lower()
    cityupper.append(y)

# print(cityupper)

cities = tuple((cityupper))

print(cities)
