'''Decorator is a way to wrap up a fuction like a wrapper'''

# First we have a person method, we want to decorate it with weapon
def person():
    return None
    
# Decorator without variable
def equip_decorator(func):
    def equipped():
        func()
        print (f'{func.__name__} got a equipment Sowrd!')
        print (f'I am a {func.__name__} with Sowrd!')
    return equipped

# Decorator with variable
def Weapon(*name):
    def equip_decorator(func):
        def equipped():
            func()
            print (f'{func.__name__} got a equipment {name}!')
            print (f'I am a {func.__name__} with {name}!')
        return equipped
    return equip_decorator

# Okay we got two type of waepon decorator
@equip_decorator
def dec_person():
    print ('Im a person')

@Weapon('Shield', 'Sword')
def dec_with_variable_person():
    print ('Im a person')

# Recursive decorator layers
@Weapon('Shield', 'Sword')
@equip_decorator
def hero_person():
    print ('Im a person')

if __name__ == '__main__':
    # equip_decorator(person)()
    # print ('\n')
    dec_person()
    print ('\n')
    dec_with_variable_person()
    print ('\n')
    hero_person()
    print ('\n')
    print ('The order of decorator: When passing variable, from inner to outer, hero_person passed to equip_decorator then return equipped, equipped passed to Weapon')
    print ('The order of decorator: When function is called, from outer to inner, Weapun called so func() is called first, which means the equipped in equip_decorator is called, so hero say with sword, then because the func goes into Weapon is equipped, so equipped says it got sowrd and shield, EOS.')