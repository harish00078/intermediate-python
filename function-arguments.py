###
# 1. diffrence between the function-arguments and function-parameters
# 2. positional and keyword arguments
# 3. default arguments
# 4. variable-length arguments(*args and **kwargs) args= arguments and kwargs = keyword arguments
# 5. container unpacking into function arguments
# 6. local vs global arguments
# 7. parameter passing (by value or by reference)###


# function = Python Functions is a block of related statements designed to perform a computational, logical, or evaluative task. The idea is to put some commonly or repeatedly done tasks together and make a function so that instead of writing the same code again and again for different inputs, we can do the function calls to reuse code contained in it over and over again. 

#Functions can be both built-in or user-defined. It helps the program to be concise, non-repetitive, and organized.


# create a function 

# def print_name(name):   #  (print_name) is our  function and (name) is our argument
#     print(name)
    
    
# print_name('alex')   # here we gave a value to our argument this is also our argument.

# def foo(a,b=2,c,d=4):  # b=2 have same value in print value that,s why this will gave us a error
#     print(a,b,c,d)
    
  
# # in these way i can get the output from the arguments  
# foo(1,2,3)
# foo(a=1,b=2,c=3)
# foo(c=1,b=2,a=3)
# #foo(1,b=2,3) # this will gave us a positional argument error
# #foo(1,b=2,a=3) #this will also gave as a error
# foo(1,2,3,7)


# that method is called variable length argument.
# def foo(a,b,*args,**kwargs): # we do not change the position or keyword of the values directly thats why in function  we use the argument for want to put a additional value or keyword-argument is use if we want to add a keyword value
#     print(a,b)
#     for arg in args:
#         print(arg)
#     for key in kwargs:
#         print(key, kwargs[key])
        
        
        
# foo(1,2,six=6,seven=7)
# foo(1,2,3,4,5)
# foo(1,2)


# force (arguments work with keyword arguments).
# def foo(a, b, *, c, d):
#     print(a,b,c,d)
    
# def foo(*args, last):
#     for arg in args:
#         print(arg)
#     print(last)
    
    
    
# foo(1,2,3, last=100)



# use list ,tuples, dictionary in function arguments.
# when we using  list,tuples,dictionary in function arguments we have to put a value acc to our variables.
# def foo(a,b,c):
#     print(a,b,c)

    


# my_dict = {'a':1,'b':2,'c':3}
# my_dict = {'e':1,'b':2,'c':3}  # this dictionary will gave me the error. 
   
# my_list = [0,1,2]
# my_list = [0,1,2,3] # this will not work beacuse it represent extra variable

# foo(*my_list)
    
    





# local and global variables.

# def foo():
#     global number  # this (global number) function will convert gobal variable into local variable
#     x = number# (x) is my local variable
#     number = 3 # global variable function will convert this local variable into global variable
#     print('number inside function',x)
    



# number = 0 # (number)is our global variable
# foo()  
# print(number)

# paramater passing.(by value or by reference).

def foo(a_list):
    # x = 5
    a_list += [200,300,400]
    # a_list.append(4)
    # a_list[0] = -100
    
    

    
my_list = [1,2,3]    
# var = 10
foo(my_list)
print(my_list)
    










