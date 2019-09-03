'''
TLDR: There are no primitive type in python, everything is object.

Immutable means it can't be changed once it's assigned with value, if you do + or something meant to change the value, you just assign new value to new memory position.
Immutable type have a feature called interning, while you assign immutable object with identical value to two variable, they acctually point to same position on memory.
example: frozenset, str, int, tuple

Mutable means it supports change on the same position in memory.
example: list, dict, set
'''

def show():
    print ('Immutable display')
    a = 'p1'
    print ('origin a position: ', id(a))
    a += 'p2'
    print ("After a += 'p2', position: ", id(a))

    print ('\nInterning display')
    a = 'p1'
    b = a
    print ('Since str is immutable, b=a will use same position, thus a is b: ', (a is b))

    print ('\nMutable display')
    a = []
    print(f'a value {a} position: ', id(a))
    a += [1,2,3]
    print(f'a value {a} position: ', id(a))
    a.append('ADD')
    print(f'a value {a} position: ', id(a))
    
if __name__ == '__main__':
    show()
