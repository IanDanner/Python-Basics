arr = ["magical unicorns",19,"hello",98.98,"world"]
# arr = [1,2,3,4,5,6]
# arr = ["what","is","my","name"]
string = "String:"
arrSum = 0
countStr = 0
countSum = 0
for idx in arr:
    if type(idx) == int or type(idx) == float:
        countSum += 1
        arrSum += idx
    if type(idx) == str:
        countStr += 1
        string += " "+idx
if countStr > 0 and countSum >0:
    print "The list you entered is of mixed type"
    print string
    print "Sum: " + str(arrSum)
elif countSum > 0:
    print "The list you entered is of integer type"
    print "Sum: " + str(arrSum)
elif countStr > 0:
    print "The list you entered is of string type"
    print string
