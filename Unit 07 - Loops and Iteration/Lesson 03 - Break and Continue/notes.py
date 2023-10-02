# break:  exits the loop or possibly the if statement.  
# continue:  skips the current step through the loops.  

while True:
    name = input("What is your name? (Enter EXIT to end.)")
    if name != "EXIT":
        print("Hi", name)
    else:
        print("EXITING")
        break

for counter in range(0, 11, 1):
    if counter % 3 == 0:
        continue
    else:
        print(counter)