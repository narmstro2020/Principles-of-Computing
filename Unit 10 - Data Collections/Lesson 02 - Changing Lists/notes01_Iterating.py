# Iterating through Lists
# top_cities = ['New York City', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix']
# for city in top_cities:
#     print('Current city:', city)


# top_cities = ['New York City', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix']
# for city_index in range(len(top_cities)):
#     print('Rank:', city_index + 1, '| Current city:', top_cities[city_index])

spendings = [32.45, 18.65, 23.45, 78.32, 5.23, 7.32]
sum = 0.0
for spending in spendings:
    sum += spending
print('Money spent:', sum)
print("Average cost per item", sum / len(spendings))
