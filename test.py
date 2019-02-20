#ssss these aren't real test
from character import Character
from character import Hero

# Characters can be instantiated with avatar and name

arya = Character("Arya Stark", "arya.png")
jon = Character("Jon Stark", "jon.png")



print(arya.name, arya.avatar)
print(jon.name, jon.avatar)

# After adding stuff two inventory
# length of inventory should == 2

arya.inventory.append('Needle')
arya.inventory.append('Mask')

print(len(arya.inventory))

# aray should have a `greet` method 
# and when called should return 
# "hello, I am arya start?"
#when i call it with `arya.greet_charactor(jon)
# should return
# 'hello jon snow, i'm arya starK?`
print(arya.greet())
print(arya.greet_character(jon))
print(arya.greet_character())

#I should be able to create a `Hero` instance
bronn = Hero("Broon of the Blackwater", "bron.png")

