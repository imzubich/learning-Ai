# #multiline Strings
# #which covers a whole paragraph (this is written in three qoutes """)
# #multiline String example

# b = """hello world how are 
# ucks ka sahi matlab hai "physical intimacy" ya "sexual relations", lekin yeh word aksar informal aur vulgar tone mein istemaal hota hai.

# Urdu mein, fucks ka matlab hai "sharamnaak kaam" ya "badmaashi", lekin yeh word aksar apni asli meaning se alag istemaal hota hai.

# Aksar, fucks word ko frustration, anger, ya disappointment ke liye bhi istemaal kiya jata hai, jaise "You fucks me" ka matlab "Tum ne mujhe pareshan kar diya" ya "Tum ne mujhe frustrate kar diya"""

# print(b)


# #to find the length of a string we use the len function

# print(len(b))



#cancatenation
#in which method we can combine the two strings and strings with other data types 

#cancatenation examples

# a =" hello"
# b = " World"
# print(a + b)


#we can use the formats to cancatenate the strings with other data types

# marks = 45
# total = "Your total marks are 100 and you got {}"
# obt = total.format(marks)
# print(obt)


# age = 24
# total = 100
# obt = 90

# res = "Your age is {} and the total marks {} in the exame and you got {}"

# final = res.format(age,total,obt)
# print(final)



#string slicing

# a = "hello world"

# print(a[0:6])


#split in strings


# a = "hello AI class"

# b = a.split(" ")
# print(a, b)

#Question
# Q1 ther is a given paragraph in which we have to find the most repeated words and count that how much that word is repeated in the paragraph


#upper case and lower in strings in python

st = "hello World!"
up = st.upper()
lo = st.lower()
print(up,lo)
