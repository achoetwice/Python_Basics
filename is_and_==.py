'''
TLDR: is means on the same position in memory, == means values lokks identical
'''

def show():
    a = [1,2,3]
    b = a
    print ('when b = a')
    print ('b is a ', (b is a))
    print ('b == a ', (b == a))

    b = a[:] # or use deepcopy
    print ('when b = a[:]')
    print ('b is a ', (b is a))
    print ('b == a ', (b == a))

if __name__ == '__main__':
    show()
