def safeDivide(dividend, divisor):
    if divisor == 0:   #This is the case for undefined.  aka None
        ## return something to handle this
        pass    ##remove the pass when done. 
    else:              #This is the case for regular division.  Return the regular divison of dividend and divisor
        ## return something to handle this.  
        pass  ## remove the pass when done.

x = safeDivide(3, 0)   # Should give you None   because 3 / 0
y = safeDivide(3, 2)   # Should give you 1.5    because 3 / 2
z = safeDivide(2, 3)   # Should give you 0.666666666667  because 2 / 3

print(x)
print(y)
print(z)