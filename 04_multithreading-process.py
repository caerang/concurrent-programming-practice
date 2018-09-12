import random
import multiprocessing


def compute(results):
    results.append(sum([random.randint(1, 100) for i in range(1000000)]))

# python 의 GIL 이슈로 멀티 스레드로 구현하는 것 보다 멀티 프로세스로 구현하는 것이
# 성능에 더 이점이 있음

with multiprocessing.Manager() as manager:
    results = manager.list()
    workers = [multiprocessing.Process(target=compute, args=(results,))
               for x in range(4)]
    for worker in workers:
        worker.start()
    for worker in workers:
        worker.join()
    print('Results: {}'.format(results))
