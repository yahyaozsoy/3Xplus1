import math
import sys
import datetime ,time
import os

currentDir = os.getcwd()
date = time.strftime("%Y %b %a  %H.%M.%S")
completeName = os.path.join(f'{currentDir}\\logs', f"{date}_log.txt")
sys.stdout = open(completeName, "w")

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