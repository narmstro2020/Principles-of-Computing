'''
Write a program that asks the user how many frisbees they would like to buy, 
and then prints out the total cost. 

Since we know nothing of user input at this point just a random number for the amount of frisbees to buy

You should declare a constant at the top of your program called COST_OF_FRISBEE and set it equal to $15. 
Remember, constants should be formatted with all capital letters.

'''
COST_OF_FRISBEE = 15
frisbees = 3

total_cost = COST_OF_FRISBEE * frisbees

print("The total cost is $", total_cost, sep="")


