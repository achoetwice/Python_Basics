# The difference between itering a generator and a list
# Use:python -m memory_profiler Generator.py and wait for a while
'''
TLDR:Itering a generator uses mush less memory than iter a list.
Generator means yield while every next() method is called, but itering a list means iter over the whole list in a time, while itering a generator means yield a variable per loop till loop over.
(i for i in range(100000) is a generator
'''

'''
Warning: 
For python2, range() just return a list of range, while in python3, range() return a iterable, immutable sequence of numbers.
For python3, range() is not a generator for sure, since you can't use next() to range() directly. However range() is a generator_like object since it defines start, step, and stop method, which make it run like a generator, yield only one variable per loop, so take less memory.
Also it is said that range() is written by C so it's faster than a list or any other python way to loop over.
'''
@profile
def sum_generator():
    sum(i for i in range(100000))
@profile
def sum_list():
    sum([i for i in range(100000)])

@profile
def for_ranger():
    for x in range(100000):
        a = x
        continue
@profile
def for_list():
    for x in list(range(100000)):
        a = x
        continue

if __name__ == '__main__':
    sum_generator()
    sum_list()
    for_ranger()
    for_list()

