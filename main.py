import matplotlib.pyplot as plt
import numpy as np
import math
import sys
import datetime ,time
import os

if not os.path.exists('logs'):
    os.makedirs('logs')

currentDir = os.getcwd()
date = time.strftime("%Y %b %a  %H.%M.%S")
completeName = os.path.join(f'{currentDir}\\logs', f"{date}_log.txt")
sys.stdout = open(completeName, "w")

num1 = int(input("Your Number: "))

def Main():
    def findnum(uInput, result):
        output = 0
        xs = [0]
        results = [uInput]
        while result != 1 and uInput != None:
            if (uInput % 2) == 0:
                result = uInput / 2
                print('Result: ' + str(result))
                uInput = result
                results.append(result)
                output += 10
                xs.append(output)
            else:
                result = (3*uInput)+1
                print('Result: ' + str(result))
                uInput = result
                results.append(result)
                output += 10
                xs.append(output)
        plt.plot(xs, results, 'o-.c')
        if len(results) <= 100:
            for x, y in zip(xs, results):
                label = "{:.2f}".format(y)

                plt.annotate(label,
                            (x,y), 
                            textcoords="offset points",
                            xytext=(0,10), 
                            ha='center') 
        else:
                label = "{:.2f}".format(results[-1])
                
                plt.annotate(label,
                            (xs[-1], results[-1]),
                            textcoords="offset points", 
                            xytext=(0,10), 
                            ha='center')

        
    last = int(0)

    if num1 != None:
        print(num1)
        findnum(num1, last)


    plt.grid()
    plt.show()


Main()

sys.stdout.close