# use cases of asterisk operator(*) or star operator 
# basically check we were we use or many ways we use the star (*) operator


# # 1. star operator  is used for multiplication
# result = 5*7
# print(result)

# # 2. if we use two stars. this represents the power

# result = 2**4
# print(result)

# # 3. use start operator in list

# zeros = [0,1] * 10
# print(zeros)

# # 4. use star operator for tuples
# zeros = (0,1) * 10
# print(zeros)

# # 5. use star operator for string
# zeros = "AB" * 10
# print(zeros)

# 6. use star operator in (args) or (kwargs)
# def foo(a,b, *args, **kwargs):
#     print(a,b)
#     for arg in args:
#         print(arg)
#     for key in kwargs:
#         print(key,kwargs[key])
        
        
        
# foo(1,2,3,4,5,six=6,seven=7)
    
# def foo(a,b,c):
#     print(a,b,c)
    
    
# my_list = [0,1,2]
# my_dict = {'a':1,'b':2,'c':3}
# foo(**my_dict)
# foo(*my_list)


# numbers = [1,2,3,4,5,6]

# *beginning, middle, secondlast, last = numbers
# print(beginning)
# print(middle)
# print(secondlast)
# print(last)
    
# 7. we can also merge list in tuple or both using star operator


my_tuple = (1,2,3)
# my_list  = [4,5,6]
my_set = {4,5,6}

new_list = [*my_tuple, *my_set]

# new_list = [*my_tuple, *my_list]
print(new_list)



dict_a = {'a': 1,'b': 2}

dict_b = {'c': 3,'d': 4}

my_dict = {**dict_a, **dict_b}
print(my_dict)