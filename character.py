# name
#  avatar (profile picture)
# inventory

class Character():
    #def dunder init :) method is the constructor 
    # always in python
    def __init__(self, new_name, new_avatar):
        # `self` customary way to refers
        #  to the instance being built
        # some other languages use `this` 
        self.name = new_name
        self.avatar = new_avatar
        self.inventory = []
        
    def greet(self):
        return "Hello, I'm %s?" % (self.name,)
    #someone=None == is a defalut argument where None == Null in javaScirpt
    def greet_character(self, someone=None):
        # When we assume `someone` has a `.name` property
        # this is an Object-Oriented Programming principle called
        # Polymorphism
        #In Python it is called 'Duck Typing' :)
        if someone is not None:
            return "Hello, %s, I'm %s?" % (someone.name, self.name)
        else:
            return "Hello, I'm %s?" % (self.name,)

