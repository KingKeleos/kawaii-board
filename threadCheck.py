import multiprocessing
import time


def useless_function(sec = 1):
    print(f'Sleeping for {sec} second(s)')
    time.sleep(sec)
    print(f'Done sleeping')
 
def start():
    start = time.perf_counter()
    process1 = multiprocessing.Process(target=useless_function)
    process1.start()
    useless_function()
    end = time.perf_counter()
    print(f'Finished in {round(end-start, 2)} second(s)') 

if __name__ == '__main__':
    multiprocessing.freeze_support()
    start()