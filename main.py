from item import Item

Item.instantiate_from_csv()

item1 = Item("MyItem", 750)
print(item1.name)
print(Item.all)
# Setting an Attribute
item1.name= "OtherItem"

# Getting an Attribute
print(item1.name)

print(Item.all)