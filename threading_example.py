import time
import threading

start = time.perf_counter()

def do_something(seconds):
    print(f'\n[+] Sleeping {seconds} second(s)...')
    time.sleep(seconds)
    print('\n[+] Done sleeping...')
# Create 2 threads
#t1 = threading.Thread(target=do_something, args=[1])
#t2 = threading.Thread(target=do_something, args=[1])

# Start the threads
#t1.start()
#t2.start()

# Join the threads to sync them up
#t1.join()
#t2.join()

# loop through and make 10 threads, passing in the args 
threads = []
for _ in range(10):
    t = threading.Thread(target=do_something, args=[1.5])
    t.start()
    # Adding each thread to list "threads"
    threads.append(t)
    
# Join and execute threads in the list together
for thread in threads:
    thread.join()

finish = time.perf_counter()
print(f"\n[*] Finished in {round(finish-start, 2)} second(s)")


    
