# something or some programs are working on system that is called process(basically it means that anything or something is running on our system is known as process)
# defination of process:-Processes are basically the programs that are dispatched from the ready state and are scheduled in the CPU for execution. PCB(Process Control Block) holds the concept of process. A process can create other processes which are known as Child Processes. The process takes more time to terminate and it is isolated means it does not share the memory with any other process. The process can have the following states new, ready, running, waiting, terminated, and suspended. 

import multiprocessing
import time




# study the muliprocessing with example
###
# create two processes
# a. first is to calculate square of all numbers
# b. second one is to calculate cube of numbers ###

square_result = [] # instead of direct execute the result store the result in global variable
### every process has its own address space (means virtual memory).thus program variable are not shared between two processes.you need to use interprocess communication (ipc)techniques if you want to share data between two processes

def calc_square(numbers):
    global square_result
    for n in numbers:
        # time.sleep(0.5)
        print('sqaure' + str(n*n)) # here (n) have a values of array list
        square_result.append(n*n)
        print('with in a process:result'+str(square_result))  # here this will print the result beacuse this is in under function or process
        
        

    
# def calc_cube(numbers):
#     for n in numbers:
#         time.sleep(0.5)
#         print('cube' +str(n*n*n))
        
        
if __name__ == "__main__":
    arr = [2,3,8,9]
    p1 = multiprocessing.Process(target=calc_square, args=(arr,))  # agrs =  we want to make a multiply function that takes any number of arguments and able to multiply them all ( basically args is used to if i want to add another values that are not  in the functions)
    # p2 = multiprocessing.Process(target=calc_cube,args=(arr,))
    
    p1.start()
    # p2.start()

    p1.join()
    # p2.join()
    
    

print('result'+str(square_result)) # here this will not print the result beacuse this is not under in function 
print("done!")
    
    
