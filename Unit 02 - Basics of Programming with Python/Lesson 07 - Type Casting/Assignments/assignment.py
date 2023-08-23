'''
Create a temperature converter.  

Ask the user for the temperature in Fahrenheit as a variable F
Convert this to a float
Use the following math to figure out the degrees in Celsius
C = 5 * (F - 32) / 9
C is the Celsius temperature.  
print out the result.  

Then do the the same for Celsius.  
Ask the user for the temp in Celsius and convert to Fahrenheit
The Formula is
F = 1.8 * C + 32
'''

fah = float(input("Enter the temp in degrees F. ")) 
cel = 5 * (fah - 32) / 9
print("The temperature in degrees C is:", cel)

#YOUDO:  the same but for the celsius to fahrenheit