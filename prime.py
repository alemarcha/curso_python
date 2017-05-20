def prime():
    x = int(input("Enter a number: "))
    i=2
    while(i<x):
        if(x%i==0):
            print("It's not a prime number")
            break;
        i+=1

    else:
        print("Its a prime number")

prime()