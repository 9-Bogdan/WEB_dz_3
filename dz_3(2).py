import time
from multiprocessing import Pool, cpu_count


def factorize(*number):
    res = []
    number_list = []
    for num in number:
        number_list.append(num)
    for num in number_list:
        result = []
        for i in range(1, num+1):
            if num % i == 0:
                result.append(i)
        res.append(result)
    return res


if __name__ == "__main__":
    numbers = [128, 255, 99999, 10651060]
    start = time.time()
    a, b, c, d = factorize(*numbers)

    assert a == [1, 2, 4, 8, 16, 32, 64, 128]
    assert b == [1, 3, 5, 15, 17, 51, 85, 255]
    assert c == [1, 3, 9, 41, 123, 271, 369, 813, 2439, 11111, 33333, 99999]
    assert d == [1, 2, 4, 5, 7, 10, 14, 20, 28, 35, 70, 140, 76079, 152158, 304316,
                 380395, 532553, 760790, 1065106, 1521580, 2130212, 2662765, 5325530, 10651060]
    finish = time.time()
    print(f"Synch:", finish - start)

    start_2 = time.time()
    with Pool(cpu_count()) as p:
        p.map(factorize, numbers)
    finish_2 = time.time()
    print(f"Parr:", finish_2 - start_2)
