import multiprocessing as mp
from multiprocessing.pool import ThreadPool
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


def initializer(my_value):
    global MY_VALUE
    MY_VALUE = my_value


def option1():
    my_lock = mp.Value(c_bool, False)
    pool = mp.Pool(3, initializer=initializer, initargs=(my_lock,))
    # pool = ThreadPool(3)

    my_tasks = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    results = []
    for i, t in enumerate(my_tasks):
        r = pool.apply_async(func=pow, args=(t,))
        results.append(r)
    print("Main: Going to sleep")
    sleep(10)
    print("Main: Waking up")
    with my_lock.get_lock():
        my_lock.value = True

    for r in results:
        y = r.get()
        print(y)


if __name__ == '__main__':
    main()