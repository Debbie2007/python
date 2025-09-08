"""
Count down:
I have a bomb that I want to detonate at Aptech but I don’t want to be caught in the blast 

Help me design and develop a countdown timer that counts down from 10 to 1
"""
import time
count = 10
while count > 0:
    print(count)
    time.sleep(1)
    count -= 1
print ("BOOM (Just kidding, safe blast at Aptech)") 