for i in range(100,100000):
    isPrime = True
    isSquare = False
    for idx in range(2,i/2):
        if i % idx == 0:
            isPrime = False
            break
    for ii in range(1,i):
        if ii * ii == i:
            isSquare = True
            break
    if i == 1:
        isPrime = False
    if isSquare == False and isPrime == False:
        print str(i)+"FooBar"
    elif isSquare == True:
        print str(i)+"Bar"
    elif isPrime == True:
        print str(i)+"Foo"

