from datetime import datetime




def create_banner_date():
  # datetime object containing current date and time
  now = datetime.now() 
  #Date: 29 June 20, Approximately 8:00 PM 
  return now.strftime("Date: %d %B %y, %I:%M %p")


def create_session_banner(session_id): 
     session_msg = "Session " + str(session_id)

     return "#" * 40 + "\n" +                                              \
       ((20 - (round(len(session_msg) / 2))) * " " + session_msg) + "\n" + \
       (create_banner_date()) + "\n" +                                     \
       "#" * 40  + "\n"


def print_session_banner(session_id):
  print(create_session_banner(session_id))

        
"""
 prints a simple text banner and accounts
for the message a length, width is 40

"""
def print_banner(msg):
  print("#"*40)
  print("#" + (20 - (round(len(msg) / 2))) * " " + msg)
  print("#"*40)











"""
msg="for example\n he went for a walk"

#######################
#      for example
# he went for a walk
#######################


try to optimize for lower-down,

break upon tokens of words.
length of sentence.


"""  


"""

 - I tried `import utility` without success...
 - I tried `from utility import utility` without success...
 
 + I tried `from utility import print_banner` with success
 + I tried `from utility import *` with success

 + I tried 

"""  




def storage_append_to_file(file_name, text):
  with open(file_name, "a") as f:
    f.write(text)

# https://docs.python.org/3/library/datetime.html#module-datetime
