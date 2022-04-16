# points related to thread.(main point:-Thread is the segment of a process means a process can have multiple threads )
# thread is also known as leight weight process.
# thread = if we scheduled a process or function or we want a process and function exectue faster or also want that process or  fucntion took a short storage of our system that why we use thread.
# 1 when we perform a big program in that program we had a small programs or function that we want to execute in short period of time or we want to scheduled there execution that's why we use thread
# 2 small , small processes we create according to my configration  is know as thread
# 3 what is thread (Threads in python are an entity within a process that can be scheduled for execution. In simpler words, a thread is a computation process that is to be performed by a computer. It is a sequence of such instructions within a program that can be executed independently of other codes).
# 4 thread is very usefull in big programs executions we can execute big programs very fast using threads
# 5 creating  thread we can use full power of our system cores or cpu
# 6 main point is that in thread use target method that will basically target a particular fucntion or value in program that we want to execute as a thread 


#defination of thread:-Thread is the segment of a process means a process can have multiple threads and these multiple threads are contained within a process. A thread has three states: Running, Ready, and Blocked. The thread takes less time to terminate as compared to the process but unlike the process, threads do not isolate. 





#  use python debugger to execute the thread or process program because sometime i had error in terminal (or try in jupyter notebook)
# this is the first way to create the thread
# example of how thread works
# from threading import Thread
# def  show():
#     print("this is a child thread")
    
# t = Thread(target=show()) # in this way we can create the thread 
# t.start()  # in this way we can start the thread

# print("this is parent thread")



# this is the second way to create the thread
# from threading import Thread
# class MyThread(Thread):
#     def run(self):
#         for i in range(5):
#             print("\nthis is a child class")
            
# t = MyThread()
# t.start()
# for i in range(5):
#     print("\nthis is the main thread") 

# this is the third way to create the thread
from threading import Thread
class demo:
    def show(self):
        for i in range(5):
            print("this is the child thread")
            
obj=demo()
t=Thread(target=obj.show())
t.start()
for i in range(5):
    print("this is the parent thread")
        
