from ast import Break
import time

#Starting the activity
print("Let's count to 10 together")

#Initiating and ending counting
number = 1
while number <= 10:
  time.sleep(1)
  print(number)
  number += 1
else:
  print("Good job!")