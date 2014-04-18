for y in xrange(1,10):
	print y

print [1,2,3] * 3
a,b,c = 3,5,6
print a,b,c
odd = [1,3,5,7,9]
even = [2,4,6,8,10]
print odd+even

# string formatting

form = ("john","jell",3.14)
fs = "hello"

print "%s hai %s king %d" % (fs,form[1],form[2])

# String formatting with list

mylis = [1,2,3]

print "This is my list %s" % (mylis)    

# Now we will go for basic string operations

one = "kri.sh.cdb.ry"

print "The length of the string  %s" %(len(one))
print "The index of h %s" %(one.index("h"))
print "The count of letter r %s" %(one.count("r"))
print "In capslock %s and the Lowerlock %s" %(one.upper(),one.lower())
print "The sub string %s" %(one[0:5])
print "They start with = %s and ends with = %s" %(one.startswith("kris"),one.endswith("ry"))
print "The splitting %s" %(one.split("."))

# Now goes with operations like boolesn comparison etc..

name = "John"
age = 23
if age == 2 and name == "John":
   print "ok"
else:
   print "no ok"

i = 1
while (i<10): 
	   print i 
	   i=i+1
name,king = "krishcdbry","krishcdbry"

if name in[king]:
  print "yess"


if name is king:
   print "hey"  

count = 1
while True:
	  print count 
	  count += 1
	  if count > 5:
	  	 break
c=0
while True: 
	  c += 1
	  if c%2==0:
	  	 continue
	  if c>5:
	     break	 

	  print c	

# Function 

def my_krish(n): 
	print "hello krish the number is %s" %(n)


def one_add(a,b):
    my_krish(a+b)

def one_main(name1,name2):
	print "Hello dudes %s and %s" %(name1,name2)



one_main("krishcdbry","kingcdbry")
one_add(5,3)


# Going to objects and classes

class Krish:
	  car_name,car_cost,color = "Ferrari",7000000,"blue" 


car_one  = Krish()
car_one.car_name , car_one.car_cost,car_one.color = "Buggati",10000000,"Merun"

print Krish().color
print car_one.color




# Dictionaries 


krishbook = {
     "krish":909090909,
   "Mohan": 964298874
}

# OR 

krishbooks = {}
krishbooks["name"] = 9099900
krishbooks["one"] = 00123213123

for name, number in krishbooks.iteritems():
    print "Phone number of %s is %d" % (name, number)

del krishbook["krish"]

print krishbook

krishbooks.pop("one")

print krishbooks

# Dealing with files

"""  Creating the file not exists  """

fi = open("new.txt","wb")
fi.write("Hello this is krishcdbry's file buddy \n \n \n and This is just a cool python script");
fi.close()

""" Reading the file """

fi = open("new.txt","r+")
str = fi.read()
print " Reading the file =  %s "%(str)
fi.tell()   # Tells the position of the cursor 
fi.seek(0,10)   # Repositioning the cursor
fi.close()   # closes the file 
