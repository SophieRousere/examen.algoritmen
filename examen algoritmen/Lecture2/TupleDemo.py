tuple1 = ("green", "red", "blue") # Create a tuple
print(tuple1)

tuple2 = tuple([7, 1, 2, 23, 4, 5]) # Create a tuple from a list
print(tuple2)
#zelfde methodes als lijst
print("length is", len(tuple2)) # Use function len
print("max is", max(tuple2)) # Use max
print("min is", min(tuple2)) # Use min
print("sum is", sum(tuple2)) # Use sum

print("The first element is", tuple2[0]) # Use indexer

tuple3 = tuple1 + tuple2 # Combine 2 tuples: gwn na elkaar
print(tuple3)

tuple3 = 2 * tuple1 # Multiple a tuple : * : duplicate a tuple !!! 2keer erin zetten na elkaar
print(tuple3)

print(tuple2[2 : 4]) # Slicing operator hier print je index 2 tem 3, de bovenlimiet niet inbegrepen
print(tuple1[-1])  #laatste

print(2 in tuple2) # in operator: true or false !!

for v in tuple1:   #overloop elk element(variabele v) in tuple 1
    print(v, end = " ")  #alles op 1 regel, spatie, niet nieuwe lijn
print()
    
list1 = list(tuple2) # Obtain a list from a tuple
list1.sort()
tuple4 = tuple(list1)
tuple5 = tuple(list1)
print(tuple4)
print(tuple4 == tuple5) # Compare two tuples : true or false
