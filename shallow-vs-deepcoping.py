# copying:

# org = 5  # org represent here (original)
# import copy
# org = [0,1,2,3,4]
# cpy = org
# cpy[0]= -10
# print(cpy)
# print(org)

# types of copy.
# 1. shallow copy -> one level deep ,only references of nested child objects
# 2. deep copy -> full independent copy


# example of shallow copy.
# import copy
# org = [0,1,2,3,4]
# # we to copy the original value
# # cpy = copy.copy(org)
# # cpy =  org.copy()
# # cpy = list(org)
# cpy = org[:]
# cpy[0]= -10
# print(cpy)
# print(org) # in shallow copy the original value doesnot get affected or change 

# import copy
# org = [[0,1,2,3,4], [5,6,7,8,9]] # we use nested list (means list inside the list)
# cpy = copy.deepcopy(org)
# cpy[0] [1]= -10 # we can also change the value of the list
# print(cpy)
# print(org) # when we use deep copying our original value will we the same.(this is the diffrence between the deep coping and shallow copying)

import copy
class person:
    def  __init__(self, name, age):
        self.name = name
        self.age = age
        
        
        
class Company:
    def __init__(self, boss, employee):
        self.boss = boss
        self.employee = employee
        
        
p1 = person('alex',55)
p2 = person('joe',27)

company = Company(p1,p2)
company_clone = copy.copy(company)  # this is our shallow copy(here the original value get effect)
company_clone = copy.deepcopy(company)# this is deep copy( here the original value does not get affected)

company_clone.boss.age = 56
print(company_clone.boss.age)
print(company.boss.age)

        
        
# p1 = person('alex',27)
# p2 = copy.copy(p1)

# p2.age = 28
# print(p2.age)
# print(p1.age)
        