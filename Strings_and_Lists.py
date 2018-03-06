words = "It's thanksgiving day. It's my birthday, too!"
what = "day"
new = "month"
print words
print words.find(what)
print words.replace(what,new)

x = [2,54,-2,7,12,98]
print x
print min(x)
print max(x)

y = ["hello",2,54,-2,7,12,98,"world"]
print y
print y[0]+y[len(y)-1]
z = [y[0],y[len(y)-1]]
print z

a = [19,2,54,-2,7,12,98,32,10,-3,6]
print a
a.sort()
print a
b = a[0:(len(a)/2)]
print b
a = a[(len(a)/2):len(a)]
print [b] + a
