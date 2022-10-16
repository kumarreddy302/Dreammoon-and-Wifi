#START OF IMPORT BLOCKS

import random

#END OF IMPORT BLOCK

#LIST DECLARATION

k = []
l = []
a = []
d = []
e = []

#COUNTER VARIABLE DECLARATION

sum = 0
sum1 = 0
sum2 = 0
sum3 = 0

#TAKING USER INPUT

print("ENTER USER INPUT")
u_i = input()

#TAKING DREAMOON RECIVED INPUT

print("Enter Dreamoon input")
d_i = input()

#FINDING THE ORGINAL POSTION OF DREAMOON

if '?' in d_i and len(u_i) == len(d_i):
    for i in u_i:
        if i == '+':
            sum1 += 1
        else :
            sum1 -= 1

    #FINDING THE ROUGH POSITION OF DREAMOON WITHOUT CONSEDERING '?' MARK         
    
    for j in d_i:
        if j == '+':
            sum2 += 1
        elif j == '-':
            sum2 -= 1
        else : 
            sum3 += 1  #FINDING NO.OF QUESTION MARKS SO THAT WE CAN CALCULATE TOTAL NO.OF OOUTCOMES

    #FINDING TOTAL NUMBEROF POSSIBLE OUTCOMES WITH RESPECTIVE '-' AND '+'

    for i in range(-sum3,sum3):
        if i > 0 :
            l.append("+")
        elif i < 0:
            l.append("-") 

    #FINDING ALL POSSIBLE VALUES IN PLACE OF '?' THAT NEED TO BE REPLACED

    for i in range(0,100):
        m = random.sample(l,sum3)
        if m in a:
            continue
        else:
            a.append(m)  #APPENDING ALL THE ELEMENTS INTO LIST SO THAT WE USE THIS TO CALCULATE THE PROBALBILTY AND TOTAL NUMBER OF OUTCOMES

    #APPENDING THE VALUE  OF + IN ALL QUESTION MARKS CASE

    for i in range(0,sum3):
        d.append("+")   
        if d not in a:
            a.append(d)

    #NOW WE HAVE A COMPLETE LIST OF ALL THE POSSIBLE VALUES OF '+' AND '-' THAT CAN BE REPLACED IN PLACE OF '?'

    #NOW WE ARE GOING TO HAVE LIST OF ALL THE POSSIBLE VALUE THAT ARE AVAILABLE AFTER THE REPLACEMENT OF EACH '?' MARK WITH THE RESPECTIVE SYMBOL

    for i in a :
        sum4 = 0
        for j in i:
            if j == '+':
                sum4 = sum4 + 1
            elif j == '-':
                sum4 -= 1
        e.append(sum4) #APPENDING ALL THE POSSIBLE POSITION VALUES INTO LIST

    #FINDING ALL THE POSSIBLE LOCATION VALUES ONE BY ONE AFTER REPLACING EVERY ? WITH ALL THE POSSIBLE VALUE

    c = 0
    for  i in e :
        z = sum2+i
        if sum1 == z : #HERE IF THE POSSIBLE LOCATION VALUE IS EQUAL TO ACTUAL POSITION WE ARE GOING TO INCREMENT THE COUNTER VARIABLE SUCH THAT WE CAN GET 
            c += 1 #HERE WE CAN GET OUR FAVOURABLE OUTCOMES

    #HERE WE ARE GOING TO FIND PROBABILITY

    prob = c/len(e)
    print("The probabilty of given Inputs is "+"{:.12f}".format(prob))
elif '?' not in d_i and len(u_i) == len(d_i):
    #FINDING THE ORGINAL POSTION OF DREAMOON

    for i in u_i:
        if i == '+':
            sum1 += 1
        else :
            sum1 -= 1

    #FINDING THE ROUGH POSITION OF DREAMOON WITHOUT CONSEDERING '?' MARK         
    
    for j in d_i:
        if j == '+':
            sum2 += 1
        elif j == '-':
            sum2 -= 1
    if sum2 == sum1 :
        prob = 1
    else:
        prob = 0
    print("The probabilty of given Inputs is "+"{:.12f}".format(prob))

    #IF USER INPUT  AND DREAMOON IS NOT OF SAME LENGTH THEN   

else :

    print("USER INPUT AND DREAMOON INPUT ARE OF SAME LENGTH")
