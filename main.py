#NumPy ufuncs:

'''
#Without ufunc, we can use Python's built-in zip() method:

x = [1, 2, 3, 4]
y = [4, 5, 6, 7]
z = []

for i, j in zip(x, y):
  z.append(i + j)
print(z)                     '''


#Create Your Own ufunc:

'''
import numpy as np
def myadd(x,y):
    return x + y

myadd = np.frompyfunc(myadd, 2, 1)
print(myadd([1,2,3,4],[5,6,7,8]))          '''


'''
#Check if a Function is a ufunc:
#Use an if statement to check if the function is a ufunc or not:

import numpy as np

if type(np.add) == np.ufunc:
  print('add is ufunc')
else:
  print('add is not ufunc')             '''


#Simple Airthmetic:

'''

#Addition: Add the values in arr1 to the values in arr2:
import numpy as np

arr1 = np.array([10, 11, 12, 13, 14, 15])
arr2 = np.array([20, 21, 22, 23, 24, 25])

newarr = np.add(arr1, arr2)

print(newarr)                     '''


'''

#Substraction: Subtract the values in arr2 from the values in arr1:
import numpy as np

arr1 = np.array([10, 20, 30, 40, 50, 60])
arr2 = np.array([20, 21, 22, 23, 24, 25])

newarr = np.subtract(arr1, arr2)

print(newarr)                             '''


'''

#Multiplication:Multiply the values in arr1 with the values in arr2:
import numpy as np

arr1 = np.array([10, 20, 30, 40, 50, 60])
arr2 = np.array([20, 21, 22, 23, 24, 25])

newarr = np.multiply(arr1, arr2)

print(newarr)            '''

'''

#Division: Divide the values in arr1 with the values in arr2:

import numpy as np

arr1 = np.array([10, 20, 30, 40, 50, 60])
arr2 = np.array([3, 5, 10, 8, 2, 33])

newarr = np.divide(arr1, arr2)

print(newarr)                                '''


'''

#Power: Raise the valules in arr1 to the power of values in arr2:
import numpy as np

arr1 = np.array([10, 20, 30, 40, 50, 60])
arr2 = np.array([3, 5, 6, 8, 2, 33])

newarr = np.power(arr1, arr2)

print(newarr)                                   '''


'''

#Remainder: Return the remainders:
import numpy as np

arr1 = np.array([10, 20, 30, 40, 50, 60])
arr2 = np.array([3, 7, 9, 8, 2, 33])

newarr = np.mod(arr1, arr2)

print(newarr)                           '''


'''

#Using remainder() function:
import numpy as np

arr1 = np.array([10, 20, 30, 40, 50, 60])
arr2 = np.array([3, 7, 9, 8, 2, 33])

newarr = np.remainder(arr1, arr2)

print(newarr)                             '''


'''

#Quotient and Mod:

#Return the quotient and mod:

import numpy as np

arr1 = np.array([10, 20, 30, 40, 50, 60])
arr2 = np.array([3, 7, 9, 8, 2, 33])

newarr = np.divmod(arr1, arr2)

print(newarr)            '''


'''

#Absolute Values:
#Return the quotient and mod:

import numpy as np

arr = np.array([-1, -2, 1, 2, 3, -4])

newarr = np.absolute(arr)                       '''


#ufunc Rounding Decimals: there are 5 methods/ways to do it -  truncation, fix, rounding, floor, ceil

'''

#truncation:
import numpy as np

newarr = np.trunc([-3.1666, 3.6667])

print(newarr)                      '''

'''
#fix :

import numpy as np
newarr= np.fix([-3.12345, 3.34567])

print(newarr)                  '''


'''

#rounding: using arround() function

import numpy as np
newarr= np.around(3.1666, 2)

print(newarr)           '''


'''
#Floor:

#Floor the elements of following array:
import numpy as np

arr = np.floor([-3.1666, 3.6667])

print(arr)                            '''


'''
#Ceil():

#Ceil the elements of following array:

import numpy as np

arr = np.ceil([-3.1666, 3.6667])

print(arr)                             '''


#NumPy Logs:

'''
#Find log at base 2 of all elements of following array:
import numpy as np

arr = np.arange(1, 10)

print(np.log2(arr))                 '''


'''
#Find log at base 10 of all elements of following array:
import numpy as np

arr = np.arange(1, 10)

print(np.log10(arr))                  '''

'''

#Find log at base e of all elements of following array:
import numpy as np

arr = np.arange(1, 10)

print(np.log(arr))           '''

'''

#Log at any Base:
from math import log
import numpy as np

nplog = np.frompyfunc(log, 2, 1)

# value of l0g 100 on base 15
print(nplog(100, 15))               '''



#NumPy Summations:

'''
#Add the values in arr1 to the values in arr2:

import numpy as np

arr1 = np.array([1, 2, 3])
arr2 = np.array([1, 2, 3])

newarr = np.add(arr1, arr2)

print(newarr)                       '''


'''

#Sum the values in arr1 and the values in arr2:
import numpy as np

arr1 = np.array([1, 2, 3])
arr2 = np.array([1, 2, 3])

newarr = np.sum([arr1, arr2])

print(newarr)                               '''

'''
#Summation Over an Axis:
import numpy as np

arr1 = np.array([1, 2, 3])
arr2 = np.array([1, 2, 3])

newarr = np.sum([arr1, arr2], axis=1)

print(newarr)                               '''


'''

#Cummulative Sum:

#Perform cummulative summation in the following array:
import numpy as np

arr = np.array([1, 2, 3])

newarr = np.cumsum(arr)                     '''


'''

#NumPy Products:

#Products:  Find the product of the elements of this array:

import numpy as np

arr = np.array([1, 2, 3, 4])

#product: 1x2x3x4= 24
x = np.prod(arr)

print(x)                      '''


'''

#NumPy Differences:-  Differences

#Compute discrete difference of the following array:

import numpy as np

arr = np.array([10, 15, 25, 5])

newarr = np.diff(arr)

print(newarr)                      '''


''''

# E.g. for [1, 2, 3, 4], the discrete difference with n = 2 would be [2-1, 3-2, 4-3] = [1, 1, 1] , then,we will do it once more, with the new result: [1-1, 1-1] = [0, 0]:

#Compute discrete difference of the following array twice:

import numpy as np

arr = np.array([10, 15, 25, 5])

newarr = np.diff(arr, n=2)

print(newarr)                              '''

'''

#NumPy LCM Lowest Common Multiple:  Finding LCM (Lowest Common Multiple)

#Find the LCM of the following two numbers:

import numpy as np

num1 = 4
num2 = 6

x = np.lcm(num1, num2)

print(x)                          '''


#NumPy Trigonometric Functions:
#Trigonometric Functins: sin(), cos(), tan()

'''

#Find sine value of PI/2:

import numpy as np

x = np.sin(np.pi/2)

print(x)                '''

'''

#Find sine values for all of the values in arr:
import numpy as np

arr = np.array([np.pi/2, np.pi/3, np.pi/4, np.pi/5])

x = np.sin(arr)

print(x)                         '''

'''

#Convert Degrees Into Radians:-

#Convert all of the values in following array arr to radians:

import numpy as np

arr = np.array([90, 180, 270, 360])

x = np.deg2rad(arr)

print(x)                     '''


'''

#Convert all of the values in following array arr to degrees:

import numpy as np

arr = np.array([np.pi/2, np.pi, 1.5*np.pi, 2*np.pi])

x = np.rad2deg(arr)

print(x)                          '''

'''

#Finding angless:
#Find the angle of 1.0:

import numpy as np

x = np.arcsin(1.0)

print(x)                         '''


#Angles of Each Value in Arrays:-

'''
#Find the angle of 1.0:

import numpy as np

x = np.arcsin(1.0)

print(x)                    '''

''''

#Angles of Each Value in Arrays:

#Find the angle for all of the sine values in the array

import numpy as np

arr = np.array([1, -1, 0.1])

x = np.arcsin(arr)

print(x)             '''


'''

#Hypotenues: Finding hypotenues using pythagoras theorem in NumPy.

#Find the hypotenues for 4 base and 3 perpendicular:

import numpy as np

base = 3
perp = 4

#hypot() function that takes the base and perpendicular values
x = np.hypot(base, perp)

print(x)                         '''


#NumPy Hyperbolic Functions:-   Hyperbolic Functions

'''
#Find sinh value of PI/2:
import numpy as np

x = np.sinh(np.pi/2)

print(x)        '''

'''

#Find cosh values for all of the values in arr:

import numpy as np

arr = np.array([np.pi/2, np.pi/3, np.pi/4, np.pi/5])

x = np.cosh(arr)

print(x)                        '''

'''

#Finding Angles:
#Find the angle of 1.0:

import numpy as np

x = np.arcsinh(1.0)

print(x)                                    '''


'''

#Angles of Each Value in Arrays:-

#Find the angle for all of the tanh values in array:
import numpy as np

arr = np.array([0.1, 0.2, 0.5])

x = np.arctanh(arr)

print(x)                                         '''



