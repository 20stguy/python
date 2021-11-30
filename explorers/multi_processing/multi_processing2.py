import multiprocessing as mp
import os


def pow(x):
    print(os.getppid(), "Hi!")
    # 몇번 프로세스가 돌아갔는지 볼 수 있다. getpprid
    return x ** 2


def main():
    pool = mp.Pool(3)

    my_tasks = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    results = []
    for i, t in enumerate(my_tasks):
        r = pool.apply_async(func=pow, args=(t,))
        results.append(r)

    for r in results:
        y = r.get()
        print(y)


if __name__ == '__main__':
    main()