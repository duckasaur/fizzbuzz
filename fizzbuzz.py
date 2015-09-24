#!/usr/bin/python

# on numbers divisible by 3, it fizzes. on numbers divisible by 5, it buzzes. on numbers 
# divisible by both, it fizzbuzzes. 

# max fizzbuzz number input
fizzbuzz_max = input("How high do you want to fizzbuzz to? > ")

num = 0
while num < fizzbuzz_max:
    num = num + 1
    if (num%3)==0 and (num%5)==0:
        print "fizzbuzz"
    elif (num%3) == 0:
        print "fizz"
    elif (num%5) == 0:
        print "buzz"
    else:
        print num