"""
TECH2 mandatory assignment - Part A

Write the implementation of part A of the exercise below.
"""
import numpy as np

# Initializing a list of numbers to calculate standard deviation
z=[1,2,3,4,5] 


def std_loops(x):

    total = 0 # Initialize sum of numbers
    count = 0 # Initialize count of numbers
    
  # First loop to calculate the sum of the list and the length
    for i in x: 
        total += i
        count += 1
    
    # Compute the mean (average) of the list
    mean = total/count
    
    variance = 0 # Initializing variance variable
   
    # Second loop to calculate the variance by summing squared differences from the mean
    for i in x:
        variance += (i-mean)**2 
    
    sd = (variance/count)**0.5 # Calculating the standard deviation
    
    return sd

print ('Standard deviation using loops is', std_loops(z))


def std_builtin(x):

    # Compute the mean using sum() and len()
    mean = sum(x)/len(x)
    
    variance = 0    # Initializing the variance variable
    
    # Loop to calculate variance by summing squared differences from the mean
    for i in x : 
        variance += (i-mean)**2 

    # Calculate the standard deviation by taking the square root of the variance
    sd = (variance/len(x))**0.5 
    
    return sd
        
print ('Standard deviation using sum() and len() is', std_builtin(z))

print ('Standard deviation using nympy is', np.std(z))
