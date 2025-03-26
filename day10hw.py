set1 = {"lahore","karachi","sialkot"}
set2 = {"gujrawala","faislabad"}
set3 = {"narowal","bahawalnagar","haroonabad"}
set4 = {"multan","rahim yar khan","quatta"}

resultset = set1 | set2 | set3 | set4

print("Joint set")
print(resultset)
print("____________________________________________________________________________")
rs1 = list(resultset)
rs2 = tuple(resultset)

print(rs1)
print("_____________________________________________________________________________")
print(rs2)