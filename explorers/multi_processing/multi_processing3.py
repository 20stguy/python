import multiprocessing as mp
import os
from time import sleep


def pow(x):

    print(os.getpid(), "Hi!")
    sleep(3)
    return x ** 2


def main():
    pool = mp.Pool(3)

    my_tasks = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    results = []
    for i, t in enumerate(my_tasks):
        r = pool.apply_async(func=pow, args=(t, ))
        results.append(r)

    for r in results:
        y = r.get()
        print(y)


if __name__ == '__main__':
    main()