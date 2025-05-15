import time
import random
import multiprocessing as mp


def summation(job, array, start, end, return_dict):
    s = 0
    for j in range(start, end):
        length = array[j]
        s += length ** 2 + sum(array[j + 1: j + 1 + length])
    return_dict[job] = s


if __name__ == '__main__':
    # n, m = map(int, input().split())
    # arr = list(map(int, input().split()))
    values = [
        (10, 10000),
        (100, 10000),
        (1000, 10000),
        (10000, 10000),
        (10, 100000),
        (100, 100000),
        (1000, 100000),
        (10000, 100000),
    ]

    for n, m in values:
        arr = [random.randint(0, n) for _ in range(m)]

        total = 0
        current = time.time()
        arr_nz = [el for el in arr if el != 0]

        if len(arr_nz) < 50000 or n < 10000:
            for i in range(len(arr_nz)):
                length = arr_nz[i]
                total += length ** 2 + sum(arr_nz[i + 1: i + 1 + length])
            # print(f'{total}')
            print(f'Single: {n = }, {m = }, {time.time() - current:.3} sec')
        else:
            num_processes = 4
            manager = mp.Manager()
            manager_dict = manager.dict()
            chunk_size = len(arr_nz) // num_processes

            processes = []
            for i in range(num_processes):
                p_start = i * chunk_size
                p_end = (i + 1) * chunk_size
                p = mp.Process(target=summation, args=(i, arr_nz, p_start, p_end, manager_dict))
                processes.append(p)
                p.start()

            for proc in processes:
                proc.join()

            # print(f'{sum(manager_dict.values())}')
            print(f'Multy: {n = }, {m = }, {time.time() - current:.3} sec')
