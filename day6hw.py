#take 10 cities and reverse there order and after that capitalize that cities

cities = ["lahore","faislabad","multan","muree","sialkot","bahawalnagar","bahawalpur","islamabad"]
rcity = []
final = []

for n in cities:
   rcity.insert(0,n)

for m in rcity:
    p= m[0:1].upper() + m[1:].lower()
    final.append(p)

# print(rcity)
print(final)
