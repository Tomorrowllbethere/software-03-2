from time import time
from multiprocessing import Pool, current_process, cpu_count
import logging

timer = time()

logger = logging.getLogger()
stream_handler = logging.StreamHandler()
logger.addHandler(stream_handler)
logger.setLevel(logging.DEBUG)

def factorize(*kwargs):
    numbers = list(kwargs)
    factors = []
    for n in numbers:
        nums = []
        for i in range(1, n+1):
                if n % i == 0:
                    nums.append(i)
        factors.append(nums)
    for factor in factors:
         logger.debug(f"pid={current_process().pid}, for number {n} is \n{factor}")
    return factors
    
if __name__ == '__main__':
    logger.info(cpu_count())
    with Pool(processes=4) as pool:
        processing = pool.map(factorize, (128, 255, 99999, 10651060))
    logger.debug(f"With multiprocessing\n It takes about {time()-timer}")    
    a, b, c, d  = factorize(128, 255, 99999, 10651060)
    assert a == [1, 2, 4, 8, 16, 32, 64, 128]
    assert b == [1, 3, 5, 15, 17, 51, 85, 255]
    assert c == [1, 3, 9, 41, 123, 271, 369, 813, 2439, 11111, 33333, 99999]
    assert d == [1, 2, 4, 5, 7, 10, 14, 20, 28, 35, 70, 140, 76079, 152158, 304316, 380395, 532553, 760790, 1065106, 1521580, 2130212, 2662765, 5325530, 10651060]
    logger.debug(f"Without multiprocessing\n It takes about {time()-timer}")