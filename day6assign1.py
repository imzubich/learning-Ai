ls = ["lahore","faislabad","karachi","Peshawar"]
lp= []
# print(ls)
for x in ls:
    p= x[0:1].lower() + x[1:2].upper() + x[2:-2].lower() + x[-2:-1].upper() + x[-1:].lower()
    print(p)
    lp.append(p)
    print(p)
print(lp)
