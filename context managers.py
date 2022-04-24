# example(1) of the context manager(open or close the database)
# two to ways to open the file.

# 1. first way to open the file or simple and recomended way to open the file
# with open('notes.txt','w') as file:
#     file.write('some tadoo...')
    
    
# # 2. second way to open the file ( but is complicated way to open the file)
    
# file = open('notes.txt','w')
# try:
#     file.write('some tadoo..')
# finally:
#     file.close()


# eample(2) of context manager is (Lock)
# from threading import Lock

# lock = Lock()
# # two ways to create a lock

# # first way of create a lock
# lock.acquire()  # were from i want to start my lock
# #.. here we have function under the lock
# lock.release() # were i want to release my lock


# # second way of creating a lock
# with lock:
#     #..


# # example(3) of the context manager ( working on our own classes)
# class managedfile:
#     def __init__(self, filename):
#         self.filename = filename
        
#     def __enter__(self): # this is our enter function
#         print('enter')   
#         self.file = open(self.filename,'w')
#         return self.file
        
        
#     def __exit__(self, exc_type, exc_value, exc_traceback):  # this is the exit function
#         if self.file:
#             self.file.close()
#         if exc_type is not None:  # (exc)  represent here exception
#             print('exception haas been handled')
#         # print('exc:',exc_type, exc_value)
#         print('exit')  
#         return True
        
        
        
        
# with managedfile('notes.txt') as file:
#     print('do some stuff....')
#     file.write('some tadoo...')
#     file.somemethod()  # this is exception that we put in our code
# print('continuing')

from contextlib import contextmanager

@contextmanager
def open_managed_file(filename):
    f = open(filename,'w')
    try:
        yield f    # in this function we use the generator
    finally:
        f.close()
    
    
with open_managed_file('notes.txt') as f:
    f.write('same tadoo....')