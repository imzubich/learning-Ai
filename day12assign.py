# def city():
#     cities = ["Lahore", "Karachi", "Peshawar","Faislabad", "Sargodha"]
#     city1 = input("Please Eneter the City Name : ")
#     for x in cities:
#         if x == city1:
#             print("City in Cleaned")
#             break
#         else:
#             print("City is Not Clean")
# city()


def city():
    cities = ["Lahore", "Karachi", "Peshawar","Faislabad", "Sargodha"]
    city1 = input("Please Eneter the City Name : ")
    bol = False
    for x in cities:
        if(x == city1):
         bol = True

    if(bol):
        print("City in Cleaned")
    else:
        print("City is Not Clean")
city()