# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 11:23:30 2020

@author: rajas
"""

#//program to perform input/output of all data types\\##
#//integer\\
x = 200
print(x)
print(type(x))

#//taking input\\
x = input()
print(x)

#//stringe\\
y = " hello world "
print(y)
print(type(y))

#//float\\
x = 12.5
print(x)
print(type(x))

#//complex\\
x = 6j
print(x)
print(type(x))

#//list\\
x = [12,"hi",12.5]
print(x)
print(type(x))

#//tuple\\
x = (20.6,"hello",125)
print(x)
print(type(x))

#//range\\
x = range(12,20)
print(x)
print(type(x))

#//dictionary\\
x = {}
x["1"] = "sri"
x["2"] = 6+2j
print(x)
print(type(x))

#//set\\
x = {20,20.8,"sri",1+6j}
print(x)
print(type(x))

#//boolean\\
x = 25
print(bool(x))
print(type(x))
y = False
print(int(y))
print(type(y))



#//program to enter two numbers and find their sum\\
a = 25
b = 30
sum = a+b



#//program to enter two numbers and perform all arthematic operations\\
a = 55
b = 19
sum = a+b
print(sum)
diff = a-b
print(diff)
mult = a*b
print(mult)
div = a/b
print(div)
per = a%b
print(per)



#//program to enter length and breadth of a rectangle and find its perimeter\\
l = 2.5
b = 6
perimeter = 2*(l+b)
print(perimeter)


#//area of rectangle//
l = 2.5
b = 6
area = l*b
print(area)



#//program to enter radius of circle and find out its diameter, circumference and area//
import math
r = 6
dia = 2*r
print(dia)
cir = 2*math.pi*r
print(cir)
area = math.pi*math.sqrt(r)
print(area)



#//program to enter lenght in CM and convert into M $ KM\\
cm = 5000
m = cm/100
print(m)
km = cm/100000
print(km)



#//program to enter temp in cel and covnter to fahrenheit\\
c = 40
f = (c*1.8)+32
print(f)



#//temp in f to c\\
f = 101
c = (f-32)/1.8
print(c)



#//program to convert days into year, weeks and days\\
days = 50
year = days/367
print(year)
weeks = (days%365)/7
print(weeks)
days = (days%365)%7
print(days)



#//program to find power of any number x^y\\
x = 9
y = 5
z = x^y
print(z)



#//program to enter any number to cal square root\\
import math
x = 8
print(int(math.sqrt(x)))



#//enter 2 angles of triangle and find 3rd angle\\
a = 38
b = 56
c = 180-(a+b)
print(int(c))



#//program to enter base and height of a triangle and find its area\\
h = 32
b = 15
a = (h*b)/2
print(int(a))



#//program to cal area of equilateral triangle\\
import math
a = 26
A =((math.sqrt(3)/4)*a)
print(int(A))



#//program to enter marks of 5 sub and cal total, average and percentage\\
t = 55
h = 65
e = 60
m = 70
s = 75
total = (t+h+e+m+s)
print(total)
avg = total/5
print(int(avg))
percent = (total/500)*100
print(int(percent))



#//program to enter p,t,r and cal simple interest\\
p = 2
t = 6
r = 3
a = (p*r*t)/100
print(a)




#//compound\\
p = 20
t = 12
r = 2
a = p* (pow((1 + r / 100), t))
print(a)