################################################################################
# demo use of class Message
# demo_nathanLan.py
# 7.15.2020
################################################################################
from nathanLanLab4 import Message

# Create the message.
aMessage = Message("Evan", "David")
aMessage.append("Have u read darren's book?")
aMessage.append("its pretty great for usaco")
aMessage.append("you should give it a try")

# Display its contents.
print(aMessage.to_string())

#bad run
demo = Message()
print(demo.sender, demo.recipient)
demo.set_sender()
demo.set_recipient()
demo.append("""aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
            aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa""")
print(demo.body)
demo.append(12345)
print(demo.body)

#run
'''
================ RESTART: D:\05CSM\CIS117\code\demo_nathanLan.py ===============
Evan
David
Have u read darren's book?
its pretty great for usaco
you should give it a try


Nathan Lan Grace Tan
From: a
To: b
input exceeds 50 characters

Please enter a valid input

>>> 
'''
