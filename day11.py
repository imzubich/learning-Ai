#all about dictionaries data type

# dic = {"name":"zubair"}
# print(type(dic))

# dic = dict({"name":"zubair"}) #is me hum paranthesis yani k small braces use nhi kr sktay constructor method me
# print(type(dic))

# print(len(dic)) #method to find the length of dictionary

#dictionary pairing values leta hai or us me hum colon (:) sy seperate krtay hain 

#CRUD METHOD IN DICTIONARY

#C FOR CREATE
#R FOR READ
#U FOR UPDATE 
#D FOR DELETE 

# CRUD method ki jankari bht zrori hai is k bgair development krna bht zyada mushkil hai blky na mumkin hai

# dic = dict({"name":"zubair"})

# print(dic["name"])

# print(dic.get("name"))

# dic["name"] = "Ali"

# dic["color"] = "white"
# print(dic)

dic = {"name":"zubair", "age":"24"}
dic.update({"color":"sanwla","height":"6f"})
# # dic.pop("color") #is me ap koi bhi key value dy kr delete kr sktay hain
# dic.popitem() #to remove last item in dictionary

# print(dic.keys())
# print(dic.values())
# print(dic.items())

# dic.clear()

# del dic
# print(dic) #here will be error after delete the dictionary

#pass by value & pass by reference

# a = 10
# b = a  #pass by value
# print(a,b)
# a = 30

# print(a,b)

a = 10
b = a  #pass by value
print(a,b)
a = 30

print(a,b)

