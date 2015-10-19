area = 0
height = 10
width = 20
#Calculate the area of a triangle
area = width * height / 2 
print(area)

print('I have %d cats' % 6)	
print('I have %3d cats' % 6)
print('I have %03d cats' % 6)
print('I have %f cats' % 6)
print('I have %.2f cats' % 6)
print("The area of the triangle would be %d" % area)
print("The area of the triangle would be %.3f" % area)

print("My favorite number is " + '42')
print("My favorite number is %d !"%42)
print("My favorite number is %05d !"%42)

#You can also use a formst method to format numeric values
print("I have {0:d} cats".format(6))
print("I have {0:3d} cats".format(6))
print("I have {0:03d} cats".format(6))
print("I have {0:f} cats".format(6))
print("I have {0:.2f} cats".format(6))

print("The area of the triangle would be {0:f} ".format(area))
print("My favorite number is {0:d} ".format(42))
print("Here are three numbres! The first is {0:d} The second is {1:4d} and {2:d}".format(7,8,9))

total = 5 + 6 + 9 \
+10 + 12
print(total)
print("Here are three numbres!" + \
    " The first is {0:d} The second is {1:4d} and {2:d}".format(7,8,9))

testValue = 2
testValue = 10 + (testValue * 2)
print("TestValue = {0:d}".format(testValue))