#!/usr/bin/env python3
count=10
if count<15:
  message=("is less than 15")
  print(count,message)
else:
  message=("is more thn 15")
  print(count,message)

X=-3
if X<0:
  message=("negative")
  print(X,message)
else:
  message=("positive")
  print(X,message)
y=25
if y<0:
  message=("is less than zero")
  print(y,message)
elif y<20:
  message=("is less than 20")
  print(y,message)
elif y>20:
  message=("is more than 20")
  print(y,message)
  if y<50:
    print(y,' is greater than 20 but less than 50')
else:
  message=("must be 20")
  print(y,message)

even_numbers='2,4,6,8,10'
if '8' in even_numbers:
  print('z is an even number')
else:
  print('z is not an even number')

a=40
if a>50:
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


