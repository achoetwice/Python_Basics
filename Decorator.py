'''Decorator is a way to wrap up a fuction like a wrapper'''

# First we have a person method, we want to decorate it with weapon
def person():
    return None
    
# Decorator without variable
def equip_decorator(func):
    def equipped():
        print (f'{func.__name__} got a equipment Sowrd!')
        print (f'I am a {func.__name__} with Sowrd!')
    return equipped

# Decorator with variable
def Weapon(*name):
    def equip_decorator(func):
        def equipped():
            print (f'{func.__name__} got a equipment {name}!')
            print (f'I am a {func.__name__} with {name}!')
        return equipped
    return equip_decorator

# Okay we got two type of waepon decorator
@equip_decorator
def dec_person():
    return None

@Weapon('Shield', 'Sword')
def dec_with_variable_person():
    return None

if __name__ == '__main__':
    # equip_decorator(person)()
    # print ('\n')
    dec_person()
    print ('\n')
    dec_with_variable_person()
    print ('\n')