##
#  Demonstrate the Message class.
#
from CIS_117_Lab4Soln import Message

# Create the message.
wishList = Message("Bob", "Santa")
wishList.append("For Christmas, I would like:")
wishList.append("Video games")
wishList.append("World peace")

# Display its contents.
print(wishList.toString())
