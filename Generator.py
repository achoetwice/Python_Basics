# The difference between itering a generator and a list
# Use:python -m memory_profiler Generator.py
'''
TLDR:Itering a generator uses mush less memory than iter a list.
Generator means yield while every __next__ in iterator is called, but itering a list means iter over the whole list in a time 

'''
@profile
def gen():
    for i in range(500000):
        continue
        return None
@profile
def li():
    for i in list(range(500000)):
        continue
        return None

if __name__ == '__main__':
    gen()
    li()
