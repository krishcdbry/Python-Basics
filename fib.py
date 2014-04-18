print "Fibonacci Series in Python \n \n"
n  = int(raw_input("Enter the range of fib"))
a,b,co,c=0,1,2,0
print "%s %s" %(a,b)
while(co<n):
	 c = a+b
	 a,b = b,c
	 print c
	 co += 1