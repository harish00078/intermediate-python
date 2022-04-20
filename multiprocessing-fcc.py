# from multiprocessing import Process
# import os

# def square_number():
#     for i in range(1000):
#         i * i
        
        
# if  __name__ == "__main__":
#     processes = []
#     num_processes = os.cpu_count() # number of cpus on the machine.usually a good choise for the number of processes
    
    
    
#     # create processes and asign a function for each process
#     for i in range(num_processes):
#         process = Process(target=square_number)
#         processes.append(process)
        
        
#     # start all processes 
#     for process in processes:
#         process.start()
        
#     # wait for all processes to finish
#     # block the main program until these processes are finished
#     for process in processes:
#         process.join()
        

from multiprocessing import Process, Value, Array, Lock
import time

def add_100(number,lock):
    for i in range(100):
        time.sleep(0.01)
        # lock.acquire()
        with lock:   #  we use (with lock) function instead of using (lock.acquire/lock.release)
            number.value += 1
        # lock.release()
        
        
if __name__ == "__main__":
    
    lock  = Lock()
    shared_number = Value('i',0)
    print("number at beginning is",shared_number.value)
    
    
    p1 = Process(target=add_100, args=(shared_number,lock))
    p2 = Process(target=add_100, args=(shared_number,lock))
    
    p1.start()
    p2.start()
    
    p1.join()
    p2.join()
    
    
    print('number at end is',shared_number.value)

    


        
        
    