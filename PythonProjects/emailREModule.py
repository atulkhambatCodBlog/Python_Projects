#a-zwscube@gmail.com
#0-9
#time1
#@time1
#.2,3
import re
email_condition="^[a-z]+[\_]?[a-z0-9]+[@]\w+[.]\w{2,3}$"
user_email=input('Enter your Email:')
if re.search(email_condition,user_email):
   print("Right Email")
  
else:
     print("Wrong Email|")