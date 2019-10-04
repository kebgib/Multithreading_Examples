import time
import concurrent.futures



def do_something(seconds):
    print(f'\n[+] Sleeping {seconds} second(s)...')
    time.sleep(seconds)
    return f'[+] Done sleeping...{seconds}'

"""
Basic
"""
start = time.perf_counter()
with concurrent.futures.ThreadPoolExecutor() as executor:
    f1 = executor.submit(do_something, 1) # passing in the args 1 to do_something
    f2 = executor.submit(do_something, 1)

    print(f1.result())
    print(f2.result())
finish = time.perf_counter()
print(f"\n[*] Finished in {round(finish-start, 2)} second(s)")


"""
Advanced methods
"""
# Spawning threads via iteration
start = time.perf_counter()
with concurrent.futures.ThreadPoolExecutor() as executor:
    results = [executor.submit(do_something, 1) for _ in range(10)]
    for f in concurrent.futures.as_completed(results):  # as_completed returns results as they come back
        print(f.result())
finish = time.perf_counter()
print(f"\n[*] Finished in {round(finish-start, 2)} second(s)")

# Iterate with a list of args, returning values as they complete
start = time.perf_counter()
with concurrent.futures.ThreadPoolExecutor() as executor:
    secs = [5, 4, 3, 2, 1]
    results = [executor.submit(do_something, sec) for sec in secs]
    for f in concurrent.futures.as_completed(results):
        print(f.result())    
finish = time.perf_counter()
print(f"\n[*] Finished in {round(finish-start, 2)} second(s)")

# returns results in the order they were started
start = time.perf_counter()
with concurrent.futures.ThreadPoolExecutor() as executor:
    secs = [5, 4, 3, 2, 1]
    results = executor.map(do_something, secs) # maping an instance of function:args for each item in list
    for result in results:
        print(result)
finish = time.perf_counter()
print(f"\n[*] Finished in {round(finish-start, 2)} second(s)")




