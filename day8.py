# ls = ["Karachi", "Lahore", "multan", "faislabad", "sargodha"]
# ls1 = []
# for x in ls:
#     if "a" in x:
#         ls1.append(x)

# print(ls1)

# ls1 = [print(x) for x in ls if "a" in x]

# ls = ["Karachi", "Lahore", "multan", "faislabad", "sargodha"]
# ls2 = [x for x in ls if x != "Karachi"]
# print(ls2)

# ls = ["Karachi", "Lahore", "multan", "faislabad", "sargodha"]

# ls3 = [x.capitalize() for x in ls]

# print(ls3)


ls = ["Karachi", "Lahore", "multan", "faislabad", "sargodha"]

ls3 = [x[0].upper + x[1:-1].lower +  for x in ls]