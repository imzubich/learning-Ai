list1 = ["school", "college","private"]
tup1 = ("university","public")

#joining in set
set0 = set(list1) | set(tup1)

print(set0)
#type casting
set2 = set(tup1)


#difference

set_0 = set0 - set2
print("this is difference")
print(set_0)

#union method

set_uni = set0 | set2
print("this is union method")
print(set_uni)


#intersection method

set_inter = set0 & set2
print("this is intersection method")
print(set_inter)
