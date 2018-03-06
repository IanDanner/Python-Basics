#Coin Tosses
import random
def coin_tosses(num):
    head = 0
    tail = 0
    coin = ""
    for idx in range(1,num+1):
        toss = random.randint(0,1)
        if toss > 0:
            coin = "tail"
            tail += 1
        else :
            coin = "head"
            head += 1
        print "Attempt #"+str(idx)+": Throwing a coin... It's a "+str(coin)+"! ... Got "+str(head)+" head(s) so far and "+str(tail)+" tail(s) so far"
coin_tosses(5000)