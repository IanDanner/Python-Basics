list_one = [1,2,3,4,5,6]
list_two = [1,2,3,4,5,6]
num = 0
if len(list_one) != len(list_two):
    print "The lists are not the same."
    num += 1
else :
    for idx in range(0,len(list_one)):
        if list_one[idx] != list_two[idx]:
            print "The lists are not the same."
            num += 1
            break
    if num < 1:
        print "The lists are the same."