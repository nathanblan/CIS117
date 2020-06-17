###########################################################
# Nathan Lan
# CIS 117 Python Programming: Lab #1
# nathanLanLab1.py
# 6.17.2020
###########################################################
print("Hello World!")

#assign information to variables
last_name = "Lan"
g_number = "G01246656"
syl_1 = "Assesments are due Tuesday at 11:59"
syl_2 = "Assignments are worth 50% of your grade"
lab_detail_1 = "that source code shouldn't exceed 80 characters per line"
lab_detail_2 = "to use meaningful names taken from the problem domain"
lab_detail_3 = "to incorporate descriptive comments on code functionality"
#use multiline string to format text instead of "\" or multiple print() statements
information = '''My last name is {0}
My G number is {1}
Two syllabus details are:
1. {2}
2. {3}
Three lab details are:
1. {4}
2. {5}
3. {6}
'''
#use the format funtion to map variables to parts of text
print(information.format(last_name, g_number, syl_1, syl_2, lab_detail_1, lab_detail_2, lab_detail_3))

#output
'''
Hello World!
My last name is Lan
My G number is G01246656
Two syllabus details are:
1. Assesments are due Tuesday at 11:59
2. Assignments are worth 50% of your grade
Three lab details are:
1. that source code shouldn't exceed 80 characters per line
2. to use meaningful names taken from the problem domain
3. to incorporate descriptive comments on code functionality
'''
