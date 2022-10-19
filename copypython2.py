#!/usr/bin/env python3
import sys
b=sys.argv[1] 
print(b)
c=sys.argv[2]
print(c)
a=int(b)
if (a)>50:
  print(a,'is greater than 50')
  if a%3==0:
    print(a,'is divisible by 3')
  else:
    print(a,'is not divisible by 3')
else:
  print(a, 'is lesser than 50')
  if a%2==0:
     print(a,'is an even number')
  else:
     print(a,'is not an even number')


