start = 1
stop = 31
while (start < stop):
    print(start)
    start = start + 1 
    if start % 3 == 0 and start % 5 == 0:
        print("fizzbuzz")
    elif start % 3 == 0:
        print("fizz")
    elif start % 5 == 0:
        print("buzz")
    else:
        print(start)

       