import math 
import os 
import sys 
import random 

class ak_math:
    os.system('clear')
    #adding tow number 
    def adding(x,y):
        result =x+y
        return result 
   # adding from list 
    def addingInList(List):
        cr=0 
        for i in List:
            cr=cr+i 
        return cr 
    #some of tow number             
    def SumTow(x,y):
        re=x+y
        return re
    #som list
    def SumList(List):
        cr =0
        for i in List:
            cr=cr+i
        return cr
    #dev of tow number 
    def dev(x,y):
        re=x/y
        return re
    #dev of List
    def devList(List):
        cr=0
        for i in List:
            cr=cr/i
        return cr
    
    def mal(x,y):
        re=x*y
        return re
    def mal_List(List):
        cr=0
        for i in List:
            cr=cr+i
        return cr
    #get random number 
    def random_Number(x,y):
        rn=random.randint(x,y)
        return rn 
    #get prime number 
    def PrimeList(List):
        for i in List:
            if i%2==0:
                print(i," isn’t a prime number ")
            else:
                print(i, " is a prime number ")
     #get Maximum number       
    def getMaxNumber(List):
        ma=max(List)
        return ma
    #get minimum number 
    def getMinNumber(List):
        ma=min(List)
        return ma
    #get Average number 
    def getAvrage(List):
        ig=0
        cr=0
        print(ig)
        for i in List:
            cr=cr+i
            ig=ig+1 
        re= cr/ig
        return re 
            
    

        
