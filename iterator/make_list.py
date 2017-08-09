#!/usr/bin/env python3

  
def make_list(seq):
    listn = []
    i = iter(seq)
    try:
        while True:
            listn.append(next(i))
    except StopIteration:
        pass
    return listn
        
            
        
    
if __name__ == '__main__':
    print(make_list(range(100)))
    print(list(range(100)))
