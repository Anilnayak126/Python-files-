# Thread = a flow like a separate order of instructions.
#         however each thread takes a turn running to achieve concurrency
#         GIL = (global interpreter lock)
#           allows only one thread to hold the control of the python intreprter at any one time
# cpu bound = program/task spends most of its time waiting for internal
#             events (CPU intensive)
#             use multi processing

# io bond = program/ task spends most of its time waiting for external events (user input, web scripting)
          # use multithreding

import threading
import time

def eat_breakfast():
    time.sleep(3)
    print('you eat breakfast')

def drink_coffee():
    time.sleep(4)
    print('you drink  cofee')
def study():
    time.sleep(5)
    print('you finish studying')


x = threading.Thread(target=eat_breakfast,args=())
x.start()

y = threading.Thread(target=drink_coffee,args=())
y.start()

z = threading.Thread(target=study,args=())
z.start()

x.join()
y.join()
z.join()

# eat_breakfast()
# drink_coffee()
# study()



print(threading.active_count())
print(threading.enumerate())
print(time.perf_counter())
