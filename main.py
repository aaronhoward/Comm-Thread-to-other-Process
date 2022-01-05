import multiprocessing
from multiprocessing.queues import Empty
import threading
from threading import Event
import time
  
def square_list(mylist, q):
    """
    function to square a given list
    """
    # append squares of mylist to queue
    while True:
      for num in mylist:
          q.put_nowait("num" * num)
  
def print_queue(q, event_stop):
    """
    function to print queue elements
    """
    print("Queue elements:")
    while not event_stop.is_set():
      try:
          print(q.get(False, 1))
      except Empty:
        continue
  
if __name__ == "__main__":
    # input list
    mylist = range(2000)
    event_stop = Event()
    event_stop.clear()
    # creating multiprocessing Queue
    q = multiprocessing.Queue()
    # creating new processes
    p1 = multiprocessing.Process(target=square_list, args=(mylist, q))
    p1.name = "Multi_Process_DATA"
    p1.daemon = True
    p2 = threading.Thread(target=print_queue, args=(q,event_stop))
    p2.name = "Thread_DATA"
    p2.daemon = True
    # running process p1 to square list
    p1.start()
    p2.start()
    time.sleep(5)
    p1.terminate()
    event_stop.set()
    p1.join() 
    p2.join()