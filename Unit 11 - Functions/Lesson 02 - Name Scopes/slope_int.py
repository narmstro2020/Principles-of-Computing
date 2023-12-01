def slope_intercept(x_coeff, y_coeff, constant):
    m = str(-x_coeff) + "/" + str(y_coeff)
    b = str(constant) + "/" + str(y_coeff)
    print("y = " + m + " x + " + b)

slope_intercept(3, 2, 5)