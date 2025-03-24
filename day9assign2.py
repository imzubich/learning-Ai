tup1 = ("Faislabad", "Jaranwala", "Lahore")
tup2 = (1,2,3,4,5,6)
# tup3 = tup2 + tup1

tupls1 = list((tup1))
tupls2 = list((tup2))

tup = []

tup[0:len(tupls1)] = tupls1
tup[len(tupls1):] = tupls2

tup_1 = tuple((tup))

print(tup_1)