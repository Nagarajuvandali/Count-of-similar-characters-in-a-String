#Asking the user to enter the string
a=input("Enter the string")

#Storing the characters in string to a list. 
b=list(a)

#Storing the length of the list in a variable so that it will be used for iterating
c=len(b)

#Asking the user to enter the character from a string
d=input("Enter the character you need to search in the string")

i=0
j=1
e=""
for  i in range(c):
    f = b[i]
    g=f.lower()
    if g == d:
        s = str(j)
        g=s
        j+=1
    e+=g
print(e)