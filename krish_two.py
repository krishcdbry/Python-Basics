
# Python basics two  
"""
   here we mainly concentrate on Classes/Objects(OOPS)
   Regular expressions , CGI Programming , Database Access , 
   Networking , E-mails , Multi-threading , XML Processing , 
   GUI Programming futhermore...!

                                  """

# Coming to classes and objects 

""" here we have to know about class , object , data member 
    class varible , function overloading , instance varible , 
     inheritence , instance , instantination , method , object , 
    operator oveloading """

 # Creating class

class oneKrish:
	  "This is a class which contains names about cars"
	  count_car = 0

	  def __init__(self,name,cost):
	  	self.name = name
	  	self.cost = cost
	  	oneKrish.count_car += 1

	  def allCars(self):
	  	print "Car Details : \n Name - %s \n Cost - %s" %(self.name,self.cost)

	  def totalCars(self):
	    print "Total cars : %s" %oneKrish.count_car	

 #creating instances 

car1 = oneKrish("Buggati-verion","$1000k") 
car2 = oneKrish("Porsh",200000)
car3 = oneKrish("Lamborgne",300000)

#gettings result 

car1.totalCars()

car1.allCars()
car2.allCars()
car3.allCars()

#checking attribures - details about atributes

print hasattr(car1,'name')               # checking the presense of attribute - here the result will be True
print setattr(car1,'name','Hummer')      # setting the name of the attribute -  from buggati-verion to Hummer -  here the result will be printed as none
print getattr(car1,'name')               # getting the attribute value - here the value is Hummer
print delattr(car1,'name')               # deleting the attribute
print hasattr(car1,'name')               # Checking the presense of attribute - here the result will be False
print setattr(car1,'name','Buggati')     # again setting the attribute to buggati 
print getattr(car1,'name')               # Getting the result - here the name Buggati will be printed


# Built-in class attributes    like  __doc__   , __dict__ , __module__ , __bases__ , __name__

print 



