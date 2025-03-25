tup = ("v1","v2","v3","v4","v5","v6","v7","v8","v9","v10")
(t1,t2,t3,t4,t5,t6,t7,t8,*t9) = tup
# print(t9)
# print(type(t9))

t9.append("Hello")
t9.append("World")

print(t9)
 
set1 = set(t9)
print(set1)
