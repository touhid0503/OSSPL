import multiprocessing


def print_sum(a,b):
    print("Sum: {}".format(a+b),end="\n")

if __name__ == "__main__":
    
    p1=multiprocessing.Process(target=print_sum,args=(1.2,3.5))
    p1.start() 
    p1.terminate()     
    p1.join()
    p2=multiprocessing.Process(target=print_sum,args=(1,3))
    p2.start()      
    p2.join()
    print("Done!")
