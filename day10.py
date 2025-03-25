#un packing of objects or packages

# tup = ("semester", "anual", "master")

# (tup1,tupe2,tup3) = tup
# print(tup1)

#agr zyada values ajain kisi b tuple me ajain or hmain sirf aik ya 2 zyada values chahiye hou or baki ko 
#unpack na krna ho to hum * use krtay hain let's see

# tup = ("semester", "anual", "master", "m phil", "phd")

# (tup1,tupe2,*tup3) = tup
# print(tup3)


#sets data type

# st = {"hello","world","how are you"}
# print(type(st))
# print(st)

#set aik unorder data type hai means yeh hai k agr hum is me values input krtay hain or bad me usko get krtay
#hain to yeh randomly print krta hai 

#set constructor method

# st = set (("hello","world","how are you"))
# print(type(st))
# print(st)


#set update methods 


# st = set (("hello","world","how are you"))
# st1 = set (("sigle", "double"))

# st.update(st1)

# print(type(st))
# print(st)

#add method
#set data structure duplicate values ko nhi leta hai or print aik hi value ko krwata hai

# st = set (("hello","world","how are you"))
# st.add("Philoshper")

# print(type(st))
# print(st)

# st = set (("hello","world","how are you", True, 1 ,0))
# # st1 = set (("sigle", "double"))

# # st.update(st1)

# print(type(st))
# print(st)

# st = set (("hello","world","how are you", True, 1 ,0 ,"yes","no"))


# print(type(st))
# print(st)

st = set (("hello","world","how are you",'hello'))
print(st)