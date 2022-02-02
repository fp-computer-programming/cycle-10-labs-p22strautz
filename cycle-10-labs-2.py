# Author: SCT (AMDG) 2/1/22

def division_of_five(list): # Defining the function  
    result = [] # Blank list to store results  
    for x in list: # loop that iterates each value in list
        if x > 500: # if value is > 500, stop
            break  
        elif x % 5 == 0 and x <= 150: # if value is divisible by 5 and <= 150, add to results
            result.append(x)
    return(result)

# Test cases
print(division_of_five([5, 10, 15, 20, 53,605]))