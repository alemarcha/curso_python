x=[]
x.append("nombre")
x.append("alexis")
x.append("nombre2")
print(x)
x.insert(2,"safir")
print(x)
print(x[2])

x.remove("alexis")
print(x)
print(x[2])

x.pop()
print(x)


y=[1,45,6,56,8,32,54,13,5]
print(y)

z=["string",12,4.2]
print(z)


for item in z:

    print(item)
w=[]
number=int(input("enter a number: "))
for item in range (number):
    w.append(item)
    print(item, w)