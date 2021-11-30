import multiprocessing as mp
from queue import Empty
from ctypes import c_bool
import os
from time import sleep


def pow(x: float):
    global MY_VALUE
    should_stop = False
    while not should_stop:
        sleep(3)

        with MY_VALUE.get_lock():
            should_stop = MY_VALUE.value

        if not should_stop:
            print(os.getpid(), "Still in the loop.")
        else:
            print(os.getpid(), "FREEDOM!")

    return x ** 2


def pow2(my_queue: mp.Queue, result_queue: mp.Queue):
    should_stop = False
    while not should_stop:
        try:
            x = my_queue.get(timeout=1)
            result = x**2
            result_queue.put(result)
        except Empty:
            print(os.getpid(), "No more stuff to calculate.")
            should_stop = True
    return


def initializer(my_value):
    global MY_VALUE
    MY_VALUE = my_value


def option1():
    my_queue = mp.Queue()
    my_result = mp.Queue()
    processes = [mp.Process(target=pow2, args=(my_queue, my_result)) for _ in range(1)]


    my_tasks = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    for i, t in enumerate(my_tasks):
        print(f"Main: Putting: {t}")
        my_queue.put(t)
    for p in processes:
        p.start()

    print("Main: Going to sleep")
    sleep(10)
    print("Main: Waking up")

    try:
        while True:
            value = my_result.get(timeout=1)
            print(value)
    except Empty:
        print("Done")


if __name__ == '__main__':
    option1()