################################################################################
# Creating an email message class
# nathanLanLab4.py
# 7.15.2020
################################################################################
#import libraries
import datetime
import re
from urllib.request import urlopen

#provide date of run
date = datetime.date.today()
print(date)

#list of topics we wish to locate in a webpage, added: space
topics = ['research', 'climate', 'evolution', 'cultural', 'leadership',
          'nation', 'space', 'physical', 'science', 'biological']

try:
    #check if the URL is valid or decodable
    response = urlopen('http://www.nasonline.org')
    page = response.read().decode()
except:
    print("The link you entered is invalid or could not be decoded")

#Find each topic in the webpage and print as summary
for topic in topics:
    #find all case insensitive matches to a topic and save number of occurances
    count = len(re.findall('(?i){}'.format(topic), page))
    print('{} appears {} times'.format(topic, count))

#run
'''
================ RESTART: D:\05CSM\CIS117\code\nathanLanLab5.py ================
2020-07-23
research appears 10 times
climate appears 4 times
evolution appears 4 times
cultural appears 8 times
leadership appears 5 times
nation appears 37 times
space appears 2 times
physical appears 1 times
science appears 58 times
biological appears 1 times
>>> 
'''
