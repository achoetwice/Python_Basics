'''Decorator is a way to wrap up a fuction like a wrapper'''
'''Class decorator is highly uesed since it's succinct to wrap up new method to an old class'''

# First we have a person class, we want to decorate it with weapon
class Person():
    def __init__(self, func):
        self.name = 'John'
        self.weapon = func
        print (f'I\'m {self.name}')
    def walk(self):
        print('I\'m walking')

@Person
def sword():
    print (f'I have a sword')




if __name__ == '__main__':
    person = sword
    person.walk()
    person.weapon()