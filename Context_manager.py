'''
TLDR: 
Q: What is context manager?
A: Any object with __enter__ and __exit__ method is a context manager.
Which means that object can be used by "with".
example:
1. In django, "with transaction.atomic():" guaranteed that the "commit or rollback" will be executed as a __exit__ method.
2. In python, "with open(filename) as f :" guaranteed that f.close() will be done as a __exit__ method. 
'''

class Custom_CM():
    def __init__(self):
        self.name = 'Adam'
    def __enter__(self):
        print('I enter.')
        return self.name

    def __exit__(self, exc_type, exc_value, traceback):
        # The three parameters in __exit__ is put because "with" method will pass three parameters to __exit__,
        # Those parameters are describing the exception which make __exit__ triggered, if no exception, those will be None,None,None
        print('I exit.')
    

if __name__ == '__main__':
    with Custom_CM() as C:
        print (f'I am {C}.')
        print ('Im doing nothing but use with to call custom context manager.')
