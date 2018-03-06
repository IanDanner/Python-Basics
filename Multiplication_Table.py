n=12
x="x"
line=""
for ii in range(1,n+1):
    x += " "+str(ii)
print x
for idx in range(1,n+1):
    for i in range(1,n+1):
        line += " "+str(idx*i)
    print str(idx)+line
    line=""

print ""
#or

n=12
x=["x"]
main=[]
line=[]
for ii in range(1,n+1):
    x.append(ii)
main.append(x)
for idx in range(1,n+1):
    line.append(idx)
    for i in range(1,n+1):
        line.append(idx*i)
    main.append(line)
    line=[]

max_width = len(str(main[-1][-1]))+1
for i in main:
    i = [str(j).rjust(max_width) for j in i]
    print(''.join(i))



