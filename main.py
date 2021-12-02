import math
import sys
import datetime ,time
import os

date = time.strftime("%a %b %Y %H.%M.%S")
sys.stdout = open(f"{date}_log.txt", "w")

def findnum(girdi, sonuc):
    while sonuc != 1 and girdi != None:
        if (girdi % 2) == 0:
            sonuc = girdi / 2
            print('Sonuç:' + str(sonuc))
            girdi = sonuc
        else:
            sonuc = (3*girdi)+1
            print('Sonuç:' + str(sonuc))
            girdi = sonuc
        
num1 = int(input("Numaran: "))
last = int(0)

if num1 != None:
    print(num1)
    findnum(num1, last)
    
sys.stdout.close