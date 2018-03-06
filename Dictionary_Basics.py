info = {
    'name': 'Ian',
    'age': 24,
    'country of birth': 'USA',
    'favorite language': 'javaScript'
}

def printInfo(info):
    for keys in info:
        print 'My '+keys+" is "+str(info[keys])

printInfo(info)