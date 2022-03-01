from ast import Break
import time

print("Let's count to 10 together")

i = 1
while i <= 10:
  time.sleep(1)
  print(i)
  i += 1
else:
  print("Good job!")