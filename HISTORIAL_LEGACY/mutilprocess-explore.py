import multiprocessing as mp
threads = []

def shadow(num):
    print(mp.current_process().name+'is on line  --  '+str(num))

for i in range(1, 100):
    threads.append(mp.Process(target=shadow, args=(i,),name="name: "+str(i)))
    threads[-1].start()

for t in threads:
    t.join()

for i in range(10):
    print(i)
