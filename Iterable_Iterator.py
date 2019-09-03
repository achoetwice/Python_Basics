'''Iterable means that a container(like list) with __iter__ method, Iterator is like a UI for us to iter over a iterable container, also iterator itself is iterable.'''
'''任何類別只要有__iter__方法皆會被視為Iterable的子類別，即使沒有顯式地繼承它，這是因為在Iterable中實作了__subclasshook__，會自動地把有__iter__方法的類別納入為子類別'''
a=[1,2]
b=iter(a)
c=iter(b)
print ('c is b ', (c is b))

print('for loop over a, round 1 ')
temp = iter(a)
while True:
    try:
        print(next(temp))
    except:
        print ('run out of numbers\n')
        break
print('for loop over a, round 2 ')
temp = iter(a)
while True:
    try:
        print(next(temp))
    except:
        print ('run out of numbers\n')
        break


print('\nfor loop over b or c, round 1 ')
temp = iter(b)
while True:
    try:
        print(next(temp))
    except:
        print ('run out of numbers\n')
        break

print('for loop over b or c, round 2 ')
temp = iter(b)
while True:
    try:
        print(next(temp))
    except:
        print ('run out of numbers\n')
        break

print('This demonstrate somethings, iterator is iteratble, but it will iter itself out so b is c. Also, a for loop is try to iter() a object and next() to it, so for loop on container sync new iterator everytime, but for loop a iterator will iter iterator itself so it can only be iter once.')