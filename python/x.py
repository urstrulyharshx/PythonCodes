# create a dictionary
squares = {1:1, 2:4, 3:9, 4:16, 5:25}  

# remove a particular  item


print(squares[4])
del squares[4] 
 

# Print squares dictionary: 
print(squares)

# remove an arbitrary item using popitem method 
res = dict(reversed(list(squares.items())))

a=res.popitem()

print(a)



# Print squares dictionary: 
square = dict(reversed(list(squares.items())))
print()

# delete a particular item
del squares[2]  

# Print squares dictionary: 
print(squares)

# remove all items using clear method
squares.clear()

# Print squares dictionary: 
print(squares)

# delete the dictionary itself
squares.clear()