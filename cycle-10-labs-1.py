# Author: SCT (AMDG) 2/1/22

# Defining the Function
def sum_all(number): # Start defining of sum function
    result = 0 # sets blank value for result
    x = 0 # sets blank value to use as a counter for while loop
    
    # While loop that iterates each number from zero, counting up and adding them until it reaches the inputed number
    while x < number: 
        result += x + 1
        x += 1
    return result

# Test Cases
print(sum_all(6))