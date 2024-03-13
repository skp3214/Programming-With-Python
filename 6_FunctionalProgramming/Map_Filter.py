menu=["espresso","mocha","latte","cappuccino","cortado"]
def find_coffee(coffee):
    if(coffee[0]=='c'):
        return coffee.capitalize()

map_coffee=map(find_coffee,menu)
print(map_coffee)
for x in  map_coffee:
    print(x)

# filter function
    
filter_coffee=filter(find_coffee,menu)
print(list(filter_coffee))