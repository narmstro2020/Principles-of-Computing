# fav_band = 'Green Day'
# print(fav_band[6])

# print(fav_band[:6])

# fav_band[6] = 'M'

# text = "please capitlise me"
# text_cap = text.upper()
# print(text_cap)

user_number = input('Please provide a number: ')
if user_number.isnumeric():
    print('Thank you, that\'s a correct number!')
elif user_number[0] == "-" and user_number[1:].isnumeric():
    print("You have a negative whole number")
elif user_number.count(".") == 1 and user_number.replace(".", "").isnumeric():
    print("You have a positive decimal number")
elif user_number.count(".") == 1 and user_number[0] == "-" and user_number.replace(".", "")[1:].isnumeric():
    print("You have a negative decimal number")
else:
    print('Sorry,', user_number, 'is not a number!')

