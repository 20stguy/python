import multiprocessing as mp
from multiprocessing.pool import ThreadPool
import os
from time import sleep


def pow(x):
    print(os.getpid(), "Hi!")
    sleep(3)
    return x ** 2


def main():
    # pool = mp.Pool(3)
    pool = ThreadPool(3)

    my_tasks = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    results = []
    for i, t in enumerate(my_tasks):
        r = pool.apply_async(func=pow, args=(t, ))
        results.append(r)
    print("Main: Going to sleep")
    sleep(10)
    print("Main: Waking up")
    for r in results:
        y = r.get()
        print(y)


if __name__ == '__main__':
    main()