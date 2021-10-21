import random

def gen_random(value, min, max):
    for i in range(value):
        yield random.randint(min,max)

if __name__ == "__main__": 
    for i in gen_random(5,1,3):
        print(i)