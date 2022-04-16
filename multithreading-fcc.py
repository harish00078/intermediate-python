# from threading import Thread



# def square_numbers():
#     for i in range(100):
#         i*i
        
        
# if __name__ == "__main__":
#     threads = []
#     num_threads = 10   # number of thread is ten
    
#     # create threads 
#     for i in range(num_threads):
#         thread = Thread(target=square_numbers)
#         threads.append(thread)
        
#     # start thread
#     for thread in threads:
#         thread.start()
        
        
#     # join threads: wait for them to complete
#     for thread in threads:
#         thread.join()
        
        
#     print('end main')

# from threading import Thread, Lock
# import time


# database_value = 0

# def increase(lock):
#     global database_value
#     # lock is use for having a better result in thread ( when you start the lock you have to end it also otherwise this will gave error to you)
#     # if i do not want to gave a start or release function to the lock we can gave a lock function to our function were we use the lock
#     with lock: # in this we can also create the lock to the thread 
        
#         local_copy = database_value
#     # lock.acquire()
#     # processing
#         local_copy += 1
#         time.sleep(0.1)
#         database_value = local_copy
#         # lock.release()
    

# if __name__ =="__main__":
    
     
#     lock = Lock()

#     print('start value',database_value)
    
    
    
#     thread1 = Thread(target=increase,args=(lock,))
#     thread2 = Thread(target=increase,args=(lock,))

#     thread1.start()
#     thread2.start()
    
#     thread1.join()
#     thread2.join()
    
#     print('end value',database_value)
    
    
#     print('end main')
    
    
# queue =  Like stack, queue is a linear data structure that stores items in First In First Out (FIFO) manner. With a queue the least recently added item is removed first. A good example of queue is any queue of consumers for a resource where the consumer that came first is served first.


# Enqueue: Adds an item to the queue. If the queue is full, then it is said to be an Overflow condition – Time Complexity : O(1)
# Dequeue: Removes an item from the queue. The items are popped in the same order in which they are pushed. If the queue is empty, then it is said to be an Underflow condition – Time Complexity : O(1)
# Front: Get the front item from queue – Time Complexity : O(1)
# Rear: Get the last item from queue – Time Complexity : O(1)

# example of queue:- how queue work
# from threading import Thread
# from queue import Queue
# import time

# if __name__ == "__main__":
#     q = Queue()
    
    
#     q.put(1)
#     q.put(2)
#     q.put(3)
    
#     # 3 2 1 -->
#     first = q.get()
#     print(first)
    
    
#     # q.task_done()
#     # q.join()
     
#     print('end main')
    
# example of queue how to use queue in thread:-
from threading import Thread, Lock, current_thread
from queue import Queue
import time


def worker(q,lock):
    while True:
        value = q.get()
        
        
        
        #processing:
        with lock:
            print(f'in {current_thread().name} got {value}')
        q.task_done()
        
    




if __name__ =="__main__":
    
    q = Queue()
    lock = Lock()
    
    num_threads = 10
    
    for i in range(num_threads):
        thread = Thread(target=worker, args=(q,lock))
        thread.daemon=True  # daemon = The threads which are always going to run in the background that provides supports to main or non-daemon threads, those background executing threads are considered as Daemon Threads. The Daemon Thread does not block the main thread from exiting and continues to run in the background.
        thread.start()
        
        
        
    for i in range(1,21):
        q.put(i)
        
    q.join()
    
    print('end  main')
    