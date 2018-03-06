# #Integer
# arr = [98,150,3,442]
# for idx in arr:
#     if idx < 100:
#         print "That's a small number"
#     else :
#         print "That's a big number!"

# #String
# arrStr = ["short","this is a long sentence so print it as so extr extra fsfskdfsdfdsfsd"]
# for idx in arrStr:
#     if len(idx) < 50:
#         print "Short sentence"
#     else :
#         print "Long sentence"

# #List
# arrLi = [[1,2,3,4,5],[2,4,6,8,10,12,14,16,18,20,22]]
# for idx in arrLi:
#     if len(idx) < 10:
#         print "Short list"
#     else :
#         print "Big list!"

val = [1,2,3,4,5,6,7,8,9,10]
if type(val) == int:
    if val < 100:
        print "That's a small number"
    else :
        print "That's a big number!"
elif type(val) == str:
    if len(val) < 50:
        print "Short sentence"
    else :
        print "Long sentence"
elif type(val) == list:
    if len(val) < 10:
        print "Short list"
    else :
        print "Big list!"