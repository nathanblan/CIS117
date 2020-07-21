################################################################################
# Creating an email message class
# nathanLanLab4.py
# 7.15.2020
################################################################################
    
class Message:
    #set local variable to check for valid character
    MAX_LEN = 50
    def __init__(self, sender = "Nathan Lan", recipient = "Grace Tan"):
        #declare attributes derived from the class
        self.sender = sender
        self.recipient = recipient
        self.body = ""
        
    def set_sender(self):
        self.sender = input("From: ")
        #force user to enter a valid input
        while not self.str_ok(self.sender):
            self.sender = input("Enter a valid name: ")

    def set_recipient(self):
        self.recipient = input("To: ")
        #force user to enter a valid name
        while not self.str_ok(self.sender):
            self.recipient = input("Enter a valid name: ")

    def append(self, line = ""):
        #check if the input to append is a valid string
        if self.str_ok(line):
            #add each line to the string "body" on a new line
            self.body += (line + "\n")
        else:
            pass

    def to_string(self):
        return "{}\n{}\n{}\n".format(self.sender,
                                          self.recipient,
                                          self.body)

    def str_ok(self, the_str):
        #try for len(the_str), which can throw an error if not given
        #a datatype the len() function can act on
        try:
            #check if input is a string
            if len(the_str) <= self.MAX_LEN and type(the_str) == str:
                return True
            else:
                #debug line
                print("input exceeds 50 characters")
                return False
        except:
            print("Please enter a valid input")
