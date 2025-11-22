a=2.5
b=5
c="welcome to my coding lesson for python "
d=True

e= c[0:40:2]
print( "sentence after slicing is:", e)
f= c[::-1]
print("sentence after reversing is:", f)

print("data type of a is: ", type(a))
print("data type of b is: ", type(b))
print("data type of c is: ", type(c))
print("data type of d is: ", type(d))

# sentence after typecasting are:

a=int(a)
b=float(b)

print("After typecasting:")
print("data type of a is: ", type(a))
print("data type of b is: ", type(b))