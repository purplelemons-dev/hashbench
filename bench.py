
from time import perf_counter
from hashlib import sha256
from random import randbytes
import multiprocessing as mp
from os import cpu_count


def calc_hash(n=512):
    return sha256(randbytes(n)).hexdigest()

def bench(itr=1000000, nproc=cpu_count()):
    per_pool = itr

    with mp.Pool(nproc) as pool:
        start = perf_counter()
        for _ in pool.starmap(calc_hash, [(512,)]*per_pool):
            pass
    time=perf_counter()-start
    print(f"Time:\t\t{time:.3f}s\nHashes:\t\t{per_pool} per process\nTotal hashes:\t{per_pool*nproc}\nAvg. h/s:\t{per_pool/time:.3f}\nProcesses:\t{nproc}")
    return time

if __name__ == "__main__":
    time=bench(itr=2**26,nproc=8)
