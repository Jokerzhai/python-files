class Animal(object):
    def run(self):
        print('animalis running...')
    
class Dog(Animal):
    def eat(self):
        print('Eating meat...')

class Cat(Animal):
    pass
    

def run_twice(animal):
    animal.run()
    animal.eat()

#dog = Dog()
#dog.run()
#dog.eat()

#cat =  Cat()
#cat.run()

#run_twice(Animal())
run_twice(Dog())

