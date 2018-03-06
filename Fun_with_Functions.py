#Odd/Even:
def odd_even(num):
    for idx in range(1,num+1):
        if idx % 2 == 0:
            print "Number is ",idx,". This is an even number."
        else :
            print "Number is ",idx,". This is an odd number."
# odd_even(2000)

#Multiply:
def multiply(arr, num):
    for idx in range(0,len(arr)):
        arr[idx] *= num
    print arr
    return arr
multiply([2,4,10,16],5)

#Hacker Challenge:
def layered_multiples(arr):
    new_array = []
    for idx in arr:
        temp_array=[]
        for i in range(1,idx+1):
            temp_array.append(1)
        new_array.append(temp_array)
    return new_array
x = layered_multiples(multiply([2,4,5],3))
print x