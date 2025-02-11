# You have to modify a tuple item without converting it into a list. Provide an example of any case where this exactly can happen. 

tuple =(1,2,3,[4,5,6])
tuple[3][1] = 9
print(tuple)