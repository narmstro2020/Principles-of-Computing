city_1 = "New York City"
city_2 = "Los Angeles"
city_3 = "Houston"
city_4 = "Chicago"
city_5 = "Indianapolis"

empty_list = []
print(empty_list)
                    #0             #1            #2         #3            #4
top_cities = ["New York City", "Los Angeles", "Houston", "Chicago", "Indianapolis"]
print(top_cities)

print(top_cities[1])
# print(top_cities[5])  this will give an error IndexError

print(top_cities[-1])
print(top_cities[-2])

print(top_cities[0:3])
print(top_cities[:3])

print(top_cities[2:])
print(top_cities[2:15])
# print(top_cities[-15]) this will give an error IndexError
