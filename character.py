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