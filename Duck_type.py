'''What is duck typing(which python uses)'''

#Unlike C, we need to define every variable with specific type to make them usable, python use duck typing, mean that as long as a object have proper method, it can be treated as what you want, if dont have that method, it just return runtime error.
#And that's why python need no type declaration.
#If a bird swim like duck, walk like duct, act like duct, then this bird is fine to be treated as a duck.
#So 1 can be treat like int, also like float, and even byte.

class Duck:
    def quack(self):
        print ("This duck is quacking.")

    def feathers(self):
        print ("It got white weather.")
        
    def intro(self):
        print ('\'Im a duck qua qua.\'')


class Person:
    def quack(self):
        print ("This man is quacking.")

    def feathers(self):
        print ("This man is showing white weatehr.")

    def intro(self):
        print ('\'Im a person, but never mind, qua qua.\'')


def in_the_forest(duck):
    duck.quack()
    duck.feathers()
    duck.intro()


def game():
    Lucky = Duck()
    Adam = Person()
    print ('Lucky in the forest, ')
    in_the_forest(Lucky)
    print ('Adam in the forest, ')
    in_the_forest(Adam)


game()