#ssss these aren't real test
from character import Character

# Characters can be instantiated with avatar and name

arya = Character("Arya", "arya.png")
jon = Character("Jon", "jon.png")



print(arya.name, arya.avatar)
print(jon.name, jon.avatar)

# After adding stuff two inventory
# length of inventory should == 2

arya.inventory.append('Needle')
arya.inventory.append('Mask')

print(len(arya.inventory))