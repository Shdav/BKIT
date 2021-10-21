from gen_random import gen_random

class Unique(object):
    def __init__(self, items, ignore_case = False, **kwargs):
        self.seen = set() 
        self.items = items
        self.ic = ignore_case
        self.kwargs = kwargs

    def __next__(self):
        it =  iter(self.items) 
        while True:
            try:
                current = next(it)
            except StopIteration:
                raise 
            else:
                if self.ic == True and isinstance(current, str):
                    temp = current[:]
                    if temp.lower() not in self.seen:
                        self.seen.add(temp.lower())
                        return current
                elif current not in self.seen:
                    self.seen.add(current)
                    return current

    def __iter__(self):
        return self

if __name__ == "__main__":

    data = [1, 1, 1, 1, 1, 2, 2, 2, 2, 2]
    print(list(Unique(data)))

    data = ['a', 'A', 'b', 'B', 'a', 'A', 'b', 'B']
    print(list(Unique(data)))

    data = gen_random(1, 3, 10)
    print(list(Unique(data)))

    