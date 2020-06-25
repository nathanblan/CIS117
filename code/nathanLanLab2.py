###########################################################
# Print student and course information
# nathanLanLab2.py
# 6.24.2020
###########################################################
import datetime as dt

num_let = input("family name: ")
my_id = input("student ID: ")

num_let = len(num_let) #update num_let to length of family name

sum_id = [] # create an empty array to store my_id as a list
for i in my_id:
    sum_id.append(int(i)) #turn my_id into a list in the form of sum_id
my_id = sum(sum_id)

x = 2#declare base value 2 for our next calculation
for i in range(2, num_let+1): #num_let + 1 for inclusivity
    x = x + 1 #calculate expression 3, store result as x

expressions = [ #create list containing all the expressions 
    "{:.2f}".format(my_id / 2),#format as 2 point float
    my_id % 2,
    x, #calculated above and stored in x
    my_id + num_let,
    abs(num_let - my_id),
    "{:.2f}".format((my_id) / (num_let + 1100)), #format as 2 point float
    bool((num_let % num_let) and (my_id * my_id)), #cast as bool
    bool(1 or (my_id / 0)), #cast as bool
    "{:.2f}".format(round(3.15, 1)) #format as 2 point float
    ]
for i in range(9): #loop through expressions and print result of each
    print("Expression" + str(i) + ": " + str((expressions[i])))

date = dt.datetime.now()#use module datetime to find current time
print(date)

#run
'''
family name: lan
student ID: 01246656
Expression0: 15.00
Expression1: 0
Expression2: 4
Expression3: 33
Expression4: 27
Expression5: 0.03
Expression6: False
Expression7: True
Expression8: 3.10
2020-06-24 22:42:57.858249
'''
