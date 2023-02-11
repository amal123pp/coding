#decorators 

#use - for example i have two functions
# 1- finding the square
# 2 - finding the cube
 
#  and my aim is to calculate the time for calculation of each function.here i have to modify the code in both places

#  what if there were 500 functions.

#also the logic of these functions were to do a mathematical calc.if i add some code related to timing, then 
#the logic is mixed and become a bit complex

#so decorator allows to wrap a function inside another function

import time

def time_it(func):
    def wrapper(*args,**kwargs):
        start = time.time()
        result = func(*args,**kwargs) #where the call to the real function takes place and returns
        end = time.time()
        print(func.__name__+'took'+str((end-start)*1000))
        return result
    return wrapper

@time_it
def calc_square(numbers):
    res =[]
    for number in numbers:
        res.append(number**2)
    return res

@time_it
def calc_cube(numbers):
    res =[]
    for number in numbers:
        res.append(number**3)
    return res

array = range(1,100000)
out_square = calc_square(array)
out_cube = calc_cube(array)