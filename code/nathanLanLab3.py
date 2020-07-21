###########################################################
# Shopping Budget -The Price List
# nathanLanLab3.py
# 7.8.2020
###########################################################
iterations = 2
for iters in range(iterations):
    try: #check if the input is valid
        #prompt user for file input, save as variable
        input_file = input("Enter a file: ")
        #open file at the location input_file
        file = open(input_file, 'r')
    except: #if not, roast user for wrong input
        print("Invalid input, try again")
    else: #if valid, no errors are created and we continue
        break
#turn file into variable containing strings of file
content = file.readlines()
file.close()
#create new file to write items and price to
outfile = open('nathanLanLab3out.txt', 'w')
#store the sum of all the prices
sum_price = 0
#iterate through each line in the file
for line in content:
    #skips all the non-item/price combos
    if ":" not in line:
        continue
    #split each line into item and price, respectively
    item, price = line.split(": ")
    #cast price as float for formatting
    price = float(price)
    sum_price += float(price)
    outfile.write("{:20}{:10.2f} \n".format(item, price))
#add sum to the bottom of the list
total = "Total:"
outfile.write('{:20}{:10.2f}'.format(total, sum_price))
outfile.close()
    
#run
'''
Enter a file: lab
Invalid input, try again
Enter a file: lab3.txt
>>>
'''
