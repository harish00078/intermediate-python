# process: an insatance of a program (e.g a python interpreter)
# defination of process:-Processes are basically the programs that are dispatched from the ready state and are scheduled in the CPU for execution. PCB(Process Control Block) holds the concept of process. A process can create other processes which are known as Child Processes. The process takes more time to terminate and it is isolated means it does not share the memory with any other process. dThe process can have the following states new, ready, running, waiting, terminated, and suspended. 
###
# +takes advantage of multiple cpus and cores
# +separate memory space --> memory is not shared between processes
# +great for cpu-bound processing
# +new process is stated independently from other processes
# +processes are interruptable/killable
# +one gil for each process -> avoids gil limitation

# -heavyweight
# -starting a process is slower than starting a thread
#--more memory
# -IPC (inter-process communication) is more complicated###




