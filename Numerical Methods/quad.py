temp = input('Hello user please input the coefficents of the quadratic equation of the form; ax^2 + bx + c = 0. a = ')
a = float(temp)
temp = input('b = ')
b = float(temp)
temp = input('c = ')
c = float(temp)

x = (-b + (b**2-4*a*c)**(1.0/2) )/ (2*a)

y = (-b - (b**2-4*a*c)**(1.0/2) )/ (2*a)

r = 2*c / (-b + (b**2-4*a*c)**(1.0/2) )

s = 2*c / (-b - (b**2-4*a*c)**(1.0/2) )


print("%.7E" % x,"%.7E" % y, "%.7E" % s, "%.7E" %  r)
