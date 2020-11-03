#Write a Python program that prints all the numbers from 0 to 6 except 3 and 6. 

#Note : Use 'continue' statement. 

#Expected Output : 0 1 2 4 5

Gnumber = input("Input the larger number " )
Gnumber = (int(Gnumber))
for j in range(Gnumber):
print(j,end=' ')
print("\n")

x1 = input("First number you want to remove ")
x1 = (int(x1))
print("\n")

x2 = input("Second number you want to remove ")
x2 = (int(x2))
print("\n")


for x in range(Gnumber):
if (x == x1 or x== x2):
continue
print("Answer is ")
print( x,end=' ')
print("\n")