from stream_service import Stream
import random
import logging
from queue import Queue
from threading import Thread
import time

queue = Queue()

stream_user = Stream(name = 'test')


names = ['java', 'python', 'c', 'golang', 'c++', 'rust']
version = [1,2,3,4,5,6,7]



# producer

def add_to_queue(queue):
    for i in range(0,10):
        print(f"[Producer] Creating item {i}")
        r = random.randint(0,3)
        payload = {'name': names[r], 'version':version[r]}
         
        queue.put(payload)
        time.sleep(0.5)
    print("[Producer] Done producing. Sending stop signal.")
    queue.put(None)
    

# append in log
def append_to_log(queue):
    while True:
        payload = queue.get()
        print(f'[Consumer] getting from queue {payload}')

        if payload is None:
            queue.task_done()
            break

        print(f"Adding to log {payload}")

        stream_user.stream_logic(payload)
    print("[Consumer] Done processing. Exiting.")


add_to_queue_thread = Thread(target = add_to_queue, args = (queue,))
append_to_log_thread = Thread(target = append_to_log, args = (queue,))

add_to_queue_thread.start()
append_to_log_thread.start()


add_to_queue_thread.join()
append_to_log_thread.join()

print('done')

